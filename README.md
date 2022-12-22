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
5. [The different results](#results)
6. Presentation video

---

### The data:

We have been provided with two different datasets, one for the training (`training_data.csv`) and another unlabelled data (`unlabelled_data.csv`) in order to make predictions with our model. They were composed of sentences with their associated index as well as the difficulty level of the sentence in the `training_data.csv` file.  

---

### The models:

As a first attempt, we decided to train and test the data on the classic classification models that we have seen in class. We trained a Logistic Regression, a KNN model, a Tree Classifier, as well as a Random Forest Classifier. We trained all these models first with the raw data without any treatment on it, and after we trained it with a tokenized data. Another model we implemented is a model based on BERT-like embeddings which makes contextual relations between words in order to classify them. 

---

## Results <a name="results"></a>

For the raw data: 

| Scores/Models  | Logistic Regression | KNN | Tree Classifier | Random Forest |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Accuracy score | 0.466  | 0.354 | 0.315 | 0.409 |
| Precision score  | 0.464 | 0.419 | 0.324 | 0.409 |
| Recall score  | 0.467 | 0.354 | 0.319 | 0.411 |
| F1 score  | 0.464 | 0.345 | 0.299 | 0.397 |

We took as well the best classic model above (Logistic Regression) and tried different tokenizers:

| Scores/Models  | Spacy | NLTK | GTP2 | 
| ------------- | ------------- | ------------- | ------------- |
| Accuracy score | 0.477  | 0.493 | 0.477 | 
| Precision score  | 0.476 | 0.489 | 0.476 |
| Recall score  | 0.478 | 0.494 | 0.478 | 
| F1 score  | 0.475 | 0.489 | 0.475 |

In the Logistic Regression, the NLTK tokenizer was returning the highest accuracy score.

For the BERT model, we compared it with our classic models tokenized with the spacy tokenizer, which was giving us the highest accuracy:

| Scores/Models  | Logistic Regression | Ridge | KNN | Tree Classifier | Random Forest | BERT-TensorFlow |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Accuracy score | 0.477  | 0.465 | 0.384 | 0.331 | 0.405 | 0.538 |
| Precision score  | 0.476 | 0.466 | 0.426 | 0.356 | 0.401 | 0.451 |
| Recall score  | 0.478 | 0.465 | 0.384 | 0.333 | 0.406 | 0.305 |
| F1 score  | 0.475 | 0.462 | 0.368 | 0.313 | 0.397 | 0.360 |


With these results we can see that our BERT-TensorFlow model is the best one in terms of accuracy. We can also notice that in the Tree Classifier and Random Forest models, the spacy tokenizer even lower the accuracy score. 



