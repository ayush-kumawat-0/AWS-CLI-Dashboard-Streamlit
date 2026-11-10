import streamlit as st

def sidebar_fun():
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