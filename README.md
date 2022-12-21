# Data Mining and Machine Learning Project 2022 : Detecting the difficulty level of French texts

## Group Coop

### Team members:

* Pierre Devillers 
* Vanja Hug
---

### Project Description:

This project is consisting in the elaboration of a model in order to estimate the difficulty level of French texts (A1, ..., C2). We were doing this through a [Kaggle competition](https://www.kaggle.com/competitions/detecting-french-texts-difficulty-level-2022). 
This repository is made to display all our documentation and resources for our prediction models as well as the different attempts of data cleaning or model implementation we have made. The structure is as the following :

1. [The different CSV files we used as training and prediction data.](CSV_files)
2. [The classic models we used](Classic_models)
3. [The implementation of the model using BERT and TensorFlow](BERT_TensorFlow_model)
4. The methodology
5. The different results
6. Presentation video

---

### The data:

We have been provided with two different datasets, one for the training (`training_data.csv`) and another unlabelled data (`unlabelled_data.csv`) in order to make predictions with our model. They were composed of sentences with their associated index as well as the difficulty level of the sentence in the `training_data.csv` file.  

---

### The models:

As a first attempt, we decided to train and test the data on the classic classification models that we have seen in class. We trained a Logistic Regression, a KNN model, a Tree Classifier, as well as a Random Forest Classifier. We trained all these models first with the raw data without any treatment on it, and after we trained it with a tokenized data. Another model we implemented is a model based on BERT-like embeddings which makes contextual relations between words in order to classify them. 

---

## Results

| Scores/Models  | Logistic Regression | KNN | Tree Classifier | Random Forest | BERT-TensorFlow
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Accuracy score | 0.47  | 0.35 | 0.41 | 0.41 | 0.54 |
| Precision score  | 0.46 | 0.42 | 0.41 | 0.41 | 0.45 |
| Recall score  | 0.47 | 0.35 | 0.41 | 0.41 | 0.31|
| F1 score  | 0.46 | 0.34 | 0.39 | 0.39 | 0.36 |

With these results we can see that our BERT-TensorFlow model is the best one in terms of accuracy. 
