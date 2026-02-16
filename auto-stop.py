<<<<<<< HEAD

=======
import boto3
ec2 = boto3.resource('ec2')

# Find all running instances
instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

for instance in instances:
    # Check if 'Project' key exists in tags
    tags = {tag['Key']: tag['Value'] for tag in instance.tags} if instance.tags else {}
    
    if 'Project' not in tags:
        print(f"Stopping instance {instance.id} - Missing Project Tag")
        instance.stop()
>>>>>>> b99bbbc (cost saver final)
