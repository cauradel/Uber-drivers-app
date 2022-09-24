# Uber-drivers-app

Uber driver app in Streamlit with clustering

[Overview]

The goal of this project was to deploy an app that would help Uber drivers navigate New York city during one of its busiest months ; July.
The idea was to use clustering with K-Means and display the results in Streamlit.

[Data]

The data comes from the entreprise Uber and gives various insights about the rides in July 2014.

Composition :

Date/Time : Date and time at which the course was ordered
Lat : Latitude
Lon : Longitude
Base : Taxi station

The data was very clean, the only modification I made was create columns from the column Date/Time to have columns with the days.


[Clustering]

I started by making clusters with the K-Means model :

<img width="781" alt="Screenshot 2022-09-24 at 17 48 45" src="https://user-images.githubusercontent.com/77899183/192107053-f4a4bdca-726a-44cd-ab6a-93fcd365a6ea.png">


[Mapping]

I then used my clusters and their centroids to create maps that would indicate where Uber drivers should go to increase their chances of getting clients :

<img width="765" alt="Screenshot 2022-09-24 at 17 51 29" src="https://user-images.githubusercontent.com/77899183/192107365-d184df87-b553-4be3-a1e1-f353aded8511.png">

Map with a closer look to the busiest streets :

<img width="761" alt="Screenshot 2022-09-24 at 17 51 40" src="https://user-images.githubusercontent.com/77899183/192107506-d7328125-03ee-4671-bddc-9f1d8aca265c.png">

[Plotting]

I then plotted the data to give Uber drivers some useful insights about New York in july.
The first one showcases what are the rush hours in July :

<img width="734" alt="Screenshot 2022-09-24 at 17 51 52" src="https://user-images.githubusercontent.com/77899183/192107567-20720ce3-f5b8-4325-9349-918ff2b7e407.png">


The second one is made with a slider and enables the Uber driver to specify which day he wants to know the rush hours for :

<img width="796" alt="Screenshot 2022-09-24 at 17 52 37" src="https://user-images.githubusercontent.com/77899183/192107596-bb9a9265-cd51-4933-a111-ebcb023eed5d.png">

