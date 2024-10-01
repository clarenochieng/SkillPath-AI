import streamlit as st
from utils import Job, Base, session, engine, add_sample_jobs

def job_search():
    st.header("Job Search")
    job_type = st.selectbox("Select Job Type:", ["Select", "New Grad", "Intern"], key="Experience")
    fields_of_interest = [
        "AI/ML", "Web Development", "Cybersecurity",
        "Data Science", "Finance", "Marketing",
        "Design", "Entrepreneurship"
    ]
    field_of_interest = st.selectbox("Select Field of Interest:", ["Select"] + fields_of_interest, key="Field")
    if st.button("Search Jobs"):
        if job_type != "Select" and field_of_interest != "Select":
            display_jobs(job_type, field_of_interest)
        else:
            st.error("Please select both job type and field of interest.")

def display_jobs(job_type, field_of_interest):
    matching_jobs = session.query(Job).filter(
        Job.job_type == job_type,
        Job.field_of_interest == field_of_interest
    ).all()

    if matching_jobs:
        st.subheader(f"Top {job_type} Jobs in {field_of_interest}")
        for job in matching_jobs:
            st.write(f"### {job.title} at {job.company}")
            st.write(f"**Location**: {job.location}")
            st.write(f"**Requirements**: {job.requirements}")
            st.write(f"**Description**: {job.description}")
            st.write(f"[Apply Here]({job.link})")
            st.write("---")
    else:
        st.info("No jobs found matching your criteria.")

def job_search():
    st.header("SkillPath Careers")
    job_type = st.selectbox("Select Job Type:", ["Select", "New Grad", "Intern"])
    fields_of_interest = [
        "AI/ML", "Web Development", "Cybersecurity",
        "Data Science", "Finance", "Marketing",
        "Design", "Entrepreneurship"
    ]
    field_of_interest = st.selectbox("Select Field of Interest:", ["Select"] + fields_of_interest)
    if st.button("Search Jobs", key="Job Button"):
        if job_type != "Select" and field_of_interest != "Select":
            display_jobs(job_type, field_of_interest)
        else:
            st.error("Please select both job type and field of interest.")

def display_jobs(job_type, field_of_interest):
    matching_jobs = session.query(Job).filter(
        Job.job_type == job_type,
        Job.field_of_interest == field_of_interest
    ).all()
    if matching_jobs:
        st.subheader(f"Top {job_type} Jobs in {field_of_interest}")
        for job in matching_jobs:
            st.write(f"### {job.title} at {job.company}")
            st.write(f"**Location**: {job.location}")
            st.write(f"**Requirements**: {job.requirements}")
            st.write(f"**Description**: {job.description}")
            st.write(f"[Apply Here]({job.link})")
            st.write("---")
    else:
        st.info("No jobs found matching your criteria.")

job_search()
