import streamlit as st

page_bg_img = """
<style>
[data-testid="stHeader"] {
    background-image: url(../../media/Group 25.png);
    background-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Groups")
st.image("media/Group 25.png")