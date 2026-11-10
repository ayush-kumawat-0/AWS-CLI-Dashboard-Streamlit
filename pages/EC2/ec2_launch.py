import streamlit as st

with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

@st.dialog("Launch Instance", width="medium")
def launch_instance():
    name = st.text_input("Instance Name", placeholder="Enter instance name")

    col1, col2 = st.columns(2)
    with col1:        
        ami_id = st.text_input("AMI ID", placeholder="Enter AMI ID")
    with col2:
        instance_type = st.selectbox("Instance Type", ["t2.micro", "t2.small", "t2.medium"])


    col1, col2 = st.columns(2)
    with col1:
        key_pair = st.selectbox("Key pair", ["my-key"])
    with col2:
        num_instances = st.number_input("Number of Instances", min_value=1, max_value=10, value = 1)


    st.divider()
    c1,c2 = st.columns(2)
    with c1:
        cancel = st.button("Cancel",width="stretch",type="secondary")
    with c2:
        launch = st.button("Launch", width="stretch",type="primary")

    if cancel:
        st.rerun()

    if launch:
        #launch logic
        st.success(f"Launching {num_instances} instance(s) of type {instance_type} with name '{name}' and AMI ID '{ami_id}'")

    else:
        st.info("Fill in the details and click 'Launch Instance' to proceed.")