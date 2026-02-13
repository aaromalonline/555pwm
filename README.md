
### Basic Guide  
Clone the repo and open the cloned repo in vscode, open new terminal in vscode  
```
- plot.py : plotting script of whatever received in the serial port (like serial plotter but with no frequency limits, Digital CRO).
- sketch.ino : a sketch/firmware to send the output recieved at the A0 pin to serial port.
```

1. Create virtual env and installing dependencies
```
python -m venv venv 
source ./venv/bin/activate (venv\Scripts\activate on windows)
pip install -r requirements.txt (or pip install pyserial, numpy, matplotlib)
```
3. Upload the arduino sketch (copy paste sketch.ino using arduino ide)
```
plug in the output of the circuit to A0 of arduino UNO.
change PORT = '/dev/ttyUSB0' in sketch to PORT = 'COM3' for windows before uploading
```

5. Close the arduino ide completly (ie serial plotter or monitor is closed) -> avoid busy serial port
```
python ./plot.py (in vscode terminal to run script or simply double click the py file)
```

**NOTE : if "python" in commands doesnt works, use python3 (especially for linux)
