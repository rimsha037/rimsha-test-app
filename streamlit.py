import streamlit as st
from PIL import image

st.title("Lahore Garrison University")
st.title("Lahore Garrison University located in metropolitan city of Lahore")
st.header("Digital forensic research and center")
st.info("this is the first ever private digital forensic and cyber security research center")

st.subheader("4th semester")
#a = 5

#Addition application
#st.info("Please enter the number between 0 to 9")
a = st.number_input("please enter a number between 0 to 9")
b = st.number_input("please enter a number between 0 to 9")
c = a + b

#a = st.text_input("Please enter a number between 0 to 9")
#b = st.text_input("Please enter a number between 0 to 9")
#c = a + b
st.text("the result after addition is")
st.write(c)

image = Image.open('Type_Error.png')
st.image(image)
