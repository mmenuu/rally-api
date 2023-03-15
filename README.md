# Rally api

## Requirements
- python 3.10.x

## Development
- Install dependencies
- Create a virtual environment
- Activate the virtual environment
- Run the application

### Setup virtual environment
```bash
python -m venv venv
```

### Activate virtual environment
#### mac / linux os
```bash
source venv/bin/activate
```
#### windows os
```bash
venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the server
```bash
uvicorn app.main:app --host 0.0.0.0 --port 3000 --reload
```