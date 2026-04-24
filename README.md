cs32-final-project
Maddox Moxham CS32 final project

The project that I chose to do was to build the code for a system that creates a schedule for my squash training. i've decided that I want it to take into account many personal preferences a user may want to work on or implement into their training, and I want to create some code that puts it all together into a feasible plan that breaks up their training properly and in a professional manner. I would take into account specific training aspects that users may prefer/not prefer when creating their training plan. For example, if they need to focus on their fitness, speed and agility, and not as much on their power and explosiveness, I'd recommend more of a running and fitness test oriented weekly plan to compensate for those imbalances. Vice versa as well. Then for the squash side, depending on what parts of their game they're working on, match tactics, front court game, deep game, etc, I would have the code insert varying drills or specific sessions that target those areas of the game depending on the user's input. I would also like to be as interactive as possible, potentially asking them how their session went per day, or if they wanted to make any changes to the program mid week/program, and being able to adapt on the spot. If there's any more information you need from me please let me know.

Step by Step:

User runs program ↓ Inputs preferences ↓ Program builds weighted priorities ↓ Scheduler assigns workouts across days ↓ Outputs weekly plan ↓ (Optionally) asks for feedback → adjusts

Current Status : FP STATUS

Currently, I'd say im about 2/3 of the way done with my final project.  To run it, you first do cd final_project, then cd Final_Project, and then just run main.py through python3 main.py (this is because I accidentally created a file within a file and havent figured out how to safely undo this).  Its current functions are centered around a self-assesment rating system.  It asks you about your pjhysical abilities, squash skills, and mental game.  For each category, it will ask you to rate different aspects within them 1-5.  This is later used to create a structured program that could (if chosen) prioritize training your weaknesses.  After that, it will ask what your goal is with this program.  Whether its to maintain, build upon flaws, or prepare for a competition, the program will adapt to your preferences.  To fully flesh out your schedule, it will ask you to enter the number of rest days you'll be taking and when during your chosen amount of weeks for this training block.  After that, I've implented the rich python library that allows me to print out the schedule in a table-like format, which is best for this form of content.  Then, you will have your personalized squash training program, with three sessions a day, created to your liking.  

Rich library was found online.  

Ai used to implement rich library, and used to develop code for the randomization process and maht involved.


All of workouts.py written by me, and what specific training days should correlate to within the other files.  
