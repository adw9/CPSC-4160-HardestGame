# Final Game Submission
# Part 1: Introduction
The name of the game is “World’s Easiest Game”. The game is inspired by the iconic flash game “World’s Hardest Game.” 
 
Game Versions
•	Python 3.10.11
•	Pygame 2.1.2
Game Controls
•	Arrow keys to move

# Part 2: Game Design
Mechanics/Technology
•	The gameplay loop in gameScript.py is primarily responsible for running the game. It calls other objects in a MVC architecture which handle most critical game features. Game.py handles level creation, while controller.py handles most collision and movement. Our main gimmick, the powerups, which are either a shield(blue) or speed(white), are handled through changes in the player file (player.py). Collisions with the powerups are handled the same as tokens in the Controller. This game is similar to others in the flash game category, with the primary difference being that this game is still supported. Powerups are also a unique feature, not seen often in this style of flash game. 
Story
•	This game does not have a significant story element, with the primary antagonist being a faceless, automated obstacle barring the player of the goal of moving a token to the “endzone”. The protagonist is the player, represented by a purple square. 
Player Experience
•	I want the player to experience the feeling of solving a mildly easy puzzle, similar to flash games of the past. The game should feel relatively light-hearted due to the lack of story or significant difficulty. There are no rewards or feedback for progression, outside of a “You Win!” message on the command line for every level advancement. There is no audio track in the game, and a lack of significant visual changes throughout the levels. 
Part 3: Game Design Changes
The game design has not changed significantly from the original proposal, due to taking significant inspiration from an existing product. Game mechanics were intended to operate in the way that they currently do, but the list of game mechanics is shortened due to a lack of development time. 
The primary challenge we faced was with the “new level” feature, as this required a huge rewrite of key features shortly before the deadline. This process was harder than expected due to poor programming processes early in development, and a lack of understanding of python classes. The new level feature is working at time of release, with 5 levels created and an easy pipeline to create more as desired. 
# Part 4: Game Development  & Documentation
CMV Description
•	The controller.py file receives player input through arrow keys and calculates collisions
•	The game.py,ball.py, and player.py files control the game state and store key data. The gameScript.py file is used to create the crucial objects and call most methods
•	The mainView.py file is used to print the actual pygame window, and update it from passing in the model files and reading their object variables. 
Code Outline
•	gameScript.py
o	Main game script, run to start the game.
o	Initialize proper objects, then loops until game is over
•	Controller.py
o	Handles collision data and player input through userInput() and collision_detection()
•	Player.py
o	Stores data for the player such as the size/speed of the user, and what powerups are being used. Contains functions to update these as needed.
•	Ball.py
o	Stores data for the balls used as obstacles such as speed and size, contains functions to update these as needed.
•	Game.py
o	Holds lists of all obstacles, powerups, and tokens. Contains fileReader(), which reads a level file and stores it in relevant data to be used in other objects.
•	MainView.py
o	Contains methods to print the actual pygame screen, after reading data passed to it from other objects.
Documented Bugs
•	Occasionally the player respawn method for new levels does not work correctly.
•	Obstacle balls can pass through the start/finish areas, and levels must be designed around this handicap. 
•	The token/powerups do not reset when the player dies, allowing them to get the token, “suicide”, and then have an easy path to the finish.
# Part 5: Group Member Roles, Tasks, and Performance
This project was completed alone, so there was no split of work. 

# Final Timeline
Milestone 1: March 30
•	Overall game structure completed – March 10 
•	Collision/Reset completed – March 12
•	Player Movement – March 12
•	Updated Game Document – March 14
Milestone 2: April 12
•	Powerup implementation – March 22
•	Implementation of separate level files – May 1
•	Atleast 5 levels – May 3
•	Updated Game Document – March 28
•	Main menu implementation – April 10
•	Updated Game Document – April 11
Final Game Submission: April 26
•	Polished game, fix misc. bugs – April 20
•	Completed Game Document – May 3
Final Game Presentation: May 4
•	Presentation materials – May 3

# Demo Video
https://youtu.be/DV357-DBtH0


