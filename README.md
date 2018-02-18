# SpeedLog
Simple script to run internet speed tests using speedtest.net and store the results in an sqlite3 database

## Install

1. Clone this repo, `git clone https://github.com/Arwic/SpeedLog`
2. Install requirements, `pip install -r requirements.txt`
3. Create task to run `speedlog.py` as often as you like. You can use the `run_in_background.vbs` script to run the script without a command line popping up in the foreground. (Google "Task Scheduler" for windows, or "cron" for linux)

## Graphing your results

1. Run `python3 speedgraph.py`
