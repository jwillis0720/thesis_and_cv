import pandas
import sys
df = pandas.read_excel('jordan/JordansReferences.xlsx')
df = df.sort_values('Rank')
df = df[df['Enabled'] == True]
df = df.fillna("")
df['Number'] = df['Number'].astype(str).apply(lambda x: '('+x[:3]+') '+x[3:6]+'-'+x[6:10])
print("\section{References}")
for i in df[df.columns[2:]].iterrows():
    print("\cvreference",end='')
    for j in i[1]:
        print("{{{}}}".format(j),end='')
    print("\n\\vspace{0.2cm}")