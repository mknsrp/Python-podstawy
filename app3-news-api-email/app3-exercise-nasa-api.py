import requests
import streamlit as st

api_key = 'Xrj4SAMJMfxf5xPAPMqTLLdqSRDnRtmtOcOqBkzd'
url = 'https://api.nasa.gov/planetary/apod'

params = {
    'api_key':api_key
}

request = requests.get(url, params=params)
request.raise_for_status()
data = request.json()

print(data)
st.header(data['title'])
st.subheader(data['date'])
st.write("")
st.image(data['url'], use_container_width=True)
st.write("")
st.write(data['explanation'])