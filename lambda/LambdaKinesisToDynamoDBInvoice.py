import json
import boto3
import base64

def lambda_handler(event, context):
   print ("Event", event)
   client = boto3.resource("dynamodb")
   
   invoiceTable = client.Table("invoices")
   
   for record in event["Records"]:
      
       encoded_payload = record["data"] # base64 string
       # json_payload is the one actually send by kinesis producer
       json_payload = base64.b64decode(encoded_payload) # base64 to json string
       print("decoded ", json_payload)
       invoice = json.loads(json_payload) # load python object from json string
         
       invoice['InvoiceNo'] = str(invoice['InvoiceNo'])
       invoice["Amount"] = invoice["Quantity"] *   invoice["UnitPrice"] 
       invoice['Amount'] = str(invoice['Amount'])
       print("writing to dynamo", invoice)
       
       result = invoiceTable.put_item(Item={'InvoiceNo': invoice['InvoiceNo'], 'Amount':  invoice['Amount'] })
       print(result)    
