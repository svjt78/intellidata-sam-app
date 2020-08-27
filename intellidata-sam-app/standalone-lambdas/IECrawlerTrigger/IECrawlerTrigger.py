#Update glue crawler

import boto3
import json

def lambda_handler(event, context):

	print (event)
	glue_client = boto3.client(service_name='glue',
              endpoint_url='https://glue.us-east-1.amazonaws.com')

	response = glue_client.start_crawler(Name = 'intellidata-employer')
