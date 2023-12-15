# Gamefinder
Introducing an Ebay developer application specifically tuned to monitor listings of gaming products.  Give it a try, monitoring the API gives you a heads up over watching the main website!

![Gamefinder Screenshot](https://raw.githubusercontent.com/bekindpleaserewind/gamefinder/main/screenshot.png)

## Registration
The very first thing you need to do is register for API access on the Ebay Developer Program at https://developer.ebay.com.  Ebay will take around one complete business day to turn around the registration and approve it.  Once this step is done you can continue to the Access Keys section below.

## Access Keys
In order to access the Ebay API, you will need a set of four different production credentials.  This includes the App ID, Dev ID, Cert ID, and Token.  It is extremely important you keep this information from public eyes, as it is your way into the Ebay environment.

Visit https://developer.ebay.com/api-docs/static/gs_create-the-ebay-api-keysets.html to continue creating Ebay Developer Program production keys for API access use with your Gamefinder installation.

## Usage
Both a native Windows 11 executable is available at https://github.com/bekindpleaserewind/gamefinder/releases as is the complete source code under the GPLv3 license.

### Binary (Windows 11)
If you are on windows, just execute the Windows 11 executable and you should be good to go.

### Source (Mac)
Mac currently supports running from source using python3.  The only pre-reqs that I am aware of is the following:

1. Install python3 using ```brew install python3```.
2. Install virtualenv with ```pip3 install virtualenv```.
3. Create the virtual environment: ```virtualenv -p python3 </path/to/store/venv>```.
4. Enter the virtual python3 environment: ```source /path/to/store/venv/bin/activate```.
5. Install the pip modules by running ```pip install -r pip.txt```. I recommend doing this is a venv dedicated to Gamefinder.
6. Ensure that the alerts/icons directories are in the same location as the source code (it is auto resolved in path.py).
7. Execute ```python3 gamefinder.py```.

### Source
General source build instructions.

1. Install the pip modules by running ```pip install -r pip.txt```. I recommend doing this is a python virtual environment dedicated to Gamefinder (see Mac source steps above).
2. Ensure that the alerts/icons directories are in the same location as the source code (it is auto resolved in path.py).
3. Execute ```python gamefinder.py```.

## Support
If you're feeling supportive today, you can buy me a cup of coffee at https://www.buymeacoffee.com/bekindpleaserewind

I'd really appreciate it!

Thanks and don't hesitate to reach out for any questions, comments, etc.