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

git clone https://github.com/Lanamahd/UDP_Peer_Messaging_and_HTTP_Web_Server.git
cd UDP_Peer_Messaging_and_HTTP_Web_Server

# Running the UDP Peer Messaging System
python udp_peer_chat.py

- Enter your name when prompted

- Start sending and receiving messages with peers on the same network

# Running the HTTP Web Server
python program.py

- Open a browser and go to http://localhost:6060 to view the hosted content

# Contact
For any inquiries, please open an issue on this repository or contact the authors through the course submission portal.

Authors: Jana Sawalmeh, Lana Musaffer, Tariq Al-Atrash
Course: ENCS3321 – Computer Networks
Instructor: Dr. Abdalkarim Awad
Semester: Second Semester 2023–2024






