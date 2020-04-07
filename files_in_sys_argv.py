#!/usr/bin/env python
import sys

print(sys.argv)

for file_name in sys.argv[1:]:
    print(file_name)

