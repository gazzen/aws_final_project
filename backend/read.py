import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MusicAlbums')


def lambda_handler(event, context):
    # Get all albums from DynamoDB
    response = table.scan()
    albums = response['Items']

    # Return albums as JSON response
    return {
        'statusCode': 200,
        'body': json.dumps(albums)
    }
