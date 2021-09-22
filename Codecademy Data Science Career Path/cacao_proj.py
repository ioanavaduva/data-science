# import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

link = requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')

soup = BeautifulSoup(link.content, 'html.parser')

rating_tags = soup.find_all(attrs = {'class':'Rating'})
ratings = []

for elem in range(1, len(rating_tags)):
  ratings.append(float(rating_tags[elem].get_text()))

plt.hist(ratings)
plt.show()

comp_tags = soup.select('.Company')
company_names = []

for tag in comp_tags[1:]:
  company_names.append(tag.get_text())

dic = {'Company': company_names, 'Ratings': ratings}
df = pd.DataFrame.from_dict(dic)

mean_ratings = df.groupby('Company').Ratings.mean()
ten_best = mean_ratings.nlargest(10)
print(ten_best)

cocoa_tags = soup.select('.CocoaPercent')
cocoa_perc = []
for tag in cocoa_tags[1:]:
  cocoa_perc.append(float(tag.get_text().strip('%')))

dic['CocoaPercent'] = cocoa_perc
df = pd.DataFrame.from_dict(dic)

plt.clf()

plt.scatter(df.CocoaPercent, df.Ratings)
z = np.polyfit(df.CocoaPercent, df.Ratings, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercent, line_function(df.CocoaPercent), "r--")
plt.show()