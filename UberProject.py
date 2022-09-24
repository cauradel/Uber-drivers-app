#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 13:42:16 2022

@author: manele
"""

import streamlit as st

import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
import seaborn as sns
import random 
from random import sample

from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.metrics import v_measure_score
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

st.header('Uber Drivers App')
st.write("New York in July is a busy month. This app aims at giving Uber drivers various insights regarding when and where to pick up drivers")


####### Load Dataset #####################

uber = pd.read_csv('/Users/manele/Downloads/uber-raw-data-jul14.csv',header= 0,index_col= False)
uber_sample = uber.sample(n=None, frac=0.01, replace=False, weights=None, random_state=None, axis=None)




######## Clustering #############

x = uber_sample[['Lat','Lon']]
kmeans = KMeans(n_clusters=7)
labels = kmeans.fit(x)
y_kmeans = kmeans.predict(x)

uber_sample['labels']= labels.labels_
centroids = kmeans.cluster_centers_
centroidss = pd.DataFrame(data = centroids, columns = [['Lat', 'Lon']])


###### map#######

centroid = centroidss.values.tolist()

uber_sample2 = uber_sample[['Lat','Lon']]
uber_sample2['centroids'] = kmeans.labels_
uber_sample2.head()
uber_sample2.rename(columns = {'Lat':'lat', 'Lon':'lon'}, inplace = True)

st.title('Busiest New York districts in July')
st.map(uber_sample2)

######### Better Map #####


import pydeck as pdk

st.title('Busiest New York districts and streets in July')
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=40.7128,
        longitude=-74.0060,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=uber_sample2,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=uber_sample2,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            pickable = True,
            get_radius=200,
        ),
    ],
))

### Clusters according to time of day ########

uber_sample['Date/Time']=pd.to_datetime(uber['Date/Time'], format='%m/%d/%Y %H:%M:%S')

uber_sample['Hour'] = uber_sample['Date/Time'].dt.hour
uber_sample['Month'] = uber_sample['Date/Time'].dt.month
uber_sample['Day'] = uber_sample['Date/Time'].dt.day
uber_sample['DayWeek'] = uber_sample['Date/Time'].dt.day_name()
uber_sample['centroids'] = kmeans.labels_

Hour = uber_sample['Hour']
Month = uber_sample['Month']
Day = uber_sample['Day']
DayWeek = uber_sample['DayWeek'] 
Centroids = uber_sample['centroids']

##### Heures de pointe #####

uber_sample3 = uber_sample.groupby('Hour', as_index=False)['centroids'].sum()
uber_sample3.sort_values('Hour', axis = 0, ascending = False)

st.title('Rush hours during the month of July')
st.bar_chart(uber_sample3)



##### Heures de pointe selon jour de la semaine#####




#table = pd.pivot_table(uber_sample, values = 'centroids', index = ['DayWeek','Hour'], aggfunc= np.sum)
#table2 = pd.DataFrame(table)

## DataFrame with centroids by hour by day

df = uber_sample.groupby(['DayWeek', 'Hour']).agg({'centroids':'sum'})
df = df.reset_index()

## Bar chart for each day of the week

st.title('Peak demand hours per day of the week')
days =['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day = st.select_slider('Select a day of the week',options= days)
st.write('Peak demand hours for : ', day)

monday = df.loc[df['DayWeek'] == 'Monday']

if day == 'Monday':
    st.title('Monday')
    st.bar_chart(data = monday, x = 'Hour', y = 'centroids' )
    
tuesday = df.loc[df['DayWeek'] == 'Tuesday']
    
if day == 'Tuesday':
    st.title('Tuesday')
    st.bar_chart(data = tuesday, x = 'Hour', y = 'centroids' )

wednesday = df.loc[df['DayWeek'] == 'Wednesday']

if day == 'Wednesday':
    st.title('Wednesday')
    st.bar_chart(data = wednesday, x = 'Hour', y = 'centroids' )

thursday = df.loc[df['DayWeek'] == 'Thursday']

if day == 'Thursday':
    st.title('Thursday')
    st.bar_chart(data = thursday, x = 'Hour', y = 'centroids' )

friday = df.loc[df['DayWeek'] == 'Friday']

if day == 'Friday':
    st.title('Friday')
    st.bar_chart(data = friday, x = 'Hour', y = 'centroids' )

saturday = df.loc[df['DayWeek'] == 'Saturday']

if day == 'Saturday':
    st.title('Saturday')
    st.bar_chart(data = saturday, x = 'Hour', y = 'centroids' )

sunday = df.loc[df['DayWeek'] == 'Sunday']

if day == 'Sunday':
    st.title('Sunday')
    st.bar_chart(data = sunday, x = 'Hour', y = 'centroids' )


###### Base Plot ######################

st.title('Most popular taxi stops')

import plotly.figure_factory as ff
base = uber_sample['Base']
location = uber_sample['Lat']
date = uber_sample['Date/Time']

arr = uber_sample['Base']
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.plotly_chart(fig)















