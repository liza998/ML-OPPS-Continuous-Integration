import streamlit as st  


st.title("Power Calculator")
st.write("Enter a Number to calculate its square,cube, fifth power")

n= st.number_input("Enter an integer", value=1,step=1)

# Calculate result 
square = n ** 2
cube = n ** 3
fifth_power = n ** 5

st.write(f"square of {n} is : {square}") 
st.write(f"square of {n} is : {cube}")
st.write(f"square of {n} is : {fifth_power}")