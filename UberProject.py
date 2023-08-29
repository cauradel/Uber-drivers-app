#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 13:42:16 2022

@author: manele
"""

import streamlit as st

import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.metrics import v_measure_score
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

st.header('Uber Drivers App')
st.write("New York in July is a busy month. This app aims at giving Uber drivers various insights regarding when and where to pick up drivers")


####### Load Dataset #####################

uber = pd.read_csv('https://github.com/cauradel/Uber-drivers-app/raw/main/uber_raw_smaller.csv',header= 0,index_col= False, sep=',', on_bad_lines='skip')
uber_sample = uber.sample(n=None, frac=0.01, replace=False, weights=None, random_state=None, axis=None)




######## Clustering #############

x = uber_sample[['Lat','Lon']].values
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

# Grouping data and calculating count of rides for each hour
uber_sample3 = uber_sample.groupby('Hour', as_index=False)['Date/Time'].count()
uber_sample3.sort_values('Hour', axis=0, ascending=False)

# Create a new column with y-axis label
uber_sample3['y_label'] = 'Number of Rides'

# Creating a bar chart to visualize rush hours
st.markdown('<h1 style="width: 80%;">Rush hours during the month of July</h1>', unsafe_allow_html=True)
st.bar_chart(uber_sample3, x='Hour', y='Date/Time', key='y_label')






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

















