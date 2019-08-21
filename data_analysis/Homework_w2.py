import pandas as pd
# import numpy as np
df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
# print (df.head())


def answer_one():
    return df['Gold'].idxmax()


def answer_two():
    diff = df['Gold']-df['Gold.1']
    return diff.abs().idxmax()


def answer_three():
    df_gold = df[(df['Gold.1']>0) & (df['Gold']>0)]
    max_number = ((df_gold['Gold']-df_gold['Gold.1']).abs()/df_gold['Gold.2']).max()
    return df_gold[((df_gold['Gold']-df_gold['Gold.1']).abs()/df_gold['Gold.2'])==max_number].index.tolist()[0]


def answer_four():
    df['Points'] = df['Gold.2']*3+df['Silver.2']*2+df['Bronze.2']*1
    return df['Points']

# Part 2
census_df = pd.read_csv('census.csv')
# census_df.head()

def answer_five():
    stname50 = census_df[census_df['SUMLEV']==50]
    stnames = stname50['STNAME'].unique()
    counties = []
    for i in stnames:
        counties.append(len(stname50[stname50['STNAME']==i]))
    results= pd.Series(counties,index=stnames)
    return results.idxmax()


def answer_six():
    stname50 = census_df[census_df['SUMLEV'] == 50]
    stnames = stname50['STNAME'].unique()
    three_best = []
    for state in stnames:
        df = stname50[stname50['STNAME']==state]
        top = df.nlargest(3,'CENSUS2010POP')['CENSUS2010POP'].sum()
        three_best.append(top)
    top_ser = pd.Series(three_best,index=stnames).sort_values(ascending=False)
    result = list(top_ser[0:3].index)
    return result

def answer_seven():
    stname50 = census_df[census_df['SUMLEV']==50]
    pop_counties = stname50[['CTYNAME','POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']]
    max_gap = []
    for c in pop_counties.iterrows():
        a = c[1][1:]
        max_gap.append(a.max()-a.min())
    results = pd.Series(max_gap,index=pop_counties['CTYNAME'])
    return results.idxmax()


def answer_eight():
    stname50 = census_df[census_df['SUMLEV']==50]
    region_one_two = stname50[stname50['REGION']<3]
    indexs = []
    for i,c in enumerate(region_one_two.CTYNAME):
        sep_name = c.split(' ')
        if sep_name[0] == 'Washington':
            indexs.append(i)
    region_one_two_name = region_one_two.iloc[indexs]
    results = region_one_two_name[lambda x:x['POPESTIMATE2015']>x['POPESTIMATE2014']]
    return results.loc[:,['STNAME', 'CTYNAME']]