import boto3
import json

def lambda_handler(event, context):

	print (event)

	s3 = boto3.resource('s3')
    obj_to_read = s3.Object('intellidatastatic1', 'media/employers.csv')
    body = obj_to_read.get()['Body'].read()

	s3 = boto3.resource('s3')
	obj = s3.Object('my-bucket','hello.json')
	data = obj.get()['Body'].read()
	print data

	bucket = 'intellidatastack-s3bucket2-1b2bujg9v2qau'

	for obj in bucket.objects.all():
    		key = obj.key
    		body = obj.get()['Body'].read()
    		data = body.decode("utf-8")
    		data1 = data.split('\n')

			print(data1)

    		#client.delete_object(Bucket=bucket, Key=key)
    		#client.Object(bucket, key).delete()
    		bucket.delete_key(keyname.key)
    		#key.delete()

    		for ix in range(len(data1)):
    				data_dic = json.loads(data1[ix])
    				recordId = str(uuid.uuid4())
    				table.put_item(
   			    		Item={
            				'ItemID': recordId,
            				'MEMBERID': data_dic["enrolee_id"],
            				'FIRSTNAME': data_dic["fname"],
            				'LASTNAME': data_dic["lname"],
            				'STREET': data_dic["street"],
            				'CITY': data_dic["city"],
            				'STATE': data_dic["state"],
            				'ZIP': data_dic["zip"],
            				'AGE': data_dic["age"],
            				'PHONE': data_dic["contact"],
            				'SMOKER': data_dic["smoker?"],
            				'GENDER': data_dic["gender"],
            				'COVERAGE': data_dic["maxamount"],
    				    	'UW_DECISION' : 'Y'
    				    #	'INCOME': data_dic["income"],
    				    #	'EXECUTIVE_STATUS': data_dic["executivestatus"]
    					}
					)

					bucket.objects.all().delete()
					break



			#End of code
