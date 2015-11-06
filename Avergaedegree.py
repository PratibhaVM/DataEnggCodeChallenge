################################ COde to CAlulate Average Degree)
try:
    import json
    import datetime
except ImportError:
    import simplejson as json
    #import datetime
    from datetime import datetime
    from datetime import timedelta


# We use the file saved from last step as example
tweets_filename = 'D:/UTD/FALL2015/InsightDE/coding-challenge-master/data-gen/tweets.txt'
tweets_file = open(tweets_filename, "r")

EFL = open('EdgeList.txt','w')
ff = open('ft2.txt', 'w')
Unicode_count = 0
NonUnicode = 0
for line in tweets_file:
    try:
        # Read in one line of the file, convert it into a json object 
        tweet = json.loads(line.strip())
        # Read in one line of the file, convert it into a json object 
        #if 'text' in tweet: # only messages contains 'text' field is a tweet
        hashtags = []
        AddNodesOld = 0
        for hashtag in tweet['entities']['hashtags']:
            hashtags.append(hashtag['text'])
            if hashtag['text'] in hashtags:
                created_at_format = '%a %b %d %H:%M:%S +0000 %Y'
                #dt1 = datetime.datetime.strptime(tweet['created_at'])
                    #dt2 = datetime.datetime.strptime(tweet[i+1]['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
                    #Difference = (dt1 - dt2)/60
                    #Diff= DIfference/60
                    #print( Diff )
                #print(hashtag['text']
                HashLength = len(tweet['entities']['hashtags'])
                #print(HashLength)
                if HashLength > 1:
                    EdgeList =[]
                    for i in range(0,HashLength):
                        print(tweet['entities']['hashtags'][i]['text'],tweet['entities']['hashtags'][i+1]['text'],file = EFL)
                    #for index in len(tweet['entities']['hashtags']):
                        #print(i)
                        #print(tweet['entities']['hashtags'][index]['text'])
                        #print('Entered2')
                        if tweet['entities']['hashtags'][i]['text'] != tweet['entities']['hashtags'][i+1]['text']:
                           # print('DOne')
                            #EdgeList =[]
                            EdgeList.append(tweet['entities']['hashtags'][i]['text'])
                            EdgeList.append(tweet['entities']['hashtags'][i+1]['text'])
                            #print (EdgeList.count(tweet['entities']['hashtags'][i+1]['text']))
                            Count1 = EdgeList.count(tweet['entities']['hashtags'][i]['text'])
                            #print(Count1)
                            Count2 = EdgeList.count(tweet['entities']['hashtags'][i+1]['text'])
                           #print('Count2 :',EdgeList.count(tweet['entities']['hashtags'][i+1]['text'])  
                            #print('E1 :',len(EdgeList))
                            LengthOf_EdgeList = len(EdgeList)
                            #print(LengthOf_EdgeList)
                            AddNodesNew = AddNodesOld +Count1+Count2
                            AverageDegree = AddNodesNew/LengthOf_EdgeList
                            print(AverageDegree)
                            AddNodesOld = AddNodesNew
                        else:
                            EdgeList
                            #print('E2 :',len(EdgeList))
    except:
        Unicode_count += 1
        # read in a line is not in JSON format (Unicodes)
        continue
    NonUnicode += 1
ff.close()

