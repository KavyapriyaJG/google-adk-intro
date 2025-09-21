## Create, Activate python virtual environment for development

```
python -m venv .venv
source .venv/bin/activate
```

## Dependency packages to install
pip install -r requirements.txt


## Folder structure
```
parent_folder/
    named_agent/
        __init__.py
        agent.py
        .env
```
name of agent should match folder name. thats how adk identifies an agent is initialized


## To run
adk run <folder_name>

