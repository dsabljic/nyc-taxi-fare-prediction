import streamlit as st
import pickle
import numpy as np
from geocoding import Geocoding
import datetime

def curr_time():
    now = datetime.datetime.now()
    return float(now.hour) , float(now.weekday())

def euc_distance(lat1, long1, lat2, long2):
    return (((lat1-lat2)**2 + (long1-long2)**2)**0.5)

def load_data():
    with open('saved_model.pkl' , 'rb') as file:
        data = pickle.load(file)
    
    return data

data = load_data()

model = data['model']
scaler = data['scaler']

def show_predict_page():
    st.title('NYC Taxi Fare Prediction')

    pickup = st.text_input('Pickup location')
    dropoff = st.text_input('Dropoff location')
    num_pass = st.slider(label = 'Number of passengers' , min_value = 1 , max_value = 6)

    ok = st.button('Predict fare')

    if ok:
        pickup_loc = Geocoding(pickup)
        dropoff_loc = Geocoding(dropoff)

        p_lat , p_long = pickup_loc.get_lat_long()
        d_lat , d_long = dropoff_loc.get_lat_long()

        x = [p_lat , p_long , d_lat , d_long , num_pass]

        hr , day_of_week = curr_time()

        x.append(hr)
        x.append(day_of_week)

        airports = {'JFK_Airport': (-73.78,40.643),
                    'Laguardia_Airport': (-73.87, 40.77),
                    'Newark_Airport' : (-74.18, 40.69)}

        x.append(euc_distance(p_lat , p_long , d_lat , d_long))

        for a in airports:
            x.append(euc_distance(p_lat , p_long , airports[a][1], airports[a][0]))
            x.append(euc_distance(d_lat , d_long , airports[a][1], airports[a][0]))

        x = np.array(x).astype(float).reshape(1 , -1)

        x = scaler.transform(x)

        fare = float(model.predict(x))

        st.subheader(f'The estimated taxi fare is {fare:.2f}')