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
python -m pip install -r requirements.txt
```

### Run the application
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 3000 --reload
```

## Example .env file
```bash
SECRET_KEY =
ALGORITHM = 
ACCESS_TOKEN_EXPIRE_MINUTES =
```

## Semantic Commit Messages
```
feat: (new feature for the user, not a new feature for build script)
fix: (bug fix for the user, not a fix to a build script)
docs: (changes to the documentation)
style: (formatting, missing semi colons, etc; no production code change)
refactor: (refactoring production code, eg. renaming a variable)
test: (adding missing tests, refactoring tests; no production code change)
chore: (updating grunt tasks etc; no production code change)
```