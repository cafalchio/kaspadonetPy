# kaspadonetPy
 Python version of kaspadonet for interacting with Kaspa with gRPC.
 Kaspa is an open-source cryptocurrency, see https://github.com/kaspanet/kaspad for more details.

## Quick install
1. Clone the repo and setup a virtual Python environment, `python -m venv venv`
2. Activate it `source venv/bin/activate`
3. Install the requirements using `pip install -r requirements.txt`

## Setup
1. Run Kaspa in the background `kaspad --uxtoindex` (Linux) or `kaspad.exe /uxtoindex` (Windows).
2. Make sure it is updated and Accepting blocks.
3. Run another terminal window for `kaspawallet start-daemon`, this will run on localhost port 8082.
4. If you need to customize your wallet host and port, copy `.env_example` to `.env` and edit it. 
5. You can then interact with the Python gRCP services from the wallet, eg: Run `python show_address_example.py`