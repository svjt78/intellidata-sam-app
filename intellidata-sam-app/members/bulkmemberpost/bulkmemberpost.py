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
	data = []
	data=json.loads(event['body'])


	for ix in range(len(data)):

		  try:
			  table.put_item(
		         Item={
		            'MEMBER_ID': data[ix]["memberid"],
		            'LOCAL_ID': data[ix]["id"],
					'ITEM_ID': ts,
		            'NAME': data[ix]["name"],
		            'SLUG': data[ix]["slug"],
		            'AGE': data[ix]["age"],

					'ADDRESS_LINE_1': data[ix]["address_line_1"],
					'ADDRESS_LINE_2': data[ix]["address_line_2"],
					'CITY': data[ix]["city"],
					'STATE': data[ix]["state"],
					'ZIPCODE': data[ix]["zipcode"],
					
		            'EMAIL': data[ix]["email"],
		            'PHONE': data[ix]["phone"],
		            'GROUP': data[ix]["group"],
					'CREATOR': data[ix]["creator"],
		            'MEMBER_DATE': data[ix]["member_date"],
		            'SMS': data[ix]["sms"],
		            'EMAILER': data[ix]["emailer"],
					'ARTEFACT': data[ix]["artefact"],
					'CONNECTION': data[ix]["backend_SOR_connection"],
					'RECORD_STATUS': data[ix]["record_status"],
					'COMMIT_INDICATOR': data[ix]["commit_indicator"],
					'RESPONSE': data[ix]["response"]


	        		 }
	    		)


		  except Exception as e:
		        print(e)
		        print('Error in reading data from intellidataTable')
		        raise e
