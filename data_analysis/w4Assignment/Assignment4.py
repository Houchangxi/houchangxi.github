import pandas as pd
import numpy as np
from scipy import stats

skpid = list(range(5))
skpid.append(6)
skpid.append(7)
# print(skpid)
GDP_all = pd.read_excel('gdplev.xls', skiprows=skpid)
def get_GDP():
    skpid = list(range(5))
    skpid.append(6)
    skpid.append(7)
    GDP_all = pd.read_excel('gdplev.xls', skiprows=skpid)
    GDP_quarter = GDP_all.drop(['Unnamed: 0','Unnamed: 3','GDP in billions of current dollars','GDP in billions of chained 2009 dollars','Unnamed: 7'],axis=1)
    GDP_quarter.rename(columns ={'Unnamed: 4':'Year'},inplace=True)
    GDP_quarter.dropna(inplace=True)
    return GDP_quarter

def get_recession_start():

    GDP_annual = GDP_all.drop(['Unnamed: 3','Unnamed: 4','GDP in billions of current dollars.1','GDP in billions of chained 2009 dollars.1','Unnamed: 7'],axis=1)
    GDP_annual.rename(columns ={'Unnamed: 0':'Year'},inplace=True)
    GDP_annual.dropna(inplace=True)
    GDP_annual['Year'] = GDP_annual['Year'].astype(int)
    GDP_annual.set_index('Year',inplace=True)
    # print(GDP_annual.head())
    # print(GDP_annual.index)

    GDP_quarter = GDP_all.drop(['Unnamed: 0','Unnamed: 3','GDP in billions of current dollars','GDP in billions of chained 2009 dollars','Unnamed: 7'],axis=1)
    GDP_quarter.rename(columns ={'Unnamed: 4':'Year'},inplace=True)
    GDP_quarter.dropna(inplace=True)
    GDP_quarter = GDP_quarter[GDP_quarter['Year']>='2000q1']
    # GDP_quarter.set_index('Year',inplace=True)
    # print(GDP_quarter.head().T)
    # print(GDP_quarter.shape)
    recession_date = []
    last = 0.0
    for index,i in GDP_quarter.iterrows():
        if i['GDP in billions of chained 2009 dollars.1'] < last:
            recession += 1
        else:
            recession = 0
        last = i['GDP in billions of chained 2009 dollars.1']
        if recession >= 2:
            recession_date.append(index-2)
    # print(GDP_quarter.loc[recession_date[0]]['Year'])
    return GDP_quarter.loc[recession_date[0]]['Year']


# print(get_recession_start())

def get_recession_end():
    '''Returns the year and quarter of the recession end time as a 
    string value in a format such as 2005q3'''
    recession_flag=0
    skpid = list(range(5))
    skpid.append(6)
    skpid.append(7)
    GDP_all = pd.read_excel('gdplev.xls', skiprows=skpid)
    GDP_quarter = GDP_all.drop(['Unnamed: 0','Unnamed: 3','GDP in billions of current dollars','GDP in billions of chained 2009 dollars','Unnamed: 7'],axis=1)
    GDP_quarter.rename(columns ={'Unnamed: 4':'Year'},inplace=True)
    GDP_quarter.dropna(inplace=True)
    GDP_quarter = GDP_quarter[GDP_quarter['Year']>=get_recession_start()]
    recession_end_date = []
    last = 0.0
    for index,i in GDP_quarter.iterrows():
        if i['GDP in billions of chained 2009 dollars.1'] > last:
            recession_flag += 1
        else:
            recession_flag = 0
        last = i['GDP in billions of chained 2009 dollars.1']
        if recession_flag >= 2:
            recession_end_date.append(index)
    return GDP_quarter.loc[recession_end_date[0]]['Year']
# print(get_recession_end())


