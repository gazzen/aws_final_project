import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MusicAlbums')

def lambda_handler(event, context):
    # Parse request body
    request_body = json.loads(event['body'])
    
    # Extract album ID
    album_id = request_body['album_id']
    
    # Delete album from DynamoDB
    table.delete_item(
        Key={'album_id': album_id}
    )
    
    # Return success response
    return {
        'statusCode': 200,
        'body': json.dumps('Album deleted successfully')
    }
