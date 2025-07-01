import websocket

url = "wss://ws1.blitzortung.org/"
ws = websocket.create_connection(url)

# Send the initial handshake to start the stream
ws.send('{"a":111}')

# Receive just one message
message = ws.recv()
print(message)

# Close connection
ws.close()
