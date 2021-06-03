import json
import boto3

def lambda_handler(event, context):
   print ("Event", event)
   client = boto3.resource("dynamodb")
   
   invoiceTable = client.Table("invoices")
   
   for record in event["Records"]:
       body = record["body"]
       print("Body", body)
       invoice = json.loads(body)
       invoice['InvoiceNo'] = str(invoice['InvoiceNo'])
       invoice['Amount'] = str(invoice['Amount'])
       print("writing to dynamo", invoice)
       
       result = invoiceTable.put_item(Item={'InvoiceNo': invoice['InvoiceNo'], 'Amount':  invoice['Amount'] })
       print(result)    
