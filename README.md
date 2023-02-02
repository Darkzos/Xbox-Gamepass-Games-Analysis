# Xbox-Gamepass-Games-Analysis

I wanted to analyze the current games in Xbox Gamepass, for this I  have to look at "https://www.trueachievements.com/" where they have an updated list of the gamepass games.
Then I went to python and with Pandas and I retrieve the data with html read table, read each page of the games and merged up all in one DataFrame.
I cleaned the data, delete some columns that I didn't want and I had to create new columns using functions to erase some text inside of the rows, also I had to change number in stringtype with comma into a integer removing the comma and replace it in a new column.
After that I had to use some excel queries to change the datatype and replace the empty spaces in the date column with dashes to make the text readable to date format.
With that I could do the analysis with PowerBi
