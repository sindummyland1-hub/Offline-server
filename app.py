import streamlit as st
import os

st.set_page_config(page_title="Control Panel", layout="centered")

st.title("⚙️ Script Control Panel")

st.write("Fill in the required data files for your script.")

# Password
password = st.text_input("Password", type="password")
if st.button("Save Password"):
    with open("password.txt", "w") as f:
        f.write(password)
    st.success("password.txt saved")

# Tokens
tokens = st.text_area("Access Tokens (one per line)")
if st.button("Save Tokens"):
    with open("token.txt", "w") as f:
        f.write(tokens)
    st.success("token.txt saved")

# Username
username = st.text_input("Username / ID")
if st.button("Save Username"):
    with open("username.txt", "w") as f:
        f.write(username)
    st.success("username.txt saved")

# Messages file upload
uploaded_messages = st.file_uploader("Upload Messages File (.txt)", type=["txt"])
if uploaded_messages:
    with open("messages.txt", "wb") as f:
        f.write(uploaded_messages.read())
    with open("file.txt", "w") as f:
        f.write("messages.txt")
    st.success("messages + file.txt saved")

# Haters name
haters_name = st.text_input("Prefix Name")
if st.button("Save Prefix"):
    with open("hatersname.txt", "w") as f:
        f.write(haters_name)
    st.success("hatersname.txt saved")

# Speed
speed = st.number_input("Delay (seconds)", min_value=1, value=2)
if st.button("Save Delay"):
    with open("time.txt", "w") as f:
        f.write(str(speed))
    st.success("time.txt saved")

st.markdown("---")

st.warning("Run your main.py manually in your terminal:")
st.code("python main.py", language="bash")
