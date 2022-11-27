import streamlit as st

st.write("""
# Greatest of three Numbers
""")

#Get Input
st.header('User Input Parameters')

def user_input_features():
    num1 = st.number_input("Number 1",step=1)
    num2 = st.number_input("Number 2",step=1)
    num3 = st.number_input("Number 3",step=1) 

    if num1>num2 and num1>num3:
        return f'Greatest number is {num1}'
    elif num2>num1 and num2>num3:
        return f'Greatest number is {num2}'
         
    return f'Greatest number is {num3}'


result = user_input_features()

st.subheader('Result')
st.write(result)
