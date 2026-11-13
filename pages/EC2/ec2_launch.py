
import streamlit as st
import base64

from services.ec2 import (
    get_key_pairs,
    create_key_pair,
    launch_instance_logic
)


# Replace these placeholder IDs with valid AMI IDs from your AWS region.
AMI_OPTIONS = {
    "Amazon Linux": "ami-04b0b8ee9ce90920a",
    "Ubuntu 24.04 LTS": "ami-083cf4acad89c8905",
    "Red Hat Enterprise Linux": "ami-0866e0e2b09f899d8",
    "Windows Server": "ami-0b17a4758d56fcf2e"
}


@st.dialog("Launch Instance", width="medium")
def launch_instance_dialog():

    instance_name = st.text_input(
        "Instance Name",
        placeholder="Enter instance name"
    )

    # AMI selection
    ami_name = st.selectbox(
        "Select AMI",
        options=list(AMI_OPTIONS.keys()),
        format_func=lambda x: f"{x} ({AMI_OPTIONS[x]})"
    )

    ami_id = AMI_OPTIONS[ami_name]

    # Instance configuration
    col1, col2 = st.columns(2)

    with col1:
        instance_type = st.selectbox(
            "Instance Type",
            ["t2.micro", "t2.small", "t2.medium"]
        )

    with col2:
        num_instances = st.number_input(
            "Number of Instances",
            min_value=1,
            max_value=10,
            value=1
        )

    st.divider()

    # Fetch existing key pairs
    key_pairs = get_key_pairs()

    st.subheader("SSH Key Pair")

    if key_pairs:

        key_pair = st.selectbox(
            "Select Existing Key Pair",
            options=key_pairs
        )

    else:
        key_pair = None
        st.warning("No existing key pairs found in this AWS region.")

    # Create new key pair
    with st.expander("Create New Key Pair"):

        new_key_name = st.text_input(
            "New Key Pair Name",
            placeholder="Enter key pair name"
        )

        if st.button("Create Key Pair", width="stretch"):

            if not new_key_name.strip():
                st.warning("Enter a key pair name.")

            else:
                success, response = create_key_pair(new_key_name.strip())

                if success:

                    st.success("Key pair created successfully!")

                    # Download private key
                    st.download_button(
                        label="Download Private Key (.pem)",
                        data=response,
                        file_name=f"{new_key_name.strip()}.pem",
                        mime="application/x-pem-file"
                    )

                    st.info(
                        "Download and securely store this private key. "
                        "AWS will not provide it again."
                    )

                    st.rerun()

                else:
                    st.error("Unable to create key pair.")
                    st.code(response)

    st.divider()

    # Launch / Cancel
    col1, col2 = st.columns(2)

    with col1:
        cancel = st.button(
            "Cancel",
            width="stretch",
            type="secondary"
        )

    with col2:
        launch = st.button(
            "Launch",
            width="stretch",
            type="primary"
        )

    if cancel:
        st.rerun()

    if launch:

        if not instance_name.strip():
            st.warning("Please enter an instance name.")

        elif ami_id == "ami-xxxxxxxx":
            st.warning("Please configure a valid AMI ID.")

        elif not key_pair:
            st.warning("Please select or create a key pair.")

        else:

            success, response = launch_instance_logic(
                instance_name.strip(),
                ami_id,
                instance_type,
                key_pair,
                num_instances
            )

            if success:

                st.success(
                    f"Launch request submitted for "
                    f"{num_instances} instance(s)!"
                )

                st.json(response)

            else:

                st.error("Failed to launch EC2 instance.")
                st.code(response)
