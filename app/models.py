from app import db

class ProcessingRequest(db.Model):
    __tablename__ = 'processing_request'
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.String(50), unique=True, nullable=False)
    status = db.Column(db.String(20), default='Pending')
    product_data = db.relationship('Product', backref='request', lazy=True)
    
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(50), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    input_image_urls = db.Column(db.Text, nullable=False)
    output_image_urls = db.Column(db.Text, nullable=True)
    request_id = db.Column(db.Integer, db.ForeignKey('processing_request.id'), nullable=False)
