import boto3


# Function helps to create a s3 bucket on AWS
def createbucket(bucket_name, bucket_location='None'):
    if bucket_location == 'None':
        s3_client = boto3.client('s3')
        s3_client.create_bucket(Bucket=bucket_name)
    else:
        s3_client = boto3.client('s3', region_name=bucket_location)
        location = {'LocationConstraint': bucket_location}
        s3_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=location)
    return "Bucket Created Successfully"



# Function to list all existing s3 buckets on the AWS account
def listallbuckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets() # Retrives all buckets data and stores in response var

    print('The Existing Buckets on the AWS account are: ')
    mybucket=[]
    for buck in response['Buckets']: # Print all buckets 
        mybucket.append(f'{buck["Name"]}')
    return mybucket

# List all files of a bucket
def listfiles(bucket):
    s3 = boto3.client('s3')
    contents = []
    for item in s3.list_objects(Bucket=bucket)['Contents']:
        contents.append(item)
    print (contents)
    return "Successfull Output On Console"


# Function helps to get all policies for a particular AWS bucket
def getbucketpolicy(bucket_name):
    s3_resource = boto3.client('s3')
    return(s3_resource.get_bucket_policy(Bucket=bucket_name))


# Function helps to delete all policies for a particular AWS bucket
def deletebucketpolicy(bucket_name):
    s3_resource = boto3.client('s3')
    return(s3_resource.delete_bucket_policy(Bucket=bucket_name))


# To upload any file to specified bucket
def uploadfile(file_name, bucket):
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    return "Successfully Uploaded"

# Function to download a given file from an S3 bucket
def downloadfile(file_name, bucket):
    s3 = boto3.resource('s3')
    output = f"downloads/{file_name}"
    s3.Bucket(bucket).download_file(file_name, output)
    return output


