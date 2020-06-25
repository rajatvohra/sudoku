import numpy as np
import pandas as pd
import os
import cv2 
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import svm
import joblib 
import pickle

digits = pd.read_csv(r"C:\Users\rajat vohra\Documents\python_2020\comp_vision\train.csv")
y=digits["label"]
X=digits.drop("label",axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,random_state=0)
model = KNeighborsClassifier() 
model.fit(X_train, y_train)
  
# Save the model as a pickle in a file 
joblib.dump(model, 'filename.pkl')