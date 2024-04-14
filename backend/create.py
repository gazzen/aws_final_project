import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MusicAlbums')


def lambda_handler(event, context):
    # Parse request body
    request_body = json.loads(event['body'])

    # Extract album details
    album_id = request_body['album_id']
    album_title = request_body['album_title']
    artist = request_body['artist']
    genre = request_body['genre']

    # Add album to DynamoDB
    table.put_item(
        Item={
            'album_id': album_id,
            'album_title': album_title,
            'artist': artist,
            'genre': genre
        }
    )

    # Return success response
    return {
        'statusCode': 200,
        'body': json.dumps('Album added successfully')
    }
