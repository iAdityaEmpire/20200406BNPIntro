#!/usr/bin/env python
import sys
from bnp.validation import moneylib

moneylib.invest()
moneylib.spend()

for path in sys.path:
    print(path)
