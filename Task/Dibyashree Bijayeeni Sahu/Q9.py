import pandas as pd

irisdataset=pd.read_csv('iris.csv')
print(irisdataset.head())
sepalsum=irisdataset["sepal_length"].sum()
print('sum of length of sepals :',sepalsum)
maxpetallength=irisdataset['petal_length'].idxmax()
print('maximum petal length index:',maxpetallength)
minpetallength=irisdataset['petal_length'].idxmin()
print('maximum petal length index:',minpetallength)
