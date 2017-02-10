import os

def getDescription():
    return "Update show status"

def execute(data):
    os.system('clear')
    print "%s\n" % getDescription()
    showCount = 0
    for show in data["showIndex"]:
        showCount += 1
        print str(showCount) + ': ' + data["showIndex"][showCount - 1]["Name"] + ', Season ' + str(data["showIndex"][showCount - 1]["Season"]) + ' Episode ' + str(data["showIndex"][showCount - 1]["Episode"])
    selection = int(raw_input('\n'))
    os.system('clear')
    print str(data["showIndex"][selection - 1]["Name"]) + '\n'
    seasonUpdate = raw_input('Season: ')
    data["showIndex"][selection - 1]["Season"] = seasonUpdate
    episodeUpdate = raw_input('Episode: ')
    data["showIndex"][selection - 1]["Episode"] = episodeUpdate
    wait = raw_input('\nUpdate Successful')
    return data
