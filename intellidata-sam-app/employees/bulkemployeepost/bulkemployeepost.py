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
	data = []
	data=json.loads(event['body'])


	for ix in range(len(data)):

		  try:
			  table.put_item(
		         Item={
		            'EMPLOYEE_ID': data[ix]["employeeid"],
		            'LOCAL_ID': data[ix]["id"],
					'ITEM_ID': ts,
					'SSN': data[ix]["ssn"],
		            'NAME': data[ix]["name"],
		            'SLUG': data[ix]["slug"],
					'GENDERCODE': data[ix]["gendercode"],
		            'AGE': data[ix]["age"],
					'BIRTHDATE': data[ix]["birthdate"],
					'MARITALSTATUS': data[ix]["maritalstatus"],
					'HOME_ADDRESS_LINE_1': data[ix]["home_address_line_1"],
					'HOME_ADDRESS_LINE_2': data[ix]["home_address_line_2"],
					'HOME_CITY': data[ix]["home_city"],
					'HOME_STATE': data[ix]["home_state"],
					'HOME_ZIPCODE': data[ix]["home_zipcode"],
					'MAIL_ADDRESS_LINE_1': data[ix]["mail_address_line_1"],
					'MAIL_ADDRESS_LINE_2': data[ix]["mail_address_line_2"],
					'MAIL_CITY': data[ix]["mail_city"],
					'MAIL_STATE': data[ix]["mail_state"],
					'MAIL_ZIPCODE': data[ix]["mail_zipcode"],
					'WORK_ADDRESS_LINE_1': data[ix]["work_address_line_1"],
					'WORK_ADDRESS_LINE_2': data[ix]["work_address_line_2"],
					'WORK_CITY': data[ix]["work_city"],
					'WORK_STATE': data[ix]["work_state"],
					'WORK_ZIPCODE': data[ix]["work_zipcode"],
					'EMAIL': data[ix]["email"],
					'ALTERNATE_EMAIL': data[ix]["alternate_email"],
					'HOME_PHONE': data[ix]["home_phone"],
					'WORK_PHONE': data[ix]["work_phone"],
					'MOBILE_PHONE': data[ix]["mobile_phone"],
					'ENROLLMENT_METHOD': data[ix]["enrollment_method"],
					'EMPLOYMENT_INFORMATION': data[ix]["employment_information"],
					'EMPLOYER': data[ix]["employer"],
					'CREATOR': data[ix]["creator"],
					'EMPLOYEE_DATE': data[ix]["employee_date"],
					'SMS': data[ix]["sms"],
					'EMAILER': data[ix]["emailer"],
					'ARTEFACT': data[ix]["artefact"],
					'CONNECTION': data[ix]["backend_SOR_connection"],
					'RESPONSE': data[ix]["response"],
					'COMMIT_INDICATOR': data[ix]["commit_indicator"],
					'RECORD_STATUS': data[ix]["record_status"],


	        		 }
	    		)


		  except Exception as e:
		        print(e)
		        print('Error in reading data from intellidataEmployeeTable')
		        raise e
