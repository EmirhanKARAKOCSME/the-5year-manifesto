import os
import shutil

# define the path dynamically 
Downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

# print and check if Python can see it
print("defined path: " , Downloads_path)
print("Does this folder exist on your computer?:", os.path.exists(Downloads_path))