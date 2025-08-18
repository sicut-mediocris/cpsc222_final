## A Concurrency & Distributed Systems Group Project (Offline Version)

Welcome to our 2D single-player shooter game — built with Python and  Pygame

What began as a small project evolved into a fast-paced, threaded game engine where:

Enemies run independently on their own threads

Gameplay is smooth with real-time animations and collision logic. This branch gives you smooth animations whereas in the online branch there was a problem getting the sprite animations and sound to work.

## Key Highlights

Offline Single-Player Mode: No internet connection required — everything runs locally

Concurrency in Action: Each enemy moves independently on its own thread

Smooth Gameplay: Sprite animations, sound effects, and collision detection for a polished feel

 
 ## Technologies Used

Python : 	Game logic and core mechanics

Pygame : 	Visuals, animations, and input handling

Threading : Independent enemy movement and logic


 ## File Overview

main.py – Heart of the game. Runs the main loop, initializes the game window, and handles player input/rendering.

arrowVector.py – Directional logic for shooting arrows, each with unique velocity and direction.

utils.py – Helper functions for movement, collision detection, and speed control.

testenemy.py – Controls enemy behavior; each enemy runs in its own Python thread.

assets/ – All visual/audio assets: sprites, backgrounds, arrow icons, explosion animations, etc.

## Controls

Move: A (left), D (right)

Shoot Arrows: Q, W, E (different directions)


## How to Run the Game


**Go to the Releases section on the repository.**


<img width="1020" height="573" alt="imp-ss" src="https://github.com/user-attachments/assets/b306fa34-602d-46d2-86e7-8c4a79948905" />




 Run the .exe file called "archeroffline" which is version V1.0



Download the .exe file and also download the assets folder and keep them in the same folder


Double-click the .exe file to play.

Enjoy the game!
Feel free to explore the code and see how Python threading makes enemy AI independent and dynamic.

