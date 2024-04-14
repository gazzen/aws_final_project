import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MusicAlbums')


def lambda_handler(event, context):
    # Parse request body
    request_body = json.loads(event['body'])

    # Extract album details
    album_id = request_body['album_id']
    album_title = request_body.get('album_title')
    artist = request_body.get('artist')
    genre = request_body.get('genre')

    # Update album attributes in DynamoDB
    response = table.update_item(
        Key={'album_id': album_id},
        UpdateExpression='SET album_title = :title, artist = :artist, genre = :genre',
        ExpressionAttributeValues={
            ':title': album_title,
            ':artist': artist,
            ':genre': genre
        },
        ReturnValues='UPDATED_NEW'
    )

    # Return updated album details
    updated_album = response['Attributes']
    return {
        'statusCode': 200,
        'body': json.dumps(updated_album)
    }
