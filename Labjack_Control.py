import u3 
import LabJackPython
import sys
from tkinter import messagebox

# Store passed arguments
# NOTE: sys.argv[0] is the script name
# Expected to recieve a camera object from the master script
if isinstance(sys.argv[1], u3.U3):
    labjack = sys.argv[1] 
else:
    messagebox.showerror("Error", "Argument[1] passed to Labjack_Control was not a u3.U3 object")
    # Close/End processes

# Init Labjack
labjack.getCalibrationData() # Calibration data will be used by functions that convert binary data to voltage/temperature and vice versa
labjack.configIO(FIOAnalog= 255) # Set the FIO to read in analog; 255 sets all eight FIO ports to analog
# labjack.streamConfig(NumChannels= self.num_channels.get(), PChannels=range(self.num_channels.get()), NChannels=[31]*self.num_channels.get(), Resolution=1, ScanFrequency=self.scan_hz.get())
labjack.streamConfig(NumChannels= 8, PChannels=range(8), NChannels=[31]*8, Resolution=1, ScanFrequency=self.scan_hz.get())

# Stream the data
labjack.streamStart()

for r in labjack.streamData():
    if r is not None:
        #new_data_ain0.extend(r['AIN0'])
        pass
    else:
        pass

    # Write the data 

    #Pipe/Send data back to master