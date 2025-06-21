# 🕹️ Multiplayer Shooter Game (Concurrency Project)

This is a **multiplayer 2D shooter game** built using **Pygame** for the frontend and **AWS** as the hosting platform to manage client-server communication. It was created as a university project to demonstrate **concurrency principles** and **real-time multiplayer communication**.

---

## 🚀 Features

- 🎮 Real-time multiplayer shooter gameplay  
- 🌐 Hosted on AWS for global access  
- 🔁 Client-server model using socket programming  
- 📡 Concurrency handling for multiple players  
- 🧱 Built with Python and Pygame

---

## 🧠 Tech Stack

| Tech        | Purpose                        |
|-------------|--------------------------------|
| Python      | Core game and server logic     |
| Pygame      | Game rendering and UI          |
| AWS EC2     | Game server hosting            |
| Socket Lib  | Client-server communication    |
| Threading   | Concurrency & client handling  |

---

## 🛠️ How It Works

1. **AWS Server (Host):**
   - An EC2 instance runs the game server.
   - Listens for incoming player connections.
   - Manages game state (player positions, bullets, hits).

2. **Clients (Players):**
   - Launch Pygame-based game on their local machine.
   - Connects to the AWS server using sockets.
   - Sends/receives game data in real-time.

3. **Concurrency:**
   - Each client connection is handled on a separate thread.
   - Shared resources like game state are synchronized to prevent race conditions.

---

## 🖥️ Running the Game

### Server Setup (AWS):
1. Launch an EC2 instance (Ubuntu recommended).
2. Install Python:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
