[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
# Calculator mini-project
This project has been created for you to practice unit testing using Pytest and Unittest. The source code contains a calculator mini-project that performs four different operations (addition, subtraction, multiplication and division). You can use it to develop a set of scenarios needed to test all the source code. Note that the suggested solutions are available in different branches of the directory structure.

## Prerequisites
- Install Python 3: [Python 3 download](https://www.python.org/downloads/)
- Install git: [Git download](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Installation
1. Download the Project to Your Local Directory:
```shell
git clone https://github.com/OpenClassrooms-Student-Center/4425126-testing-python.git 
cd 4425126-testing-python
```

2. Set up a Virtual Environment:
  - Create the virtual environment: `python -m venv venv`
  - Activate the virtual environment:
    - Windows: `venv\Scripts\activate.bat`
    - Unix/MacOS: `source venv/bin/activate`
3. Install project dependencies
```shell
pip install -r requirements.txt
```

## Run
Run the script using the following command: `python main.py`

## Solutions
1. Suggested solution for unit testing using Unittest:
```shell
git checkout unittest-test
python -m unittest discover tests/
```

2. Suggested solution for unit testing using Pytest:
```shell
git checkout pytest-test
pytest
```

3. Suggested solution for mocks using Pytest:
```shell
git checkout mock-test
pytest
```

4. Suggested solution for parametrized testing using Pytest:
```shell
git checkout parametrize-test
pytest
```