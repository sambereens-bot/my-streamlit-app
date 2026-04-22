
import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Ambereen's Portfolio", page_icon="🎨", layout="wide")

# --- INITIALIZE STATE ---
if "profile_data" not in st.session_state:
    st.session_state.profile_data = {
        "name": "Ambereen Shaikh",
        "bio": "Grade 11 Student | Nile Academy",
        "bg_color": "#F0F2F6",  # Default light grey
        "text_color": "#31333F",
        "profile_pic": "https://via.placeholder.com/150",
        "resume_bytes": None,
        "resume_name": None
    }

# --- STYLING ENGINE ---
# This block dynamically updates the background and text color based on your admin choices
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {st.session_state.profile_data['bg_color']};
        color: {st.session_state.profile_data['text_color']};
    }}
    /* Ensures headings contrast with background */
    h1, h2, h3 {{
        color: {st.session_state.profile_data['text_color']};
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR / ADMIN PANEL ---
with st.sidebar:
    st.image(st.session_state.profile_data["profile_pic"], width=150, caption="Profile Preview")
    st.title("Admin Control")
    
    password = st.text_input("Enter Admin Password", type="password")
    
    if password == "secret123":
        st.success("Admin Mode Active")
        st.write("---")
        
        # 1. CHANGE BACKGROUND COLOR
        st.subheader("🎨 Aesthetics")
        st.session_state.profile_data["bg_color"] = st.color_picker(
            "Background Color", st.session_state.profile_data["bg_color"]
        )
        st.session_state.profile_data["text_color"] = st.color_picker(
            "Text Color", st.session_state.profile_data["text_color"]
        )
        
        # 2. UPLOAD PHOTO
        st.subheader("📸 Profile Photo")
        uploaded_img = st.file_uploader("Upload a new photo", type=["jpg", "png", "jpeg"])
        if uploaded_img:
            st.session_state.profile_data["profile_pic"] = uploaded_img
            
        # 3. UPLOAD RESUME
        st.subheader("📄 Resume File")
        uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
        if uploaded_file:
            st.session_state.profile_data["resume_bytes"] = uploaded_file.getvalue()
            st.session_state.profile_data["resume_name"] = uploaded_file.name
            st.info(f"Loaded: {uploaded_file.name}")
    else:
        st.info("Enter password to customize site")

# --- MAIN PAGE CONTENT ---
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.title(st.session_state.profile_data["name"])
    st.write(st.session_state.profile_data["bio"])
    
    # DOWNLOAD BUTTON (Only shows if a file has been uploaded)
    if st.session_state.profile_data["resume_bytes"]:
        st.download_button(
            label="📥 Download My Resume",
            data=st.session_state.profile_data["resume_bytes"],
            file_name=st.session_state.profile_data["resume_name"],
            mime="application/pdf"
        )
    else:
        st.button("📥 Download Resume", disabled=True, help="Upload a resume in Admin Mode first!")

# --- QUICK SECTIONS ---
st.write("---")
st.header("Education")
st.write("Grade 11 | Nile Academy (2020 - 2026)")

st.header("Experience")
st.write("**Costco Super Centre** | Store Employee")
st.write("**City Councillor Office** | Volunteer")

# --- FOOTER ---
if password == "secret123":
    st.write("---")
    st.caption("🛠 Admin Mode is currently visible. Lock the sidebar to hide controls.")