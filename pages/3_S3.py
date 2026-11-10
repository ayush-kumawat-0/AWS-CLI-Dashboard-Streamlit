import streamlit as st
from components.sidebar import sidebar_fun 

st.set_page_config(
    page_title = "S3 Management",
    page_icon = "🪣",
    layout = "wide"
)

with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

sidebar_fun()

col1 , col2 = st.columns([4,1])

with col1:
    st.title("🪣 S3 Management")
    st.caption("Manage your Amazon S3 buckets and objects.")

# with col2:
    # st.button("🔄 Refresh", width="stretch")


st.divider()

st.subheader("Resource Overview")

col1 , col2 , col3 , col4 = st.columns(4)

with col1:
    st.metric("Total Buckets","4")

with col2:
    st.metric("Total Objects", "130")

with col3:
    st.metric("Active Regions", "3")

with col4:
    st.metric("Storage Service", "1")


st.divider()

st.subheader("S3 Overview")

buckets = [
    {"Bucket Name": "project-backups-2026", "Region": "ap-south-1", "Objects": 24, "Created": "2026-10-12"},
    {"Bucket Name": "static-website-assets", "Region": "us-east-1", "Objects": 12, "Created": "2026-09-21"},
    {"Bucket Name": "application-logs-prod", "Region": "ap-south-1", "Objects": 86, "Created": "2026-08-15"},
    {"Bucket Name": "dev-storage-bucket", "Region": "eu-west-1", "Objects": 8, "Created": "2026-07-10"},
]

col1 , col2 = st.columns([3,1], vertical_alignment="bottom")

with col1:
    search = st.text_input("Search Buckets",placeholder="Search by bucket name or region...")

with col2:
    region_filter = st.selectbox(label="Select Region",options=["1","2"])

filtered_buckets = buckets

if search:
    filtered_buckets = [
        b for b in filtered_buckets
        if search.lower() in b["Bucket Name"].lower()
        or search.lower() in b["Region"].lower()
    ]

st.subheader("All Buckets")

st.dataframe(
    filtered_buckets,
    width="stretch",
    hide_index=True,
)