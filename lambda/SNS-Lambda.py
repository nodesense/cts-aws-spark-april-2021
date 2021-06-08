import json
import boto3

def lambda_handler(event, context):
    sns = boto3.client("sns", 
                   region_name="us-east-2")
                   
    sns.publish(TopicArn="arn:aws:sns:us-east-2:495478549549:low-inventory", 
            Message="Apple 432423432 low stock", 
            Subject="apple no more..")
