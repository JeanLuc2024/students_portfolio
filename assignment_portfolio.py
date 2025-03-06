import streamlit as st

# Set page config
st.set_page_config(page_title="My Digital Footprint", page_icon="🎓", layout="wide")

# Initialize session state for profile details
if "profile" not in st.session_state:
    st.session_state.profile = {
        "name": "IZABAYO HARANIRA Jean Luc Severin",
        "location": "Musanze, Rwanda",
        "field_of_study": "Software Engineering, Year 3",
        "university": "INES Ruhengeri",
        "about_me": "I am a Software Engineering Student with interest in Website Development and Data Mining."
    }

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Testimonials", "Contact", "Timeline"])

# Home Page with Editable Profile (except profile picture)
if page == "Home":
    st.title("🎓 My Digital Footprint – Showcasing My Journey")
    st.image("1.png", width=150, caption="Profile Picture")
    with st.form("edit_profile"):
        st.session_state.profile["name"] = st.text_input("👤 Name", st.session_state.profile["name"])
        st.session_state.profile["location"] = st.text_input("📬 Location", st.session_state.profile["location"])
        st.session_state.profile["field_of_study"] = st.text_input("💻 Field of Study", st.session_state.profile["field_of_study"])
        st.session_state.profile["university"] = st.text_input("🎓 University", st.session_state.profile["university"])
        st.session_state.profile["about_me"] = st.text_area("🔗 About Me", st.session_state.profile["about_me"])

        submitted = st.form_submit_button("💾 Save Changes")
        if submitted:
            st.success("✅ Profile updated successfully!")

    # Display updated profile info
    st.subheader("Personal Info")
    st.write(f"📬 {st.session_state.profile['location']}")
    st.write(f"💻 {st.session_state.profile['field_of_study']}")
    st.write(f"🎓 {st.session_state.profile['university']}")
    st.write(f"🔗 {st.session_state.profile['about_me']}")

    # Download resume
    try:
        with open("resume.pdf", "rb") as file:
            resume_bytes = file.read()
        st.download_button(label="📄 Download Resume", data=resume_bytes, file_name="resume1.pdf", mime="application/pdf")
    except FileNotFoundError:
        st.warning("⚠ Resume file not found. Please upload your resume.")

# Projects Page with Filtering System
elif page == "Projects":
    st.title("💻 My Projects")

    project_category = st.selectbox("🗂️ Filter by Category", ["All", "Year 1 Project", "Group Projects", "Class Assignment", "Dissertation Project"])

    projects = [
        {"title": "Rubavu Fleet Management System", "category": "Year 1 Project", "description": "Analyzing trends in Rubavu Fleet Terminal, solving manual data collection.", "technologies": "HTML, CSS, PHP, MYSQL"},
        {"title": "Furniture Management System", "category": "Individual Projects", "description": "Developed Cargo Furniture company Management System.", "technologies": "HTML, CSS, PHP, MYSQL"},
        {"title": "Bus Ticket Booking System", "category": "Class Assignment", "description": "Designed and developed a website for Caritas Gikongoro using WordPress CMS.", "technologies": "Python, Streamlit"},
        {"title": "Easy Transcript Management System", "category": "Dissertation Project", "description": "Streamlining academic transcript requests at INES Ruhengeri.", "technologies": "Python, Django, Streamlit, PostgreSQL"}
    ]

    filtered_projects = [project for project in projects if project_category == "All" or project["category"] == project_category]

    for project in filtered_projects:
        with st.expander(f"📊 {project['title']}"):
            st.write(f"**Category:** {project['category']}")
            st.write(f"**Description:** {project['description']}")
            st.write(f"**Technologies:** {project['technologies']}")

# Skills Page
elif page == "Skills":
    st.title("⚡ Skills and Achievements")

    st.subheader("Programming Skills")
    skill_python = st.slider("Python", 0, 100, 90)
    st.progress(skill_python)

    skill_js = st.slider("JavaScript", 0, 100, 75)
    st.progress(skill_js)

    skill_AI = st.slider("Artificial Intelligence", 0, 100, 65)
    st.progress(skill_AI)

    skill_Java = st.slider("Java", 0, 100, 75)
    st.progress(skill_Java)

    skill_Machinelearning = st.slider("Machine Learning", 0, 100, 75)
    st.progress(skill_Machinelearning)

    st.subheader("🏆 Certifications & Achievements")
    st.write("✔ High school Diploma in Software Engineering, from ESTG, 2021, Rwanda.")
    st.write("✔ Year 1 Transcript (In Computer Science), from INES, 2023, Rwanda.")
    st.write("✔ Year 2 Transcript (In Computer Science), from INES, 2024, Rwanda.")

# Contact Page
elif page == "Contact":
    st.title("📬 Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("✅ Message sent successfully!")

    st.write("📧 Email: izabayojeanlucseverin@gmail.com")
    st.write("[📂 GitHub](https://github.com/JeanLuc2024)")

# Testimonials section
elif page == "Testimonials":
    st.title("🗣️ Testimonials")

    st.write("*Work like a slave to live like a King.----Mr.NGABO")

    st.markdown("---")

    # Allow classmates or mentors to leave testimonials
    st.subheader("✍ Leave a Testimonial")

    with st.form("testimonial_form"):
        name = st.text_input("Your Name")
        relationship = st.selectbox("Your Relationship", ["Classmate", "Mentor", "Teammate", "Other"])
        testimonial_message = st.text_area("Your Testimonial")

        submitted = st.form_submit_button("Submit Testimonial")
        if submitted:
            if name and testimonial_message:
                st.success(f"✅ Thank you, {name}! Your testimonial has been submitted.")
                st.write(f"🗨 {testimonial_message} — {name} ({relationship})")
            else:
                st.error("⚠ Please fill in all fields before submitting.")

# Timeline Section
elif page == "Timeline":
    st.title("⏳ Academic & Project Milestones")
    milestones = [
        "Year 1: First project completed ✅",
        "Year 2: INES Programming Competition 🏆",
        "Year 3: Internship at IKIGUGU LTD 💼",
        "Year 4: Final year Dissertation Submission 📌"
    ]
    for milestone in milestones:
        st.write(milestone)
