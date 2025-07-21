#  A Concurrency & Distributed Systems Group Project

Welcome to our **2D multiplayer shooter game** — built with Python, Pygame, and a whole lot of teamwork.

What started as a simple single-player shooter turned into a fully interactive multiplayer experience, featuring:
- Enemies running independently on their own threads
- Real-time player communication via AWS-hosted sockets

---

##  Key Highlights

- **Multiplayer Support:** Connect multiple players online using a client-server model  
- **Concurrency in Action:** Each enemy moves independently on its own thread  
- **Real-Time Syncing:** Game state updates flow seamlessly across clients  
- **Smooth Gameplay:** Built with sprite animations, sound effects, and collision logic  
- **Hosted on AWS:** The server is live on the cloud, accessible from anywhere  

---

##  Technologies Used

| Technology | Purpose                                 |
|------------|------------------------------------------|
| **Python** | Game logic and networking                |
| **Pygame** | Game visuals, animations, and input      |
| **Threading** | Enemy concurrency & client handling  |
| **Socket** | Real-time multiplayer communication      |
| **AWS EC2** | Server deployment & hosting             |

---


Here’s a quick overview of the main files and what each of them does:

- `main.py` – The heart of the game. Runs the offline version, manages the main loop, initializes the game window, and handles player input and rendering.
- `arrowVector.py` – Handles directional logic for shooting arrows. Each arrow has its own direction and velocity.
- `utils.py` – Contains helper functions like movement calculations, collision detection, and asset speed control.
- `testenemy.py` – Controls how enemies behave. Each enemy is run in its own Python thread, allowing for independent movement and animations.
- `Client/` – Contains the files for the multiplayer version of the game.
  - Inside `Client/dist/`, you'll find the `main.exe` (Windows executable for online play).
- `assets/` – This folder includes all the game’s visual and audio assets: sprites, backgrounds, arrow icons, explosion animations, etc.

##  How to Play

- **Move:** `A` (left), `D` (right)  
- **Shoot Arrows:** `Q`, `W`, `E` (different directions)

---

##  How to Run the Game (Online Multiplayer)

1. Navigate to the `Client` folder → then open the `dist` folder  
2. Download `main.exe`  
3. Also download the `assets` folder and place it **in the same directory as `main.exe`**  
4. Run `main.exe`  

> Make sure you're connected to the internet — the game connects to our AWS-hosted server

---

##  How to Run the Game (Offline Mode)

If you prefer to play the local single-player version:

1. Open the project folder  
2. Run `main.py`  

> The game works fully offline, with enemies still running independently through Python threads!

---

Enjoy the game!  
Let us know what you think, or feel free to explore the code and see how concurrency and networking come together!
