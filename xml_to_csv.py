import requests
import csv
from io import StringIO
from lxml import etree
import boto3

def lambda_handler(event, context):

    # Retrieve XML file from URL
    url = "https://drive.google.com/uc?id=1TjIfzzyoBe4mqrtRVa0N9dv-91eH9Qv7&export=download"
    response = requests.get(url)

    # Parse XML string
    root = etree.fromstring(response.content)

    # Convert XML to CSV
    csv_data = StringIO()
    writer = csv.writer(csv_data)

    header = ['Name', 'Age', 'Gender', 'Email', 'Phone']
    writer.writerow(header)

    for person in root.findall('Person'):
        name = person.find('Name').text
        age = person.find('Age').text
        gender = person.find('Gender').text
        email = person.find('ContactDetails/Email').text
        phone = person.find('ContactDetails/Phone').text
        writer.writerow([name, age, gender, email, phone])

    csv_string = csv_data.getvalue()

    # Upload CSV file to S3 bucket
    s3 = boto3.resource('s3')
    bucket_name = 'aryansteeleye'
    key = 'people.csv'
    s3.Object(bucket_name, key).put(Body=csv_string)

    return {
        'statusCode': 200,
        'body': 'CSV file uploaded to S3 bucket'
    }
