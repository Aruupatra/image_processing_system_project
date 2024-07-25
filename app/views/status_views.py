from flask import Blueprint


bp = Blueprint('status', __name__)

@bp.route('/status/<request_id>', methods=['GET'])
def status(request_id):
    from app.controllers.status_controller import check_status
    return check_status(request_id)
