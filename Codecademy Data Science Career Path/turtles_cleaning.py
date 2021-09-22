import requests
from bs4 import BeautifulSoup
import pandas as pd

prefix = "https://content.codecademy.com/courses/beautifulsoup/"
webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

turtle_links = soup.find_all("a")
links = []
#go through all of the a tags and get the links associated with them"
for a in turtle_links:
  links.append(prefix+a["href"])
    
#Define turtle_data:
turtle_data = {}

#follow each link:
for link in links:
  webpage = requests.get(link)
  turtle = BeautifulSoup(webpage.content, "html.parser")
  turtle_name = turtle.select(".name")[0].get_text()
  
  stats = turtle.find("ul")
  stats_text = stats.get_text("|")
  turtle_data[turtle_name] = stats_text.split("|")

# datafame formatting
turtle_df = pd.DataFrame(turtle_data)
print(turtle_df)

for row in turtle_df.index:
  if row%2 == 0:
    turtle_df.drop([row], axis = 0, inplace = True)
turtle_df.rename(index = {1:'AGE', 3:'WEIGHT', 5:'SEX', 7:'BREED', 9: 'SOURCE'}, inplace = True)  

turtles_df = turtle_df.transpose()

turtles_df['AGE'] = turtles_df['AGE'].str.replace(r'AGE: ', '')
turtles_df['WEIGHT'] = turtles_df['WEIGHT'].str.replace(r'WEIGHT: ', '')
turtles_df['SEX'] = turtles_df['SEX'].str.replace(r'SEX: ', '')
turtles_df['BREED'] = turtles_df['BREED'].str.replace(r'BREED: ', '')
turtles_df['SOURCE'] = turtles_df['SOURCE'].str.replace(r'SOURCE: ', '')

print(turtles_df)