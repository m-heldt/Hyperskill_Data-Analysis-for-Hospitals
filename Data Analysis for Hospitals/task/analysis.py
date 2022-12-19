# write your code here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 8)

general = pd.read_csv('general.csv')
prenatal = pd.read_csv('prenatal.csv')
sports = pd.read_csv('sports.csv')

prenatal.columns = general.columns
sports.columns = general.columns

# preprocessing
df = pd.concat([general, prenatal, sports], ignore_index=True)
df.drop(columns=['Unnamed: 0'], inplace=True)
df.dropna(axis=0, thresh=1, inplace=True)
df.loc[(df.gender == 'man') | (df.gender == 'male'), 'gender'] = 'm'
df.loc[(df.gender == 'woman') | (df.gender == 'female'), 'gender'] = 'f'
df.loc[df.hospital == 'prenatal', 'gender'] = df.loc[df.hospital == 'prenatal', 'gender'].fillna('f')
df.fillna({'bmi':0, 'diagnosis':0, 'blood_test':0, 'ecg':0, 'ultrasound':0, 'mri':0, 'xray':0, 'children':0, 'months':0}, inplace=True)

# hospital_most_patients = df.hospital.value_counts().index[0]
# stomach_part = df.loc[(df.hospital == 'general') & (df.diagnosis == 'stomach'),'diagnosis'].count()/df.loc[df.hospital == 'general','diagnosis'].count()
# dislocation_part = df.loc[(df.hospital == 'sports') & (df.diagnosis == 'dislocation'),'diagnosis'].count()/df.loc[df.hospital == 'sports','diagnosis'].count()
# age_diff = df.loc[df.hospital == 'general', 'age'].median() - df.loc[df.hospital == 'sports', 'age'].median()
# most_blood_hospital = df.loc[df.blood_test == 't', 'hospital'].describe()['top']
# most_blood_tests = df.loc[df.blood_test == 't', 'hospital'].describe()['freq']
#
# print(f"The answer to the 1st question is {hospital_most_patients}")
# print(f"The answer to the 2nd question is {stomach_part:.3f}")
# print(f"The answer to the 3rd question is {dislocation_part:.3f}")
# print(f"The answer to the 4th question is {int(age_diff)}")
# print(f"The answer to the 5th question is {most_blood_hospital}, {most_blood_tests} blood tests")

figure, axis = plt.subplots(3, 1)
plt.figure(1)



# to answer the 1st question in stage 5
plt.hist(df['age'], bins=[0,15,35,55,70,80])

# to answer the 2nd question in stage 5
plt.figure(2)
plt.pie(df.diagnosis.value_counts(), labels=df.diagnosis.value_counts().index)

# to answer the 2nd question in stage 5

general_height = df.groupby(['hospital']).get_group('general').height
prenatal_height = df.groupby(['hospital']).get_group('prenatal').height
sports_height = df.groupby(['hospital']).get_group('sports').height
plt.figure(3)
plt.violinplot([general_height, prenatal_height, sports_height])
plt.show()


print(f"The answer to the 1st question: 15-35")
print(f"The answer to the 2nd question: pregnancy")
print(f"The answer to the 3rd question: It's because people love each other :love:")
