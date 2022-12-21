# Import required packages
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
sns.set_style("whitegrid")

def evaluate(test, pred):
  accuracy = accuracy_score(test, pred)
  precision = precision_score(test, pred, average='macro')
  recall = recall_score(test, pred, average='macro')
  f1= f1_score(test, pred, average='macro')
  return accuracy, precision, recall, f1
  print(f'CONFUSION MATRIX:\n{confusion_matrix(test, pred)}')
  print(f"ACCURACY SCORE:\n{accuracy:.6f}")
  print(f'CLASSIFICATION REPORT:\n\tPrecision: {precision:.6f}\n\tRecall: {recall:.6f}\n\tF1_Score: {f1:.6f}')

def accuracy_conf_mat(y_test, y_pred):
  print(round(accuracy_score(y_test, y_pred), 4))
  conf_mat = confusion_matrix(y_test, y_pred)
  fig, ax = plt.subplots(figsize=(5,5))
  sns.heatmap(conf_mat, annot=True, fmt='d')
  plt.ylabel('Actual')
  plt.xlabel('Predicted')
  plt.show()