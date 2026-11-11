import streamlit as st
import subprocess


def list_instances():
    result = subprocess.run(
        [   
            "aws", "ec2", "describe-instances",
            "--query",
            "Reservations[].Instances[].{Name: Tags[?Key=='Name']|[0].Value, \"Instance ID\": InstanceId, Type: InstanceType, State: State.Name}",
            "--output", "json"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return result.stdout
    else:
        return st.error(result.stderr)

