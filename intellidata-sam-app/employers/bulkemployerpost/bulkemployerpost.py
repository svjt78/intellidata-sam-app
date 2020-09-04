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
	data = []
	data=json.loads(event['body'])


	for ix in range(len(data)):

		  try:
			  table.put_item(
		         Item={
		            'EMPLOYER_ID': data[ix]["employerid"],
		            'LOCAL_ID': data[ix]["id"],
					'ITEM_ID': ts,
		            'NAME': data[ix]["name"],
		            'SLUG': data[ix]["slug"],
		            'DESCRIPTION': data[ix]["description"],
		            'FEDERAL_EMPLOYER_IDENTIFICATION_NUMBER': data[ix]["FederalEmployerIdentificationNumber"],
		            'CARRIER_MASTER_AGREEMENT_NUMBER': data[ix]["CarrierMasterAgreementNumber"],
					'ADDRESS_LINE_1': data[ix]["address_line_1"],
					'ADDRESS_LINE_2': data[ix]["address_line_2"],
					'CITY': data[ix]["city"],
					'STATE': data[ix]["state"],
					'ZIPCODE': data[ix]["zipcode"],
					'PURPOSE': data[ix]["purpose"],
					'PLANADMIN_EMAIL': data[ix]["planadmin_email"],
					'PHOTO': data[ix]["photo"],
					'TRANSMISSION': data[ix]["transmission"],
					'SOURCE': data[ix]["source"],
					'TRANSMISSIONID': data[ix]["transmissionid"],
		            'CREATOR': data[ix]["creator"],
		            'EMPLOYER_DATE': data[ix]["employer_date"],
		            'CONNECTION': data[ix]["backend_SOR_connection"],
					'RECORD_STATUS': data[ix]["record_status"],
					'COMMIT_INDICATOR': data[ix]["commit_indicator"],
					'RESPONSE': data[ix]["response"]


	        		 }
	    		)


		  except Exception as e:
		        print(e)
		        print('Error in reading data from intellidataEmployerTable')
		        raise e
