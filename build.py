import subprocess
import os

subprocess.run(["git clone https://github.com/Microsoft/Recognizers-Text.git"], shell=True)


subprocess.run(["which python"], cwd="Recognizers-Text/python/libraries/resource-generator/", shell=True)

subprocess.run(["python index.py ../recognizers-number/resource-definitions.json"], cwd="Recognizers-Text/python/libraries/resource-generator/", shell=True)
subprocess.run(["python index.py ../recognizers-number-with-unit/resource-definitions.json"], cwd="Recognizers-Text/python/libraries/resource-generator/", shell=True)
subprocess.run(["python index.py ../recognizers-date-time/resource-definitions.json"], cwd="Recognizers-Text/python/libraries/resource-generator/", shell=True)

if not os.path.exists("Recognizers-Text/python/libraries/recognizers-text/dist"):
   subprocess.run(["python -m build"], cwd="Recognizers-Text/python/libraries/recognizers-text/", shell=True)
   subprocess.run(["python -m build"], cwd="Recognizers-Text/python/libraries/recognizers-number/", shell=True)
   subprocess.run(["python -m build"], cwd="Recognizers-Text/python/libraries/recognizers-number-with-unit/", shell=True)
   subprocess.run(["python -m build"], cwd="Recognizers-Text/python/libraries/recognizers-date-time/", shell=True)

subprocess.run(["poetry add ./Recognizers-Text/Python/libraries/recognizers-text/dist/recognizers_text-1.0.0a0-py3-none-any.whl"], shell=True)
subprocess.run(["poetry add ./Recognizers-Text/Python/libraries/recognizers-number/dist/recognizers_text_number-1.0.0a0-py3-none-any.whl"], shell=True)
subprocess.run(["poetry add ./Recognizers-Text/Python/libraries/recognizers-number-with-unit/dist/recognizers_text_number_with_unit-1.0.0a0-py3-none-any.whl"], shell=True)
subprocess.run(["poetry add ./Recognizers-Text/Python/libraries/recognizers-date-time/dist/recognizers_text_date_time-1.0.0a0-py3-none-any.whl"], shell=True)
