
import pandas as pd

df = pd.read_excel('for.xlsx')
#df2 = df[['First', 'Second']]

first = df['First']
last = df['Last']

mylist = ((first, last))

for values in mylist:
    if values < 3:    
        print(values)



'''
myList = [first, last]
myList2 = [0, 1, 2, 3, 4, 5, 10]


for value in myList2:
    if value <3:
        print(value)

#print(vals)      
'''
      


'''
#print(for_df)
for i in range(0,3):
    for j in range(0, 5):
        if j > 5-2:     
            print(i, j)
'''


#for i in range(0,3):       


            

