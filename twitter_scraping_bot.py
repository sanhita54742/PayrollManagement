

# import matplotlib.pyplot as plt
import tweepy 
import numpy as np                                                                                                                                      
import pandas as pd
from random import randrange
import datetime
from datetime import timedelta
from datetime import datetime
# import seaborn as sns
# import pandas.util.testing as tm
import math
import re
import datetime
import time
import mysql.connector
import random
import string
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  port=3306
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS payrolldb")
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  port=3306,
  database="payrolldb"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS User(User_Id  INT NOT NULL PRIMARY KEY AUTO_INCREMENT, UserName VARCHAR(100) NOT NULL, Password VARCHAR(100) NOT NULL, Email_Id VARCHAR(100) NOT NULL, UserType VARCHAR(50) NOT NULL)")
mycursor.execute("CREATE TABLE IF NOT EXISTS Project(Project_Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, ProjectName VARCHAR(100) NOT NULL)")
mycursor.execute("CREATE TABLE IF NOT EXISTS PayGrade(PayGrade_Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,PayGrade_Basic INT NOT NULL, PayGrade_Bonus INT NOT NULL, PayGrade_Pf INT NOT NULL, PayGrade_Tax INT NOT NULL)")
mycursor.execute("CREATE TABLE IF NOT EXISTS Employee(Emp_Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, Project_Id INT NOT NULL, Emp_Name VARCHAR(100) NOT NULL, Emp_Dob DATE NOT NULL, Emp_Doj DATE NOT NULL, Emp_Mobile BIGINT NOT NULL, Emp_Email VARCHAR(100) NOT NULL, FOREIGN KEY(Project_Id) REFERENCES Project(Project_Id))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Salary(Transaction_Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, Emp_Id INT NOT NULL, Emp_Salary_Month VARCHAR(100) NOT NULL, Emp_Salary_Year VARCHAR(100) NOT NULL, Emp_Department_Id INT NOT NULL, Emp_Basic BIGINT NOT NULL, Emp_Tax INT NOT NULL, FOREIGN KEY(Emp_Id) REFERENCES Employee(Emp_Id))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Tweets(Tweet_Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, TweetUser VARCHAR(100) NOT NULL, TweetUrl VARCHAR(100) NOT NULL, TweetText VARCHAR(300) NOT NULL,TweetTime DATETIME NOT NULL, TweetLikes INT NOT NULL, TweetRetweet INT NOT NULL, ProfileImageUrl VARCHAR(500) NOT NULL,TweetLocation TEXT NOT NULL,JoinDate DATE NOT NULL)")
mycursor.execute("CREATE TABLE IF NOT EXISTS Tweet_Url(TweetUrl_Id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, TweetUrl VARCHAR(100) NOT NULL, Tweet_Id INT NOT NULL, FOREIGN KEY(Tweet_Id) REFERENCES Tweets(Tweet_Id))")


consumer_key = 'mefN1uUeyCfFpediJAP276cGP'
consumer_secret = 'JyMP1LGngDnikoPencO7CHo4oxswxzDkiFmeYHQedc2uWCm7yO'
access_token = '919526007714889729-BBRGO6q6c7FmNl6ak3NMA79yQuoTPQj'
access_token_secret = 'bB38RPapKHRAZz9FHf8XIQ8YdIO0iVEB44jTLXlJoOVJA'


# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)
def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)
def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.datetime.fromtimestamp(now_timestamp) - datetime.datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


ans1=0
sql = "SELECT * FROM `paygrade`"
                        
mycursor.execute(sql)

# store all the fetched data in the ans variable
ans = mycursor.fetchall()


try:
        mycursor.fetchall()  # fetch (and discard) remaining rows
except mysql.connector.errors.InterfaceError as ie:
        if ie.msg == 'No result set to fetch from.':
                # no problem, we were just at the end of the result set
                pass
        else:
                raise
if len(ans)==0:
        sql = "INSERT INTO `paygrade`(`PayGrade_Basic`, `PayGrade_Bonus`, `PayGrade_Pf`, `PayGrade_Tax`) VALUES (%s,%s,%s,%s)"
        val = (25000,2000,5000,3000)
        mycursor.execute(sql,val)
        mydb.commit()
        val = (30000,3000,6000,4000)
        mycursor.execute(sql,val)
        mydb.commit()
        val = (35000,4000,7000,5000)
        mycursor.execute(sql,val)
        mydb.commit()
        val = (40000,5000,8000,6000)
        mycursor.execute(sql,val)
        mydb.commit()
        val = (50000,6000,9000,7000)
        mycursor.execute(sql,val)
        mydb.commit()
