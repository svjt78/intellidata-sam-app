import boto3
import json
import urllib.request

def lambda_handler(event, context):
	print (event)
	client = boto3.resource('s3')
	bucket=client.Bucket('intellidatastack-s3bucket4-ei1vvvn7anez')
	other_bucket=client.Bucket('intellidatastack-s3bucket3-1ezrm28ljj9z9')
	for obj in bucket.objects.all():
		key = obj.key
		body = obj.get()['Body'].read()
		data = body.decode("utf-8")
		data1 = data.split('\n')
		print(data1)
		obj_to_write = client.Object('intellidatastatic1', 'media/employees_nonstd.csv')
		obj_to_write.put(Body=data)
		bucket.objects.all().delete()
		other_bucket.objects.all().delete()
		break
