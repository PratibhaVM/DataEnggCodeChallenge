####################################### CODE TO CLACULATE ROLLING AVERAGE DEGREE FOR INCOMING TWITTER MESSAGES #######################################################
#################################################### within time window of 60 seconds ################################################################################

# This code 'average_degree.py' is written in python programming language
# This code filters out the messages with hashtags first
# EdgeList is created if there are 2 or more distinct hashtags per each incoming message.
# This also assigns Degree to each node(hashtag)
# Finally calculates the rolling average degree with each incoming message (also maintains 60 sectime window)

# TO TEST THE CODE PROVIDE THE  'tweets_filename' PATH PROPERLY.
#
# AFTER SUCCESSFULLY RUNNING THE PROGRAM, CHECK THE OUPTUT BY OPENING 'NodeAvg.txt' and 'ft2.txt' files, which will be present at the directory
# where this program will be run form


## USAGE: >> python average_degree.py
#Run this on python shell..

########################################################################################################################################################################



try:
    import json
    import datetime
    #import networkx as nx
except ImportError:
    import simplejson as json
    import datetime
    from datetime import datetime,date,time
    from datetime import timedelta

tweets_filename = 'D:/UTD/FALL2015/InsightDE/coding-challenge-master/data-gen/tweets.txt'
tweets_file = open(tweets_filename, "r")
HFile = open('HashFile.txt', 'w')
EFL = open('EdgeList.txt','w')
AvgFile = open('NodeAvg.txt','w')

Start = "00:00:00"
DT2 = datetime.datetime.strptime(Start,'%H:%M:%S')
DT3 = DT2.strftime('%H:%M:%S')
created_at_format = '%a %b %d %H:%M:%S +0000 %Y'
Time_format = 'H:%M:%S'
TotalSec_Before =0
print('Start')


for line in tweets_file:
    try:    
### Read in one line of the file, convert it into a json object 
        tweet = json.loads(line.strip())
        hashtags = []
        AddNodesOld = 0
        for hashtag in tweet['entities']['hashtags']:
            hashtags.append(hashtag['text'])
            if hashtag['text'] in hashtags:
                created_at_format = '%a %b %d %H:%M:%S +0000 %Y'
                HashLength = len(tweet['entities']['hashtags'])
                if HashLength > 1:
                    EdgeList =[]
                    for i in range(0,HashLength):
                        print(tweet['entities']['hashtags'][i]['text'],tweet['entities']['hashtags'][i+1]['text'],file = HFile)
                        if tweet['entities']['hashtags'][i]['text'] != tweet['entities']['hashtags'][i+1]['text']:
                            EdgeList.append(tweet['entities']['hashtags'][i]['text'])
                            print(EdgeList,file=EFL) # EdgeList is created
                            EdgeList.append(tweet['entities']['hashtags'][i+1]['text'])
                            Count1 = EdgeList.count(tweet['entities']['hashtags'][i]['text'])
                            Count2 = EdgeList.count(tweet['entities']['hashtags'][i+1]['text'])
                            LengthOf_EdgeList = len(EdgeList)
                            #print(LengthOf_EdgeList)
                            AddNodesNew = AddNodesOld +Count1+Count2
                            AverageDegree = AddNodesNew/LengthOf_EdgeList
                            print(AverageDegree,file = AvgFile) # Rolling Average Degree is calculted here
                            AddNodesOld = AddNodesNew
                        else:
                            EdgeList
                            DT1 = datetime.datetime.strptime(tweet['created_at'],created_at_format)
                            abefore = 0
                            Hours= DT1.hour
                            #print(Hours)
                            Now_Minute = DT1.minute
                            Now_Sec = DT1.second
                            aNow = "%d:%d:%d" % (DT1.hour,DT1.minute,DT1.second)
                            t1 = 0
                            m1=0
                            h1=0
                            H =DT1.hour - h1 
                            M=DT1.minute - m1
                            T = DT1.second - t1
                            Total_Sec_Now = (H*3600)+(M * 60) + (T)
                            for i in tweet['created_at']:
                                Diff = Total_Sec_Now - TotalSec_Before
                                #print('DIFF :',Diff)
                                if(Diff > 60):
                                    TotalSec_Before = Total_Sec_Now
    except:
        
        # read in a line is not in JSON format (Unicodes)
        continue
    #print('After :',TotalSec_Before)
HFile.close
EFL.close()
AvgFile.close()
print('DONE:Open all text files to check the output')

                 
            
            
    
