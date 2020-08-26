import boto3
import json
import uuid
import csv

def lambda_handler(event, context):

	recordId = str(uuid.uuid4())
	print (recordId)
	s3 = boto3.resource(
    	's3'
	)

	bucket = client.Bucket('intellidatastatic')
	keyname = "media/employees.csv"

    csvfile = s3.get_object(Bucket=bucket, Key=keyname)
    csvcontent = csvfile['Body'].read().split(b'\n')

    csv_data = csv.DictReader(csvcontent)

	print(csv_data)



			#End of code
