### About

This is a Tkinter desktop-app based agent client using Pydantic AI.

Please note this is exploratory code so the quality is low and it's also a work in progress.

Also, while you could develop the app on the low-powered PC itself, I would recommend developing it on a stronger computer with a big display and hot reload to speed up development. I wrote the youtube branch of this app on a 1080P monitor connected by VGA to the Eee PC 1005HA. This was pretty brutal, every time I would start the app up it took 30 seconds before it rendered the app.

### Setup

#### Environment credentials

You will need to add a `.env` file in this folder and put your LLM model provider keys in there as shown in the `.env.example` file.

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

Please note, it takes around 3-4 hours to install pydantic ai if doing on the Eee PC itself (1005HA). Should probably find another way to get the wheels such as tiktoken, cryptography, etc...

#### Credentials

For model API keys these are stored in a `.env` file

#### Run app from source

`$python3 main.py` will launch the desktop app
