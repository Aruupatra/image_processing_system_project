import requests
from PIL import Image
from io import BytesIO
import os
import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv

load_dotenv()

S3_BUCKET = os.getenv('S3_BUCKET')
S3_REGION = os.getenv('S3_REGION')
S3_ACCESS_KEY = os.getenv('S3_ACCESS_KEY')
S3_SECRET_KEY = os.getenv('S3_SECRET_KEY')

s3_client = boto3.client(
    's3',
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
    region_name=S3_REGION
)

def download_image(url):
    response = requests.get(url)
    response.raise_for_status()
    return Image.open(BytesIO(response.content))

def compress_image(image):
    output = BytesIO()
    image.save(output, format='JPEG', quality=50)
    output.seek(0)
    return output

def upload_to_s3(file_content, file_name):
    try:
        s3_client.put_object(
            Body=file_content,
            Bucket=S3_BUCKET,
            Key=file_name,
            ContentType='image/jpeg'
        )
        return f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{file_name}"
    except NoCredentialsError:
        print("Credentials not available")
        return None

def process_images(image_urls, output_dir):
    output_urls = []
    for url in image_urls:
        try:
            image = download_image(url)
            compressed_image = compress_image(image)
            file_name = os.path.basename(url)
            file_name = f"{output_dir}/{file_name}"
            output_url = upload_to_s3(compressed_image, file_name)
            if output_url:
                output_urls.append(output_url)
        except Exception as e:
            print(f"Failed to process image {url}: {str(e)}")
    return output_urls
