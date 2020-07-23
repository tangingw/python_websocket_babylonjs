# Python on Android

## Code structure:

* `orientation_ctrl.py` - the script file that runs on QPython
* `orientation_webapp.py` - the web interface for the script
* `bottle_sms.py` - the web interface for the sms sender - needs to run in QPython

## How to run

* Run `orientation_ctrl.py` on your QPython App
* Change the Websocket IP Address in `orientation_webapp.py`
* `python orientation_webapp.py` on your terminal
* `http://127.0.0.1:5000/babylon_orientation`