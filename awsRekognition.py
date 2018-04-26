
import boto3
import os.path
import requests

###
# Process a local file and use AWS Rekognition detect labels and confidence factor
###
def process_local_file(file_name, aws_client):
    with open(file_name, 'rb') as imageBytes:
        response = aws_client.detect_labels(Image={'Bytes': imageBytes.read()})
        print('Detected labels in ' + file_name)
        return response


def process_s3_file(file_name, bucket, aws_client):
    response = aws_client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':file_name}})
    print('Detected labels in ' + file_name +' in S3 bucket ' + bucket)
    return response

def init_process_local_file(file_name):
    aws_client=boto3.client('rekognition','eu-west-1')
    response = process_local_file(file_name, aws_client)
    url_to_call = 'http://localhost:3000/trash'
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
        if label['Name'] in ['Cup']:
            print('We will Trash this. Matched: ' + label['Name'])
            url_to_call = 'http://localhost:3000/trash'
            break
        if label['Name'] in ['Paper', 'Food']:
            print('We will recycle this. Matched: ' + label['Name'])
            url_to_call = 'http://localhost:3000/recycle'
            break
    print('Will call: ' + url_to_call)
    requests.get(url_to_call)
        



if __name__ == "__main__":
    fileName='input.jpg'
    bucket='rekognition-examples-bucket'
    imageFileName='/var/tmp/IMG_4209.JPG'
    capturedImage='/var/tmp/capturedImage.JPG'
    
    client=boto3.client('rekognition','eu-west-1')

    response = process_local_file(imageFileName, client)   
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
 