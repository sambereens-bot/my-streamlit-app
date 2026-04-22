
import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Ambereen's Professional Portfolio", page_icon="🎓", layout="wide")

# --- INITIALIZE STATE ---
if "profile_data" not in st.session_state:
    st.session_state.profile_data = {
        "name": "Ambereen Shaikh",
        "bio": "Dedicated Grade 11 student at Nile Academy with a focus on Computer Science and Community Leadership. Proven ability to balance rigorous academics with part-time work and volunteer commitments.",
        "skills": "Python (Intermediate), Streamlit, SQL, Public Speaking, Microsoft Office 365, Team Collaboration, Time Management",
        "theme_color": "#2E4053",
        "font_size": 18,
        "profile_pic": "https://via.placeholder.com/150",
        "resume_file": None,
        # Expanded Sections
        "edu_details": "Relevant Coursework: Computer Science, Functions (Grade 11), Physics, English Literature. \nGPA: 3.8/4.0",
        "costco_details": "- Managed point-of-sale systems and handled high-volume cash transactions accurately.\n- Assisted in inventory management and floor organization to improve customer experience.\n- Recognized for 'Employee of the Month' (March 2023) for efficiency.",
        "volunteer_details": "- Facilitated community outreach programs for the City Councillor’s office.\n- Organized youth engagement events, coordinating schedules for 20+ participants.\n- Drafted weekly newsletters to keep constituents informed of local policy changes.",
        "awards": "Honor Roll (2021-2024), Waterloo Math Competition Top 25%, National Public Speaking Finalist.",
        "extracurriculars": "Captain of the Debate Club, Member of the Robotics Team (FRC), Varsity Soccer."
    }

if "admin_mode" not in st.session_state:
    st.session_state.admin_mode = False

# --- CUSTOM AESTHETICS ---
st.markdown(f"""
    <style>
    .main {{ background-color: #ffffff; }}
    h1, h2, h3 {{ color: {st.session_state.profile_data['theme_color']}; border-bottom: 2px solid {st.session_state.profile_data['theme_color']}; padding-bottom: 5px; }}
    p, li {{ font-size: {st.session_state.profile_data['font_size']}px !important; line-height: 1.6; }}
    .stButton>button {{ background-color: {st.session_state.profile_data['theme_color']}; color: white; border-radius: 8px; }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image(st.session_state.profile_data["profile_pic"], width=150)
    st.title("Admin Panel")
    pwd = st.text_input("Access Key", type="password")
    if pwd == "secret123":
        st.session_state.admin_mode = True
        st.success("Editing Enabled")
        st.write("---")
        st.session_state.profile_data["theme_color"] = st.color_picker("Brand Color", st.session_state.profile_data["theme_color"])
        st.session_state.profile_data["font_size"] = st.slider("Text Size", 14, 22, st.session_state.profile_data["font_size"])
        uploaded_img = st.file_uploader("Change Photo", type=["jpg", "png"])
        if uploaded_img: st.session_state.profile_data["profile_pic"] = uploaded_img
        uploaded_pdf = st.file_uploader("Upload PDF Resume", type=["pdf"])
        if uploaded_pdf: st.session_state.profile_data["resume_file"] = uploaded_pdf.getvalue()
    else:
        st.session_state.admin_mode = False
    
    st.write("---")
    st.write("📍 Toronto, Canada")
    st.write("📧 ambereen@example.com")
    st.write("🔗 [LinkedIn](https://linkedin.com)")

# --- HERO ---
col1, col2 = st.columns([2, 1])
with col1:
    if st.session_state.admin_mode:
        st.session_state.profile_data["name"] = st.text_input("Display Name", st.session_state.profile_data["name"])
        st.session_state.profile_data["bio"] = st.text_area("Summary", st.session_state.profile_data["bio"])
    else:
        st.title(st.session_state.profile_data["name"])
        st.write(st.session_state.profile_data["bio"])

    if st.session_state.profile_data["resume_file"]:
        st.download_button("📥 Download PDF Resume", st.session_state.profile_data["resume_file"], file_name="Ambereen_Resume.pdf")

# --- SKILLS ---
st.header("🛠 Skills & Competencies")
if st.session_state.admin_mode:
    st.session_state.profile_data["skills"] = st.text_area("Skills (Comma separated)", st.session_state.profile_data["skills"])
else:
    st.write(st.session_state.profile_data["skills"])

# --- EDUCATION ---
st.header("🎓 Education")
col_edu, col_year = st.columns([3, 1])
with col_edu:
    st.markdown("**Nile Academy** | High School Diploma Candidate")
with col_year:
    st.write("Expected Graduation: June 2026")

if st.session_state.admin_mode:
    st.session_state.profile_data["edu_details"] = st.text_area("Education Details", st.session_state.profile_data["edu_details"])
else:
    st.write(st.session_state.profile_data["edu_details"])

# --- EXPERIENCE ---
st.header("💼 Experience")
st.markdown("### Store Employee | **Costco Super Centre**")
st.caption("Jan 2022 – Present")
if st.session_state.admin_mode:
    st.session_state.profile_data["costco_details"] = st.text_area("Costco Bullets", st.session_state.profile_data["costco_details"])
else:
    st.markdown(st.session_state.profile_data["costco_details"])

st.markdown("### Community Volunteer | **City Councillor's Office**")
st.caption("June 2020 – Dec 2021")
if st.session_state.admin_mode:
    st.session_state.profile_data["volunteer_details"] = st.text_area("Volunteer Bullets", st.session_state.profile_data["volunteer_details"])
else:
    st.markdown(st.session_state.profile_data["volunteer_details"])

# --- NEW SECTIONS FOR HIGH SCHOOLERS ---
c1, c2 = st.columns(2)
with c1:
    st.header("🏆 Awards & Honors")
    if st.session_state.admin_mode:
        st.session_state.profile_data["awards"] = st.text_area("Edit Awards", st.session_state.profile_data["awards"])
    else:
        st.write(st.session_state.profile_data["awards"])

with c2:
    st.header("🏀 Extracurriculars")
    if st.session_state.admin_mode:
        st.session_state.profile_data["extracurriculars"] = st.text_area("Edit Extracurriculars", st.session_state.profile_data["extracurriculars"])
    else:
        st.write(st.session_state.profile_data["extracurriculars"])