# Chat Server

- Create or load encryption keys +
- Connect ot the database (need to install mysql-connector-python) +
- Start the server,listen for connections
- For each incoming connection:
  - Authenticate
  - If OK, start a new thread
  - Get the public key and store
  - Send server's public key
  - Read message and dispatch to the receiver
  - Also store in the database