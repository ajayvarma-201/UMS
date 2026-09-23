# Python and Streamlit Project.
# Motive of this project is to revise important python concepts.
# University Management System.

import streamlit as st

# config the main app page
st.set_page_config(
    page_title = "University System",
    layout = "wide"
)

st.title("University Management System")

# Create a empty list of colleges
if "colleges" not in st.session_state:
    st.session_state.colleges = []
    
menu_choice = st.sidebar.radio(
    "SELECT OPTION",
    (
        "Create College",
        "Add Students",
        "Add Teachers",
        "Display Students",
        "Display Teachers",
        "List of Colleges"
    )
)

# College class to store college name, students and teachers
class college:
    def __init__(self, cname):
        self.cname = cname
        self.students = []
        self.teachers = []
        
    def add_student(self, s):
        self.students.append(s)
        
    def add_teacher(self, t):
        self.teachers.append(t)
        
class person:
    def __init__(self, name, branch):
        self.branch = branch
        self.name = name
        
class student(person):
    def __init__(self, roll, sname, branch):
        self.roll = roll
        super().__init__(sname, branch)  # call parent constructor function and store sname, branch
        
class teacher(person):
    def __init__(self, subject, tname, branch):
        self.subject = subject
        super().__init__(tname, branch)

# based upon college name, college class object is find
def find_college(cname):
    for c in st.session_state.colleges:
        if c.cname == cname:
            return c
    
    return None
        
if menu_choice == "Create College":
    cname = st.text_input("Enter new college name")
    if st.button("CREATE"):
        clg_obj = college(cname)  # creating a college class object
        st.session_state.colleges.append(clg_obj)   # storing a college class object in college list
        st.success(f"College created successfully : {cname}")
        
elif menu_choice == "Add Students":
    if not st.session_state.colleges:
        st.info("Please add the college first")
    else:
        clgname = st.selectbox("Choose college", [c.cname for c in st.session_state.colleges])
        roll = st.number_input("Enter Your Rollno", min_value = 1, max_value =100)
        sname = st.text_input("Enter student name")
        branch = st.text_input("Enter your branch")
        if st.button("ADD STUDENT"):
            if not (roll and sname and clgname and branch):
                st.error("Please fill all the fields")
            else:
                clg_ob = find_college(clgname)  # find the college object based upon college name
                stu_obj = student(roll, sname, branch)  # Created student class object
                clg_ob.add_student(stu_obj)
                st.success("student added successfully")
            
elif menu_choice == "Add Teachers":
    if not st.session_state.colleges:
        st.info("Please add the college first")
    else:
        clgname = st.selectbox("Choose college", [c.cname for c in st.session_state.colleges])
        subject = st.text_input("Enter Your Subject")
        tname = st.text_input("Enter Teacher name")
        branch = st.text_input("Enter your branch")
        if st.button("ADD TEACHER"):
            if not (subject and tname and clgname and branch):
                st.error("Please fill all the fields")
            else:
                clg_ob = find_college(clgname)  # find the college object based upon college name
                tea_obj = teacher(subject, tname, branch)  # Created teacher class object
                clg_ob.add_teacher(tea_obj)
                st.success("Teacher added successfully")
                
elif menu_choice == "Display Students":
    if not st.session_state.colleges:
        st.info("Please add the college first")
    else:
        clgname = st.selectbox("Choose college", [c.cname for c in st.session_state.colleges])
        clg_ob = find_college(clgname)  # find the college object based upon college name
        st.subheader(f"List of Students in {clgname}")
        if clg_ob.students:
            for i, s in enumerate(clg_ob.students, 1):
                st.write(f"{i} : {s.name}")
        else:
            st.warning("No students found in this college")
            
elif menu_choice == "Display Teachers":
    if not st.session_state.colleges:
        st.info("Please add the college first")
    else:
        clgname = st.selectbox("Choose college", [c.cname for c in st.session_state.colleges])
        clg_ob = find_college(clgname)  # find the college object based upon college name
        st.subheader(f"List of Teachers in {clgname}")
        if clg_ob.teachers:
            for i, t in enumerate(clg_ob.teachers, 1):
                st.write(f"{i} : {t.name}")
        else:
            st.warning("No teachers found in this college")
            
elif menu_choice == "List of Colleges":
    if not st.session_state.colleges:
        st.info("Please insert the college first") 
    else:
        st.subheader(f"List of Colleges")
        for i , c in enumerate(st.session_state.colleges, 1):
            st.write(f"{i} : {c.cname}")