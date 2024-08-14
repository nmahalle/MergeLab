import boto4
client = boto3.client('ec2')
response = client.terminate_instance(
	InstanceIds=[
		'i-035dfdfd54343sdfsdf43'
],
)
