
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AWS Automation Dashboard",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Sidebar
with st.sidebar:

    st.title("☁️ AWS Dashboard")

    st.markdown("---")

    st.page_link("app.py", label="Home", icon="🏠")
    st.page_link("pages/2_EC2.py", label="EC2", icon="🖥️")
    st.page_link("pages/3_S3.py", label="S3", icon="🪣")
    st.page_link("pages/4_IAM.py", label="IAM", icon="🔐")
    st.page_link("pages/5_Lambda.py", label="Lambda", icon="⚡")
    st.page_link("pages/6_API_Gateway.py", label="API Gateway", icon="🌐")
    st.page_link("pages/7_Account_Info.py", label="Account Info", icon="👤")


# Main Header
col1, col2 = st.columns([4, 1])

with col1:
    st.title("AWS Automation Dashboard")
    st.caption("Manage AWS resources using Python and AWS CLI")

with col2:
    st.success("● AWS CLI Connected")


st.divider()


# Resource Statistics
st.subheader("Resource Overview")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("EC2 Instances", "12", "+2")

with col2:
    st.metric("S3 Buckets", "8", "+1")

with col3:
    st.metric("IAM Users", "6")

with col4:
    st.metric("Lambda Functions", "4")

with col5:
    st.metric("API Gateways", "3")


st.divider()


# AWS Services
st.subheader("AWS Services")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.subheader("🖥️ EC2")
        st.write("Manage virtual servers and instances.")
        st.page_link("pages/2_EC2.py", label="Manage EC2 →")

    with st.container(border=True):
        st.subheader("🔐 IAM")
        st.write("Manage users, roles and permissions.")
        st.page_link("pages/4_IAM.py", label="Manage IAM →")

with col2:
    with st.container(border=True):
        st.subheader("🪣 S3")
        st.write("Manage storage buckets and objects.")
        st.page_link("pages/3_S3.py", label="Manage S3 →")

    with st.container(border=True):
        st.subheader("⚡ Lambda")
        st.write("Manage and execute Lambda functions.")
        st.page_link("pages/5_Lambda.py", label="Manage Lambda →")

with col3:
    with st.container(border=True):
        st.subheader("🌐 API Gateway")
        st.write("Create and manage API endpoints.")
        st.page_link("pages/6_API_Gateway.py", label="Manage API Gateway →")


st.divider()


# Quick Actions
st.subheader("Quick Actions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("List EC2 Instances", use_container_width=True):
        st.switch_page("pages/2_EC2.py")

with col2:
    if st.button("List S3 Buckets", use_container_width=True):
        st.switch_page("pages/3_S3.py")

with col3:
    if st.button("List IAM Users", use_container_width=True):
        st.switch_page("pages/4_IAM.py")
