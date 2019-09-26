# Multiprocess Chat Support System

Python program that serves multiple clients parallely, based on predefined input and output.
If the requested input is not found, a human responds.

## How to Use:

`$ python3 datasetGenerator.py`

`Enter keyword`

(Enter your desired keyword)(Enter 'close' to exit)

`Enter Response`

(Enter your expected output)

Created the set of  responses.

The following steps must be done in this order:

**Terminal 1:**`$ python3 humanServing.py`

**Terminal 2:**`$ python3 server.py`

**Terminal 3:**`$ python3 client.py`

Request a keyword from Terminal 3.

Human waits on Terminal 1, waiting for a phrase.

He sends a response, which is received at the client side. 

Also this response is saved into our response file(*responses.json*).

### Running multiple clients:

Run multiple instances of *client.py* from different terminals.
