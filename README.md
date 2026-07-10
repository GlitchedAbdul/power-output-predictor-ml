# Power Output Predictor for Combined Cycle Power Plants

A machine learning application that predicts the electrical power output of a Combined Cycle Power Plant using environmental and operational conditions.

## Project Overview

This project compares multiple regression models and integrates the best-performing model into an interactive Streamlit web application.

The application predicts net electrical energy output using:

- Ambient Temperature
- Exhaust Vacuum
- Ambient Pressure
- Relative Humidity

## Machine Learning Models

The following models were trained and evaluated:

- Linear Regression
- Decision Tree Regression
- Random Forest Regression

Random Forest Regression achieved the strongest overall performance and was selected for the final prediction application.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Seaborn
- Jupyter Notebook
- Pickle

## My Contributions

This project was completed as part of a three-member engineering team.

My primary responsibilities included:

- Developing the Streamlit user interface
- Integrating the trained machine learning model with the interface
- Implementing real-time prediction functionality
- Supporting dataset exploration and cleaning
- Refining model integration and application performance
- Contributing to project documentation and presentation

## Project Structure

```text
power-output-predictor-ml/
├── app.py
├── requirements.txt
├── data/
├── models/
├── notebooks/
├── docs/
└── screenshots/
