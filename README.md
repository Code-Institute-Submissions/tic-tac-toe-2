### Tic Tac Toe.

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

# Validating
- pep8 code gives trailing white space errors.
- ![pep9](https://github.com/ejkington/tic-tac-toe/blob/main/readme.md%20assets/pep8.PNG)
- js css and html is written by codeinstitute and is not tested by me
  
  ## Testing 
 Test | Test action | Expected outcome      | Test outcome
------- | ---------------- | ---------- | ---------:
pressing 1 to 9 show accurate move in game | pressing 1 to 9 as player one (X) | an X is show at the correct square on the board | PASS
pressing 1 to 9 show accurate move as player two  |  pressing 1 to 9 as player two (O)        | an O is shown at the correct square of the board       | PASS
if player chooses same square allready taken   | pressing 1 to 9 and choosing same square allready taken | prints "space allready occupied and player gets to choose again    | PASS
when X or O wins   | getting 3 in a row with X or O  | prints "Game over X or O won    | PASS
Game is a Tie   | tieing the game or filling the board with no winner | prints Tie    | PASS
 
# Deployment

# Credits 
- James Shaha.
- Stackoverflow
- Brian machina my mentor
- Slack community
