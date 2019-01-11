How To Use:

STEP 1 (Installing Python):
  Install Anaconda Python 3.7 Version

  https://www.anaconda.com/download/

  When prompted during the install to check two boxes to add 
  Anaconda to the PATH variable and to make Anaconda the default
  Python installation, make sure both of those boxes are checked. 

STEP 2 (Installing the ChromeDriver):
  Once Anaconda is installed find your Anaconda3 folder. It should
  be located at C:\Users\<Your Username>\Anaconda3 if you chose the 
  default install location.

  From this folder drag the chromedriver.exe file into that folder.

  Also if you don't for some reason have chrome installed, install 
  google chrome.

  https://www.google.com/chrome/

STEP 3 (Setting Up the Viewbot Settings):
  This part might be a litte tricky. Figure out what search on YouTube
  brings your video up as the first option. Make note of that exact
  search.

  You are going to go into the config.txt file then and edit the 
  parameters how you want them.

  search_string: This is the search that gets your video as the number
                 one result

  min_watch: This is the minimum amount of time in seconds that the bot 
             could spend watching the video

  max_watch: This is the maximum amount of time in seconds that the bot 
             could spend watching the video

  wait_after: This is the amount of time in seconds that the bot 
              will wait to watch the video again. If you don't want
              to wait between views, you can make this value None.

  views: This is the amount of views that you want the bot to attempt 
         to gain.

  multicore: If you don't want to use your computer for anything else
             besides running the bot, set this to True. If this is True
             it will utilze most of your CPU cores to view the video

  
STEP 4 (Running the Bot):
  First take note of the location of the folder that you extracted.
  Then start up a command prompt. Look at the full path that the folder
  is in. I.e. C:\Users\<Your Username>\Desktop\Youtube-View-Bot.
  From the command prompt navigate to this folder.

  I.e. if you command prompt says C:\Users\<Your Username> >, then
  you want to type in 'cd Desktop\Youtube-View-Bot' followed by enter.

  Once your command prompt is in the Youtube-View-Bot folder you want
  to type in 'pip install -r requirements.txt' followed by enter. You
  only need to run this step the very first time.

  Once that command is complete you'll want to type in 'python viewbot.py'
  followed by enter.

 