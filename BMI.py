import streamlit as st
st.set_page_config(page_title="Body Mass Index")
st.title("Body Mass Index")
st.write("calculate your BMI here")

 # User Inputs
weight=st.number_input("Enter your weight (kg)",value=0.0)
height=st.number_input("Enter your height (m)",value=0.0)

#Calculate Button
if st.button("calculate"):
    result=weight/(height*height)
    st.success(f"result :{result:.2f}")
    if result<=18.5:
        st.write("Eat some food")
    elif result>=18.5 and result<=24.9:
        st.write("Ambada healthy kutta")
    elif result>=25.0 and result<=29.9:
        st.write("Do exercise")
    elif result>=30.0:
        st.write("you've obesity")
