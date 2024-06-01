import pandas as pd
iris_df = pd.read_csv('iris.csv')
iris_df.rename(columns={'S_length': 'sepal length',
                        'S_width': 'sepal width',
                        'P_length': 'petal length',
                        'P_width': 'petal width'}, inplace=True)
print(iris_df.head())
print(iris_df.columns)
sepal_length_sum = iris_df['sepal_length'].sum()
print("Sum of sepal lengths is:", sepal_length_sum)
max_length_index = iris_df['petal_length'].idxmax()
min_length_index = iris_df['petal_length'].idxmin()
print("Index value of maximum petal length:", max_length_index)
print("Index value of minimum petal length:", min_length_index)
