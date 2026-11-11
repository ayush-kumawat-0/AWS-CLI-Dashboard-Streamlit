import streamlit as st
import subprocess
import json
import pandas as pd
from components.sidebar import sidebar_fun 
from services.ec2 import start_instance,stop_instance,reboot_instance,terminate_instance,launch_instance
from pages.EC2.ec2_instances import list_instances
from pages.EC2.ec2_instance_details import full_instance_detail

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
    st.title("🖥️ EC2 Management")
    st.caption("Manage and monitor your Amazon EC2 infrastructure.")

with col2:
    if st.button("🔄 Refresh", width="stretch"):
        st.rerun()


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




col1 , col2 = st.columns([3,1], vertical_alignment="bottom")
with col1:
    search = st.text_input("Search Instance",placeholder="Search by name or instance ID...",type="search")

with col2:
    if st.button("➕ Launch Instance", width="stretch"):
        launch_instance()



filtered_instances = json.loads(list_instances())

if search:
    filtered_instances = [
        instance for instance in filtered_instances
        if search.lower() in (instance.get("Name") or "").lower()
        or search.lower() in instance["Instance ID"].lower()
    ]


st.dataframe(
    filtered_instances,
    width="stretch",
    hide_index=True,
)




st.subheader("Instance Actions")


col1,col2 = st.columns([4,1],vertical_alignment="top")

with col1:
    selected_Instance = st.selectbox(label="Select an Instance",options=filtered_instances,format_func=lambda x: f"{x.get('Name') or 'Unamed'} ({x['Instance ID']}) - {x['State']}")

    display_instance = full_instance_detail(selected_Instance["Instance ID"])

    if display_instance:
        df = pd.DataFrame(
            display_instance.items(),
            columns=["Property", "Value"]
        )

    st.dataframe(
        df,
        width="stretch",
        hide_index=True
    )

with col2:
    if st.button("▶️ Start", width="stretch"):
        start_instance(selected_Instance["Instance ID"])
        st.toast(f"Instance {selected_Instance.get('Name') or 'Unnamed'} started successfully!", icon="✅")

    if st.button("⏹️ Stop", width="stretch"):
        stop_instance(selected_Instance["Instance ID"])
        st.toast(f"Instance {selected_Instance.get('Name') or 'Unnamed'} stopped successfully!", icon="✅")

    if st.button("🔄 Reboot", width="stretch"):
        reboot_instance(selected_Instance["Instance ID"])
        st.toast(f"Instance {selected_Instance.get('Name') or 'Unnamed'} reboot request sent!", icon="🔄")

    if st.button("🗑️ Terminate", width="stretch"):
        terminate_instance(selected_Instance["Instance ID"])
        st.toast(f"Instance {selected_Instance.get('Name') or 'Unnamed'} termination request sent!", icon="⚠️")