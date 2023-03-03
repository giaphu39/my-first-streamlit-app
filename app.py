import streamlit as st
st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
a = st.number_input('tham số a',min_value=1)
b = st.number_input('tham số b',min_value=2)
x=(-b)/a
s='Phương trình có một nghiệm '+ str(x)
if st.button('OK'):
  st.success(s)