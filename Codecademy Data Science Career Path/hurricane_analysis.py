# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1 Hurricanes, also known as cyclones or typhoons, are one of the most powerful
# forces of nature on Earth. Due to climate change caused by human activity, the
# number and intensity of hurricanes has risen, calling for better preparation
# by the many communities that are devastated by them. As a concerned
# environmentalist, you want to look at data about the most powerful hurricanes
# that have occurred. Begin by looking at the damages list. The list contains
# strings representing the total cost in USD($) caused by 34 category 5
# hurricanes (wind speeds ≥ 157 mph (252 km/h )) in the Atlantic region. For
# some of the hurricanes, damage data was not recorded ("Damages not recorded"),
# while the rest are written in the format "Prefix-B/M", where B stands for
# billions (1000000000) and M stands for millions (1000000). Write a function
# that returns a new list of updated damages where the recorded data is
# converted to float values and the missing data is retained as "Damages not
# recorded". Test your function with the data stored in damages. Update Recorded
# Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def conver_damage(damage_list, conversion):
  new_damage = []
  for damage in damage_list:
    if damage == 'Damages not recorded':
      new_damage.append(damage)
    elif damage.find('M') == -1:
      new_damage.append(float(damage[:-1]) * conversion['M'])
    elif damage.find('B') == -1:
      new_damage.append(float(damage[:-1]) * conversion['B'])
  return new_damage

# test function by updating damages
new_dam = conver_damage(damages, conversion)
# print(new_dam)

# 2 Additional data collected on the 34 strongest Atlantic hurricanes are
# provided in a series of lists. The data includes: names: names of the
# hurricanes, months: months in which the hurricanes occurred, years: years in
# which the hurricanes occurred,max_sustained_winds: maximum sustained winds
# (miles per hour) of the hurricanes, areas_affected: list of different areas
# affected by each of the hurricanes, deaths: total number of deaths caused by
# each of the hurricanes. The data is organized such that the data at each index,
# from 0 to 33, corresponds to the same hurricane. For example, names[0] yields
# the “Cuba I” hurricane, which ouccred in months[0] (October) years[0] (1924).
# Write a function that constructs a dictionary made out of the lists, where the
# keys of the dictionary are the names of the hurricanes, and the values are
# dictionaries themselves containing a key for each piece of data (Name, Month,
# Year,Max Sustained Wind, Areas Affected, Damage, Death) about the hurricane.
# Thus the key "Cuba I" would have the value: {'Name': 'Cuba I', 'Month':
# 'October', 'Year': 1924, 'Max Sustained Wind': 165, 'Areas Affected':
# ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 'Damage':
# 'Damages not recorded', 'Deaths': 90}. Test your function on the lists of data
# provided. 

# Create a Table
def build_dic(name, month, year, wind, areas, damage, deaths):
  dic = {}
  for index in range(len(names)):
    dic.update({name[index]: {'Name': name[index], 'Month': month[index], 'Year': year[index], 'Max Sustained Wind': wind[index], 'Areas Affected': areas[index], 'Damage': damage[index], 'Deaths': deaths[index]}})
  return dic

# Create and view the hurricanes dictionary
hurricanes_dic = build_dic(names, months, years, max_sustained_winds, areas_affected, new_dam, deaths)
print(hurricanes_dic['Cuba I'])

# 3 In addition to organizing the hurricanes in a dictionary with names as the
# key, you want to be able to organize the hurricanes by year. Write a function
# that converts the current dictionary of hurricanes to a new dictionary, where
# the keys are years and the values are lists containing a dictionary for each
# hurricane that occurred in that year. For example, the key 1932 would yield
# the value: [{'Name': 'Bahamas', 'Month': 'September', 'Year': 1932, 'Max
# Sustained Wind': 160, 'Areas Affected': ['The Bahamas', 'Northeastern United
# States'], 'Damage': 'Damages not recorded', 'Deaths': 16}, {'Name': 'Cuba II',
# 'Month': 'November', 'Year': 1932, 'Max Sustained Wind': 175, 'Areas
# Affected': ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The
# Bahamas', 'Bermuda'], 'Damage': 40000000.0, 'Deaths': 3103}]. Test your
# function on your hurricane dictionary. 

# Organizing by Year
def hurricanes_by_year(dictio):
  year_hurricanes = {}
  for hurricane in dictio:
    current_year = dictio[hurricane]['Year']
    current_hurricane = dictio[hurricane]
    if current_year not in year_hurricanes:
      year_hurricanes[current_year] = [current_hurricane]
    else:
      year_hurricanes[current_year].append(current_hurricane)
  return year_hurricanes

# create a new dictionary of hurricanes with year and key
hurricanes_year = hurricanes_by_year(hurricanes_dic)
# print(hurricanes_year[1932])

# 4 You believe that knowing how often each of the areas of the Atlantic are
# affected by these strong hurricanes is important for making preparations for
# future hurricanes. Write a function that counts how often each area is listed
# as an affected area of a hurricane. Store and return the results in a
# dictionary where the keys are the affected areas and the values are counts of
# how many times the areas were affected. Test your function on your hurricane
# dictionary.

#  Counting Damaged Areas
def damaged_areas_dic(dictio):
  area_count = {}
  for hurricane in dictio.values():
    for area in hurricane['Areas Affected']:
      current_area = area
      if current_area in area_count:
        area_count[current_area] +=1
      else:
        area_count[current_area] = 1
  return area_count

# create dictionary of areas to store the number of hurricanes involved in
areas = damaged_areas_dic(hurricanes_dic)
# print(areas)

