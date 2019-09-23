# Multiprocess Chat Support System

Python program that serves multiple clients parallely, based on predefined input and output.
If the requested input is not found, a human responds.

## How to Use:

`$ python3 datasetGenerator.py`

Created the set of  responses.

**Terminal 1:**`$ python3 humanServing.py`

**Terminal 2:**`$ python3 server.py`

**Terminal 3:**`$ python3 client.py`

Request a keyword from Terminal 3.

Human waits on Terminal 1, waiting for a phrase.

He sends a response, which is received at the client side. 

Also this response is saved into our response file(*responses.json*).

### Running multiple clients:

Run multiple instances of *client.py* from different terminals.
