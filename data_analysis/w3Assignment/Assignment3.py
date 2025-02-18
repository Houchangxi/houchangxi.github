import pandas as pd
import numpy as np



#Question 1 (20%)
# Load the energy data from the file Energy Indicators.xls, which is a list of indicators of energy supply and renewable electricity production from the United Nations for the year 2013, and should be put into a DataFrame with the variable name of energy.
#
# Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer and header information from the datafile. The first two columns are unneccessary, so you should get rid of them, and you should change the column labels so that the columns are:
#
# ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
#
# Convert Energy Supply to gigajoules (there are 1,000,000 gigajoules in a petajoule). For all countries which have missing data (e.g. data with "...") make sure this is reflected as np.NaN values.
#
# Rename the following list of countries (for use in later questions):
#
# "Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"
#
# There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these,
#
# e.g.
#
# 'Bolivia (Plurinational State of)' should be 'Bolivia',
#
# 'Switzerland17' should be 'Switzerland'.
#
#
#
# Next, load the GDP data from the file world_bank.csv, which is a csv containing countries' GDP from 1960 to 2015 from World Bank. Call this DataFrame GDP.
#
# Make sure to skip the header, and rename the following list of countries:
#
# "Korea, Rep.": "South Korea",
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"
#
#
#
# Finally, load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from the file scimagojr-3.xlsx, which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame ScimEn.
#
# Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).
#
# The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'].
#
# This function should return a DataFrame with 20 columns and 15 entries

def get_energy():
    skipr= list(range(16))
    skipr.append(17)
    # skipfooter是倒着数  na_values是把某一个值设为NaN  skiprows可以穿一个list
    energy = pd.read_excel('Energy Indicators.xls','Energy', skiprows= skipr, skipfooter= 38,na_values='...')
    energy.drop(['Unnamed: 0','Unnamed: 1'],axis=1,inplace = True)
    energy.rename(columns={'Unnamed: 2':'Country'},inplace = True)
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    renames = {"Republic of Korea": "South Korea","United States of America20": "United States","United Kingdom of Great Britain and Northern Ireland19": "United Kingdom","China, Hong Kong Special Administrative Region3": "Hong Kong"}
    energy.replace(renames,inplace=True)
    energy['Energy Supply'] *= 1000000
    energy['Country'] = energy['Country'].str.split('\d+').str[0]
    energy['Country'] = energy['Country'].str.split('\s\(').str[0]
    return energy

def get_GDP():
    GDP = pd.read_csv('world_bank.csv',skiprows=4)
    GDP_rename = {"Korea, Rep.": "South Korea","Iran, Islamic Rep.": "Iran","Hong Kong SAR, China": "Hong Kong"}
    GDP.replace(GDP_rename,inplace = True)
    GDP.rename(columns={'Country Name':'Country'},inplace=True)
    GDP = GDP[['Country', '2006', '2007', '2008','2009','2010', '2011','2012','2013','2014','2015']]
    return GDP

def get_ScimEn():
    ScimEn = pd.read_excel('scimagojr-3.xlsx','Sheet1')
    return ScimEn


def answer_one():
    energy,GDP,ScimEn = get_energy(),get_GDP(),get_ScimEn()
    GDP_energy = pd.merge(energy, GDP, how='inner', left_on='Country', right_on='Country')
    GDP_energy_Scimen = pd.merge(GDP_energy, ScimEn, how='inner', left_on='Country', right_on='Country')
    result = (GDP_energy_Scimen.dropna(subset=['Country']).set_index('Country').sort_values(by='Rank').iloc[:15,:])
    return result

# Question 2 (6.6%)
# The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?
#
# This function should return a single number.


def answer_two():
    energy,GDP,ScimEn = get_energy(),get_GDP(),get_ScimEn()
    GDP_energy = pd.merge(GDP, energy, how='inner', left_on='Country', right_on='Country')
    GDP_energy_Scimen = pd.merge(GDP_energy, ScimEn, how='inner', left_on='Country', right_on='Country')
    GDP_energy_outer = pd.merge(GDP, energy, how='outer', left_on='Country', right_on='Country')
    GDP_energy_Scimen_outer = pd.merge(GDP_energy_outer, ScimEn, how='outer', left_on='Country', right_on='Country')
    return len(GDP_energy_Scimen_outer)-len(GDP_energy_Scimen)


# Question 3 (6.6%)
# What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)
#
# This function should return a Series named avgGDP with 15 countries and their average GDP sorted in descending order.




#
# GDP_energy_outer = pd.merge(GDP, energy, how='outer', left_on='Country Name', right_on='Country')
# GDP_energy_Scimen_outer = pd.merge(GDP_energy_outer, ScimEn, how='outer', left_on='Country Name', right_on='Country')
#
# print(GDP_energy_outer.shape,'+',GDP_energy_Scimen_outer.shape)
# # Q2 result
# print(len(GDP_energy_Scimen_outer)-len(GDP_energy_Scimen))
#
#
# Question 3 (6.6%)
# What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)
#
# This function should return a Series named avgGDP with 15 countries and their average GDP sorted in descending order.


