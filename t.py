import boto3

dynamodb = boto3.resource('dynamodb')
scanTable = dynamodb.Table('ScanTable')

