import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Digital Resume", page_icon="📄", layout="wide")

# --- LOAD CUSTOM CSS ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stHeader {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://via.placeholder.com/150", caption="Your Profile Picture") # Replace with your photo URL or local path
    st.title("Contact Me")
    st.write("📧 email@example.com")
    st.write("🔗 [LinkedIn](https://linkedin.com)")
    st.write("💻 [GitHub](https://github.com)")
    st.write("📍 City, Country")

# --- HERO SECTION ---
col1, col2 = st.columns([2, 1], vertical_alignment="center")
with col1:
    st.title("Ambereen Shaikh")
    st.subheader("Highschool Student")
    st.write(
        "I am a passionate developer with expertise in building data-driven applications. "
        "Experienced in Python, Streamlit, and SQL to solve complex problems."
    )
    if st.button("📥 Download Resume"):
        st.info("Link your PDF file here!")

# --- SKILLS ---
st.write("---")
st.header("Technical Skills")
st.write("""
- **Detailed Oriented**
- **Data Visualization:** Streamlit, Plotly, Matplotlib
- **Tools:** Git, Docker, AWS, VS Code
""")

# --- EXPERIENCE ---
st.write("---")
st.header("Professional Experience")

st.markdown("### **Store Employee | Costco Super Centre**")
st.caption("Jan 2022 – Present")
st.write("""
- Developed automated reporting dashboards using Streamlit, reducing manual work by 40%.
- Optimized SQL queries resulting in a 20% improvement in data retrieval speeds.
- Collaborated with cross-functional teams to define KPIs.
""")

st.markdown("### **Volunteer | City Councillor Office**")
st.caption("June 2020 – Dec 2021")
st.write("""
- Assisted in helping formulate group activities.
- Maintained legacy Python scripts and improved documentation clarity.
""")

# --- PROJECTS ---
st.write("---")
st.header("Personal Projects")
col_p1, col_p2 = st.columns(2)



# --- EDUCATION ---
st.write("---")
st.header("Education")
st.write("Grade 11 | Nile Academy (2020 - 2026)")
st.write( Nile Academy (2020 - 2026)")