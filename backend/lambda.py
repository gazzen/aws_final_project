import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('musical_song')


def lambda_handler(event, context):
    if event['httpMethod'] == 'GET':
        # Perform read operation
        response = table.scan()
        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'])
        }
    elif event['httpMethod'] == 'POST':
        # Perform create operation
        data = json.loads(event['body'])
        table.put_item(Item=data)
        return {
            'statusCode': 200,
            'body': 'Item created successfully'
        }
   