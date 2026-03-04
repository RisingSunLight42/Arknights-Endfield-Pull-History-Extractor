# Arknights Endfield Pull History Extractor

> This repository is not affiliated with Hypergryph or Gryphline. All trademarks are property of their respective owners.

**Arknights Endfield Pull History Extractor** is a python script extracting your pull history in a CSV (one per banner category). 

This script DOESN'T store your auth token for the gacha history anywhere outside of your computer.  
Don't use it if you do not understand it at least partially and don't hesitate to contact peers on different social media that are better informed on the matter to fact check the script if you have any doubts.  
*If anyway, if you have doubts about it, don't use it. I'm a stranger and hence, cannot be trusted.*

> The script will be commented in the near future to allow understandability for most of the people to ensure everyone know what is running on their computer.  

> The only internet requests made by the script are to the webview link for the pull history.

## Installation

I'll assume you have some basic understandings of programming, in case you have not, don't hesitate to reach to me on the Arknights: Endfield Discord (`@risingsunlight`). It will help me improve the section bellow to help people use the script.

1. [Install python 1.12 (or above)](https://www.python.org/downloads/) if not already install on your computer
2. Open a command promt (can be Powershell or whatever works on your OS)
3. Do `git clone https://github.com/RisingSunLight42/Arknights-Endfield-Pull-History-Extractor`. This will create a new folder.
4. Go in said folder
5. Do `python -m venv .venv`. This creates a "virtual" environment to avoid messing up with any of your python configuration
6. Do `.\.venv\Scripts\activate` to ensure your virtual environment is activated (if you want to check if you're in the virtual environment, run `pip -V`, it will show the path to your current environment, if .venv appears in it, all good!)
7. Do `pip install -r requirements.txt`. This will install the required libraries to run the script
8. Check Usage section

## Usage

> NEVER share your token to anyone.  

> If you cannot find any webportal url, that means you've never checked your pull history in game. To do so, open the headhunting panel and click on the "details button".

1. To use the script, you need to create a `.env` file based on the `.env.template` file available in the repository.  
2. The only required element is your token that can be found in `{YOUR_USER}\AppData\LocalLow\Gryphline\Endfield\sdklogs` in the file HGWebview.txt on Windows.   
3. Search the keyword "gacha_char", you'll find something like `WebPortal url: [url]`. The token is in the URL, copy the token and put it in the .env file like that: `TOKEN="YOUR_TOKEN"`.
4. Once done, you can run `python ./pull_history_extractor.py`.
5. Follow the instructions prompted
6. Wait
7. If everything has worked properly, you'll get one or multiple CSV files

## Additionnal informations

This script is still a work in progress. Any contribution is welcomed and any question too. 
