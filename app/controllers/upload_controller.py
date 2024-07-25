import uuid
from flask import request, jsonify
from app import db
from app.models import ProcessingRequest, Product
from app.services.csv_processing import validate_csv
import csv
import io

def upload_csv():
    from app.services.image_processing import process_images_task
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    if not validate_csv(file):
        return jsonify({'error': 'Invalid CSV format'}), 400

    request_id = str(uuid.uuid4())
    processing_request = ProcessingRequest(request_id=request_id)
    db.session.add(processing_request)
    db.session.commit()

    content = file.read().decode('utf-8')
    csv_file = io.StringIO(content)
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        product = Product(
            serial_number=row[0],
            product_name=row[1],
            input_image_urls=row[2],
            request_id=processing_request.id
        )
        db.session.add(product)
    db.session.commit()

    process_images_task.delay(request_id)
    return jsonify({'request_id': request_id}), 202
