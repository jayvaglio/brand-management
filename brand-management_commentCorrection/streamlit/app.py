import streamlit as st

st.set_page_config(page_title='Online Presence Monitor', layout='wide')
st.title('Online Presence Monitor (Streamlit)')

API_BASE = st.secrets['API_BASE_URL']

st.components.v1.html(f'''
<iframe src="{API_BASE}" width="100%" height="800px" style="border:none;"></iframe>
''')
