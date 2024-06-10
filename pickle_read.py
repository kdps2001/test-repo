import numpy as np
import pandas as pd
import seaborn as sns
sns.set_palette('husl')
import matplotlib.pyplot as plt
import pickle

url='https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv' 
col_name = ['sepal_length','sepal_width','petal_length','petal_width','class']
dataset = pd.read_csv(url,names = col_name)

x = dataset.drop(['class'], axis = 1)
y = dataset['class']

print('x shape : ', x.shape,'y shape : ', y.shape)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)


with open('C:/Users/qwepa/OneDrive/Desktop/python_repository/svm.pickle','rb') as f:
    model = pickle.load(f)
    
predictions = model.predict(x_test)

from sklearn.metrics import accuracy_score
prediction_score = accuracy_score(y_test, predictions)

print(prediction_score)

from sklearn.metrics import classification_report
print(classification_report(y_test, predictions))

from sklearn.metrics import ConfusionMatrixDisplay
ConfusionMatrixDisplay.from_predictions(y_test, predictions)
plt.show()

data = {
    'sepal_length': [4.0],
    'sepal_width': [2.0],
    'petal_length': [1.0],
    'petal_width': [0.1]
}
df = pd.DataFrame(data)
print(df)
iris_class = model.predict(df)
print(iris_class)
#########pawan####