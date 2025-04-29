import numpy as np
import pandas as pd
import streamlit as st
from helper import transform

st.title('Fake News Detection')

input_text = st.text_area("Enter your message:")