import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

my_data = pd.read_csv('appstore_games.csv')

md_price = my_data['Price'].replace(0, np.NaN)
md_AUR = my_data['Average User Rating'].replace(0, np.NaN)
md_URC = my_data['User Rating Count'].replace(0, np.NaN)
md_size = my_data['Size'].replace(0, np.NaN)
md_AR = my_data['Age Rating'].replace(0, np.NaN)

md_price.dropna(inplace=True)
md_AUR.dropna(inplace=True)
md_URC.dropna(inplace=True)
md_size.dropna(inplace=True)
md_AR.dropna(inplace=True)

print(my_data['Price'])

data_top = my_data.head()

for col in my_data.columns:
    print(col)

print("Price mean is", + md_price.mean()) # Avg Price of the Games
print("Price mode is", + md_price.mode())
print("Price median is", + md_price.median())
print("Price max is", + md_price.max())
print("Price min is", + md_price.min(), '\n')

print("Average User Rating mean is", + md_AUR.mean()) # Ave of amount of in app purchases
print("Average User Rating mode is", + md_AUR.mode())
print("Average User Rating median is", + md_AUR.median())
print("Average User Rating max is", + md_AUR.max())
print("Average User Rating min is", + md_AUR.min(), '\n')

print("User Rating Count mean is", + md_URC.mean()) # total avg user rating of the dataset.
print("User Rating Count mode is", + md_URC.mode())
print("User Rating Count median is", + md_URC.median())
print("User Rating Count max is", + md_URC.max())
print("User Rating count min is", + md_URC.min(), '\n')

print("App Size mean is", + md_size.mean()/ 8000000) # total Size of the dataset.
print("App Size mode is", + md_size.mode()/ 8000000)
print("App Size median is", + md_size.median()/ 8000000)
print("App Size max is", + md_size.max()/ 8000000)
print("App Size min is", + md_size.min()/ 8000000, '\n')

print("Age Rating mean is", + md_AR.mean()) # total Age Rating  rating of the dataset.
print("Age Rating mode is", + md_AR.mode())
print("Age Rating median is", + md_AR.median())
print("Age Rating max is", + md_AR.max())
print("Age Rating min is", + md_AR.min(), '\n')




md_price.plot.hist(grid=True, bins=20, rwidth=0.9, color='#607c8e')
plt.title('Price Histogram')
plt.xlabel('Cost of app')
plt.ylabel('Frequence of App cost')
plt.grid(axis='y', alpha=0.75)

md_URC.plot.hist(grid=True, bins=20, rwidth=0.9, color='#607c8e')
plt.title('Number of User Ratings Histogram')
plt.xlabel('User Rating Count')
plt.ylabel('Frequence of User Rating')
plt.grid(axis='y', alpha=0.75)

md_AUR.plot.hist(grid=True, bins=20, rwidth=0.9, color='#607c8e')
plt.title('Average User Rating Histogram')
plt.xlabel('Rating Scale')
plt.ylabel('Frequence of Rating occurance')
plt.grid(axis='y', alpha=0.75)

(md_size/8000000).plot.hist(grid=True, bins=10, rwidth=0.9, color='#607c8e')
plt.title('Size Histogram')
plt.xlabel('Size Range')
plt.ylabel('Frequence of Size')
plt.grid(axis='y', alpha=0.75)

md_AR.plot.hist(grid=True, bins=10, rwidth=0.9, color='#607c8e')
plt.title('Age Rating Histogram')
plt.xlabel('Age Range')
plt.ylabel('Frequence of Age')
plt.grid(axis='y', alpha=0.75)




pmf_price = md_price.value_counts().sort_index() / len(md_price)
pmf_price.plot.bar()
plt.title('Probability Mass Function of Price')
plt.xlabel('Price')
plt.ylabel('Probability')

pmf_age_rating = md_AR.value_counts().sort_index() / len(md_AR)
pmf_age_rating.plot.bar()
plt.title('Probability Mass Function of Age Rating')
plt.xlabel('Age rating')
plt.ylabel('Probability')

aur = md_AUR.sort_values()
aur[len(aur)] = aur.iloc[-1]
cum_dist = np.linspace(0.,1.,len(aur))
aur_cdf = pd.Series(cum_dist, index=aur)
aur_cdf.plot(drawstyle='steps')
plt.title('Cumulative Distribution Function of Average User Rating')
plt.xlabel('Average User Rating')
plt.ylabel('Probablity')





sns.stripplot(md_price[(md_price < 10)], md_AUR, jitter = 0.5)
plt.title("Average User Rating vs Price")
plt.xlabel('Price')
plt.ylabel('Average User Rating')

sns.stripplot(md_price[(md_price < 10)], md_URC[(md_URC < 100000)], jitter = True)
plt.title("Price vs User Rating Count")
plt.xlabel('Price')
plt.ylabel('User Rating Count')

#sns.regplot(my_data['Average User Rating'], my_data['Age Rating'])



sns.regplot(x = md_URC, y = md_AUR)

#dr_price = my_data['Price'].replace(0, np.NaN)
#dr_price.dropna(inplace=True)
#print(dr_price)
#
#dr_aur = my_data['Average User Rating'].replace(0, np.NaN)
#dr_aur.dropna(inplace=True)
#print(dr_aur)

#np.cov(dr_price, dr_aur)
#from numpy import cov
#cova =cov(md_AR == md_price)
#print(cova)

