# Gamefinder
Introducing an Ebay developer application specifically tuned to monitor listings of gaming products.  Give it a try, monitoring the API gives you a heads up over watching the main website!

## Registration
The very first thing you need to do is register for API access on the Ebay Developer Program at https://developer.ebay.com.  Ebay will take around one complete business day to turn around the registration and approve it.  Once this step is done you can continue to the Access Keys section below.

## Access Keys
In order to access the Ebay API, you will need a set of four different production credentials.  This includes the App ID, Dev ID, Cert ID, and Token.  It is extremely important you keep this information from public eyes, as it is your way into the Ebay environment.

Visit https://developer.ebay.com/api-docs/static/gs_create-the-ebay-api-keysets.html to continue creating Ebay Developer Program production keys for API access use with your Gamefinder installation.

## Usage
Both a native Windows 11 executable is available at https://github.com/bekindpleaserewind/gamefinder/releases as is the complete source code under the GPLv3 license.

### Binary (Windows 11)
If you are on windows, just execute the Windows 11 executable and you should be good to go.

### Source
If you're running through source, you need to go through the following steps:

1. Install the pip modules by running ```pip install -r pip.txt```. I recommend doing this is a venv dedicated to Gamefinder.
2. Ensure that the alerts/icons directories are in the same location as the source code (it is auto resolved in path.py).
3. Execute ```python gamefinder.py```.

## Support
If you're feeling supportive today, you can buy me a cup of coffee at https://www.buymeacoffee.com/bekindpleaserewind

I'd really appreciate it!

Thanks and don't hesitate to reach out for any questions, comments, etc.