try:
    import json
except ImportError:
    import simplejson as json

# We use the file saved from last step as example
# Here please change the path if you are using some other directory
tweets_filename = 'tweets.txt'
tweets_file = open(tweets_filename, "r")

ff = open('ft1.txt', 'w')
Unicode_count = 0
NonUnicode = 0
for line in tweets_file:
    try:
        # Read in one line of the file, convert it into a json object 
        tweet = json.loads(line.strip())
        if 'text' in tweet: # only messages contains 'text' field is a tweet    
            #print(tweet['id']) # This is the tweet's id
            ff.write(print(tweet.get('text',''),tweet['id'],"(timestamp :)",tweet['created_at'],file=ff))# when the tweet posted        

           print (hashtags)
    except:
        Unicode_count += 1
        # read in a line is not in JSON format (Unicodes)
        continue
    NonUnicode += 1
print('Number of Unicode_count = ' ,Unicode_count)
print('NON_Unicode_count = ' ,NonUnicode)

print("Number of Unicode_count = ",Unicode_count,file = ff)
ff.close()
