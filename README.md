# Warlock Discord Bot
A bot for use within Khopper Dice's Discord

## Commands
w.roll xdy
: for x and y as positive integers, "rolls" x number of y-sided dice. Ex w.roll 3d6 generates three random numbers between 1 and 6

w.greet
: returns "Hi {user}"

## Local Build
- Currently requires python3 and a connection to GCP for secret management and logging
- Install required packages
```pip install -r requirements.txt```
- Set up to be built into docker image and pushed to GCP Artifact Repo, and run on a Compute Engine instance