# Rally API

## Requirements
- python 3.10.x

## Development
- Create a virtual environment
- Activate the virtual environment
- Install dependencies
- Run the application

### Create virtual environment
```bash
python3 -m venv venv
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
python3 -m pip install -r requirements.txt
```

### Run the application
```bash
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 3000 --reload
```