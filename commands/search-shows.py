import os

def getDescription():
    return "Search shows"

def execute(data):
    os.system('clear')
    print "%s\n" % getDescription()
    continueWaiting = True
    while continueWaiting:
        os.system('clear')
        query = raw_input()
        shows = list(filter(lambda s: query in s["Name"].lower(), data["showIndex"]))
        for s in shows:
            print s["Name"]
        continueWaiting = raw_input() != '\\' # this is broken
