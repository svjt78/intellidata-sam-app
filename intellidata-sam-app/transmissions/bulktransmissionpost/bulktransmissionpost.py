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

	table = dynamodb.Table('intellidataTransmissionTable')
	data = []
	data=json.loads(event['body'])


	for ix in range(len(data)):

		  try:
			  table.put_item(
		         Item={
		            'TRANSMISSION_ID': data[ix]["transmissionid"],
		            'LOCAL_ID': data[ix]["id"],
					'ITEM_ID': ts,
		            'SENDER_NAME': data[ix]["SenderName"],
		            'BENEFIT_ADMINISTRATOR_PLATFORM': data[ix]["BenefitAdministratorPlatform"],
		            'RECEIVER_NAME': data[ix]["ReceiverName"],
		            'TEST_PRODUCTION_CODE': data[ix]["TestProductionCode"],
		            'TRANSMISSION_TYPE_CODE': data[ix]["TransmissionTypeCode"],
		            'SYSTEM_VERSION_IDENTIFIER': data[ix]["SystemVersionIdentifier"],
		            'CREATOR': data[ix]["creator"],
		            'CREATE_DATE': data[ix]["create_date"],
		            'CONNECTION': data[ix]["backend_SOR_connection"],
					'RECORD_STATUS': data[ix]["record_status"],
					'COMMIT_INDICATOR': data[ix]["commit_indicator"],
					'RESPONSE': data[ix]["response"]


	        		 }
	    		)


		  except Exception as e:
		        print(e)
		        print('Error in reading data from intellidataTransmissionTable')
		        raise e
