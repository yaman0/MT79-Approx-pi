# MT79-Approx-pi
## Summary
School project for develop few functions to approximate pi number
## Requirement
- python 3.6
## Dependencies
- If you only have python 3 on your system
```bash
pip install -r requirements.txt
```
- If you have both
```bash
pip3 install -r requirements.txt
```
## Usage
- Basic usage
```bash
python approxPi.py -h
```
- Generate pi with ramanujan method and depth=20
```bash
python approxPi.py genpi --method r 20
```
- Search pi's 4^^th^^ decimals with imparis method
```bash
python approxPi.py findpi --method i 4
```

- Display a graph to see convergence difference between imparis and classic
```
python approxPi.py diffgraph 200
```

- Display a graph to see convergence for Monte-Carlo
```
python approxPi.py diffgraphmc 200
```  

- Display circle with 200 points for Monte-Carlo
```
python approxPi.py circle 200
```  
## Anatomy
```
├── approxPi.py         => main
├── requirement.txt     => dependencies for pip
├── src/                => classes used
├── test/               => tests
```
