
# PayrollManagement
**Team members:**
Margi Praful Adesara (NUID – 002792152) 
Sanhita Sawant (NUID – 002786796)
Github Id’s: MargiAdesara & sanhita54742

# project Description 
The "Payroll Management System" is intended to automate the current manual system using computer software, meeting their needs and enabling for the storage of their vital information and data for a longer period of time with simple access and manipulation. The necessary software is readily available and simple to use. Without receiving duplicate entries, this web application can maintain and view records. The project outlines how to organize user data for optimal efficiency and to provide better services.Payroll consists of the process by which a business pays its employees for work performed during aspecific period. A payroll system allows businesses to follow a set series of processes in order to maketimely, correct payments in compliance with government regulations. The payroll process typicallyincludes calculating employee pay, recording payroll transactions. A company must have in place a timekeeping system that accurately reflects the hours and number of days put in by employees as well as the regular salary payments for exempt workers. Companies also must withhold Social Security and Medicare contributions from employees' salary and pay a matching amount.

SQL Statements for the conceptual model:
**User Table:**
CREATE TABLE `User` (
‘User_Id’ INT,
 ‘UserName’ VARCHAR (100),
 ‘Password’ VARCHAR(100),
 ‘Email_Id’ VARCHAR(100),
 ‘UserType’ VARCHAR(50),
 PRIMARY KEY (‘User_Id’)
);

**Project Table:**

CREATE TABLE `User` (
‘Project_Id’ INT,
‘ProjectName’ VARCHAR (100),
 PRIMARY KEY (‘Project_Id’)
);

**PayGrade Table:**

CREATE TABLE `PayGrade` (
‘PayGrade_Id’ INT,
‘PayGrade_Basic’ INT,
‘PayGrade_Bonus’ INT,
‘PayGrade_Pf’ INT,
‘PayGrade_Tax’ INT,
PRIMARY KEY (‘PayGrade_Id’)
);

**Employee Table:**

CREATE TABLE `Employee` (
‘Emp_Id’ INT,
‘Project_Id’ INT,
‘Emp_name’ VARCHAR(100),
‘Emp_Dob’ DATE,
‘Emp_Doj’ DATE,
‘Emp_Mobile’ BIGINT,
‘Emp_Email’ VARCHAR(100),
PRIMARY KEY (‘Emp_Id’)
);

**Salary Table:**

CREATE TABLE `Employee` (
‘Transaction_Id’ INT,
‘Emp_Id’ INT,
‘Emp_Salary_Month’ VARCHAR(100),
‘Emp_Salary_Year’ VARCHAR(100),
‘Imp_Department_Id’ INT,
‘Emp_Basic’ BIGINT,
‘Emp_Tax’ INT,
PRIMARY KEY (‘Transaction_Id’)
);

**Tweets Table:**

CREATE TABLE `Tweets` (
Tweet_Id’ INT,
‘TweetUser’ VARCHAR(100),
‘TweetUrl’ VARCHAR(100),
‘TweetText’ TEXT,
‘TweetTime’ DATETIME,
‘TweetLikes’ INT,
‘TweetRetweet’ INT,
‘ProfileImageUrl’ TEXT,
‘TweetLocation’ TEXT,
PRIMARY KEY (‘Tweet_Id’)
);

**Tweet_URL Table:**

CREATE TABLE `Tweet_URL` (
‘TweetURL_Id’ INT,
‘TweetUrl’ VARCHAR(100),
‘Tweet_Id’ INT,
PRIMARY KEY ('TweetURL_Id')
);

**Constraint for Tweet Table:**

ALTER TABLE `Tweet_URL`
ADD CONSTRAINT `TweetsURL_fk1` FOREIGN KEY (‘Tweet_Id’)
REFERENCES Tweets(‘Tweet_Id’);

**Constraint for Tweet_URL Table**

ALTER TABLE `Tweet_URL’
ADD CONSTRAINT `TweetsURL_fk1’ FOREIGN KEY (‘Tweet_Id’)
REFERENCES Tweets(‘Tweet_Id’);

**Constraint for Employee Table:**

ALTER TABLE `Employee’
ADD CONSTRAINT `EmployeeID_fk1’ FOREIGN KEY (‘Project_Id’)
REFERENCES Project(‘Project_Id’);

