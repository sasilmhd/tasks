import streamlit as st
import pandas as pd
from datetime import date

# ===================================
# PAGE CONFIG
# ===================================
st.set_page_config(
    page_title="Task Manager",
    page_icon="📋",
    layout="wide"
)

# ===================================
# CUSTOM CSS
# ===================================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #f8fafc
    );
}
.main .block-container {
    max-width: 700px;
    margin: auto;
    padding-top: 2rem;
}
.big-title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: white;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #d1d5db;
    margin-bottom: 20px;
}
div[data-testid="stForm"] {
    background-color: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)
# ===================================
#SESSION STATE
#====================================
if "users" not in st.session_state:
    st.session_state.users = {}
if "tasks" not in st.session_state:
    st.session_state.tasks = {}
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "current_user" not in st.session_state:
    st.session_state.current_user = None
# ===================================
# REGISTER
# ===================================
def register():
    st.header("Register")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input(
        "Password",
        type="password"
    )
    if st.button("Register"):
        if not username or not email or not password:
            st.error("Please fill all fields")
        elif username in st.session_state.users:
            st.error("Username already exists")
        else:
            st.session_state.users[username] = {
                "email": email,
                "password": password
            }
            st.session_state.tasks[username] = []
            st.success("Registration Successful!")

# ===================================
# LOGIN
# ===================================
def login():
    st.header("Login")
    username = st.text_input(
        "Username",
        key="login_user"
    )
    password = st.text_input(
        "Password",
        type="password",
        key="login_pass"
    )
    if st.button("Login"):
        if (
            username in st.session_state.users
            and
            st.session_state.users[username]["password"] == password
        ):
            st.session_state.logged_in = True
            st.session_state.current_user = username
            st.rerun()
        else:
            st.error("Invalid Username or Password")

# ===================================
# DASHBOARD
# ===================================
def dashboard():

    if st.session_state.current_user is None:
        st.error("Please login first")
        st.session_state.logged_in = False
        st.rerun()
    user = st.session_state.current_user
    st.markdown(
        "<h1 class='main-title'>TASK MANAGER</h1>",
        unsafe_allow_html=True
    )
    st.success(f"Welcome {user}")

    # -------------------
    # Add Task Form
    # -------------------

    st.subheader("Create New Task")
    title = st.text_input("Task Title")
    description = st.text_area(
        "Task Description"
    )
    priority = st.selectbox(
    "Priority",
    ["Low", "Medium", "High"]
    )
    due_date = st.date_input(
        "Due Date",
        min_value=date.today()
    )
    if st.button("Add Task"):
        if title:
            task_id = len(
                st.session_state.tasks[user]
            ) + 1
            st.session_state.tasks[user].append(
                {
                    "id": task_id,
                    "title": title,
                    "description": description,
                    "priority":priority,
                    "due_date": str(due_date),
                    "completed": False
                }
            )
            st.success("Task Added Successfully")
            st.rerun()
        else:
            st.error("Task Title is required")

    st.divider()

    # -------------------
    # Task Table
    # -------------------
    st.subheader("My Tasks")
    tasks = st.session_state.tasks[user]
    if tasks:
        df = pd.DataFrame(
            [
                {
                    "ID": task["id"],
                    "Task Title": task["title"],
                    "Description": task["description"],
                    "Priority":
                "🟢 Low" if task["priority"] == "Low"
                else "🟡 Medium" if task["priority"] == "Medium"
                else "🔴 High",
                    "Due Date": task["due_date"],
                    "Completed": "✅ Yes"
                    if task["completed"]
                    else "❌ No"
                }
                for task in tasks
            ]
        )
        st.dataframe(
            df,
            use_container_width=True
        )
        st.divider()
        st.subheader(
            "Update Task Status"
        )
        for index, task in enumerate(tasks):
            col1, col2, col3 = st.columns(
                [4, 2, 1]
            )
            with col1:
                st.write(
                    f"**{task['title']}**"
                )
            with col2:
               if task["completed"]:
                 st.success("✅ Completed")
               else:
                if st.button(
                    "Complete",
                    key=f"complete_{index}"
                ):
                 task["completed"] = True
                 st.rerun() 
            with col3:
                if st.button(
                    "🗑 Delete",
                    key=f"delete_{index}"
                ):
                    st.session_state.tasks[user].pop(
                        index
                    )
                    st.rerun()
    else:
        st.info(
            "No Tasks Available"
        )
    st.divider()
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.rerun()
# ===================================
# MAIN APP
# ===================================
if st.session_state.logged_in:
    dashboard()
else:
    st.markdown(
        "<h1 class='main-title'>TASK MANAGER</h1>",
        unsafe_allow_html=True
    )
    option = st.sidebar.selectbox(
        "Menu",
        [
            "Login",
            "Register"
        ]
    )
    if option == "Login":
        login()
    else:
        register()