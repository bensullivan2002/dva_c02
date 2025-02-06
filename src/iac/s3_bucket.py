import boto3

s3 = boto3.client("s3")

s3.create_bucket(Bucket="my-test-buckt-8374598374", CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})
s3.upload_file("src/test.json", "my-test-buckt-8374598374", "test.json")
