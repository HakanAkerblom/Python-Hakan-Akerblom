import os, sys

os.system("cls")

print(f"{'='*30}=main.py{'='*30}")

# code imported from another module is executed when imported
import module1

# note __name__ is module1 when ran from outside of module.py
# when module1.py is run -> __name__ = '__main__'
import math

# when importing a module - a reference will be created to sys.modules
print("globals namespace")
print(globals()["module1"])

# when importing a module - it will be stored in sys.modules
print("sys modules")
print(sys.modules)

print(f"\n{'='*30}end main{'='*30}")