!wget https://archive.ics.uci.edu/static/public/186/wine+quality.zip

import zipfile

with zipfile.ZipFile('wine+quality.zip', 'r') as zip_ref:
    zip_ref.extractall()

"""# Importing the Libraries"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df1 = pd.read_csv('winequality-red.csv', sep=';')
df1.columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality']
df1.head()

df1.columns

# Making a heatmap so as to select the feature vectors

correlation_matrix = df1.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

plt.scatter(df1['fixed acidity'], df1['quality'])
plt.xlabel('fixed acidity')
plt.ylabel('quality')
plt.show()

"""# Making the X and y columns"""

X = df1.drop('quality', axis=1)
y = df1['quality']

X_train,X_test, y_train, Y_test = train_test_split(df1.drop('quality', axis=1), df1['quality'], test_size=0.2, random_state=42)

"""# Training with Decision Tree"""

from sklearn.tree import DecisionTreeClassifier
Model1 = DecisionTreeClassifier()
Model1.fit(X_train, y_train)

from sklearn.metrics import accuracy_score
Y_pred1 = Model.predict(X_test)
accuracy_score(Y_test, Y_pred1)

"""# Training with Random Forest Classifier"""

from sklearn.ensemble import RandomForestClassifier
Model2 = RandomForestClassifier()
Model2.fit(X_train, y_train)

y_pred2 = Model.predict(X_test)
accuracy_score(Y_test, y_pred2)

"""# Training with XGBoost"""

from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y_train_encoded = le.fit_transform(y_train)

Model3 = XGBClassifier(n_estimators=100, learning_rate=0.01)
Model3.fit(X_train, y_train_encoded)

y_test_encoded = le.transform(Y_test)
y_pred3 = model.predict(X_test)
accuracy_score(y_test_encoded, y_pred3)

def get_score(model, X_train, X_test, y_train, y_test):

    le = LabelEncoder()
    y_train_encoded = le.fit_transform(y_train)
    y_test_encoded = le.transform(y_test)

    model.fit(X_train, y_train_encoded)
    y_pred = model.predict(X_test)
    return accuracy_score(y_test_encoded, y_pred)

"""# Making folds (used stratified K-fold so as to make normal distribution)"""

from sklearn.model_selection import StratifiedKFold

folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

for train_index, test_index in folds.split(X, y):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y[train_index], y[test_index]
    print(get_score(Model1, X_train, X_test, y_train, y_test))
    print(get_score(Model2, X_train, X_test, y_train, y_test))
    print(get_score(Model3, X_train, X_test, y_train, y_test))

