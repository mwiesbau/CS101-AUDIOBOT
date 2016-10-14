*ROBOT Project for CS101 - FALL 2016*

1. To use this repository please install the following software first.

  - Python 3.5 `https://www.python.org/downloads/`
  - Docker `https://www.docker.com/`
  - Git `https://git-scm.com/`

2. Now clone this repository into a local directory with the following command
`git clone https://github.com/mwiesbau/CS101-AUDIOBOT.git`

3. Next please go to the directory where the file `requirements.txt` is located and run the following command. `pip install -r requirements.txt`
this will install all the Python dependencies.

4. Now you can run the Tipboard Docker container with the following command, please replace `[local tipboard folder]` in the command below with the path of your local `git clone` directory.
`docker run --rm -d -ti -v [local tipboard folder]:/root/.tipboard -p 7272:727 mwiesbau/tipboard:cs101`
 
5. If everything worked, you can now access the tipboard app using the following link `http://172.16.0.2:7272`

6. If you run `python audiobot.py` the Tipboard server should receive the updates from the python script in realtime




