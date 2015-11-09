################################################ CODE TO CLEAN THE DATA #################################################################

#########################################################################################################################################
#This code is written in python
#Thefile 'tweets_cleaned.py' provides the two ouput files "ft1.txt" and "ft2.txt" files
## ft1.txt contains the cleaned data from raw json input text file(tweets.txt)
## ft2.txt contains extracted 'hashtags' and 'timestamp' fields fromt the provided json message files(tweets.txt)


# TO TEST THE CODE PROVIDE THE  'tweets_filename' PATH PROPERLY AND ALSO AFTER SUCCESSFULLY RUNNING THE PROGRAM
# CHECK THE OUPTUT BY OPENING 'ft1.txt' and 'ft2.txt' files, which will be present at the directory where this program will be run form


## USAGE: >> python tweets_cleaned.py
#Run this on python shell..
#########################################################################################################################################

#########################################################################################################################################
try:
    import json
except ImportError:
    import simplejson as json

# I am using the 'text file path' as txt input file
# To run this program please provide the right path of text file at your local environment
tweets_filename = 'D:/UTD/FALL2015/InsightDE/coding-challenge-master/data-gen/tweets.txt'
tweets_file = open(tweets_filename, "r")

ff = open('ft1.txt', 'w')
HF = open('ft2.txt','w')
Unicode_count = 0
NonUnicode = 0
for line in tweets_file:
    try:
        # Read in one line of the file, convert it into a json object 
        tweet = json.loads(line.strip())
        if 'text' in tweet:
            hashtags = []
            for hashtag in tweet['entities']['hashtags']:
                hashtags.append(hashtag['text'])
                #print('Hi')
                if 'created_at' in tweet:
                    created_at_format = '%a %b %d %H:%M:%S +0000 %Y'
                ff.write(print((hashtags),"(timestamp :)",tweet['created_at'],file=HF))
            ff.write(print(tweet.get('text',''),tweet['id'],"(timestamp :)",tweet['created_at'],file=ff))           
    except:
        Unicode_count += 1
        # reads in a line which is not in JSON format
        continue
    NonUnicode += 1
print('Number of Unicode_count = ' ,Unicode_count)
#print('NON_Unicode_count = ' ,NonUnicode)
print("\n \n NUMBER UNICODES COUNT = ",Unicode_count,file = ff)
ff.close()
