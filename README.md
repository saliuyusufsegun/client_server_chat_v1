# Client Server Chat v1 - Walkie Talkie

A simple 1-to-1 chat platform in Python using sockets.  
Works like a walkie-talkie: Client sends a message → Server replies → Back and forth.

## Features
- **Real-time 2-way chat** between 1 Client and 1 Server
- **Runs on localhost** - no internet needed
- **Type `exit`** to close connection from either side
- **Built with core Python**: `socket`, `while loop`, `if/else`

## How It Works
1. **Server** waits for a client to connect on port `1111`
2. **Client** connects to the server
3. Both can send and receive messages until someone types `exit`
4. Connection closes automatically

## Requirements
- Python 3.x
- Both server and client on the same machine, or same network

## How to Run

### 1. Start the Server First
Open terminal 1:
```bash
python server.py

### 2. Then Start the Client
Open terminal 2:
python client.py

then chat....
