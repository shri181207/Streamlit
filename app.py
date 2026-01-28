import streamlit as st
import pandas as pd

#
# If you moved it to the same folder as app.py
st.image("bg.png", width=800)
st.title("welcome")
st.write("Hello Streamlit")

# Section 1: Basic Input
st.subheader("Your details")
name1 = st.text_input("Enter your name", key="name1")
age1 = st.number_input("Enter your age", min_value=1, key="age1")
mark1 = st.number_input("Enter your marks", min_value=0, max_value=100, key="mark1")
if st.button("Submit", key="btn1"):
    st.write("Name:", name1)
    st.write("Age:", age1)
    st.write("Marks:", mark1)   
st.divider()



# Section 3: Session State (Persistent Data)
st.subheader("Your team mate details")
name2 = st.text_input("Enter name of your team mate ", key="name2")
age2 = st.number_input("Enter age of your team mate ", min_value=1, key="age2")
mark2 = st.number_input("Enter marks of your team mate ", min_value=0, max_value=100, key="mark2")  
if "student_list" not in st.session_state:
    st.session_state.student_list = []
if st.button("Submit", key="btn2"):
    if name2:
        st.session_state.student_list.append({"name": name2, "age": int(age2), "marks": int(mark2)  })
        st.success("Student added")
    else:
        st.warning("Please enter a name")
st.table(st.session_state.student_list)

st.divider()

st.subheader("Section 2: Static Student Table")
students = [
    {"name": name1,"age":age1,"marks":mark1 },
    {"name": name2, "age": age2, "marks": mark2},
]
st.table(students)

st.divider()

# Section 4: Bar Chart
st.subheader("Subject Marks")
data = {
    "Name": [name1,name2],
    "Marks": [mark1,mark2],
}
df = pd.DataFrame(data)
st.bar_chart(df.set_index("Name"))