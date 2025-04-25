# UDP Peer Messaging and HTTP Web Server

This project implements two networking applications using Python socket programming:

- A UDP-based Peer-to-Peer Messaging System for real-time communication.
- An HTTP Web Server that serves static content (HTML, CSS, images) and handles routing, redirections, and custom error pages.

Developed as part of the ENCS3321 – Computer Networks course project.

## Features

### UDP Peer Messaging
- Peer-to-peer communication over UDP.
- Real-time message exchange within the same local network.
- Uses broadcasting and threading for simultaneous receive/send.

### HTTP Web Server
- Built using Python and TCP sockets.
- Serves HTML, CSS, PNG, and JPG files.
- Handles URL-based routing, including:
  - `/`, `/index.html`, `/main_en.html`, `/en` → English homepage
  - `/ar` → Arabic homepage
  - `/so` → Redirects to StackOverflow
  - `/itc` → Redirects to BZU ITC
- Displays custom 404 error page with client IP and port.

## Tech Stack

- Python – Socket programming and threading
- HTML/CSS – Static content served by the web server
- Command Line – Terminal interaction for messaging

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Clone the Repository
1. Clone the repository:
     ```bash
      git clone https://github.com/Lanamahd/UDP_Peer_Messaging_and_HTTP_Web_Server.git
      cd UDP_Peer_Messaging_and_HTTP_Web_Server

2. Install dependenciess:
     ```bash
    pip install -r requirements.txt

## Usage
### Running the UDP Peer Messaging System

1. Navigate to the UDP messaging directory.

2. Execute the script:
     ```bash  
    python udp_peer_chat.py

3. Follow the instructions on-screen to connect and start messaging.   


### Running the HTTP Web Server

1. Navigate to the HTTP server directory.
2. Start the server:
     ```bash
     python program.py

3. Open your browser and navigate to http://localhost:PORT to view the hosted content.









