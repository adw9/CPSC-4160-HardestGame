# CPSC-4160-HardestGame

Milestone 1 CPSC 4160
https://github.com/adw9/CPSC-4160-HardestGame
# Part 1: Updates to Game Document
• The game and current development design have not updated since the original project proposal.

• The Model has undergone changes to support a much wider variety of objects than anticipated.

o Obstacles will be stored in a separate list from tokens and powerups

o Start/finish position also will be stored in a list

# Part 2: Updated Project Timeline
Division of Labor

Andrew Williams is the only team member on this project, so all labor will be completed alone.

Expected Workload:
• Overall game structure – 2 hours (95% Done)

o A separate file to read from level files may be created, otherwise this is done.

• Implementation of separate level files – 4 hours

• Level design – 8 hours

• Collision/Reset from hitting obstacles – 1 hour (95% Done)

o A bug where the reset doesn’t occur until another player input is logged has not been
fixed, otherwise this is done.

• Player movement - <1 hour (100% Done) - Speed may be adjusted after levels are designed

• Powerup implementation – 1 hour (50% Done)
-This will be easier than expected, adjusting it from 2 hours to 1 hour. Most code will be
reusable from collision code

• Main Menu – 6(?) hours (0% Done)
The only anticipated issue is the possibility of underestimating how long certain tasks will take. In the
event that this happens, certain functionality may be reduced in order to meet deadlines.

Updated Timeline

Milestone 1: March 30

• Overall game structure completed – March 10

• Collision/Reset completed – March 12

• Player Movement – March 12

• Updated Game Document – March 14

Milestone 2: April 12

• Powerup implementation – March 22

• Implementation of separate level files – March 25

• Atleast 5 levels – March 28

• Updated Game Document – March 28

• Main menu implementation – April 10

• Updated Game Document – April 11

Final Game Submission: April 26

• Polished game, fix misc. bugs – April 20

• Completed Game Document – April 24

Final Game Presentation: May 4

• Presentation materials – May 1

# Part 3: Technical Difficulties
The primary technical issue at hand is how to store level data, and how to generate trial data for
features being developed before levels are introduced. The potential for a major gameScript rewrite is
there, and must be avoided to keep development time low. Reading level data should be the next
feature developed so that the rest of the project can work around its constraints. Level data will likely be
stored in a simple .txt file, not an efficient solution but one that works for this project.
The other technical difficulty is a simple bug regarding player collisions with obstacles. The player sprite
is not updated when a collision happens, but only later when the player inputs any movement
command. This is odd, and will be resolved during the next sprint. 
