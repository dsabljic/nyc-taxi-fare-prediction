# NYC Taxi Fare Prediction Project

## Project Overview

This project aims to accurately predict New York City taxi fares using various features such as pickup and dropoff coordinates, passenger count, day of the week, and hour of the ride. The model focuses on enhancing the accuracy of fare estimation by including engineered features like travel distance and distances from major airports (JFK, LaGuardia, Newark). We used an XGBoost Regressor (XGBRegressor) for model training and prediction, and the model was serialized using the pickle module for deployment.

## Key Features

- **Data Features**: Utilizes core data features like pickup and dropoff longitude and latitude, passenger count, day of the week, and hour of the ride.
- **Engineered Features**: Includes calculated distances like travel distance, distances to/from JFK, LaGuardia, and Newark airports.
- **Model**: Uses XGBoost Regressor, a powerful, efficient, and scalable implementation of gradient boosting.
- **Serialization**: The model is serialized using the pickle module for ease of deployment and inference.
- **Web Application**: Deployed via Streamlit, providing a user-friendly interface for input and predictions.

## How It Works

1. **User Input**: Users input natural language descriptions of pickup and dropoff locations (e.g., "Upper Manhattan").
2. **Geocoding**: The input is converted to geographical coordinates using the Position Stack Geocoding API (https://positionstack.com/).
3. **Feature Engineering**: Additional required features for prediction, like travel distance and distances from major airports, are calculated based on the geocoded coordinates.
4. **Prediction**: The processed input is fed into the XGBRegressor model to predict the taxi fare.

## Deployment

The project is deployed using Streamlit, creating an accessible web application. This application allows users to enter ride details in natural language, which are then processed and used to predict the fare.

## Repository Structure

- `model/`: Contains the serialized model file.
- `scripts/`: Includes scripts for training the model and preprocessing data.
- `app/`: Contains the Streamlit application files for deployment.
- `notebooks/`: Jupyter notebooks for exploratory data analysis and model experimentation.
- `requirements.txt`: Lists all the dependencies for the project.
- `README.md`: This file, describing the project and how to use it.

## Getting Started

1. **Clone the Repository**: Clone this repo to your local machine.
2. **Install Dependencies**: Run `pip install -r requirements.txt` to install required packages.
3. **Run the Web App**: Execute `streamlit run app/main.py` to start the Streamlit application.
4. **Predict Fares**: Enter the ride details on the web interface and receive fare predictions.

## Contributions

Contributions to this project are welcome. Please fork the repository and submit a pull request for review.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

This README provides a high-level overview of the NYC Taxi Fare Prediction project. For more detailed information, refer to the documentation within each directory.
