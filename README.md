
## Indonesia-Address-Parser
[![Build Status](https://travis-ci.org/jingw2/size_constrained_clustering.svg?branch=master)](https://travis-ci.org/jingw2/size_constrained_clustering)
[![PyPI version](https://badge.fury.io/py/size-constrained-clustering.svg)](https://badge.fury.io/py/size-constrained-clustering)
![GitHub](https://img.shields.io/github/license/jingw2/size_constrained_clustering)
[![codecov](https://codecov.io/gh/jingw2/size_constrained_clustering/branch/master/graph/badge.svg)](https://codecov.io/gh/jingw2/size_constrained_clustering)
![PyPI - Downloads](https://img.shields.io/pypi/dm/size-constrained-clustering)
![Codecov](https://img.shields.io/codecov/c/github/jingw2/size_constrained_clustering)


Implementation of Indonesian-Address-Parser. 

### Installation
Requirement Python >= 3.6
* install from PyPI
```shell
pip install Indonesian_Address_Parser
```

### Methods
* My Module algorithms


### Usage:
```python
# setup
from Indonesian_Address_Parser import Indonesian_Address_Parser
```

```python
# import class from module
from Indonesian_Address_Parser import Indonesian_Address_Parser

# create object Parser
indonesianParser = Indonesian_Address_Parser()

# calling parser method for one address
indonesianParser.parser("Jl. Kolonel Sulaiman Amin, Komplek Pemda, Blok H3 No 35, KM7, Palembang, Indoensia")

# calling parser method for one list of addresses
addressParser = indonesianParser.parser(
    [
        "Jl. Kolonel Sulaiman Amin, Komplek Pemda, Blok H3 No 35, KM7, Palembang, Indoensia", 
        "Jl. Ahmad Yani, No 3, Plaju, Palembang, Indonesia"
    ]
)
print(addressParser)

```

## Copyright
Copyright (c) 2022 Tri Basuki Kurniawan. Released under the MIT License. 

Third-party copyright in this distribution is noted where applicable.

### Reference
* [Github Project](https://github.com/tribasuki74/myenglish)
