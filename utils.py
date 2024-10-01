from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Text, Date
from sqlalchemy.orm import sessionmaker
from datetime import date

Base = declarative_base()

class Mentor(Base):
    __tablename__ = 'mentors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    current_workplace = Column(String)
    job_title = Column(String)
    years_experience = Column(Integer)
    degrees = Column(String)
    email = Column(String)
    school = Column(String)
    location = Column(String)
    linkedin = Column(String)
    optional_email = Column(String)

class Mentee(Base):
    __tablename__ = 'mentees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    school = Column(String)
    graduation_date = Column(Date)
    major = Column(String)
    interests = Column(String)
    fun_fact = Column(Text)
    linkedin = Column(String)
    optional_email = Column(String)
    location = Column(String)

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    requirements = Column(String)
    description = Column(Text)
    link = Column(String)
    job_type = Column(String)
    field_of_interest = Column(String)

def add_sample_jobs():
    sample_jobs = [
        Job(
            title="Software Engineer Intern",
            company="Tech Innovators Inc.",
            location="New York, NY",
            requirements="Python, Machine Learning, Data Structures",
            description="Work on cutting-edge AI projects and assist in developing machine learning models.",
            link="https://techinnovators.com/jobs/123",
            job_type="Intern",
            field_of_interest="AI/ML"
        ),
        Job(
            title="Junior Web Developer",
            company="Web Solutions Co.",
            location="San Francisco, CA",
            requirements="JavaScript, HTML, CSS",
            description="Develop and maintain web applications for various clients in a collaborative environment.",
            link="https://websolutions.com/careers/456",
            job_type="New Grad",
            field_of_interest="Web Development"
        ),
        Job(
            title="Data Analyst Intern",
            company="Data Insights LLC",
            location="Boston, MA",
            requirements="SQL, Data Visualization, Python",
            description="Assist in analyzing data sets to extract meaningful insights and support decision-making.",
            link="https://datainsights.com/internships/789",
            job_type="Intern",
            field_of_interest="Data Science"
        ),
        Job(
            title="Marketing Associate",
            company="Market Leaders",
            location="Chicago, IL",
            requirements="Communication, Content Creation, SEO",
            description="Develop marketing strategies and content to enhance brand awareness.",
            link="https://marketleaders.com/jobs/1010",
            job_type="New Grad",
            field_of_interest="Marketing"
        ),
        Job(
            title="Cybersecurity Intern",
            company="SecureTech",
            location="Washington, D.C.",
            requirements="Network Security, Ethical Hacking, Risk Assessment",
            description="Support the security team in identifying and mitigating cyber threats.",
            link="https://securetech.com/careers/internships/1111",
            job_type="Intern",
            field_of_interest="Cybersecurity"
        ),
        Job(
            title="Financial Analyst",
            company="Finance Plus",
            location="New York, NY",
            requirements="Excel, Financial Modeling, Accounting",
            description="Analyze financial data to support investment decisions and company growth.",
            link="https://financeplus.com/careers/1212",
            job_type="New Grad",
            field_of_interest="Finance"
        ),
        Job(
            title="Graphic Design Intern",
            company="Creative Minds Studio",
            location="Los Angeles, CA",
            requirements="Adobe Creative Suite, Illustration, Branding",
            description="Collaborate with the design team to create visual content for marketing campaigns.",
            link="https://creativemindsstudio.com/internships/1313",
            job_type="Intern",
            field_of_interest="Design"
        ),
        Job(
            title="Product Manager Trainee",
            company="Innovatech",
            location="Austin, TX",
            requirements="Project Management, Communication, Agile Methodologies",
            description="Assist product managers in overseeing product development cycles.",
            link="https://innovatech.com/careers/1414",
            job_type="New Grad",
            field_of_interest="Entrepreneurship"
        ),
        Job(
            title="Machine Learning Engineer",
            company="AI Labs",
            location="Seattle, WA",
            requirements="Python, TensorFlow, Neural Networks",
            description="Develop and implement machine learning algorithms for data-driven solutions.",
            link="https://ailabs.com/jobs/1515",
            job_type="New Grad",
            field_of_interest="AI/ML"
        ),
        Job(
            title="Digital Marketing Intern",
            company="BrandBoost",
            location="Miami, FL",
            requirements="Social Media Management, SEO, Content Creation",
            description="Support the marketing team in executing digital campaigns across various platforms.",
            link="https://brandboost.com/internships/1616",
            job_type="Intern",
            field_of_interest="Marketing"
        ),
        Job(
            title="Business Analyst",
            company="Enterprise Solutions",
            location="Denver, CO",
            requirements="Data Analysis, Business Strategy, Communication",
            description="Work with cross-functional teams to improve business processes and performance.",
            link="https://enterprisesolutions.com/careers/1717",
            job_type="New Grad",
            field_of_interest="Finance"
        ),
        Job(
            title="Front-End Developer Intern",
            company="AppWorks",
            location="Portland, OR",
            requirements="React, JavaScript, UI/UX Design",
            description="Assist in developing user interfaces for web and mobile applications.",
            link="https://appworks.com/internships/1818",
            job_type="Intern",
            field_of_interest="Web Development"
        ),
        Job(
            title="Data Scientist",
            company="Big Data Corp",
            location="San Jose, CA",
            requirements="Python, Machine Learning, Statistics",
            description="Analyze large datasets to uncover trends and build predictive models.",
            link="https://bigdatacorp.com/careers/1919",
            job_type="New Grad",
            field_of_interest="Data Science"
        ),
        Job(
            title="UX/UI Design Intern",
            company="DesignHub",
            location="Atlanta, GA",
            requirements="Wireframing, Prototyping, User Research",
            description="Collaborate on designing intuitive user experiences for our applications.",
            link="https://designhub.com/internships/2020",
            job_type="Intern",
            field_of_interest="Design"
        ),
        Job(
            title="AI Research Intern",
            company="FutureTech Labs",
            location="Palo Alto, CA",
            requirements="Python, Deep Learning, Research Skills",
            description="Participate in cutting-edge AI research projects alongside experienced scientists.",
            link="https://futuretechlabs.com/internships/2121",
            job_type="Intern",
            field_of_interest="AI/ML"
        ),
        Job(
            title="Sales Development Representative",
            company="Global Sales Corp",
            location="Dallas, TX",
            requirements="Communication, CRM Tools, Lead Generation",
            description="Identify and qualify sales opportunities to drive company growth.",
            link="https://globalsalescorp.com/careers/2222",
            job_type="New Grad",
            field_of_interest="Entrepreneurship"
        ),
        Job(
            title="Information Security Analyst",
            company="SecureNet",
            location="Seattle, WA",
            requirements="Security Protocols, Risk Management, Compliance",
            description="Monitor and protect the organization's information systems from cyber threats.",
            link="https://securenet.com/careers/2323",
            job_type="New Grad",
            field_of_interest="Cybersecurity"
        ),
        Job(
            title="Content Writer Intern",
            company="MediaWorks",
            location="Philadelphia, PA",
            requirements="Writing, Editing, SEO",
            description="Create engaging content for blogs, social media, and marketing materials.",
            link="https://mediaworks.com/internships/2424",
            job_type="Intern",
            field_of_interest="Marketing"
        ),
        Job(
            title="Junior Data Engineer",
            company="DataStream Inc.",
            location="Houston, TX",
            requirements="Python, ETL Processes, SQL",
            description="Build and maintain data pipelines to support analytics initiatives.",
            link="https://datastreaminc.com/careers/2525",
            job_type="New Grad",
            field_of_interest="Data Science"
        ),
        Job(
            title="Mobile App Developer Intern",
            company="AppVentures",
            location="San Diego, CA",
            requirements="Flutter, Dart, Mobile UI Design",
            description="Assist in developing cross-platform mobile applications.",
            link="https://appventures.com/internships/2626",
            job_type="Intern",
            field_of_interest="Web Development"
        ),
    ]
    session.bulk_save_objects(sample_jobs)
    session.commit()

engine = create_engine('sqlite:///mentorship.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

#add_sample_jobs()
