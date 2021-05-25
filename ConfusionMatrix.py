from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
import numpy as np
y_prediction = classifier.predict(X_test)

predicted_value = []
for i in y_prediction:
    if i == 0:
        predicted_values.append("No")
  else:
    predicted_values.append("Yes")

actual_values = []
for i in Y_test.ravel():
  if i == 0:
    actual_values.append("No")
  else:
    actual_values.append("Yes")