**Constraint for Salary Table:**

ALTER TABLE `Salary’
ADD CONSTRAINT `EmployeeID_fk1’ FOREIGN KEY (‘Emp_Id’)
REFERENCES Employee(‘Emp_Id’);

**Questions to be answered based on the data fetched from twitter:**
1. **What user posted this tweet?**
 SELECT tw.TweetUser, tw.TweetURL, emp.Emp_Name FROM Employee as emp INNER JOIN Tweets as tw ON emp.Emp_Name = tw.TweetUser WHERE Emp.Emp_Name = 'Frontend.LA' AND TweetText = '#SantaClarita #jobs #hiring #opportunity @ Global Lighting Supply | Industrial Designer https://t.co/owemzCd3oQ |… https://t.co/5xsEhzAO0m'

Relational Algebra for the above query :
 π tw . tweetuser, tw . tweeturl, emp . emp_name 
 σ emp . emp_name = "Margi Adesara" AND tw . tweettext = "This user has posted the tweet." 
 (ρ emp employee ⋈ emp . emp_id = tw . tweet_id 
 ρ tw tweets)

2. **When did the user post this tweet?**
 SELECT TweetTime, TweetUser FROM Tweets WHERE TweetUser = 'Frontend.LA' AND TweetText = '#SantaClarita #jobs #hiring #opportunity @ Global Lighting Supply | Industrial Designer https://t.co/owemzCd3oQ |… https://t.co/5xsEhzAO0m'

Relational Algebra for the above query :
 π tweettime, tweetuser
 σ tweetuser = "Margi Adesara" AND tweettext = "User posted the tweet at this time" tweets

3. **What tweets have this user posted in the past 24 hours?**
 SELECT tw.TweetUser, tw.TweetURL, emp.Emp_Name FROM Employee as emp INNER JOIN Tweets as tw ON emp.Emp_Name = tw.TweetUser WHERE Emp.Emp_Name = 'Frontend.LA' AND Tw.TweetTime >= NOW() - INTERVAL 1 DAY

Relational Algebra for the above query :
 π tw . tweetuser, tw . tweeturl, emp . emp_name 
 σ emp . emp_name = "Margi Adesara" AND tw . tweettime >= interval 1 day
 (ρ emp employee ⋈ emp . emp_id = tw . tweet_id 
 ρ tw tweets)

4. **How many tweets have this user posted in the past 24 hours?**
 SELECT count(TweetText) FROM Tweets WHERE TweetUser = 'Frontend.LA' AND TweetTime >= NOW() - INTERVAL 1 DAY
 
Relational Algebra for the above query :
 π COUNT (tweettext) 
 γ COUNT (tweettext) 
 σ tweettime >= interval 1 day tweetuser = "Margi Adesara" tweets 

5. **When did this user join Twitter?**
 SELECT tw.JoinDate, tw.TweetUser FROM Employee as emp INNER JOIN Tweets as twON emp.Emp_Id = tw.Tweet_ID WHERE Emp.Emp_Name = 'Jobs via Tweet'
 
Relational Algebra for the above query :
 π tw . join_date, tw . tweetuser
 σ emp . emp_name = "Margi Adesara" 
 (ρ emp employee ⋈ emp . emp_id = tw . tweet_id 
 ρ tw tweets)

6. **What tweets are popular?**
 SELECT TweetUser, TweetText, (TweetRetweet*10 + Tweetlikes) as popular_tweets FROM Tweets Order by popular_tweets desc
 
Relational Algebra for the above query:
 τ popular_tweets ↓ 
 π tweetuser, tweettext, tweetretweet * 10 + likes → popular_tweets tweets
 
 1. **Use Case: Register for an account in DSW**
Description: Employee register for a twitter account
Actor: Employee
Precondition: Asking the employee to register for twitter account.
Steps:
Actor action: User request for registration
System Responses: If employee information is correct then employee is registered and use case ends.
Post Condition: Employee successfully registered
Alternate Path: The employee request is not correct and system throws an error
Error: User information is incorrect
SQL Statements:
INSERT INTO User
(User_Id, UserName, Password, Email_Id, UserType)
VALUES (01, @Margi, margi1309, margiadesara@gmail.com, Employee)
INSERT INTO User
(User_Id, UserName, Password, Email_Id, UserType)
VALUES (02, @Sanhita, sanhita0209, Sanhitasawant@gmail.com, Employee)

