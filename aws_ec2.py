import boto3, os

# Creata any instance
def create_instance(keyname):
    ec2_client = boto3.client("ec2", region_name="us-west-2")
    key_pair = ec2_client.create_key_pair(KeyName=keyname)

    private_key = key_pair["KeyMaterial"]
    with os.fdopen(os.open("/tmp/%s.pem" %keyname, os.O_WRONLY | os.O_CREAT, 0o400), "w+") as handle:
        handle.write(private_key)
    ec2_client = boto3.client("ec2", region_name="us-west-2")
    instances = ec2_client.run_instances(
        ImageId="ami-0b0154d3d8011b0cd",
        MinCount=1,
        MaxCount=1,
        InstanceType="t4g.nano",
        KeyName=keyname
    )

    print(instances["Instances"][0]["InstanceId"])
    return 'created'

# Get public Ip of any instance using instance ID
def get_public_ip(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-west-2")
    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")
    str = ''
    for reservation in reservations:
        for instance in reservation['Instances']:
            str = (instance.get("PublicIpAddress"))
    return str


# Get all running instances on the server
def get_running_instances():

    ec2_client = boto3.client("ec2", region_name="us-west-2")
    reservations = ec2_client.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
        }
    ]).get("Reservations")

    myinstance=[[]]
    for reservation in reservations:
        for instance in reservation["Instances"]:
            myin=[]
            instance_id = instance["InstanceId"]
            myin.append(instance_id)
            instance_type = instance["InstanceType"]
            myin.append(instance_type)
            public_ip = instance["PublicIpAddress"]
            myin.append(public_ip)
            private_ip = instance["PrivateIpAddress"]
            myin.append(private_ip)
            print(f"{instance_id}, {instance_type}, {public_ip}, {private_ip}")
            myinstance.append(myin)
    return myinstance


# To stop any insatnce using instance_id
def stopinstance(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-west-2")
    response = ec2_client.stop_instances(InstanceIds=[instance_id])
    print(response)
    return 'Your Instance Has Been Stopped'


# To terminate any insatnce using instance_id
def terminateinstance(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-west-2")
    response = ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(response)
    return 'Your Instance Has Been Terminated'



# To reboot any insatnce using instance_id
def rebootinstance(instance_id):
    ec2 = boto3.client('ec2',region_name="us-west-2")
    ec2.reboot_instances(InstanceIds=[instance_id])
    return 'Instance Reboot Successful'
