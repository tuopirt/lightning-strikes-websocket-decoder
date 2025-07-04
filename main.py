import websocket
import json
import time
import threading

import os
from dotenv import load_dotenv

from decode import LZW_decode
from filter import customfilter

load_dotenv()
URL = os.getenv("WEBSOCKETURL")



def on_open(ws):
    print("Starting...")
    ws.send(json.dumps({"a": 111})) # handshake message

    # Automatically close after 5 seconds
    def close_ws():
        time.sleep(5)
        print("Closing WebSocket after 5 seconds")
        ws.close()

    threading.Thread(target=close_ws).start()



def on_data(ws, data, data_type, continue_flag):
    compressed_bytes = data.encode('utf-8', errors='ignore') #encode bytes
    decoding_data = LZW_decode(compressed_bytes) # run decode function
    decoded_data = json.loads(decoding_data.decode('utf-8', errors='replace')) #decode bytes

    filtered_data = customfilter(decoded_data) # fitler out what we dont want
    # any additional steps here
    print(filtered_data)



def on_error(ws, error):
    print("\n!!! Error Detected !!!:", error)



def on_close(ws, close_status_code, close_msg):
    print("\nConnection closed. Status code:", close_status_code,", closing message:", close_msg)


if __name__ == "__main__":
    ws = websocket.WebSocketApp(
        URL,
        on_open=on_open,
        #on_message=on_message,
        on_data=on_data,
        on_error=on_error,
        on_close=on_close
    )

    ws.run_forever(ping_interval=30, ping_timeout=10)


