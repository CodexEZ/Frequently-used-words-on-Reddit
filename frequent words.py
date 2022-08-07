from sqlite3 import paramstyle
import praw
from praw.models import MoreComments
import matplotlib.pyplot as plt
from cleantext import clean
import operator

reddit = praw.Reddit(
    client_id="9uaf1tMjfGNKQniG5shFZA",
    client_secret="Ka6bG6j9SB9JvUDW3cGLlNpjZ4aFCg",
    user_agent="<console:CHAD:1.0>",
    username="gigomegabot",
    password="Ash@41938"
)
score=[]
count=[]
articles="a an the about above across after against that not just along among around at before behind between beyond but by concerning despite down during except following for from in including into like near of off on onto out over past plus since throughout to towards under until up upon up to with within without 🤓🤓🤓 🐒 is this [removed] me you and but because was so are what if else my how get"
para=""
c=1
subbreddit=reddit.subreddit("memes")
for post in subbreddit.hot(limit=10):
    for comment in post.comments:

        if isinstance(comment, MoreComments):
            continue
        lowercomment=comment.body.lower()
        clean(lowercomment,no_emoji=False)
        clean(lowercomment,no_urls=True)
        clean(lowercomment,no_urls=True)
        lowercomment=lowercomment.split()
        for i in lowercomment:
            if i not in articles:
                para=para + " " + i

unique=[]
para = para.split()
for i in para:
    if i not in unique:
        unique.append(i);
count={}
for i in unique:
    count[i]=para.count(i)
count = sorted(count.items(),key=operator.itemgetter(1), reverse=True)
for i in range (5):
    print(count[i])
