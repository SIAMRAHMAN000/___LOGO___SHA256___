# EXAMPLE 
from hashlib import sha256

logo = """


  ██████    ██     █████      ███    ███
 ██         ██    ██   ██     ████  ████
  █████     ██    ███████     ██ ████ ██
      ██    ██    ██   ██     ██  ██  ██
 ██████     ██    ██   ██     ██      ██

"""

s = sha256(logo.encode("utf-8")).hexdigest()
print(s)

# START METHOD

from hashlib import sha256

logo = """


  ██████    ██     █████      ███    ███
 ██         ██    ██   ██     ████  ████
  █████     ██    ███████     ██ ████ ██
      ██    ██    ██   ██     ██  ██  ██
 ██████     ██    ██   ██     ██      ██

"""
if sha256(logo.encode("utf-8")).hexdigest() != "4866638cc161a728b51db7521d7b44bc40a7355ca7da056799a01e11fa4e2405":
    print(f"ERROR")
