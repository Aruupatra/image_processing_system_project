from flask import jsonify


def check_status(request_id):
    from app.models import ProcessingRequest
    request = ProcessingRequest.query.filter_by(request_id=request_id).first()
    if not request:
        return jsonify({'error': 'Invalid request ID'}), 404
    return jsonify({'request_id': request_id, 'status': request.status})
