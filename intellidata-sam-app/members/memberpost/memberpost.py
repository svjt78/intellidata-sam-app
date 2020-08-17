import boto3
import json
import uuid
import csv
import time

def lambda_handler(event, context):

	recordId = str(uuid.uuid4())

#	ts = datetime.datetime.now().timestamp()
	ts = int(round(time.time() * 1000))

	dynamodb = boto3.resource('dynamodb')

	table = dynamodb.Table('intellidataMemberTable')
	data=json.loads(event['body'])

	try:
		table.put_item(
	        Item={
	             'MEMBER_ID': data["memberid"],
				 'LOCAL_ID': data["id"],
				 'ITEM_ID': ts,
				 'NAME': data["name"],
				 'SLUG': data["slug"],
				 'AGE': data["age"],

				 'ADDRESS_LINE_1': data["address_line_1"],
				 'ADDRESS_LINE_2': data["address_line_2"],
				 'CITY': data["city"],
				 'STATE': data["state"],
				 'ZIPCODE': data["zipcode"],

				 
				 'EMAIL': data["email"],
				 'PHONE': data["phone"],
				 'GROUP': data["group"],
				 'CREATOR': data["creator"],
				 'MEMBER_DATE': data["member_date"],
				 'SMS': data["sms"],
				 'EMAILER': data["emailer"],
				 'ARTEFACT': data["artefact"],
				 'CONNECTION': data["backend_SOR_connection"],
				 'RECORD_STATUS': data["record_status"],
				 'COMMIT_INDICATOR': data["commit_indicator"],
				 'RESPONSE': data["response"]

	           }
	    )


	except Exception as e:
	        print(e)
	        print('Error in reading data from intellidataTable')
	        raise e
