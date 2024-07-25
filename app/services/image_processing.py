from app import celery,db
from app.models import Product, ProcessingRequest
from app.services.async_worker import process_images
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@celery.task(name='app.services.image_processing.process_images_task')
def process_images_task(request_id):
    logger.info(f"Processing images task started for request_id: {request_id}")
    # Add additional logging or debug information as needed
    # Example: process images here
    logger.info(f"Processing complete for request_id: {request_id}")
    from app import app
    with app.app_context():
        request = ProcessingRequest.query.filter_by(request_id=request_id).first()
        logger.info(f"Processing in app context for request_id: {request_id}")
        if not request:
            logger.error(f"No processing request found with request_id: {request_id}")
            return
        for product in request.product_data:
            input_urls = product.input_image_urls.split(',')
            output_urls = process_images(input_urls, 'static/processed_images')
            product.output_image_urls = ','.join(output_urls)
        request.status = 'Completed'
        db.session.commit()