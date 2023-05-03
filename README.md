# Game Project

To run this porgram follow the instructiosn in your terminal:

```sh
cd game
python3 main.py
```

# App Project

```sh
git clone
cd app
python3 -m venv env 
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

# Web server

```sh
git clone
cd web-server
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
uvicorn main:app --reload
```

## How to guides

Create a virtual environment:
- Go to the desired folder and run:
```sh
python3 -m venv env    
source env/bin/activate
```

Automate the istallation of all dependencies:
- Create a requirements.txt file with all the dependencies:
  `pip3 freeze > requirements.txt`

- Install all dependencies:
  `pip3 install -r requirements.txt`
