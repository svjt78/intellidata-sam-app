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

	table = dynamodb.Table('intellidataEmployerTable')
	data=json.loads(event['body'])

	try:
		table.put_item(
	        Item={
	            'EMPLOYER_ID': data["employerid"],
				'LOCAL_ID': data["id"],
				'ITEM_ID': ts,
				'NAME': data["name"],
				'SLUG': data["slug"],
				'DESCRIPTION': data["description"],
				'FEDERAL_EMPLOYER_IDENTIFICATION_NUMBER': data["FederalEmployerIdentificationNumber"],
				'CARRIER_MASTER_AGREEMENT_NUMBER': data["CarrierMasterAgreementNumber"],
				'ADDRESS_LINE_1': data["address_line_1"],
				'ADDRESS_LINE_2': data["address_line_2"],
				'CITY': data["city"],
				'STATE': data["state"],
				'ZIPCODE': data["zipcode"],
				'PURPOSE': data["purpose"],
				'PHOTO': data["photo"],
				'TRANSMISSION': data["transmission"],
				'SOURCE': data[ix]["source"],
				'CREATOR': data["creator"],
				'EMPLOYER_DATE': data["employer_date"],
				'CONNECTION': data["backend_SOR_connection"],
				'RECORD_STATUS': data["record_status"],
				'COMMIT_INDICATOR': data["commit_indicator"],
				'RESPONSE': data["response"]

	           }
	    )


	except Exception as e:
	        print(e)
	        print('Error in reading data from intellidataEmployerTable')
	        raise e
