from sqlite3 import paramstyle
import praw
from praw.models import MoreComments
import matplotlib.pyplot as plt
from cleantext import clean
import operator

reddit = praw.Reddit(
    client_id="",#Enter client ID
    client_secret="",#Enter your secret number
    user_agent="",#console name
    username="",#Enter your account username
    password=""#Enter your password here
)
score=[]
count=[]
#All the words that need to be excluded from the list since they dont have much value and are simple prepositions and articles
articles="a an the about above across after against that not just they along among around at before behind between beyond but by concerning despite down during except following for from in including into like near of off on onto out over past plus since throughout to towards under until up upon up to with within without 🤓🤓🤓 🐒 is this [removed] me you and but because was so are what if else my how get"
para=""#stores all the words in one paragraph
c=1
subbreddit=reddit.subreddit("memes")#Opens subreddit r/memes
for post in subbreddit.hot(limit=10):#Goes through top 10 hot posts
    for comment in post.comments:

        if isinstance(comment, MoreComments):
            continue
        lowercomment=comment.body.lower()
        clean(lowercomment,no_emoji=True)
        clean(lowercomment,no_urls=True)
        clean(lowercomment,no_urls=True)
        lowercomment=lowercomment.split()
        for i in lowercomment:
            if i not in articles:
                para=para + " " + i

unique=[]
para = para.split()
for i in para:              
    if i not in unique:         #Stores all the unique words in a list
        unique.append(i);
count={}#Stores all the unique words along with their frequencies
for i in unique:
    count[i]=para.count(i)
count = sorted(count.items(),key=operator.itemgetter(1), reverse=True) #Sorts dictionary according to the values
for i in range (5):#Here i have set it to show top 5 words in reddit comments
    print(count[i])
