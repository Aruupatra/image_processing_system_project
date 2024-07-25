from flask import Blueprint


bp = Blueprint('upload', __name__)

@bp.route('/upload', methods=['POST'])
def upload():
    from app.controllers.upload_controller import upload_csv
    return upload_csv()
