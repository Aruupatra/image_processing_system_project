from flask import Blueprint, request, jsonify

bp = Blueprint('webhook', __name__)

@bp.route('/webhook', methods=['POST'])
def handle_webhook():
    # Extracting data from external
    data = request.json
    if not data or 'request_id' not in data or 'status' not in data:
        return jsonify({'error': 'Invalid payload'}), 400

    # Process the data 
    request_id = data['request_id']
    status = data['status']

    # This example doesn't update the status since we are handling it in the processing task
    return jsonify({'message': 'Webhook received successfully'}), 200
