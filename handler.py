import json, boto3, logging, os

logger = logging.getLogger()
logger.setLevel(logging.INFO)



def hello(event, body):
    reqBody = json.loads(event['body'])
    logger.info(reqBody)
    resource = ''.join([reqBody.get('resource_id'),'.pdf'])
    s3Client = boto3.client('s3')
    url = s3Client.generate_presigned_url('get_object', Params = {'Bucket': os.getenv('bucket'), 'Key': resource}, ExpiresIn = 100)

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": "true"
        },
        "body": json.dumps(url)
    }

    return response
