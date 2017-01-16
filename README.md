#TweetsData
This has files for DataEngineering Code Challenge:


Both "tweets_cleaned.py" and "average_degree.py" source files are written in python programming language.

tweets_cleaned.py 
================================
#Thefile 'tweets_cleaned.py' provides the two ouput files "ft1.txt" and "ft2.txt" files
#ft1.txt contains the cleaned data from raw json input text file(tweets.txt)
## ft2.txt contains extracted 'hashtags' and 'timestamp' fields fromt the provided json message files(tweets.txt)

# TO RUN THIS CODE PROVIDE THE  'tweets_filename' PATH PROPERLY  and ALSO AFTER SUCCESSFULLY RUNNING THE PROGRAM
# CHECK THE OUPTUT BY OPENING 'ft1.txt' and 'ft2.txt' files, which will be present at the directory where this program will be run from
Usage:
===========
## USAGE: >> python tweets_cleaned.py
#Run this on python shell..

average_degree.py 
========================================================

# This code 'average_degree.py' is written in python programming language
# This code filters out the messages with hashtags first
# EdgeList is created if there are 2 or more distinct hashtags per each incoming message.
# This also assigns Degree to each node(hashtag)
# Finally calculates the rolling average degree with each incoming message (also maintains 60 sectime window)

# TO TEST THE CODE PROVIDE THE  'tweets_filename' PATH PROPERLY.
#
# AFTER SUCCESSFULLY RUNNING THE PROGRAM, CHECK THE OUPTUT BY OPENING 'NodeAvg.txt' and 'ft2.txt' files, which will be present at the directory
# where this program will be run form

Usage:
=================
## USAGE: >> python average_degree.py
In some cases it can be run using "./average_degree.py" But, I suggest to use the above one as I have coded using python IDLE.
#Run this on python shell..
