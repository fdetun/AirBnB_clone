#!/usr/bin/python3
import subprocess
bashCommand = "pep8 --statistics -qq models/engine/file_storage.py"
process = subprocess.run(bashCommand.split(), stdout=subprocess.PIPE)
print(process.stdout)