# 5 Write a function that finds the area affected by the most hurricanes, and
# how often it was hit. Test your function on your affected area dictionary.

# Calculating Maximum Hurricane Count
def max_hurricane_count(hurricane_areas):
  max_count = 0
  area = ''
  for key, value in hurricane_areas.items():
    if value > max_count:
      max_count = value
      area = key
  return 'Most affected area is ' + area + ' with a count of ' + str(max_count)

# find most frequently affected area and the number of hurricanes involved in
most_hit_area = max_hurricane_count(areas)
# print(most_hit_area)

# 6 Write a function that finds the hurricane that caused the greatest number of
# deaths, and how many deaths it caused. Test your function on your hurricane
# dictionary.

# Calculating the Deadliest Hurricane
def most_deaths(hurricanes):
  max_deaths = 0
  max_deaths_hurricane = ''
  for hurricane in hurricanes.values():
    # print(hurricane)
    if int(hurricane['Deaths']) > max_deaths:
      max_deaths = hurricane['Deaths']
      max_deaths_hurricane = hurricane['Name']
  return 'The hurricane ' + max_deaths_hurricane + ' has most deaths, with ' + str(max_deaths)

# find highest mortality hurricane and the number of deaths
most_deaths_hurr = most_deaths(hurricanes_dic)
# print(most_deaths_hurr)

# 7 Just as hurricanes are rated by their windspeed, you want to try rating
# hurricanes based on other metrics. Write a function that rates hurricanes on a
# mortality scale according to the following ratings, where the key is the
# rating and the value is the upper bound of deaths for that rating. For
# example, a hurricane with a 1 mortality rating would have resulted in greater
# than 0 but less than or equal to 100 deaths. A hurricane with a 5 mortality
# rating would have resulted in greater than 10000 deaths. Store the hurricanes
# in a new dictionary where the keys are mortality ratings and the values are
# lists containing a dictionary for each hurricane that falls into that
# mortality rating. Test your function on your hurricane dictionary.

# Rating Hurricanes by Mortality
def mortality_rating(hurricanes):
  mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for hurricane in hurricanes.values():
    if mortality_scale[0] <= int(hurricane['Deaths']) < mortality_scale[1]:
      hurricanes_by_mortality[0].append(hurricane)
    elif mortality_scale[1] <= int(hurricane['Deaths']) < mortality_scale[2]:
      hurricanes_by_mortality[1].append(hurricane)
    elif mortality_scale[2] <= int(hurricane['Deaths']) < mortality_scale[3]:
      hurricanes_by_mortality[2].append(hurricane)
    elif mortality_scale[3] <= int(hurricane['Deaths']) < mortality_scale[4]:
      hurricanes_by_mortality[3].append(hurricane)
    elif int(hurricane['Deaths']) >= mortality_scale[4]:
      hurricanes_by_mortality[4].append(hurricane)
  return hurricanes_by_mortality
              
# categorize hurricanes in new dictionary with mortality severity as key
mortality_hurricanes = mortality_rating(hurricanes_dic)
# print(mortality_hurricanes[3])

# 8 Write a function that finds the hurricane that caused the greatest damage,
# and how costly it was. Test your function on your hurricane dictionary.

# Calculating Hurricane Maximum Damage
def most_damage(hurricanes):
  max_damage = 0
  max_damage_hurricane = ''
  for hurricane in hurricanes.values():
    # print(hurricane)
    if hurricane['Damage'] == 'Damages not recorded':
      continue
    elif int(hurricane['Damage']) > max_damage:
      max_damage = hurricane['Damage']
      max_damage_hurricane = hurricane['Name']
  return 'The hurricane ' + max_damage_hurricane + ' has most deaths, with ' + str(max_damage)
# find highest damage inducing hurricane and its total cost
hurricane_most_damage = most_damage(hurricanes_dic)
print(hurricane_most_damage)

# 9 Lastly, you want to rate hurricanes according to how much damage they cause.
# Write a function that rates hurricanes on a damage scale according to the
# following ratings, where the key is the rating and the value is the upper
# bound of damage for that rating. For example, a hurricane with a 1 damage
# rating would have resulted in damages greater than 0 USD but less than or
# equal to 100000000 USD. A hurricane with a 5 damage rating would have resulted
# in damages greater than 50000000000 USD (talk about a lot of money). Store the
# hurricanes in a new dictionary where the keys are damage ratings and the
# values are lists containing a dictionary for each hurricane that falls into
# that damage rating. Test your function on your hurricane dictionary.

# Rating Hurricanes by Damage

def damage_rating(hurricanes):
  damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for hurricane in hurricanes.values():
    if hurricane['Damage'] == 'Damages not recorded':
      continue
    elif damage_scale[0] <= float(hurricane['Damage']) < damage_scale[1]:
      hurricanes_by_damage[0].append(hurricane)
    elif damage_scale[1] <= float(hurricane['Damage']) < damage_scale[2]:
      hurricanes_by_damage[1].append(hurricane)
    elif damage_scale[2] <= float(hurricane['Damage']) < damage_scale[3]:
      hurricanes_by_damage[2].append(hurricane)
    elif damage_scale[3] <= float(hurricane['Damage']) < damage_scale[4]:
      hurricanes_by_damage[3].append(hurricane)
    elif float(hurricane['Damage']) >= damage_scale[4]:
      hurricanes_by_damage[4].append(hurricane)
  return hurricanes_by_damage
# categorize hurricanes in new dictionary with damage severity as key
damage_hurricanes = damage_rating(hurricanes_dic)
# print(damage_hurricanes[4])
