open the repo cloned repo in vscode, open new terminal in vscode 

1. create virtual env for installing dependencies
python -m venv venv 
source ./venv/bin/activate (venv\Scripts\activate on windows)
pip install -r requirements.txt

2. upload the arduino sketch (copy paste sketch.ino using arduino ide)

3. close the arduino ide completly (ie serail plotter or monitor is closed)
python ./plot.py (in vscode terminal to run script or simply double click the py file)


**NOTE : if "python" in commands doesnt works, use python3 (especially for linux)
