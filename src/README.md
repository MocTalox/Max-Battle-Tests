# Testing Code

The testing code is developed in Python and it has been organized in multiple files. These codes are grouped in different categories: Modules with testing functions, testing scripts and auxiliary methods.

### Testing Functions

- [`max_utils.py`](./max_utils.py) - Holds the main Attack and Defense CPM testing methods:
  - `mult`: Calculates a range of values for both Attack and Defense CPM.
  - `seg`: To verify if a Defense CPM value is correct for a certain HP value.
- [`hp_test.py`](./hp_test.py) - Holds the main HP testing method:
  - `hp_lcm`: Calculates the HP value using the *LCM* method.

This test functions can be easily executed inside a Python console (on the root folder):

```py
from src.max_utils import mult
from src.max_utils import seg
from src.hp_test import hp_lcm
```

### Testing Scripts

- [`def_test.py`](./def_test.py) - Script that calculates a range of values for the Defense CPM.
- [`help_test.py`](./help_test.py) - Script that calculates a range of values for a bonus value (mainly used for Helpers bonus).

This test scripts can be executed using the following commands (on the root folder):

```
python -m src.def_test
python -m src.help_test
```

### Auxiliary Code

Testers dont need to worry about this Python modules.

- [`mult_test.py`](./mult_test.py) - Auxiliary testing methods for `def_test.py` and `help_test.py`.
- [`py_utils.py`](./py_utils.py) - Auxiliary python utility methods.
- [`hp_test_adv.py`](./hp_test_adv.py) - Extension of `hp_test.py` used for extremely precise HP testing. Used a few times to prove the stats model were exact, but there is no need to use it anymore. It holds a script as an example of its functionality.
