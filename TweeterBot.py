import os
import tweepy as tw
import ctypes
import random as rnd
from datetime import datetime
"""Connect the twitter account"""
consumer_key = 'kZ7RQz4tyWc8z7SGzXao7oXZx'
consumer_secret = '1rAOo2tL0UXri3ziR7ZqBMZ2oKHQTXggXOEK023dAuQd5ctOD3'
access_token = '1212857104194621440-dTMO2RDfXRJcW2Nqb7Z1uJrTGmX0uf'
access_token_secret= 'oruhhkxvkpribcu6BVXYjOBaUYGxWpFFf3tVYb2GFTdDh'
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)
""""""
"""Make sure you do not upload twice a day"""
day=datetime.today().strftime('%A')
tweets=api.user_timeline("DailyRoil")
last_text=tweets[0].text
if day in last_text:
    exit()
"""Get the day number(number of post) from a file"""
postIndex = 0
t = open("Resources\currentPostIndex.txt", "r")
postIndex = int(t.read())
t.close()
"""Find the oldest file in the Puns folder(exit if there are no puns)"""
path = 'Puns'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
if(len(files)==0):
    exit()
oldest = files[0]
"""Post the oldest pun to Twitter"""
api.update_with_media(oldest, 'Day '+str(postIndex)+' '+day)
"""Move the posted image to the UsedPuns folder"""
os.chdir('..')
new_path = './UsedPuns' ## destination path
while 1:
    try:
        os.rename(oldest, new_path+'/'+oldest)
        break
    except:
        os.rename(oldest,new_path+'/'+'a'+str(rnd.randint(0,999999)+oldest))
##
##Change wallpaper if the bot is empty of puns
"""
SPI_SETDESKWALLPAPER = 20
BoogPic=os.path.abspath("../Resources/Boog_bg.jpg")
NeedToFill=os.path.abspath("../Resources/NeedToFill.png")

if len(os.listdir('../Puns')) != 0:
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0,  BoogPic, 3)
else:
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0,  NeedToFill, 3)
"""
message=""
if (len(os.listdir('../Puns'))==0):
    message="Please refill the puns stock"    
##Write in the index file that another post have been posted(move to the next day)
t=open("./Resources/currentPostIndex.txt", "w")
postIndex = postIndex+1
t.write(str(postIndex))
t.close()
os.system("start Resources/WeeklyPlan.jpeg")
os.system("shutdown -s -t 600 -c "+message)
##END
