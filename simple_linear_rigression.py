import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score , mean_squared_error
import os

data = pd.read_csv('/content/sample_data/Salary_Data.csv')
#data.head()
#data.info()
data.describe()

sns.pairplot(data ,x_vars=['YearsExperience'],y_vars=['Salary'],size =6 , kind = 'scatter')

X = data.iloc[:,:-1]
Y = data['Salary']

X_train,X_test,Y_train,Y_test = train_test_split(X ,Y , train_size = 0.8 ,random_state= 10)

model = LinearRegression()
model.fit(X_train,Y_train)
model.score(X_train,Y_train)
model.score(X_test,Y_test)

plt.scatter(X_train,Y_train,color = 'red')
plt.plot(X_train,model.predict(X_train),color = 'BLUE')
plt.title('Traning set')

y_pred = model.predict(X_test)
plt.scatter (X_test , y_pred , color = 'red')
plt.plot (X_test , y_pred , color = 'blue')

c = [ i for i in range (1,len(Y_test)+1)]
# to make list from every element index in y test and y predict to compare
plt.plot(c,Y_test, color = 'red',linestyle = '-')
plt.plot(c,y_pred, color = 'blue',linestyle = '-')
plt.xlabel('Index')
plt.ylabel('Salary')

##plt the error
c = [ i for i in range (1,len(Y_test)+1)]
# to make list from every element index in y test and y predict to compare
#y_test minus y_pred
plt.plot(c,Y_test-y_pred, color = 'red',linestyle = '-')

# to know accuracy we use score , to know error we use mse by the way no one use graphs its just to know
mse = mean_squared_error(Y_test,y_pred)
rsq = r2_score (Y_test,y_pred)
#rsq use to to determine the proportion of sample and higher rsq mean more fit
print('mean square error :',mse)
print('r square :',rsq)

print('Intercept of the model:',model.intercept_)
print('Coefficient of the line:',model.coef_)

