#First we import pandas module for data manipulation
import pandas as pd

#Url variable with the full link of the page where we are going to retrieve the data
url = r'https://www.trueachievements.com/xbox-game-pass/games'
tables = pd.read_html(url) # Returns list of all tables on page
gamepass1 = tables[0] # Select table of interest
df1 = pd.DataFrame(gamepass1) #Convert that table to a DataFrame 

#Repeat with each table that we want because we are going to join them in a log one
url = r'https://www.trueachievements.com/xbox-game-pass/games?page=2'
tables = pd.read_html(url) # Returns list of all tables on page
gamepass2 = tables[0] # Select table of interest
df2 = pd.DataFrame(gamepass2)

url = r'https://www.trueachievements.com/xbox-game-pass/games?page=3'
tables = pd.read_html(url) # Returns list of all tables on page
gamepass3 = tables[0] # Select table of interest
df3 = pd.DataFrame(gamepass3)

url = r'https://www.trueachievements.com/xbox-game-pass/games?page=4'
tables = pd.read_html(url) # Returns list of all tables on page
gamepass4 = tables[0] # Select table of interest
df4 = pd.DataFrame(gamepass4)

url = r'https://www.trueachievements.com/xbox-game-pass/games?page=5'
tables = pd.read_html(url) # Returns list of all tables on page
gamepass5 = tables[0] # Select table of interest
df5 = pd.DataFrame(gamepass5)

lt = [df1,df2,df3,df4,df5] #Pass those DataFrames to a list for concatenation

Gptable = pd.concat(lt,ignore_index=True) #Concatenate the previous list

#Now that we have all the tables in one DataFrame, we proceed to get drop the columns that we don't want to be there
Gptable.drop(['Game','Unnamed: 8'], inplace = True, axis = 1) 

#Renaming one column for better understanding
Gptable.rename(columns = {'Game.1':'Game'}, inplace = True)

#Checking our Dataframe if everything is ok
print(Gptable['Score'])

#We have a problem here, the Score column has more values in each row than we want and is a string

#Function that makes that string into a list, replaces the comma with nothing, and convert that string into an integer
def gsscore(Score):
  x = Score.split()
  y = x[0].replace(",","")
  f= int(y)
  return f

#Function that remove "hours" from the Comp Time column for easier visualization
def comptime(Comp_Time):
  x = str(Comp_Time)
  f = x.split()
  y = f[0]
  return y

#Applying that function to the Score column and create a new one with the integers
Gptable['gScore'] = Gptable['Score'].apply(gsscore)

#Dropping the old Score column
Gptable.drop('Score', inplace = True, axis = 1) 

#Applying the function to the Comp Time column and create a new one withouth the "hours"
Gptable['Comp Time (hrs)'] = Gptable['Comp Time'].apply(comptime)

#Dropping the old Compt Time column
Gptable.drop('Comp Time', inplace = True, axis = 1) 

#Checking if it worked
print(Gptable['Comp Time (hrs)'])

#Checking the list of columns
print(list(Gptable))
#Checking the full DataFrame
print(Gptable)

#Convert the DataFrame to a csv file that we can work with for the data analysis
#Gptable.to_csv('Gamepass_games1', index = False)

