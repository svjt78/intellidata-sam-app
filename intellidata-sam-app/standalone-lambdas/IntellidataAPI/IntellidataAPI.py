import boto3
import json
import urllib.request

def lambda_handler(event, context):
	print (event)
	client = boto3.resource('s3')
	bucket=client.Bucket('intellidatastack-s3bucket2-1or0jvq5z9me6')
	other_bucket=client.Bucket('intellidatastack-s3bucket1-digncfllaejn')
	for obj in bucket.objects.all():
		key = obj.key
		body = obj.get()['Body'].read()
		data = body.decode("utf-8")
		data1 = data.split('\n')
		print(data1)
		obj_to_write = client.Object('intellidatastatic1', 'media/employers_nonstd.csv')
		obj_to_write.put(Body=data)
		bucket.objects.all().delete()
		other_bucket.objects.all().delete()
		break
