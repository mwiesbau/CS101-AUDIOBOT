# ROBOT Project for CS101 - FALL 2016


## SETUP
1. To use this repository please install the following software first.

  - Python 3.5 `https://www.python.org/downloads/`
  - Docker `https://www.docker.com/`
  - Git `https://git-scm.com/`

2. Now clone this repository into a local directory with the following command
`git clone https://github.com/mwiesbau/CS101-AUDIOBOT.git`

3. Next please go to the directory where the file `requirements.txt` is located and run the following command. `pip install -r requirements.txt`
this will install all the Python dependencies.

4. Now you can run the Tipboard Docker container with the following command, please replace `[local tipboard folder]` in the command below with the path of your local `git clone` directory.
`docker run --rm -ti -v [local tipboard folder]:/root/.tipboard -p 7272:7272 mwiesbau/tipboard:cs101`
 
5. If everything worked, you can now access the tipboard app using the instructions below
  1 If you are using docker on windows with Hyper-V, open the Hyper-V manager and select your PC on the left side. Now you can select the Moby Linux virtual machine. Once selected please select the Networking tab at the bottom to reveal the IP address. https://docs.docker.com/machine/img/hyperv-manager.png

  2 On Windows with Virtual Box, please us the command `docker-machine ip` to get the IP to access tipboard.

  3 On Linux please use `http://172.17.0.2:7272`, if that does not work use `docker inspect [container_name] | grep IP` to get the IP address

6. If you run `python audiobot.py` the Tipboard server should receive the updates from the python script in realtime


## USE

### robot.py
This is the main class and starts the robot control.
Contains the logic needed for the demo.

### motorcontrol.py
This file contains all the movement logic for the robot

### audiocontrol.py
This file controls the audioinput and evaluates the DB level

### publishToTipboard.py
Contains the functions to publish the robot metrics to the Tipboard web interface

### tipboard folder
#### Dockerfile
Contains the docker build script for the Tipboard docker image.

#### layout_config


