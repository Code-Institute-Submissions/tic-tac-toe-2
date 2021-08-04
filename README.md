### Tic Tac Toe.

[Link to Live Website on heroku](https://tic-tac-toepp3.herokuapp.com/)

[GitHub Repo](https://github.com/ejkington/tic-tac-toe)

# Data used 
i used dictionaries in python,access dictionaries, iterate over dictionaries, for loop, if-else conditions and functions

# Python terminal game of tic tac toe.

![Responsive Mockup](https://github.com/ejkington/tic-tac-toe/blob/main/readme.md%20assets/mockup.PNG)

# Rules 
- Simple game of tic tac toe for 2 players, first player is X and second player is O.
- Players takes turnes to choose and too win you have too have 3 in a row, horizontaly, verticaly, or dioganaly.
- If game ends in a tie. (board gets filled with no winner, the game ends as a tie.
- Players takes turnes to pick a number from 1 to 9, 1 being in the bottom left and 9 in the top right corner,

# Flow chart.

![flowchart](https://github.com/ejkington/tic-tac-toe/blob/main/readme.md%20assets/flowchart.jpeg)
# Bugs

- bug where when pressing number outside of 1 to 9 game crashes (unsolved)
- bug where when pressing same number allready occupied game crashes. (fixed)
- bug where when the game is a tie game doesnet ask if players wants to play again. (unsolved in mock terminal)
- Gamearea / Board. not updating when move is made. (solved)
- When game ends win or tie game stops and a page refresh is needed to play again in the mock terminal. (works as intended in gitpod terminal)
- 
# Validating
- pep8 code gives trailing white space errors. removed and now shows no errors
- js css and html is written by codeinstitute and is not tested by me
  
  ## Testing 
 Test | Test action | Expected outcome      | Test outcome
------- | ---------------- | ---------- | ---------:
pressing 1 to 9 show accurate move in game | pressing 1 to 9 as player one (X) | an X is show at the correct square on the board | PASS
pressing 1 to 9 show accurate move as player two  |  pressing 1 to 9 as player two (O)        | an O is shown at the correct square of the board       | PASS
if player chooses same square allready taken   | pressing 1 to 9 and choosing same square allready taken | prints "space allready occupied and player gets to choose again    | PASS
when X or O wins   | getting 3 in a row with X or O  | prints "Game over X or O won    | PASS
Game is a Tie   | tieing the game or filling the board with no winner | prints Tie    | PASS

## Technologies Used 

* HTML5 - Mark-up language using semantic structure. (code already provided in the template)
* CCS3 - Cascading style sheet used to style. (code already provided in the template)
* Gitpod.io - for writing the code. Using the command line for committing and pushing to Git Hub
* Pyton3 - Used to add function of game.
* GitHub - Used to host repository 
* GIT - for version control of the project.

# Compatibility
Tested on iOS, Android 10, and Windows 10.
Tested on Firefox(latest version), Microsoft edge(latest version), Chrome(latest version), opera 76(latest version), Internet Explorer(latest version)
Without any errors.


# Adding and commiting files

To add files to the repository take the following steps

In the command line type -
        git add .  
        git commit -m "This is being committed"
        git push

To add all new files or modified file use " ."  - To add a single file use the pathway to the file eg .index.html  or assets/css/style.css
When committing make sure your comments are clear about what changes have been made. 
Pushing will send your work to the repository

# Deployment

The project was deployed with the following steps

* Logged into git hub
* Clicked the "Settings" button in the menu above the Repository.
* Scroll down the Settings page to the "GitHub Pages" Section.
* Under "Source", click the dropdown called "None" and then select "Master Branch".
* The page will automatically refresh, and a link displaced.  It may take some time for the link to show the website.
* If the page will not load go down to "template" under the "source" and select a template. 
* Scroll back down through the page to locate the now published site link in the "GitHub Pages" section.

* Logged in to heroku
* Clicked add app and gave it its name
* go to settings and add the buildpacks python and node.js
* go to deploy tab and connect heroku to github
* Locate the project and add it.
* Scroll down to deploy project and choose main/master branch and press deploy branch
* wait for the app too build and then press view button at the bottom of the page
* enjoy playing in the mock terminal provided by codeinstitute.

### Game can also be played using your own IDE, copy the code and use 
### python3 run.py
### in the terminal




# Credits 
- James Shaha.
- Stackoverflow
- Brian machina my mentor
- Slack community
