import json
import boto3
import base64
from decimal import Decimal


def lambda_handler(event, context):
   print ("Event", event)
   client = boto3.resource("dynamodb")
   
   invoiceTable = client.Table("invoices")
   
   for record in event["Records"]:
       kinesis = record["kinesis"]
       encoded_payload = kinesis["data"] # base64 string
       # json_payload is the one actually send by kinesis producer
       json_payload = base64.b64decode(encoded_payload) # base64 to json string
       print("decoded ", json_payload)
       invoice = json.loads(json_payload) # load python object from json string
         
       invoice['InvoiceNo'] = str(invoice['InvoiceNo'])
       invoice["Amount"] =    Decimal(invoice["UnitPrice"] * invoice["Quantity"])
       invoice["UnitPrice"] = Decimal(invoice["UnitPrice"] )
       print("writing to dynamo", invoice)
        
       #result = invoiceTable.put_item(Item={'InvoiceNo': invoice['InvoiceNo'], 'Amount':  invoice['Amount'] })
       result = invoiceTable.put_item(Item=invoice)
        
       print(result)    
