import streamlit as st
from components.sidebar import sidebar_fun 

st.set_page_config(
    page_title = "IAM Management",
    page_icon = "🛡️",
    layout = "wide"
)

with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

sidebar_fun()

col1 , col2 = st.columns([4,1])

with col1:
    st.title("🛡️ IAM Management")
    st.caption("Manage IAM users, groups, roles and permissions.")

# with col2:
    # st.button("🔄 Refresh", width="stretch")


st.divider()

st.subheader("Resource Overview")

users = [
    {"User Name": "admin-user", "User ID": "AIDA001", "Created": "2026-08-12", "Status": "Active"},
    {"User Name": "developer", "User ID": "AIDA002", "Created": "2026-09-05", "Status": "Active"},
    {"User Name": "test-user", "User ID": "AIDA003", "Created": "2026-09-20", "Status": "Active"},
    {"User Name": "backup-user", "User ID": "AIDA004", "Created": "2026-10-01", "Status": "Active"},
]

roles = [
    {"Role Name": "EC2-Admin-Role", "Role ID": "AROA001", "Created": "2026-08-10"},
    {"Role Name": "Lambda-Execution-Role", "Role ID": "AROA002", "Created": "2026-09-15"},
    {"Role Name": "S3-ReadOnly-Role", "Role ID": "AROA003", "Created": "2026-10-02"},
]

col1 , col2 , col3 , col4 = st.columns(4)

with col1:
    st.metric("Total Users",len(users))

with col2:
    st.metric("Total Roles", len(roles))

with col3:
    st.metric("Active Users", len(users))

with col4:
    st.metric("IAM Groups", "-")


st.divider()

st.subheader("IAM Overview")

t1,t2 =st.tabs(["Users","Roles"])

with t1:
    col1 , col2 = st.columns([3,1], vertical_alignment="bottom")

    with col1:
        user_search = st.text_input("Search Users",placeholder="Search by username or user ID....")

    with col2:
        user_filter = st.selectbox("User Status",["All Users", "Active"],)

    filtered_users = users

    if user_search:
        filtered_users = [
            u for u in filtered_users
            if user_search.lower() in u["User Name"].lower()
            or user_search.lower() in u["User ID"].lower()
        ]

    st.subheader("All Buckets")

    st.dataframe(
        filtered_users,
        width="stretch",
        hide_index=True,
    )

with t2:
    # col1 , col2 = st.columns([3,1], vertical_alignment="bottom")

    # with col1:
    role_search = st.text_input("Search Roles",placeholder="Search by role name or role ID...")

    # with col2:
    #     role_filter = st.selectbox("User Status",["All Users", "Active"],)

    filtered_roles = [
        r for r in roles
        if role_search.lower() in r["Role Name"].lower()
        or role_search.lower() in r["Role ID"].lower()
    ] if role_search else roles

    # st.subheader("All Buckets")

    st.dataframe(
        filtered_roles,
        width="stretch",
        hide_index=True,
    )