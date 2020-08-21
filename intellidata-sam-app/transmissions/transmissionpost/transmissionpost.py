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
	data=json.loads(event['body'])

	try:
		table.put_item(
	        Item={
	            'TRANSMISSION_ID': data["transmissionid"],
				'LOCAL_ID': data["id"],
				'ITEM_ID': ts,
				'SENDER_NAME': data["SenderName"],
				'BENEFIT_ADMINISTRATOR_PLATFORM': data["BenefitAdministratorPlatform"],
				'RECEIVER_NAME': data["ReceiverName"],
				'TEST_PRODUCTION_CODE': data["TestProductionCode"],
				'TRANSMISSION_TYPE_CODE': data["TransmissionTypeCode"],
				'SYSTEM_VERSION_IDENTIFIER': data["SystemVersionIdentifier"],
				'CREATOR': data["creator"],
				'CREATE_DATE': data["create_date"],
				'CONNECTION': data["backend_SOR_connection"],
				'RECORD_STATUS': data["record_status"],
				'COMMIT_INDICATOR': data["commit_indicator"],
				'RESPONSE': data["response"]


	           }
	    )


	except Exception as e:
	        print(e)
	        print('Error in reading data from intellidataTransmissionTable')
	        raise e
