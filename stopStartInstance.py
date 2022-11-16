import time
import boto3


def lambda_handler(event, context):

#Event
    print(event)

# Client
    client = boto3.client("ec2")
    InstanceId = ['i-0fe3a1b6c42a19e97']

# Stopping instance
    client.stop_instances(InstanceIds=InstanceId)
    print('Stop your instances: ' + str(InstanceId))    

# Getting instance information
    # time.sleep(240)
    estado = 1
    while (estado):
        describeInstance = client.describe_instances()

# fetchin instance id of the running instances
        for i in describeInstance["Reservations"]:
            for instance in i["Instances"]:
                if (instance["State"]["Name"] == "stopped") or (instance["State"]["Name"] == "termineted"):
                    print(f'Estados:  {instance["State"]["Name"]}\n')
                    estado = 0
                    #estado = estado+1
                else:
                    print(f'Estados:  {instance["State"]["Name"]}\n')
                    #estado = estado+1
        time.sleep(3)

# Count attempts                    
    attempts = 0
    while(True):
        try:
            client.start_instances(InstanceIds=InstanceId)
            print('Started your instances: ' + str(InstanceId)) 
            break
        except Exception as e:
            print(attempts,"-",e)
            attempts=attempts+1
