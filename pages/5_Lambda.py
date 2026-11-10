import streamlit as st
from components.sidebar import sidebar_fun 

st.set_page_config(
    page_title = "Lambda Management",
    page_icon = "λ",
    layout = "wide"
)

with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

sidebar_fun()

col1 , col2 = st.columns([4,1])

with col1:
    st.title("λ Lambda Management")
    st.caption("Monitor and manage your AWS Lambda functions.")

# with col2:
    # st.button("🔄 Refresh", width="stretch")


st.divider()

st.subheader("Resource Overview")

functions = [
    {
        "Function Name": "user-authentication",
        "Runtime": "python3.12",
        "Memory (MB)": 256,
        "Timeout (sec)": 30,
        "Last Modified": "2026-10-20",
        "State": "Active"
    },
    {
        "Function Name": "image-processor",
        "Runtime": "python3.11",
        "Memory (MB)": 512,
        "Timeout (sec)": 60,
        "Last Modified": "2026-10-15",
        "State": "Active"
    },
    {
        "Function Name": "data-backup",
        "Runtime": "nodejs22.x",
        "Memory (MB)": 128,
        "Timeout (sec)": 15,
        "Last Modified": "2026-09-28",
        "State": "Active"
    },
    {
        "Function Name": "log-cleanup",
        "Runtime": "python3.12",
        "Memory (MB)": 128,
        "Timeout (sec)": 20,
        "Last Modified": "2026-09-10",
        "State": "Inactive"
    },
]

c1 , c2 , c3 , c4 = st.columns(4)

with c1:
    st.metric("Total Functions", len(functions))
with c2:
    st.metric("Active Functions", sum(f["State"] == "Active" for f in functions))
with c3:
    st.metric("Inactive Functions", sum(f["State"] == "Inactive" for f in functions))
with c4:
    st.metric("Runtimes", len(set(f["Runtime"] for f in functions)))


st.divider()

st.subheader("Lambda Function Management")
st.caption("View and manage your serverless functions.")



col1 , col2 = st.columns([3,1], vertical_alignment="bottom")

with col1:
    search = st.text_input("Search Functions",placeholder="Search by function name or runtime...")

with col2:
    state_filter = st.selectbox(
        "Function State",
        ["All Functions", "Active", "Inactive"]
    )

filtered_functions = functions

if search:
    filtered_functions = [
        f for f in filtered_functions
        if search.lower() in f["Function Name"].lower()
        or search.lower() in f["Runtime"].lower()
    ]

st.subheader("All Lambda Functions")

st.dataframe(
    filtered_functions,
    width="stretch",
    hide_index=True,
)