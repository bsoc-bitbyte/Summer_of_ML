import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r'C:\Users\Shruti Sachan\Downloads\final_cccf.csv')
print(df.shape)
df1=df.dropna()
print(df1)
print(df1.shape)
X=df1['cc_rating']
Y=df1['cf_rating']
correlation=df1['cc_rating'].corr(df1['cf_rating'])
print(correlation)
plt.figure(figsize=(10,6))
plt.scatter(X,Y)
plt.title(f'Scatterplot with correlation:{correlation:.2f}')
plt.xlabel('cc_rating')
plt.ylabel('cf_rating')
plt.savefig('relationship_plot.png')
plt.show()
sns.regplot(x=X,y=Y,scatter_kws={'color':'blue'},line_kws={'color':'red'})
plt.title('RegressionLine')
plt.show()
import numpy as np
x_mean=np.mean(X)
y_mean=np.mean(Y)
numerator=np.sum((X-x_mean)*(Y-y_mean))
denominator=np.sum((X-x_mean)**2)
slope=numerator/denominator
intercept=y_mean-slope*x_mean
print(slope)
print(intercept)