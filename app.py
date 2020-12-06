import sys
import pandas as pd
from PIL import Image
import streamlit as st
import time

st.markdown("<h1 style='text-align: center; color: Red;'>Recommendor System RBM!!</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: blue;'>Snackwise!!</h2>", unsafe_allow_html=True)

    

image = Image.open('YumYum.png')

st.image(image,use_column_width=True)


def get_dataset(userID):
    serverURL="http://127.0.0.1:8000/docs#/default/read_item_RBM_recommendation_get" + userID
    req = requests.get(serverURL)
    return req.json()

st.markdown("<h1 style='text-align: left; color: blue;'>Select UserID</h1>", unsafe_allow_html=True)
title = st.number_input('User ID',min_value =1,max_value=100,value = 1,step =1)




if st.button('Login'):
     data = pd.read_csv('snack_recommend.csv')  
     df1 =  data['UserID']==title
     df2 =data[df1]
     if df2.empty:
         #st.write('No User Found')
         image = Image.open('UserNotFound.jpeg')
         st.image(image,use_column_width=True)
     else:
         image = Image.open('InSnack.jpeg')
         st.image(image,use_column_width=True)
         st.write(data[df1])


def get_data():
    return pd.read_csv('snack_recommend.csv',header=None)

