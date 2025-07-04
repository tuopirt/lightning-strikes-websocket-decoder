# Lightning Strike Collector

This project connects to the [Blitzortung.org] live lightning data stream via its WebSocket, receives compressed lightning strike data, and decodes it in real time.

## WebSocket Source

- **URL:** `https://www.blitzortung.org/en/live_lightning_maps.php`
- The WebSocket sends continuous lightning strike updates across the globe.
- !! To receive data, a small JSON handshake message needs to be sent first sent: `{"a":111}` !!

## Tech & Concepts

- **Python WebSockets:** `websocket-client` library for connections
- **LZW Decoding:** Blitzortung sends data in LZW-compressed format. Decoded using LZW decoding algorithm
- **Real-Time JSON Parsing:** After decoding, each message is valid JSON containing strike information and the detecting stations.
- **Data Filtering (Optional):** custom filter for decoded JSON data.

- **Additional Add-ons:** a way to store the collected data (location, polarity, etc.).

## Requirements

- Python 3.7+
- `websocket-client` (install via pip)

