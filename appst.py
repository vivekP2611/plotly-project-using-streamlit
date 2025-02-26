import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv("indian plotly project data.csv")

list_of_state = list(df["State"].unique())
list_of_state.insert(0,"Overall india")

st.sidebar.title("india data visualization")
selected_state = st.sidebar.selectbox("select a state",list_of_state)
primary = st.sidebar.selectbox("select primary parameter",sorted(df.columns[5:]))
secondary = st.sidebar.selectbox("select secndary parameter",sorted(df.columns[5:]))

plot = st.sidebar.button("plot graph")

if plot:
    st.text('Size represent primary parameter')
    st.text('Color represents secondary parameter')
    if selected_state == "Overall india":
        #plot graph
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4,size_max=35,
                                mapbox_style="carto-positron",width=1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
        
    else:
       state_df = df[df['State'] == selected_state]

       fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=6, size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700,hover_name='District')

       st.plotly_chart(fig, use_container_width=True)