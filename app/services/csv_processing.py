import io
import csv

def validate_csv(file):
    content = file.read().decode('utf-8')
    csv_file = io.StringIO(content)
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)

    expected_headers = ['serial_number', 'product_name', 'input_image_urls']
    if headers != expected_headers:
        return False

    file.seek(0)
    return True
