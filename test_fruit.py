# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 00:55:55 2021

@author: super_000
"""

import streamlit as st
import plotly.express as px
import pandas as pd

def radar_chart(val):  
    df = pd.DataFrame(dict(
    r=[Love_val, Joy_val, Peace_val, Patience_val, Kindness_val, Goodness_val, Faithfulness_val, Gentleness_val, SelfCon_val],
     
    theta=['Love','Joy','Peace','Patience','Kindness', 'Goodness', 'Faithfulness', 'Gentleness', 'Self-Control']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    st.write(fig)
    
if __name__ == '__main__':
    val=10
    Love_val = st.slider('Love',0,10,1)
    Joy_val = st.slider('Joy',0,10,1)
    Peace_val = st.slider('Peace',0,10,1)
    Patience_val = st.slider('Patience',0,10,1)
    Kindness_val = st.slider('Kindness',0,10,1)
    Goodness_val = st.slider('Goodness',0,10,1)
    Faithfulness_val = st.slider('Faithfulness',0,10,1)
    Gentleness_val = st.slider('Gentleness',0,10,1)
    SelfCon_val = st.slider('Self-Control',0,10,1)
    radar_chart(val)