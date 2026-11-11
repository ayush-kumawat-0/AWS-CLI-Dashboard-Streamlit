# This is the EC2 code
import subprocess




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


def launch_instance():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("       LAUNCH INSTANCE")
    print(f"============================{RESET}\n")

    ami_id = input(f"{BLUE}AMI ID: {RESET}").strip()
    instance_type = input(f"{BLUE}Instance type: {RESET}").strip()

    print(f"\n{YELLOW}Launching EC2 instance...{RESET}\n")

    result = subprocess.run(
        [
            "aws", "ec2", "run-instances",
            "--image-id", ami_id,
            "--instance-type", instance_type,"--output", "table"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ Instance launch request successful.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()


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