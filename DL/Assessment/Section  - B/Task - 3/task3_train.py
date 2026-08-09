import numpy as np
import matplotlib.pyplot as plt
import joblib
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


num_samples = 600
hour_of_day = np.random.randint(0, 24, num_samples)
day_of_week = np.random.randint(0, 7, num_samples)
temperature_celsius = np.random.uniform(10, 45, num_samples)

X = np.column_stack([hour_of_day, day_of_week, temperature_celsius])


score = (hour_of_day * 1.5) + (day_of_week * 2.0) + (temperature_celsius * 1.2)
y_raw = np.zeros(num_samples, dtype=int)
y_raw[score > np.percentile(score, 33)] = 1
y_raw[score > np.percentile(score, 66)] = 2

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
joblib.dump(scaler, "scaler.pkl")

y_encoded = to_categorical(y_raw, num_classes=3)            # 3 classes: Low(0), Medium(1), High(2)

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

model = Sequential([
    Dense(64, activation='relu', input_shape=(3,)),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dropout(0.3),
    Dense(3, activation='softmax')
])  

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'])

history = model.fit(
    X_train, y_train, 
    epochs=30, 
    validation_split=0.2, 
    batch_size=32)

loss, accuracy = model.evaluate(X_test, y_test)
print(f"Final Test Accuracy: {accuracy * 100:.2f}%")


plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training vs Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig("task3_accuracy.png")
plt.show()

model.save('demand_model.keras')