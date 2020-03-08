#COMMENT GRAPH 1
#Graph One indicates that the sales for video games has been increasing steadily since 2004, with the exception of 2008.  The decline in 2008 is likely explained
#by the recession.  This graph leads us to conclude that video games were heavily affected by the recession, just like most other industries.

#COMMENT GRAPH 2 
#Graph Two displays the average rating of a game made on a particular console.  Several things are of note here.  Firstly, the large disparity in game rating between
#the two Nintendo consoles (Wii and DS) indicate a huge difference in popularity, possibly due to the handheld nature of the DS.  This is supported by the high ratings of
#the Sony PSP.  Overall, this data indicates a general preference for handheld devices amongst consumers.

#------------------------------------------------------------------------------------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("video_games.csv") #creates DataFrame from the file of video game information

#Graph 1   -- will plot the amount of games made over several years 

plt.xlabel("Year")
plt.ylabel("Number of Games")
plt.gcf().canvas.set_window_title('Graph 1 ') #sets the figure above the title of the graph 
graph1 = data["Release.Year"].value_counts(sort = False).plot(kind = "line", color = ["red"], title ="Number of Video Games Made by Year", marker ='o', markerfacecolor='black' )
#^ part above counts the number of times the five release years appear in thier specific column and then plots a line graph of the information
graph1.locator_params(integer=True) #changes the years on the x axis from floats to ingegers 

#------------------------------------------------------------------------------------------------------------------------------------------------------------

#Graph 2  -- will plot the average metric review score for consoles from 2004 to 2008

#initializing elements used in creating the graph 
total_dictionary = {} #console:total
game_count = {} #console:count
years = [] #list of years 
consoles = [] #list of consoles
average_score = [] #average review score of each console 

bar_graph = pd.DataFrame(columns = [data["Release.Year"],data["Release.Console"],data["Metrics.Review Score"]]) #creates a DataFrame from the csv file

for columns in bar_graph: #creates lists with one value for each year and console
    if columns[0] in years: #years list 
        pass
    else:
        years.append(columns[0])
    if columns[1] in consoles: #console list
        pass
    else:
        consoles.append(columns[1])
 
#makes a dictionary for all the consoles (set up for finding the average metric game rating for each console)
for types_of_consoles in consoles: 
    total_dictionary[types_of_consoles] = 0 #creating elements in total dictionary
    game_count[types_of_consoles] = 0 #creating elements in count dictionary
    
for columns in bar_graph: #adds up reviews for each game
    total_dictionary[columns[1]] += columns[2]
    game_count[columns[1]] += 1

for types in consoles: #calculates the average for each game console 
    for reviews in total_dictionary:
        total = total_dictionary[types]
        pass
    for count in game_count:
        games_made = game_count[count]
        pass
    average_review = total/games_made #actual calculation
    average_score.append(average_review) #appends score to to average_scores

bar_graphs = pd.DataFrame({'Consoles':consoles, 'Average_Score':average_score}) #creates the new data frame for the console and average information that was just created

graph3 = bar_graphs.plot(kind = "bar",x='Consoles', y='Average_Score', rot=0, title = "Average Metric Review Score by Console", legend = False) #plots the graph as a bargraph
plt.xlabel("Console")
plt.ylabel("Review Score")
plt.gcf().canvas.set_window_title('Graph 2') #sets the figure

#------------------------------------------------------------------------------------------------------------------------------------------------------------

plt.show() #shows the graphs 
