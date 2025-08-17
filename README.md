## A Concurrency & Distributed Systems Group Project (Online Multiplayer Version)

Welcome to our 2D online multiplayer shooter game — built with Python, Pygame, AWS-hosted sockets, and a whole lot of engineering magic.

What started as a small offline shooter evolved into a fully cloud-powered, real-time multiplayer experience where:

Players connect from anywhere in the world

Enemies run on independent threads for dynamic gameplay

A dedicated AWS EC2 server keeps the action alive in real-time

---


 ## Key Highlights

True Multiplayer Support: Players connect over the internet using a custom client–server model

Concurrency Everywhere: Each enemy runs independently in its own Python thread, while multiple players update simultaneously

Real-Time Syncing: Game state updates flow seamlessly between clients through socket communication

Always-Available Server: Hosted on AWS EC2 — accessible 24/7 while the instance is running

Cloud Deployment Skills: Configured, deployed, and managed a Python multiplayer game server using AWS free tier resources

## Technologies & Cloud Infrastructure

Python : Game logic and networking

Pygame	: Game visuals, animations, and input

Threading	: Enemy concurrency & client handling

Socket	: Real-time multiplayer communication

AWS : EC2	Server hosting & deployment

Linux (Ubuntu): 	Server environment for server.py

Cloud Networking: 	Configured open ports & inbound rules for multiplayer connectivity

---

##  Cloud Deployment Process

The game’s backend (server.py) runs on an AWS EC2 instance. I configured the instance to:

Host Python code for the multiplayer server.

Keep the socket connection open for all players.

Manage inbound rules to allow real-time communication.

Run on Ubuntu, with Python environment setup and dependencies installed.

Since we are  using AWS Free Tier, the server runs for limited days per month — but while it’s active, it’s online 24/7.

If you want to play when the free tier time is used up, just contact me on LinkedIn and I can spin the server back up for you.

## File Overview

server.py – The multiplayer backend, running on AWS EC2 to handle player connections and game state syncing.

main.py – The game client for local play and multiplayer mode.

arrowVector.py – Directional logic for shooting arrows.

utils.py – Helper functions for movement, collision detection, and speed control.

testenemy.py – Enemy AI, each enemy running in its own thread.

Client/ – Contains the multiplayer client build.

Web/ - Contains files which interact with the AWS

assets/ – Visual/audio assets: sprites, backgrounds, arrow icons, explosion animations, etc.

---

## Controls

Move: A (left), D (right)

Shoot Arrows: Q, W, E (different directions)

---

## How to Play (Online Multiplayer)

Just go to the release version archeronline. Download the .exe file and then also download the assets folder,keep the assets folder and the .exe file in the same folder and then just run the .exe file. 

---

## Note on Server Availability

The AWS server runs on the free tier and has limited uptime per month.
If the server is not currently online, send me a message on LinkedIn(www.linkedin.com/in/sukirat-singh-dhillon-275054321) and I’ll bring it back up for you.

While it’s running, the experience is real-time, global, and powered entirely by Python + AWS cloud infrastructure.

Enjoy the game!
And if you’re curious about the backend magic, check out server.py to see how threads, sockets, and cloud hosting come together to keep multiplayer alive.
