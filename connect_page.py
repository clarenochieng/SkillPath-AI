import streamlit as st
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Text, Date
from sqlalchemy.orm import sessionmaker
from datetime import date
from utils import Mentor, Mentee, Base, session, engine
import random

def assess_compatibility(mentor_profile, mentee_profile):
    score = 0
    max_score = 10  
    explanation = []

    # Preprocess function
    def preprocess(text):
        return set(map(str.strip, text.lower().split(',')))

    mentor_degrees = preprocess(mentor_profile['degrees'])
    mentee_major = preprocess(mentee_profile['major'])
    major_match = mentor_degrees & mentee_major
    if major_match:
        score += 3
        explanation.append(f"Common field of study in {', '.join(major_match)}.")

    if mentor_profile['school'].lower() == mentee_profile['school'].lower():
        score += 2
        explanation.append(f"Both attended {mentor_profile['school']}.")

    mentor_interests = preprocess(mentor_profile.get('interests', ''))
    mentee_interests = preprocess(mentee_profile['interests'])
    interests_match = mentor_interests & mentee_interests
    if interests_match:
        score += 2
        explanation.append(f"Shared interests in {', '.join(interests_match)}.")

    if mentor_profile['location'].lower() == mentee_profile['location'].lower():
        score += 2
        explanation.append(f"Both located in {mentor_profile['location']}.")

    if mentor_profile['years_experience']:
        expected_graduation_year = mentee_profile['graduation_date'].year
        if mentor_profile['years_experience'] >= (date.today().year - expected_graduation_year):
            score += 1
            explanation.append("Mentor has sufficient experience to guide the mentee.")

    if score == 0:
        score = 1  # Minimum score
    explanation_text = ' '.join(explanation)

    return score, explanation_text

def mentor_registration():
    st.header("Mentor Registration")
    with st.form(key='mentor_form'):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        current_workplace = st.text_input("Current Workplace")
        job_title = st.text_input("Job Title")
        years_experience = st.number_input("Number of Years of Experience", min_value=0, max_value=50, step=1)
        degrees = st.text_input("Degrees (comma-separated)")
        email = st.text_input("Email Address")
        school = st.text_input("School Attended")
        location = st.text_input("Location")
        linkedin = st.text_input("LinkedIn Profile URL")
        optional_email = st.text_input("Optional Email Address")
        submit_button = st.form_submit_button(label='Register as Mentor')
    if submit_button:
        new_mentor = Mentor(
            first_name=first_name,
            last_name=last_name,
            current_workplace=current_workplace,
            job_title=job_title,
            years_experience=years_experience,
            degrees=degrees,
            email=email,
            school=school,
            location=location,
            linkedin=linkedin,
            optional_email=optional_email
        )
        session.add(new_mentor)
        session.commit()
        st.success("Mentor registered successfully!")

def mentee_registration():
    st.header("Mentee Registration")
    with st.form(key='mentee_form'):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        school = st.text_input("School")
        graduation_date = st.date_input("Graduation Date", min_value=date.today())
        major = st.text_input("Major")
        interests = st.multiselect("Interests", ["AI/ML", "Web Development", "Cybersecurity", "Data Science", "Finance", "Marketing", "Design", "Entrepreneurship"])
        fun_fact = st.text_area("Fun Fact About Yourself")
        linkedin = st.text_input("LinkedIn Profile URL")
        optional_email = st.text_input("Optional Email Address")
        location = st.text_input("Location")
        submit_button = st.form_submit_button(label='Register as Mentee')
    if submit_button:
        new_mentee = Mentee(
            first_name=first_name,
            last_name=last_name,
            school=school,
            graduation_date=graduation_date,
            major=major,
            interests=','.join(interests),
            fun_fact=fun_fact,
            linkedin=linkedin,
            optional_email=optional_email,
            location=location
        )
        session.add(new_mentee)
        session.commit()
        st.success("Mentee registered successfully!")
        mentee_profile = {
            'first_name': first_name,
            'last_name': last_name,
            'school': school,
            'graduation_date': graduation_date,
            'major': major,
            'interests': ','.join(interests),
            'fun_fact': fun_fact,
            'linkedin': linkedin,
            'optional_email': optional_email,
            'location': location
        }
        display_matches(mentee_profile)

def find_top_matches(mentee_profile):
    mentors = session.query(Mentor).all()
    matches = []
    for mentor in mentors:
        mentor_dict = {
            'first_name': mentor.first_name,
            'last_name': mentor.last_name,
            'current_workplace': mentor.current_workplace,
            'job_title': mentor.job_title,
            'years_experience': mentor.years_experience,
            'degrees': mentor.degrees,
            'email': mentor.email,
            'school': mentor.school,
            'location': mentor.location,
            'linkedin': mentor.linkedin,
            'optional_email': mentor.optional_email
        }
        score, explanation = assess_compatibility(mentor_dict, mentee_profile)
        matches.append({
            'mentor': mentor_dict,
            'score': score,
            'explanation': explanation
        })
    # Sort and return top matches
    matches.sort(key=lambda x: x['score'], reverse=True)
    return matches[:5]

def display_matches(mentee_profile):
    st.header("Top Mentor Matches")
    matches = find_top_matches(mentee_profile)
    for match in matches:
        mentor = match['mentor']
        st.subheader(f"{mentor['first_name']} {mentor['last_name']} (Score: {match['score']}/10)")
        st.write(f"**Current Workplace**: {mentor['current_workplace']}")
        st.write(f"**Job Title**: {mentor['job_title']}")
        st.write(f"**Years of Experience**: {mentor['years_experience']}")
        st.write(f"**Degrees**: {mentor['degrees']}")
        st.write(f"**School Attended**: {mentor['school']}")
        st.write(f"**Location**: {mentor['location']}")
        st.write(f"**LinkedIn**: {mentor['linkedin']}")
        st.write(f"**Why this is a good match**: {match['explanation']}")
        st.link_button(f"Request Mentorship from {mentor['first_name']} {mentor['last_name']}", url="https://www.linkedin.com")

def main():
    st.title("SkillConnect - Connecting Mentors and Mentees")
    selection = st.selectbox("Choose an option:", ["Mentor Registration", "Mentee Registration"])

    if selection == "Mentor Registration":
        mentor_registration()
    elif selection == "Mentee Registration":
        mentee_registration()
    else:
        st.write("Welcome to SkillConnect!")
        st.write("Please select an option from the dropdown menu to get started.")

main()

