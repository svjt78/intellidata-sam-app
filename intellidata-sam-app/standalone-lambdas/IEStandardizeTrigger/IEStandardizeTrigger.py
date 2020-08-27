#Example: Create and Run a Glue Job
#The following example shows how call the AWS Glue APIs using Python, to create and run an ETL job.

import boto3

import json

def lambda_handler(event, context):
    # TODO implement
    glue = boto3.client(service_name='glue',
                         endpoint_url='https://glue.us-east-1.amazonaws.com')

    #Create a job. You must use glueetl as the name for the ETL command, as shown in the following code:

    myJob = glue.create_job(Name='intellidata-glue-job', Role='AWSGlueServiceRole', Command={'Name': 'glueetl', 'ScriptLocation': 's3://aws-glue-scripts-321504535921-us-east-1/root/intellidata-glue-job'})

    #Start a new run of the job that you created in the previous step:

    myNewJobRun = glue.start_job_run(JobName=myJob['Name'])

    #Get the job status:

   # status = glue.get_job_run(JobName=myJob['Name'], RunId=myNewJobRun['JobRunId'])

    #Print the current state of the job run:

    status = glue.get_job_run(JobName=myJob['Name'], RunId=myNewJobRun['JobRunId'])
    print ("GLUE_JOB run ID: " + myNewJobRun['JobRunId'])
    print ("GLUE_JOB run State: " +status['JobRun']['JobRunState'])
