import streamlit as st
import subprocess
import json
import pandas as pd
from components.sidebar import sidebar_fun 
from pages.EC2.ec2_launch import launch_instance_dialog
from services.ec2 import start_instance,stop_instance,reboot_instance,terminate_instance
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



col1 , col2 = st.columns([4,1],vertical_alignment="bottom")

with col1:
    st.title("🖥️ EC2 Management")
    st.caption("Manage and monitor your Amazon EC2 infrastructure.")

with col2:
    if st.button("🔄 Refresh", width="stretch"):
        st.rerun()


st.divider()

instances = json.loads(list_instances())

total_instances = len(instances)

running_instances = sum(
    1 for instance in instances
    if instance["State"] == "running"
)

stopped_instances = sum(
    1 for instance in instances
    if instance["State"] == "stopped"
)

terminated_instances = sum(
    1 for instance in instances
    if instance["State"] == "terminated"
)

st.subheader("Resource Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Instances", total_instances)

with col2:
    st.metric("Running", running_instances)

with col3:
    st.metric("Stopped", stopped_instances)

with col4:
    st.metric("Terminated", terminated_instances)

st.divider()


st.subheader("Instance Overview")




col1 , col2 = st.columns([3,1], vertical_alignment="bottom")
with col1:
    search = st.text_input("Search Instance",placeholder="Search by name or instance ID...",type="search")

with col2:
    if st.button("➕ Launch Instance", width="stretch"):
        launch_instance_dialog()



filtered_instances = instances.copy()

if search:
    filtered_instances = [
        instance for instance in filtered_instances
        if search.lower() in (instance.get("Name") or "").lower()
        or search.lower() in instance["Instance ID"].lower()
    ]


event = st.dataframe(
    filtered_instances,
    width="stretch",
    hide_index=True,
    on_select="rerun",
    selection_mode="single-row",
    key="instance_table",
)

st.subheader("Instance Actions")

selected_rows = event.selection.rows

if not selected_rows:
    st.info("Click a row in the table above to select an instance.")
else:
    selected_Instance = filtered_instances[selected_rows[0]]
    name = selected_Instance.get("Name") or "Unnamed"
    instance_id = selected_Instance["Instance ID"]

    col1, col2 = st.columns([4, 1], vertical_alignment="center")

    with col1:
        st.markdown(f"**Selected:** {name} ({instance_id}) · {selected_Instance['State']}")

        display_instance = full_instance_detail(instance_id)
        if display_instance:
            df = pd.DataFrame(display_instance.items(), columns=["Property", "Value"])
            st.dataframe(df, width="stretch", hide_index=True)

    with col2:
        if st.button("▶️ Start", width="stretch"):
            start_instance(instance_id)
            st.toast(f"Instance {name} started successfully!", icon="✅")

        if st.button("⏹️ Stop", width="stretch"):
            stop_instance(instance_id)
            st.toast(f"Instance {name} stopped successfully!", icon="✅")

        if st.button("🔄 Reboot", width="stretch"):
            reboot_instance(instance_id)
            st.toast(f"Instance {name} reboot request sent!", icon="🔄")

        if st.button("🗑️ Terminate", width="stretch"):
            terminate_instance(instance_id)
            st.toast(f"Instance {name} termination request sent!", icon="⚠️")