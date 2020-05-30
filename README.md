# Twitter Scraper
Python script to download tweets from a given Twitter user.
## Dependencies
This script uses [Twint](https://github.com/twintproject/twint). This can be installed from the command line:
```
$ pip3 install twint
```
Advantages of using Twint over the Twitter API:
* able to download all tweets from a user (Twitter API imposes a limit of 3200)
* can be used anonymously without Twitter signup
* no rate limitations
## Installation
Clone this repository:
```
$ git clone https://github.com/erikdyan/twitter_scraper.git
```
## Usage
Run the script from the command line:
```
$ python3 download_tweets.py [-h] [-c] [-i] [-l [LIMIT]] username
```
With no optional flags set, this script will download all available tweets from the specified Twitter user to `<username>.txt`, storing one tweet on each line.
### Optional Flags
* `-c, --csv`: output tweets to a CSV file
* `-i, --include_links`: include tweets containing links
* `-l [LIMIT], --limit [LIMIT]`: maximum number of tweets to retrieve. Default = all