# sql = "INSERT INTO tweets(TweetUser, TweetUrl, TweetText, TweetTime, TweetLikes, TweetRetweet, ProfileImageUrl, TweetLocation,JoinDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# val = (tweetuser,url[0],tweet,tweettime,int(tweetlikes),int(retweet),profile_image_url,tweetlocation,joindate)
# mycursor.execute(sql,val)
# mydb.commit()
# for tweet in tweets.data:
month = ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
for tweet in tweepy.Cursor(api.search_tweets,q="#Hiring",
                        lang="en",
                        include_entities=False).items(5):
        created_date_local = datetime_from_utc_to_local(tweet.created_at)
        # print(f"{tweet.user.name} said: {tweet.text} at time:{created_date_local}")
        tweettext=tweet.text

        
        url=[]
        url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweettext)

        tweetuser=tweet.user.name
        joindate = tweet.user.created_at
        tweettime=str(created_date_local)
        
        
        retweet = tweet.retweet_count
        tweetlikes = tweet.favorite_count
        
        profile_image_url=tweet.user.profile_image_url
        tweetlocation = tweet.user.location
        data = ( [tweet.user.name, url, tweettext,tweettime,retweet,tweetlikes,profile_image_url,tweetlocation,joindate],)
    
    # print()
        
        for tweetuser,url,tweet,tweettime,retweet,tweetlikes,profile_image_url,tweetlocation,joindate in (data):
                
        # print("here")
        # print(tweet+"+++"+tweettime+"+++"+str(retweet)+"+++"+str(tweetlikes)+"+++"+tweettime+"+++"+profile_image_url+"+++"+tweetlocation)
                
                if len(url)!=0:
                        # print("==================================================="+len(url)+"=======================")
                        sql = "INSERT INTO tweets(TweetUser, TweetUrl, TweetText, TweetTime, TweetLikes, TweetRetweet, ProfileImageUrl, TweetLocation,JoinDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        val = (tweetuser,url[0],tweet,tweettime,int(tweetlikes),int(retweet),profile_image_url,tweetlocation,joindate)
                        mycursor.execute(sql,val)
                        mydb.commit()
                        
                        mycursor = mydb.cursor()
                        urlitem = url[0]
                        sql = "SELECT Tweet_Id FROM tweets WHERE TweetUser = '"+tweetuser+"' AND TweetUrl = '"+urlitem+"'"
                        
                        mycursor.execute(sql)
 
                        # store all the fetched data in the ans variable
                        ans = mycursor.fetchone()[0]
                        try:
                                mycursor.fetchall()  # fetch (and discard) remaining rows
                        except mysql.connector.errors.InterfaceError as ie:
                                if ie.msg == 'No result set to fetch from.':
                                        # no problem, we were just at the end of the result set
                                        pass
                                else:
                                        raise
                        sql = "INSERT INTO tweet_url(TweetUrl,Tweet_Id) VALUES (%s,%s)"
                        val=(urlitem,int(ans))
                        mycursor.execute(sql,val)
                        mydb.commit()
                        project_id = random.randint(1000,9999999)
                        d1 = datetime.datetime.strptime('1990/10/10', '%Y/%m/%d')
                        d2 = datetime.datetime.strptime('2000/11/20', '%Y/%m/%d')

                        Dob = random_date(d1, d2)
                        mobile_no = random.randint(1000000000,9999999999)
                        # print(project_id)
                        email_id = random_char(7)+"@gmail.com"
                        # print(email_id)
                        sql = "INSERT INTO project(ProjectName) VALUES (%s)"
                        val = (random_char(7),)
                        mycursor.execute(sql,val)

                        sql = "SELECT project_id FROM project WHERE ProjectName = '"+val[0]+"'"
                        
                        mycursor.execute(sql)
 
                        # store all the fetched data in the ans variable
                        ans = mycursor.fetchone()[0]
                        try:
                                mycursor.fetchall()  # fetch (and discard) remaining rows
                        except mysql.connector.errors.InterfaceError as ie:
                                if ie.msg == 'No result set to fetch from.':
                                        # no problem, we were just at the end of the result set
                                        pass
                                else:
                                        raise
                        # 
                        sql = "INSERT INTO employee(Emp_Id,Project_Id,Emp_Name,Emp_Dob,Emp_Doj,Emp_Mobile,Emp_Email) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                        val = (int(ans),ans,tweetuser,Dob, tweettime,mobile_no,email_id)
                        mycursor.execute(sql,val)
                        sql = "INSERT INTO user(UserName,Password,Email_Id,UserType) VALUES (%s,%s,%s,%s)"
                        val = (tweetuser,random_char(7), email_id,1)
                        mycursor.execute(sql,val)
                        sql = "SELECT Emp_Id FROM employee"
                        
                        mycursor.execute(sql)
 
                        # store all the fetched data in the ans variable
                        ans = mycursor.fetchall()[ans1][0]
                        ans1+=1
                        
                        try:
                                mycursor.fetchall()  # fetch (and discard) remaining rows
                        except mysql.connector.errors.InterfaceError as ie:
                                if ie.msg == 'No result set to fetch from.':
                                        # no problem, we were just at the end of the result set
                                        pass
                                else:
                                        raise
                        
                        month3 = random.choice(month)
                        
                        sql="INSERT INTO `salary`(`Transaction_Id`, `Emp_Id`, `Emp_Salary_Month`, `Emp_Salary_Year`, `Emp_Department_Id`, `Emp_Basic`, `Emp_Tax`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                        val= (random_char(7),ans,month3,"2020",random.randint(1000,9999),random.randint(10000,90000),random.randint(1000,8000))
                        mycursor.execute(sql,val)
                        mydb.commit()