# -*- coding: utf-8 -*-
"""Heart Disease Predictor_Mitul.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_ONptMeLCPzKTwICEB9sgAWl5r6XrTaP
"""

#the required libraries are being imported
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# the dataset is being loaded
df = pd.DataFrame()
df = pd.read_csv("https://drive.google.com/uc?id=1r_suZP4KhNxR05J68Qk9m3z4xl5kFvla")

# Split the data into features (X) and labels (y)
# here the name of the data frame id df

X = df.drop('target', axis=1)
y = df['target']


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier
clf = RandomForestClassifier()

# Train the model
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.DataFrame()
df = pd.read_csv("https://drive.google.com/uc?id=1r_suZP4KhNxR05J68Qk9m3z4xl5kFvla")

# Split the data into features (X) and labels (y)
# df is the name of the data frame
X = df.drop('target', axis=1)
y = df['target']


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier
clf = RandomForestClassifier()

# Train the model
clf.fit(X_train, y_train)

# Get the weights of the model
weights = clf.feature_importances_

# Quantize the weights
quantized_weights = [int(round(weight)) for weight in weights]

# Initialize a new Random Forest Classifier with the quantized weights
new_clf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42, class_weight={0: quantized_weights[0], 1: quantized_weights[1]})

# Train the new model
new_clf.fit(X_train, y_train)

# Get the features of the test set
X_test_np = X_test.to_numpy()

# Reshape the test set features to match the training set
X_test_np = X_test_np.reshape(X_test_np.shape[0], X_train.shape[1])


# Make predictions on the test set
y_pred = new_clf.predict(X_test_np)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy After Quantization:", accuracy)

# Show the predicted values
print("Predicted values:", y_pred)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# the required libraries are being imported

# the dataset is being loaded
df = pd.DataFrame()
df = pd.read_csv("https://drive.google.com/uc?id=1r_suZP4KhNxR05J68Qk9m3z4xl5kFvla")

# Split the data into features (X) and labels (y)
# here the name of the data frame id df

X = df.drop('target', axis=1)
y = df['target']


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier
clf = RandomForestClassifier()

# Train the model
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy Before Quantization:", accuracy)

# Quantize the model
from sklearn.preprocessing import QuantileTransformer

transformer = QuantileTransformer(n_quantiles=4)
X_train_q = transformer.fit_transform(X_train)
X_test_q = transformer.transform(X_test)

# Retrain the model on the quantized data
clf_q = RandomForestClassifier()
clf_q.fit(X_train_q, y_train)

# Make predictions on the test set
y_pred_q = clf_q.predict(X_test_q)

# Evaluate the quantized model
accuracy_q = accuracy_score(y_test, y_pred_q)
print("Accuracy After Quantization:", accuracy_q)

# Print the predicted values for the test set
print("Predicted values:", y_pred_q)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import time

# Load the dataset
df = pd.read_csv("https://drive.google.com/uc?id=1r_suZP4KhNxR05J68Qk9m3z4xl5kFvla")

# Split the data into features (X) and labels (y)
X = df.drop('target', axis=1)
y = df['target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier with reduced complexity
clf = RandomForestClassifier(n_estimators=50, max_depth=10)

# Train the model and measure the runtime
start_time = time.time()
clf.fit(X_train, y_train)
end_time = time.time()

# Calculate the runtime
runtime = end_time - start_time

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy Before Quantization:", accuracy)
print("Runtime Before Quantization:", runtime, "seconds")

# Quantize the model
from sklearn.preprocessing import QuantileTransformer

transformer = QuantileTransformer(n_quantiles=4)
X_train_q = transformer.fit_transform(X_train)
X_test_q = transformer.transform(X_test)

# Retrain the model on the quantized data and measure the runtime
start_time = time.time()
clf_q = RandomForestClassifier(n_estimators=50, max_depth=10)
clf_q.fit(X_train_q, y_train)
end_time = time.time()

# Calculate the runtime
runtime_q = end_time - start_time

# Make predictions on the quantized test set
y_pred_q = clf_q.predict(X_test_q)

# Evaluate the quantized model
accuracy_q = accuracy_score(y_test, y_pred_q)
print("Accuracy After Quantization:", accuracy_q)
print("Runtime After Quantization:", runtime_q, "seconds")

# Print the predicted values for the test set
print("Predicted values:", y_pred_q)