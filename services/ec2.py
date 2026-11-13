# This is the EC2 code
import subprocess
import json



def start_instance(instance_id):
    result = subprocess.run(
            ["aws", "ec2", "start-instances", "--instance-ids", instance_id],
            capture_output=True,
            text=True
        )
    
    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr
   

def stop_instance(instance_id):
    result = subprocess.run(
        ["aws", "ec2", "stop-instances", "--instance-ids", instance_id,],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr


def reboot_instance(instance_id):
    result = subprocess.run(
        ["aws", "ec2", "reboot-instances", "--instance-ids", instance_id],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr


def get_key_pairs():
    result = subprocess.run(
        [
            "aws", "ec2", "describe-key-pairs",
            "--query", "KeyPairs[].KeyName",
            "--output", "json"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return json.loads(result.stdout)

    return []


def create_key_pair(key_name):
    result = subprocess.run(
        [
            "aws", "ec2", "create-key-pair",
            "--key-name", key_name,
            "--query", "KeyMaterial",
            "--output", "text"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return True, result.stdout

    return False, result.stderr


def launch_instance_logic(instance_name, ami_id, instance_type, key_pair, num_instances):

    result = subprocess.run(
        [
            "aws", "ec2", "run-instances",
            "--image-id", ami_id,
            "--instance-type", instance_type,
            "--key-name", key_pair,
            "--count", str(num_instances),
            "--tag-specifications",
            f"ResourceType=instance,Tags=[{{Key=Name,Value={instance_name}}}]",
            "--output", "json"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return True, json.loads(result.stdout)

    return False, result.stderr



def terminate_instance(instance_id):
    result = subprocess.run(
        ["aws", "ec2", "terminate-instances", "--instance-ids", instance_id],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr