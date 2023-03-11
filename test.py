import math
import sys
from os import rename

import requests


print(sys.version)
# print(sys.executable)
def greet(who_to_greet):
    greeting = f"Hello, {who_to_greet}"
    return greeting


# print(greet("World"))
# print(greet("Lina"))
# print(greet("Lesley"))
r = requests.get("https://www.google.com")
print(r.status_code)
