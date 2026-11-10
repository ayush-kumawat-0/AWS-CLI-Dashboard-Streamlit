import streamlit as st
from components.sidebar import sidebar_fun 

st.set_page_config(
    page_title = "EC2 Management",
    page_icon = "🖥️",
    layout = "wide"
)

with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

sidebar_fun()

col1 , col2 = st.columns([4,1])

with col1:
    st.title("EC2 Management")
    st.caption("Manage and monitor your Amazon EC2 infrastructure.")

with col2:
    st.button("🔄 Refresh", use_container_width=True)


st.divider()

st.subheader("Resource Overview")

col1 , col2 , col3 , col4 = st.columns(4)

with col1:
    st.metric("Total instance", "12","+2")

with col2:
    st.metric("Running", "8","+1")

with col3:
    st.metric("Stopped", "3","-2")

with col4:
    st.metric("Terminated", "1")


st.divider()


st.subheader("Recent Instances")

col1 , col2 ,  col3 = st.columns(3)

with col1:
    if st.button("📋 View All Instances", use_container_width=True):
        st.switch_page("pages/EC2/ec2_instance_details.py")

with col2:
    if st.button("➕ Launch Instance", use_container_width=True):
        st.switch_page("pages/EC2/ec2_instance_details.py")

with col3:
    if st.button("🔐 Security Groups", use_container_width=True):
        st.switch_page("pages/EC2/ec2_instance_details.py")