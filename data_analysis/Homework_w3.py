import pandas as pd
import numpy as np

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')
print(staff_df.head())
print()
print(student_df.head())
print(pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True))
print(pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True))
print(pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True))
print(pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True))
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
print(pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name'))

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])
print(pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name'))

staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])
staff_df
student_df
print(pd.merge(staff_df, student_df, how='inner', left_on=['First Name','Last Name'], right_on=['First Name','Last Name']))

df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
df.rename(columns={0: 'Grades'}, inplace=True)


s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])
t = pd.Categorical(['Low','Medium','High'], ordered=True)
print('+',s.astype(dtype=t))

# print(s.astype('category',categories=['Low','Medium','High'],ordered=True))

# Pivot Tables
df = pd.read_csv('cars.csv')
print(df.head())
df.pivot_table(values='(kW)',index='YEAR',columns='Make',aggfunc=np.mean)
print()
# df.pivot_table(values='(kW)',index='YEAR',columns='Make',aggfunc=[np.mean,np.min],margins=True)

# Bikes.pivot_table(values=['Price','Rating'],index='Manufacturer',columns='Bike Type',aggfunc=np.mean)



