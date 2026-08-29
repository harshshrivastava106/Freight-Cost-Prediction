# Freight Cost Prediction

## About the Project

This project focuses on predicting freight cost based on the purchase amount.

The analysis was performed using data stored in a SQLite database. Different tables were explored and the vendor invoice data was used for the freight cost prediction model.

I compared Linear Regression, Decision Tree Regression and Random Forest Regression models and selected the model based on their performance.

A Streamlit application was also created where a purchase amount can be entered and the predicted freight cost is displayed.

## Data

The database contains the following tables:

- purchases
- purchase_prices
- vendor_invoice
- begin_inventory
- end_inventory

The vendor invoice table contains information such as vendor, invoice date, quantity, purchase amount and freight cost.

## Approach

The project follows these steps:

1. Connect to the SQLite database
2. Explore the available tables
3. Analyse the vendor invoice data
4. Check the relationship between quantity, freight and purchase amount
5. Select purchase amount as the input feature
6. Use freight cost as the target variable
7. Split the data into training and testing sets
8. Train different regression models
9. Compare model performance
10. Save the selected model
11. Use the model in a Streamlit application

## Models Used

Three regression models were compared:

- Linear Regression
- Decision Tree Regression
- Random Forest Regression

### Model Performance

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 24.11 | 124.72 | 96.99% |
| Decision Tree Regression | 38.12 | 138.25 | 96.30% |
| Random Forest Regression | 30.31 | 130.66 | 96.69% |

Linear Regression gave the best R² score among the three models and was selected for the final application.

## Streamlit Application

The Streamlit application takes the purchase amount as input and predicts the freight cost using the saved Linear Regression model.

For example, the user enters:

Purchase Amount: $1000

The application then displays the predicted freight cost.

## Technologies Used

- Python
- Pandas
- NumPy
- SQLite
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

## Project Structure

```text
Freight-Cost-Prediction/
│
├── app.py
├── freight_cost_prediction.ipynb
├── freight_model.pkl
├── requirements.txt
└── README.md
