import os

def getDescription():
    return "List current shows"

def execute(data):
    os.system('clear')
    print "%s\n" % getDescription()
    showCount = 0
    for show in data['showIndex']:
        print data["showIndex"][showCount]["Name"] + ', Season ' + str(data["showIndex"][showCount]["Season"]) + ' Episode ' + str(data["showIndex"][showCount]["Episode"])
        showCount += 1
    wait = raw_input('\n')
    return data