Relational Algebra:
Cannot be made for insert statements.

2. **Use Case: Employee having salary above certain amount**
Description: View the list of Employees having salary above $25000
Actor: User
Precondition: 
Steps:
Actor action: HR views the list of the employees having the salary above $20000 on querying the 
database
System Responses: the list of employees is displayed having salary above $25000
Post Condition: system displays the list of employees for the condition.
SQL Statements:
SELECT Emp_Id, Emp_Salary_Month, Emp_Salary_Year 
FROM SALARY
WHERE 
Emp_Salary_Month > 25000

Relational Algebra:
π emp_id, emp_salary_month, emp_salary_year 
σ emp_salary_month > 25000 salary

3. **Use Case: Employee tweets on twitter.**
Description: Employee tweets on twitter between 1st January to 31st of January
Actor: Employee
Precondition: Employee should have a twitter account.
Steps:
Actor action: Employee has tweeted tweets on twitter at anytime between 1st January to 31st of 
January
System Responses: Employee has tweeted on twitter 
Post Condition: Employee has tweeted on twitter successfully.
Alternate Path: 
Error: User information is incorrect
SQL Statements:
SELECT TweetText, TweetUser
FROM Tweets
WHERE Emp_Name = ‘Someone’
AND
TweetTime Between '2022-01-01' AND ‘2022-01-31';

Relational Algebra:
π tweettext, tweetuser
σ emp_name = "Someone" AND ("2022-01-01" <= tweettime AND tweettime <= "2022-01-31") tweets

4. **Use Case: How many people have retweeted the tweet by Employee after the date 05-06-2022**
SELECT
 TweetUser, TweetText, count(TweetRetweet) as User_tweets
 FROM Tweets
 WHERE 
 TweetUser = “Sanhita Sawant”
 AND TweetTime >= ‘05-06-2022'
 
Relational Algebra for the above query:
 πtweetuser, tweettext, COUNT (tweetretweet) → user_tweets 
 γ COUNT (tweetretweet) 
 σ tweetuser = "Sanhita Sawant" AND tweettime >= 5 - 6 - 2022 tweets

5. **Use Case: Number of projects in the company with the number of employees.**
SELECT Count(pj.ProjectName), emp.Emp_Name, emp.EMP_Id 
 FROM Employee as emp 
 INNER JOIN Project as pj
 ON emp.Emp_Id = pj.Project_ID
 
 
Relational Algebra for the above query:
π COUNT (projectname), emp . emp_name, emp . emp_id 
γ COUNT (projectname) 
 (ρ emp employee ⋈ emp . emp_id = pj . project_id 
 ρ pj project)

6. **Use Case: Number of Employees born in year 1995**
 SELECT Emp_Name, Count(Emp_Id)
 FROM Employee
 WHERE
 Emp_Dob = ‘1995’
 
 
Relational Algebra for the above query:
π emp_name, COUNT (emp_id) 
γ COUNT (emp_id) 
 σ emp_dob = 1995 employee

7. **Use Case: Number of Employees joined after November 2021.**
 SELECT Emp_Name, Count(Emp_Id)
 FROM Employee
 WHERE
 Emp_Doj > ‘01-11-2021'
 
Relational Algebra for the above query:
π emp_name, COUNT (emp_id) 
γ COUNT (emp_id) 
 σ emp_doj > 1 - 11 - 2021 employee

8. **Use Case: Bonus given to all the employess.****
 SELECT PayGrade_Id, sum(PayGrade_Bonus)
 FROM PayGrade
 
Relational Algebra for the above query:
πpaygrade_id, SUM (paygrade_bonus) 
γ SUM (paygrade_bonus) paygrade

9. **Use Case: Select Tweets that contains #Hiring in it**
SELECT TweetText, TweetUser
FROM Tweets
WHERE                
TweetText like '%#Hiring%'

Relational Algebra for the above query:
π tweettext, tweetuser 
σ tweettext LIKE "%#Hiring%" tweets

10. **Use Case : Select maximium basic pay for the employee**
SELECT Emp_Id, max(Emp_Basic)
FROM Salary

Relational Algebra for the above query:
π emp_id, MAX (emp_basic)
 γ MAX (emp_basic) salary






