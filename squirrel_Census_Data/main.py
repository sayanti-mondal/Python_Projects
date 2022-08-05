import pandas as pd

#converting the csv to a dataframe
data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

#getting the squirrel count according to their color from data
gray_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrel_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel_count = len(data[data['Primary Fur Color'] == 'Black'])


# print(gray_squirrel_count)
# print(cinnamon_squirrel_count)
# print(black_squirrel_count)

# creating a dictionary with the color and their corresponding count
data_dict = {
    "Fur Color": ["gray", "cinnamon", "black"],
     "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

#print(data_dict) # {'Fur Color': ['gray', 'cinnamon', 'black'], 'Count': [2473, 392, 103]}

# converting the dictionary into a dataframe by pd.DataFrame method
df = pd.DataFrame(data=data_dict)

# converting the dataframe to a csv file, which would create a new csv file under the current WD
df.to_csv("squirrel_count.csv")