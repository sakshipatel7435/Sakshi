import joblib
import numpy as np
from sklearn.linear_model import LinearRegression

# Features: [distance (km), order_value (Rs), time_of_day (0=Morning, 1=Afternoon, 2=Evening, 3=Night)]
np.random.seed(42)
X_dummy = np.random.rand(100, 3)
X_dummy[:, 0] = X_dummy[:, 0] * 49 + 1  # distance: 1 to 50 km
X_dummy[:, 1] = X_dummy[:, 1] * 900 + 100  # order_value: 100 to 1000 Rs
X_dummy[:, 2] = np.random.randint(0, 4, 100)  # time_of_day: 0 to 3

# estimated delivery time in minutes
# Base formula: 15 mins + (1.5 * distance) + (time_of_day * 3) + noise
y_dummy = 15 + (1.5 * X_dummy[:, 0]) + (X_dummy[:, 2] * 3) + np.random.normal(0, 3, 100)

model = LinearRegression()
model.fit(X_dummy, y_dummy)

joblib.dump(model, "delivery_model.pkl")
print("Successfully created and saved 'delivery_model.pkl'!")