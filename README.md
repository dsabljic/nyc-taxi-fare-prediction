# NYC Taxi Fare Prediction

## Project Overview

This project aims to accurately predict New York City taxi fares using various features such as pickup and dropoff coordinates, passenger count, day of the week, and hour of the ride. The model focuses on enhancing the accuracy of fare estimation by including engineered features like travel distance and distances from major airports (JFK, LaGuardia, Newark). The project uses a combination of Multi-Layer Perceptron (MLP) and XGBoost Regressor (XGBRegressor) for the machine learning model. After comparing both models, the XGBRegressor was chosen for deployment due to its performance. The model was serialized using the `pickle` module for [deployment](https://dsabljic-nyc-taxi-fare-prediction.streamlit.app/).

Dataset: (New York City Taxi Fare)[https://www.kaggle.com/competitions/new-york-city-taxi-fare-prediction]
## Repository Contents

- `Predicting Taxi Fares.ipynb`: A Jupyter notebook that contains data loading, preprocessing, model building with MLP and XGBRegressor, and model selection.
- `app.py`: The main script that runs the Streamlit application for the project.
- `geocoding.py`: Implements a geocoding class that uses the Position Stack API (https://positionstack.com/) to convert addresses into coordinates.
- `utils.py`: Contains utility functions for preprocessing and feature engineering required for the model.
- `saved_model.pkl`: The saved XGBRegressor model serialized using the pickle module.
- `requirements.txt`: Lists all the Python dependencies necessary to run the project locally or deploy it.
- `predict_page.py`: Defines the main functionality of the Streamlit page. It utilizes the utility functions for preprocessing, feature engineering, making predictions, and displaying the results.

## Deployment
The Streamlit web application is currently hosted and can be accessed [here](https://dsabljic-nyc-taxi-fare-prediction-app-4w64qw.streamlitapp.com/).

## Getting Started

To set up this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/dsabljic/nyc-taxi-fare-prediction.git
   ```
2. Navigate to the repository folder:
   ```bash
   cd nyc-taxi-fare-prediction
   ```
3. Set up a Python virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   ```
   Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```bash
     source venv/bin/activate
     ```
4. Install the required dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

5. Run the Streamlit app locally:
   ```bash
   streamlit run app.py
   ```

## Usage

Once the app is running, input the required fields to predict the taxi fare. The app will communicate with the backend to process the input, make predictions, and display the estimated fare.
