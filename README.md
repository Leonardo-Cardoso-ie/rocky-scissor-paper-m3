# Rocky, Scissor and Paper







![responsive](https://user-images.githubusercontent.com/96269648/190932976-c6803a36-bdcf-47c9-9fd8-e741aa5c69d7.png)









The Live link can be found here: https://rocky-scissor-paper-ms3.herokuapp.com/  





Rock, paper and scissors (also known by other orderings of the three items, with "rock" sometimes being called "stone," or as Rochambeau, roshambo, or ro-sham-bo) is a hand game originating from China, usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. These shapes are "rock" (a closed fist), "paper" (a flat hand), and "scissors" (a fist with the index finger and middle finger extended, forming a V). "Scissors" is identical to the two-fingered V sign (also indicating "victory" or "peace") except that it is pointed horizontally instead of being held upright in the air.


### Introduction / UX

 The Rocky Scissor Paper game is an application developed in Python, and is a very simple version of the rock, paper and scissors game, where the user chooses one of the three options and plays against the computer, and just type a letter R (Rock), P (paper) and S for (Scissors), being able to type both uppercase and lowercase letters. The purpose of this project is to put into practice the knowledge about the Python language acquired during the course.
 It was imported from Pyhtom, the Random Module, so that the computer also makes some choice, in a random way, to be able to interact with the user.


  
  ![terminal](https://user-images.githubusercontent.com/96269648/190933022-ae1dcbf0-56b1-434e-9526-efe6bc6efe47.png)

  
  
  
  
 
 
 

 
  



 
 




     
 
 ### Python
 
All code is written in Python 3.10.0



  


### Validator Testing 

Application tested using PEP8 Online Check PEP8 Online Check.



![pepvalid](https://user-images.githubusercontent.com/96269648/190932878-4d4fbd72-4b31-43eb-b242-eaab52f7ada7.png)


## Bugs

At times I had problems with the code indentation, I was writing the code and when I went through the validator some kind of error appeared, some of them I could not identify, even when I implemented my project on Heroku, a syntax error occurred in the line 16, and the code did not run. Since I had already deployed the project on the platform, I just put it in automatic mode, that is, any changes I make on my Github and give a push, automatically the code was corrected and started working normally, to resolve the bug, I just rewrote the code, as I couldn't identify the error.
 
  





  
## Deployment

### GITHUB

Forking the GitHub Repository and Running this Project Locally
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

Log in to GitHub and locate the GitHub Repository

At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.

You should now have a copy of the original repository in your GitHub account.

Run the index.html file in your local browser.


### HEROKU

If your requirements.txt file has not changed you can skip this step. Otherwise, in your terminal type 'pip freeze > requirements.txt' then save and push the changes.
Go to Heroku.com and sign in or create a free account.
From the heroku dashboard click the 'Create new app' button.
Name the app something unique and choose what region you are in then click 'Create app'.
Go to the settings tab and find the Config Vars section. Click 'Reveal Config Vars'.
For this project, you required to add a environment variable to connect to SMTP server from GMAIL. In the field KEY, enter PORT_GMAIL in all capitals, then for VALUE enter 465. (Note that you must differentiate between PORT and PORT_GMAIL. Otherwise, your deployment may fail) Then click 'Add'.
In the field for KEY enter PORT in all capitals, then in the field for VALUE enter 8000. Then click 'Add'.
Scroll down to the Buildpacks section and click 'Add buildpack'.
Click Python then save changes.
Add another buildpack by clicking 'Add buildpack' and this time click Nodejs then save changes.
Make sure that Python appears above Nodejs in the buildpack section. If it does not you can click and drag them to change the order.
Then head over to the deploy section by clicking deploy from the nav bar at the top of the page.
From the 'Deployment method' section select GitHub and click 'Connect to GitHub'.
Enter the repository name as it is in GitHub and click 'search'.
Click the 'connect' button next to the repository to link it to heroku.
To deploy, scroll down and click the 'Deploy Branch' button.
Heroku will notify you that the app was successfully deployed with a button to view the app.
If you want to rebuild your app automatically you can also select the 'Enable Automatic Deploys' button which will then rebuild the app every time you push any changes.



## Credits 

In addition to the content, made available by the Code Institute, I also followed classes from some Youtubers, such as Gustavo Guanabara:
https://www.youtube.com/watch?v=S9uPNppGsGo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0





## Special Thanks

 My special thanks go out to my family, my wife and my son, they know how hard it has been but they believe in me and the Code Institute 
