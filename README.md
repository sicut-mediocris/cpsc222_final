A  Concurrency & Distributed Systems group project:

Welcome to our 2D multiplayer shooter game — built with Python, Pygame, and a whole lot of teamwork. What started as a simple single-player shooter turned into a fully interactive multiplayer experience, featuring enemies running on their own threads and real-time player communication through AWS-hosted sockets.

We built this game not just to play — but to showcase core concepts of concurrency, threading, and distributed systems in action.

 Key Highlights
Multiplayer Support: Connect multiple players online using a client-server model

Concurrency in Action: Each enemy moves independently on its own thread

Real-Time Syncing: Game state updates flow seamlessly across clients

Smooth Gameplay: Built with sprite animations, sound effects, and collision logic

Hosted on AWS: The server is live on the cloud, accessible from anywhere

 Technologies Used
Tech	Purpose
Python	Game logic and networking
Pygame	Game visuals, animations, and input
Threading	Enemy concurrency & client handling
Socket	Real-time multiplayer communication
AWS EC2	Server deployment & hosting

 How to Play
 Controls
Move: A (left), D (right)

Shoot Arrows: Q, W, E (for different directions)

 How to Run the Game
 For Online Multiplayer:
Go to the Client folder → then dist

Download main.exe

Also download the assets folder and place it in the same folder as main.exe

Run main.exe and enjoy playing online!

Make sure you're connected to the internet. The game communicates with the server hosted on AWS.

🕹 For Offline Mode:
If you want to play the local single-player version:

Simply run the main.py file

Everything works offline — enemies will still act independently using threads!

