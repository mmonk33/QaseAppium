# QaseAppium

### Pytest integration with Qase via API: run test plan, list of cases, run functions specified in case steps 

## Test preparation
1. Create cases in Qase.io  
2. Create a test plan and add your cases to it

## Preparing a Job in Jenkins
```bash
export CODE=${CODE}; export PLAN_ID=${PLAN_ID}; pytest Test.py
```
![изображение](https://user-images.githubusercontent.com/102417439/186091913-c7a0a90c-f5af-483f-b444-aeb3ddd26dd1.png)

## How to write test case steps in Qase.io
![image](https://user-images.githubusercontent.com/102417439/187589956-ddf1923c-8e2a-4549-aca2-5707db473714.png)
![image](https://user-images.githubusercontent.com/102417439/187590112-fe76a749-4ff7-43df-a550-f74fb5bddf2b.png)
![image](https://user-images.githubusercontent.com/102417439/187590202-824086e3-a106-4b47-9726-21289ea97915.png)


Action          | Input data           | Function Description
----------------|----------------------|-----------------------
Start           | Package Activity     | Launches the application with the activity specified in the input data 
Click           | Locator              | Finds the element with the specified locator and clicks on it
Wait            | Seconds              | Wait with the specified number of seconds


## Actions for STB
Action          | Function Description     
----------------|----------------------
Press ok        | Simulate pressing the OK button on the remote control    
Press down      | Simulate pressing the DOWN button on the remote control             
Press up        | Simulate pressing the UP button on the remote control            
Press right     | Simulate pressing the RIGHT button on the remote control             
Press left      | Simulate pressing the LEFT button on the remote control             
Press home      | Simulate pressing the HOME button on the remote control          
Press back      | Simulate pressing the BACK button on the remote control
 
## Adding features

The functions called through the steps in the case are described in Funcs.oy:
```Python
functions = {
    'Press down': Remote.down,
    'Press up': Remote.up,
    'Press left': Remote.left,
    'Press right': Remote.right,
    'Press ok': Remote.ok,
    'Press home': Remote.home,
    'Press back': Remote.back,
    'Press settings': Remote.settings,
    'Package installed': ADB.package_installed,
    'Click': click,
    'Start': start_activity,
    'Screenshot': Allure.screenshot,
    'Wait': wait
```
