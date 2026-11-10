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


st.subheader("Instance Overview")


# st.subheader("Recent Instances")

# col1 , col2 ,  col3 = st.columns(3)

# with col1:
#     if st.button("📋 View All Instances", use_container_width=True):
#         st.switch_page("pages/EC2/ec2_instance_details.py")

# with col2:
#     if st.button("➕ Launch Instance", use_container_width=True):
#         st.switch_page("pages/EC2/ec2_instance_details.py")

# with col3:
#     if st.button("🔐 Security Groups", use_container_width=True):
#         st.switch_page("pages/EC2/ec2_instance_details.py")


instances = [
    {
        "Name": "Web-Server",
        "Instance ID": "i-0a1234567890abcd1",
        "Type": "t2.micro",
        "State": "Running"
    },
    {
        "Name": "Database-Server",
        "Instance ID": "i-0b1234567890abcd2",
        "Type": "t2.medium",
        "State": "Stopped"
    },
    {
        "Name": "Test-Server",
        "Instance ID": "i-0c1234567890abcd3",
        "Type": "t3.micro",
        "State": "Running"
    }
]

col1 , col2 = st.columns([3,1], vertical_alignment="bottom")

with col1:
    search = st.text_input("Search Instance",placeholder="Search by name or instance ID...",type="search")

with col2:
    if st.button("➕ Launch Instance", use_container_width=True):
        st.switch_page("pages/EC2/ec2_instance_details.py")

if not search:
    filtered_instances = instances
else:
    filtered_instances = []

for instance in instances:
    if search.lower() in instance["Name"].lower() or search.lower() in instance["Instance ID"].lower():
        filtered_instances.append(instance)



st.dataframe(
    filtered_instances,
    use_container_width=True,
    hide_index=True,
)




st.subheader("Instance Actions")


col1,col2 = st.columns([4,1],vertical_alignment="top")

with col1:
    selected_Instance = st.selectbox(label="Select an Instance",options=["1","2"])

with col2:
    if st.button("▶️Start", use_container_width=True):
        st.info("Not yet started")
    if st.button("⏹️Stop", use_container_width=True):
        st.info("Not yet started")
    if st.button("🔄Reboot", use_container_width=True):
        st.info("Not yet started")
    if st.button("🗑️Terminate", use_container_width=True):
        st.info("Not yet started")