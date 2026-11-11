import streamlit as st
import subprocess
import json

def full_instance_detail(instance_id):

    result = subprocess.run(
        [
            "aws", "ec2", "describe-instances",
            "--instance-ids", instance_id,
            "--query",
            "Reservations[0].Instances[0].{Name:Tags[?Key=='Name']|[0].Value,InstanceId:InstanceId,State:State.Name,InstanceType:InstanceType,ImageId:ImageId,PublicIP:PublicIpAddress,PrivateIP:PrivateIpAddress,PublicDNS:PublicDnsName,PrivateDNS:PrivateDnsName,VPC:VpcId,Subnet:SubnetId,AvailabilityZone:Placement.AvailabilityZone,KeyPair:KeyName,LaunchTime:LaunchTime,SecurityGroups:SecurityGroups,Volumes:BlockDeviceMappings,IAMProfile:IamInstanceProfile,Architecture:Architecture,Platform:PlatformDetails}",
            "--output", "json"
            
        ],
        capture_output=True,
        text=True
    )

    # AWS CLI returns JSON through stdout, Python receives it as a string
    # json.loads() converts that string into Python objects.

    if result.returncode == 0:
        return json.loads(result.stdout)
    else:
        st.error(result.stderr)
        return None