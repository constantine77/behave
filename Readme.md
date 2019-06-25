
# Acceptance Testing 

We are using Behave framework and Gherkin scenarios into automated acceptance tests for our project.

### Installation
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
deactiva

Execute the following command to install behave with pip:

```buildoutcfg
pip install behave
```

###Acceptance Testing with behave framework

Acceptance Testing with behave framework operates on directories containing:

*feature file* written by your PO/Business Analyst/ or  whoever with your behaviour scenarios in it.

and

*steps* directory with Python step implementations for the scenarios.

Before we write any Python code, we need to prepare our test case first. 

Gherkin test scenarios are placed in a .feature file. They consist of a few keywords that are necessary to run the tests – Feature, Scenario, Scenario Outline and steps keywords – Given, When, Then, And.

Steps are written in a Python file and have to be placed in a separate directory /steps, please see the following:

Test execution:

Once we have test scenario and step definition, we can finally run our test in the console:

```buildoutcfg
behave -i example.feature
```

## Introduction:
https://semaphoreci.com/community/tutorials/getting-started-with-behavior-testing-in-python-with-behave

Before we write more, we need to understand the three phases of a basic Behave test: “Given”, “When”, and “Then”. 
“Given” initializes a state, “When” describes an action, and “Then” states the expected outcome. 