def answer_three():
    Top15 = answer_one()
    rows = ['2006', '2007', '2008',
           '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    Top15['avgGDP'] =Top15[rows].mean(axis=1)
    return Top15.sort_values('avgGDP',ascending = False)['avgGDP']


Top15 = answer_one()
# Question 4 (6.6%)
# By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
#
# This function should return a single number.

def answer_four():
    Top15["AvgGDP"] = answer_three()
    Top15.sort_values("AvgGDP", ascending=False, inplace=True)
    final = Top15.iloc[5]['2015']
    initial = Top15.iloc[5]['2006']
    return abs(final - initial)


# Question 5 (6.6%)
# What is the mean Energy Supply per Capita?
#
# This function should return a single number.
def answer_five():
    Top15 = answer_one()

    return Top15['Energy Supply per Capita'].mean()


# Question 6 (6.6%)
# What country has the maximum % Renewable and what is the percentage?
#
# This function should return a tuple with the name of the country and the percentage.

def answer_six():
    Top15 = answer_one()
    return (Top15['% Renewable'].idxmax(),Top15['% Renewable'].max())


# Question 7 (6.6%)
# Create a new column that is the ratio of Self-Citations to Total Citations. What is the maximum value for this new column, and what country has the highest ratio?
#
# This function should return a tuple with the name of the country and the ratio.

def answer_seven():
    Top15 = answer_one()
    Top15['ratio'] = Top15['Self-citations']/Top15['Citations']
    return (Top15['ratio'].idxmax(),Top15['ratio'].max())



# Question 8 (6.6%)
# Create a column that estimates the population using Energy Supply and Energy Supply per capita. What is the third most populous country according to this estimate?
#
# This function should return a single string value

def answer_eight():
    Top15 = answer_one()
    Top15['population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']

    return Top15.sort_values(by='population', ascending=False).index[2]



# Question 9 (6.6%)
# Create a column that estimates the number of citable documents per person. What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the .corr() method, (Pearson's correlation).
#
# This function should return a single number.


def answer_nine():
    Top15 = answer_one()
    Top15['population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable Documents per Capita'] = Top15['Citable documents'] / Top15['population']

    return Top15['Citable Documents per Capita'].corr(Top15['Energy Supply per Capita'])



# Question 10 (6.6%)
# Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.
#
# This function should return a series named HighRenew whose index is the country name sorted in ascending order of rank.


def answer_ten():
    Top15 = answer_one()
    reference = Top15["% Renewable"].median(axis=0)
    Top15["HighRenew"] = Top15.apply(lambda x: 1 if x["% Renewable"] >= reference else 0, axis=1)
    Top15.sort_values(by='Rank', inplace=True)
    return Top15["HighRenew"]


# Question 11 (6.6%)
# Use the following dictionary to group the Countries by Continent, then create a dateframe that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.
#
# ContinentDict  = {'China':'Asia',
#                   'United States':'North America',
#                   'Japan':'Asia',
#                   'United Kingdom':'Europe',
#                   'Russian Federation':'Europe',
#                   'Canada':'North America',
#                   'Germany':'Europe',
#                   'India':'Asia',
#                   'France':'Europe',
#                   'South Korea':'Asia',
#                   'Italy':'Europe',
#                   'Spain':'Europe',
#                   'Iran':'Asia',
#                   'Australia':'Australia',
#                   'Brazil':'South America'}
# This function should return a DataFrame with index named Continent ['Asia', 'Australia', 'Europe', 'North America', 'South America'] and columns ['size', 'sum', 'mean', 'std']


def answer_eleven():
    Top15 = answer_one()
    Top15['population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}
    Continent = pd.DataFrame(columns=['size', 'sum', 'mean', 'std'])
    for group, frame in Top15.groupby(ContinentDict):
        Continent.loc[group] = [frame.shape[0], frame['population'].sum(), frame['population'].mean(),
                                frame['population'].std()]

    return Continent



# Question 12 (6.6%)
# Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?
#
# This function should return a Series with a MultiIndex of Continent, then the bins for % Renewable. Do not include groups with no countries.

def answer_twelve():
    Top15 = answer_one()
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}
    Top15["bins"] = pd.cut(Top15["% Renewable"], 5)

    return Top15.groupby([ContinentDict, Top15['bins']]).size()

# Question 13 (6.6%)
# Convert the Population Estimate series to a string with thousands separator (using commas). Do not round the results.
#
# e.g. 317615384.61538464 -> 317,615,384.61538464
#
# This function should return a Series PopEst whose index is the country name and whose values are the population estimate string.

def answer_thirteen():
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['PopEst'] = Top15['PopEst'].map('{:,}'.format)
    return Top15['PopEst']

