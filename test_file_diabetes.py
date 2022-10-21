import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


dbtes = pd.read_csv("C:\\Users\\anand\\Desktop\\diabetes.csv")
'''print (dbtes.head())
print ('the data types are\n', dbtes.dtypes)
duplicate_rows_dbtes = dbtes[dbtes.duplicated()]
print ('\n number of duplicate rows:', duplicate_rows_dbtes, '\n')
print ('\n the number of values are: \n',dbtes.count())
print ('\n the number of cells with no values are: \n', dbtes.isnull().sum())
'''

sns.boxplot (dbtes, x = 'Outcome', y = 'Age')
plt.show()
sns.boxplot (dbtes, x = 'Outcome', y = 'BMI')
plt.show()
fig,ax = plt.subplots(figsize = (10,6))
ax.scatter(dbtes['Glucose'], dbtes['Insulin'])
ax.set_xlabel('glucose')
ax.set_ylabel('insulin')
plt.show()
'''
fig = px.box(df, x='Outcome', y='Age')
fig.update_traces(marker_color="midnightblue",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig.update_layout(title_text='Age and Outcome')
fig.show()
'''
