import streamlit as st
import time
import requests

st.image('./assets/header-iris.png')
st.title('Iris Classifier App')
st.markdown('*Created by Nanda Fadhil Azman | Batch May 2024*')
st.divider()

with st.form(key='iris-form'):
    sepal_length = st.number_input('Sepal Length', min_value = 0, help='Input the numerical sepal length')
    sepal_width = st.number_input('Sepal width', min_value = 0, help='Input the numerical sepal width')
    petal_length = st.number_input('Petal Length', min_value = 0, help='Input the numerical petal length')
    petal_width = st.number_input('Petal Width', min_value = 0, help='Input the numerical petal width')

    submit_button = st.form_submit_button('Predict')

    if submit_button:
        st.balloons()

        data = {
            'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width,
        }

        with st.spinner('Wait for it...'):
            response = requests.post('http://backend:8000/predict', json=data)
            result = response.json()
            
            
        # if success
        if response.status_code == 200:
            st.success(result['result'])
            st.balloons()
        else:
            st.error(result['detail_error'])