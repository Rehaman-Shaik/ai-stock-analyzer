"""
predict future price using
Time Series Analysis
ARIMA (AutoRegressive Integrated Moving Average) model // Algo

"""
from django.core.management.base import BaseCommand
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA


class Command(BaseCommand):
    def get_data(self):
        data = {
            "date": ["7-11", "8-11", "11-11", "12-11", "13-11", "14-11", "18-11", "19-11", "20-11", "21-11"],
            "price": [9.86, 9.26, 9.47, 9.30, 8.89, 9.06, 8.89, 8.92, 8.33, 8.98]
        }

        # Create a pandas DataFrame
        df = pd.DataFrame(data)
        df["date"] = pd.to_datetime(df["date"])
        df.set_index("date", inplace=True)

        print(df)
        return df

    def final_step(self, df):
        # Step 1: Plot the historical data
        plt.figure(figsize=(10, 6))
        plt.plot(df.index, df["price"], label="Historical Prices", marker='o')
        plt.title("Stock Price History")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid()
        plt.show()

        # Step 2: Fit the ARIMA model
        # (p, d, q): parameters for ARIMA (you can experiment with these values)
        model = ARIMA(df["price"], order=(2, 1, 2))  # AR(2), I(1), MA(2)
        fitted_model = model.fit()

        # Step 3: Predict future values
        forecast_steps = 5  # Number of days to predict
        forecast = fitted_model.forecast(steps=forecast_steps)

        # Step 4: Display the results
        print("Future Predictions:")
        print(forecast)

        # Step 5: Visualize predictions
        forecast_dates = pd.date_range(
            df.index[-1] + pd.Timedelta(days=1), periods=forecast_steps)
        plt.figure(figsize=(10, 6))
        plt.plot(df.index, df["price"], label="Historical Prices", marker='o')
        plt.plot(forecast_dates, forecast,
                 label="Predicted Prices", marker='x')
        plt.title("Stock Price Prediction")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid()
        plt.show()

    def handle(self, *args, **kwargs):
        print("Yup working")
        df = self.get_data()
        self.final_step(df)
