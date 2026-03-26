### Setup

#### Python virtual env

- `$python3 -m venv .venv`
- `source .venv/bin/activate`

(may need to run `sudo apt install python3.11-venv`)

I'm using Debian 12

- `$sudo apt install pkg-config build-essential python3-dev python3-tk`
- `$sudo apt install curl`
- `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
- `$sudo apt install protobuf-compiler`

#### Requirements

You should see `(.venv)` in your terminal if your virtual environment is activated.

Then you can run `$pip install -r requirements.txt`

#### Credentials

For model API keys these are stored in a `.env` file

#### Run app from source

`$python3 main.py` will launch the desktop app