def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a 
    string value in a format such as 2005q3'''
    GDP_quarter = get_GDP()
    GDP_quarter = GDP_quarter[GDP_quarter['Year'] >= get_recession_start()]
    GDP_quarter = GDP_quarter[GDP_quarter['Year'] <= get_recession_end()]
    # print(GDP_quarter.loc[GDP_quarter['GDP in billions of chained 2009 dollars.1'].idxmin()]['Year'])
    return GDP_quarter.loc[GDP_quarter['GDP in billions of chained 2009 dollars.1'].idxmin()]['Year']

# print(get_recession_bottom())


#
# print(citys_all_homes.head())
# print(citys_all_homes.head().T)
# university_towns = pd.read_table("university_towns.txt", header = None,names = ['all'])

university_towns = pd.read_csv('university_towns.txt',header=None,names= ['raw data'])
index_num = 0
result = pd.DataFrame(columns=["State", "RegionName"])
states = []
regions = []
for index,row in university_towns.iteritems():
    # print(len(row))
    # print()
    for c in row:
        if '[edit]' in c:
            index_num += 1
            # print(c.split('[edit]')[0],index_num)
            states.append(c.split('[edit]')[0])
        else:
            regions.append([c.split(' (')[0],index_num])


for i,c in enumerate(states):
    for j in regions:
        if i+1 == j[1]:
            result.loc[result.shape[0]+1] = [c,j[0]]


# print(result)
# print(states)
# print('++++++++++++++++++')
# print(regions)


def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  )

    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''

    university_towns = pd.read_csv('university_towns.txt', header=None, names=['raw data'],sep='\n')
    index_num = 0
    result = pd.DataFrame(columns=["State", "RegionName"])
    states = []
    regions = []
    for index, row in university_towns.iteritems():
        for c in row:
            if '[edit]' in c:
                index_num += 1
                states.append(c.split('[edit]')[0])
            else:
                regions.append([c.split(' (')[0], index_num])

    for i, c in enumerate(states):
        for j in regions:
            if i + 1 == j[1]:
                result.loc[result.shape[0] + 1] = [c, j[0]]

    return result.reset_index().drop(['index'],axis=1)

get_list_of_university_towns()


# print(university_towns.head())
# test = get_list_of_university_towns()
# test['RegionName'] = test[0].apply(lambda x: x.split('(')[0].strip() if x.count('(') > 0 else x.rstrip('\n') if x.count('\n') > 0 else np.NaN)

def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean 
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].

    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.

    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''

    states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National',
              'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana',
              'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho',
              'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan',
              'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi',
              'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota',
              'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut',
              'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York',
              'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado',
              'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota',
              'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia',
              'ND': 'North Dakota', 'VA': 'Virginia'}
    citys_all_homes = pd.read_csv('City_Zhvi_AllHomes.csv')

    citys_all_homes['State_F'] = citys_all_homes['State'].map(states)
    citys_all_homes_new = pd.merge(citys_all_homes[citys_all_homes.columns[0:2]],
                                   citys_all_homes[citys_all_homes.columns[-201:]], how='outer', left_index=True,
                                   right_index=True)
    citys_all_homes_new.fillna(0, inplace=True)
    for i in range(int((len(citys_all_homes.columns[-201:]) - 1) / 3)):
        if int(citys_all_homes_new.columns[i * 3 + 4].split('-')[1]) / 3 == 1.:
            name = citys_all_homes_new.columns[i * 3 + 4].split('-')[0] + 'q1'
            citys_all_homes_new[name] = citys_all_homes_new[citys_all_homes_new.columns[i * 3 + 2:i * 3 + 5]].mean(
                axis=1)
        elif int(citys_all_homes_new.columns[i * 3 + 4].split('-')[1]) / 3 == 2.:
            name = citys_all_homes_new.columns[i * 3 + 4].split('-')[0] + 'q2'
            citys_all_homes_new[name] = citys_all_homes_new[citys_all_homes_new.columns[i * 3 + 2:i * 3 + 5]].mean(
                axis=1)
        elif int(citys_all_homes_new.columns[i * 3 + 4].split('-')[1]) / 3 == 3.:
            name = citys_all_homes_new.columns[i * 3 + 4].split('-')[0] + 'q3'
            citys_all_homes_new[name] = citys_all_homes_new[citys_all_homes_new.columns[i * 3 + 2:i * 3 + 5]].mean(
                axis=1)
        elif int(citys_all_homes_new.columns[i * 3 + 4].split('-')[1]) / 3 == 4.:
            name = citys_all_homes_new.columns[i * 3 + 4].split('-')[0] + 'q4'
            citys_all_homes_new[name] = citys_all_homes_new[citys_all_homes_new.columns[i * 3 + 2:i * 3 + 5]].mean(
                axis=1)

    citys_all_homes_new['2016q3'] = citys_all_homes_new[citys_all_homes_new.columns[200:202]].mean(axis=1)
    citys_all_homes_new.rename(columns={'State_F': 'State'}, inplace=True)
    citys_all_homes_new.set_index(['State', 'RegionName'], inplace=True)
    result = citys_all_homes_new[citys_all_homes_new.columns[-67:]]

    return result


recession_button = get_recession_bottom()
recession_start = get_recession_start()
recession_end = get_recession_end()
print(recession_start,recession_button,recession_end)

house_price_all = convert_housing_data_to_quarters()

l_date = house_price_all.columns.values.tolist()
print(l_date[l_date.index(recession_start):l_date.index(recession_button)+1])
recession_house_data = house_price_all[l_date[l_date.index(recession_start):l_date.index(recession_button)+1]]

# print((house_price_all.columns >recession_start))


# decline_house_price =









