


### Install and Setup Behave Framework

Setup Virtual Environment:

Create virtual environment

```buildoutcfg
python3 -m venv env
```

Activate virtual environment

```buildoutcfg
source env/bin/activate
```

Stop virtual environment
```buildoutcfg
deactivate
```

Install Behave:
```buildoutcfg
pip3 install behave
```

Run Behave Feature:
```buildoutcfg
behave -i example.feature

```

## Introduction:
https://semaphoreci.com/community/tutorials/getting-started-with-behavior-testing-in-python-with-behave

Before we write more, we need to understand the three phases of a basic Behave test: “Given”, “When”, and “Then”. 
“Given” initializes a state, “When” describes an action, and “Then” states the expected outcome. 
