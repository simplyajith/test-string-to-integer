# Testing python int() function

Automated Test cases for python builtin int() function

## Getting Started


### Prerequisites

```
git
python3
python3 in system path
pip3

```

### Installation

##Mac OS 
```
git clone https://github.com/simplyajith/four-in-a-row.git
cd four-in-a-row/
pip install virtualenv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
python play_game.py

```

##Windows

```
git clone https://github.com/simplyajith/four-in-a-row.git
cd four-in-a-row/
pip install virtualenv
python -m venv venv
cd venv/Scripts
activate

#After activating the virtual environment. go back to four-in-a-row folder.
cd four-in-a-row/
pip install -r requirements.txt
python play_game.py
```

## Test cases
Valid test data

```
List of (input,expected)
[("1", 1), ("1000", 1000), ("+888", 888), ("-1", -1), ("-9999", -9999),
 ("2147483647", 2147483647), ("-2147483647", -2147483647), ("0", 0),(True, 1)])

```

Invalid test data

```
["", "999.5", "3/4", "abc", "abc946", "$%^", "--667", "++-6567",
None, (), {}, [], (1, 1), [55, ], {56: 77},"0b100","0xABC"]
```
No input data

Stress tests by generating valid numeric strings of length greater than 2000, 8000 and 10000.

## Test results
In four-in-a-row folder, run the below command

```
pytest -v -s --html=results/report.html  --self-contained-html
```
HTML output will be present in the results folder.

## Built With

* [Python3](https://www.python.org/download/releases/3.0/) - Language used


## Authors

* **Ajith Sundararaj** - *Initial work* - [simplyajith](https://github.com/simplyajith)

