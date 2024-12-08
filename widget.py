import streamlit as st
import datetime
import pandas as pd


# membuat inputan untuk text
name = st.text_input(label='Nama Lengkap', value='')
if st.button('Say hello'):
    st.write('Hello  ', name, '!')
st.write('Nama : ', name)
age = st.number_input(label='Usia')
st.write('Usia : ', int(age), 'tahun')
date_birth = st.date_input(label='Tanggal Lahir',
                           min_value=datetime.date(1900, 1, 1))
st.write('Tanggal Lahir : ', date_birth)
phone = st.number_input(label='Nomor Whatsapp')
st.write('Nomor Whatsapp : ', phone)
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)
