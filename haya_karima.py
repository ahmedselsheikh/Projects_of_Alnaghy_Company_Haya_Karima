import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.header('Alnaghi company projects')
with open('design.css') as source_file:
    st.markdown(f"<style>{source_file.read()}</style", unsafe_allow_html=True)

st.subheader('Projects of Haya Karima')

df = pd.read_excel('final_projects.xlsx', skiprows=4)
# Convert DataFrame to HTML table
# Convert DataFrame to HTML table
# Convert DataFrame to HTML table
# df_html = df.to_html(escape=False)
#
# # Add custom CSS to modify table styling
# styled_html = """
# <style>
# table {
#   max-height: 400px; /* Adjust the value as needed */
#   overflow-y: auto;
# }
# </style>
# """ + df_html
#
# st.markdown(styled_html, unsafe_allow_html=True)

# Create a copy of the DataFrame with aligned text
styled_df = df.style.set_properties(**{'text-align': 'center'})
st.dataframe(styled_df, width=1200)

st.subheader('Some Images of projects')
col1, col2, col3 = st.columns(3)

with col1:
    for i in range(1, 18):
        st.image(f'images/{i}.JPG')


with col2:
    for i in range(18, 35):
        st.image(f'images/{i}.JPG')

with col3:
    for i in range(35, 52):
        st.image(f'images/{i}.JPG')


