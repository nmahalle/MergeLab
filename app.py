import boto3
client = boto3.client('ec3')
response = client.terminate_instance(
	InstanceIds=[
		'i-035dfdfd54343sdfsdf43'
],
)
