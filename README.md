# HuskyBot
Anti Bullying Twitterbot

## Introduction
HuskyBot is a twitterbot that monitors the tweets and direct messages sent to you on twitter and detects abusive and bullying tweets and messages.
If any such incident is detected, husky sends a direct message to that user on your behalf and warns them not to bully you.

## Installation
You need to create a new twitter application in order to deploy this bot. Follow these steps to do the same:

### Step 1:
Go to https://apps.twitter.com and sign in to your twitter account. Now click on "Create New App".

### Step 2:
Enter a name in the Application Details (It can be anything). Enter https://my.example.com in the Website field
![ScreenShot](/Installation%20Screens/Step%201.PNG?raw=true)

Accept the Developer Agreement and click on "Create Your Twitter Application"
![ScreenShot](/Installation%20Screens/Step%202.PNG?raw=true)

### Step 3:
Now go to permissions tab. Set Access to Read, Write and Access direct messages and click on "Update Settings"
![ScreenShot](/Installation%20Screens/Step$203.PNG?raw=true)

### Step 4:
Go to the Keys and Access Tokens tab. Copy the Consumer Key. Now open the [credentials.py](/credentials.py) file and paste at the consumer key (replacing the Xs)
![ScreenShot](/Installation%20Screens/Step%204.PNG?raw=true)
Do the same with Consumer Secret

### Step 5:
Now scroll down and click on "Create my access token"
![ScreenShot](/Installation%20Screens/Step%205.PNG?raw=true)
Now your Access Token and Access Token Secret have been generated, paste them to the [credentials.py](/credentials.py) file
![ScreenShot](/Installation%20Screens/Step%206.PNG?raw=true)

## Running the code
All you need to run the bot is to run the [bully_reply.py](/bully_reply.py) file and all who bullied you will be sent a Warning in the form of a direct message.
