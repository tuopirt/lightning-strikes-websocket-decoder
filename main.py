import websocket
import json
import time
import threading

import os
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv("WEBSOCKETURL")



def on_open(ws):
    print("Connected to Blitzortung WebSocket")
    
    ws.send(json.dumps({"a": 111})) # handshake message

    # Automatically close after 10 seconds
    def close_ws():
        time.sleep(1)
        print("Closing WebSocket after 1 seconds")
        ws.close()

    threading.Thread(target=close_ws).start()
    
    print("Sent start command to begin streaming")


# we dont need this in this case as the data isn't being passed as a binary
def on_data(ws, data, data_type, continue_flag):
    if data_type == websocket.ABNF.OPCODE_BINARY:
        print("Binary frame received. Length:", len(data))
    else:
        print("Non-binary data type:", data_type)



def on_message(ws, message):
    # Messages come in as binary — decode to JSON string
    print("→", message)
    print(type(message))



def on_error(ws, error):
    print("\n!!! Error Detected !!!:", error)



def on_close(ws, close_status_code, close_msg):
    print("\nConnection closed. Status code:", close_status_code, ", closing message:", close_msg)



if __name__ == "__main__":
    ws = websocket.WebSocketApp(
        URL,
        on_open=on_open,
        on_message=on_message,
        #on_data=on_data,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever(ping_interval=30, ping_timeout=10)


