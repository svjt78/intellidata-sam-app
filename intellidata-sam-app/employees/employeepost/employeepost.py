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

	table = dynamodb.Table('intellidataEmployeeTable')
	data=json.loads(event['body'])

	try:
		table.put_item(
	        Item={
	             'EMPLOYEE_ID': data["employeeid"],
				 'LOCAL_ID': data["id"],
				 'ITEM_ID': ts,
				 'SSN': data["ssn"],
				 'NAME': data["name"],
				 'SLUG': data["slug"],
				 'GENDERCODE': data["gendercode"],
				 'AGE': data["age"],
				 'BIRTHDATE': data["birthdate"],
				 'MARITALSTATUS': data["maritalstatus"],
				 'HOME_ADDRESS_LINE_1': data["home_address_line_1"],
				 'HOME_ADDRESS_LINE_2': data["home_address_line_2"],
				 'HOME_CITY': data["home_city"],
				 'HOME_STATE': data["home_state"],
				 'HOME_ZIPCODE': data["home_zipcode"],
				 'MAIL_ADDRESS_LINE_1': data["mail_address_line_1"],
				 'MAIL_ADDRESS_LINE_2': data["mail_address_line_2"],
				 'MAIL_CITY': data["mail_city"],
				 'MAIL_STATE': data["mail_state"],
				 'MAIL_ZIPCODE': data["mail_zipcode"],
				 'WORK_ADDRESS_LINE_1': data["work_address_line_1"],
				 'WORK_ADDRESS_LINE_2': data["work_address_line_2"],
				 'WORK_CITY': data["work_city"],
				 'WORK_STATE': data["work_state"],
				 'WORK_ZIPCODE': data["work_zipcode"],
				 'EMAIL': data["email"],
				 'ALTERNATE_EMAIL': data["alternate_email"],
				 'HOME_PHONE': data["home_phone"],
				 'WORK_PHONE': data["work_phone"],
				 'MOBILE_PHONE': data["mobile_phone"],
				 'ENROLLMENT_METHOD': data["enrollment_method"],
				 'EMPLOYMENT_INFORMATION': data["employment_information"],
				 'EMPLOYER': data["employer"],
				 'CREATOR': data["creator"],
				 'EMPLOYEE_DATE': data["employee_date"],
				 'SMS': data["sms"],
				 'EMAILER': data["emailer"],
				 'SOURCE': data["source"],
				 'EMPLOYERID': data["employerid"],
				 'ARTEFACT': data["artefact"],
				 'CONNECTION': data["backend_SOR_connection"],
				 'RESPONSE': data["response"],
				 'COMMIT_INDICATOR': data["commit_indicator"],
				 'RECORD_STATUS': data["record_status"],

	           }
	    )


	except Exception as e:
	        print(e)
	        print('Error in reading data from intellidataEmployeeTable')
	        raise e
