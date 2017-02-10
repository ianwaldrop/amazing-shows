import os
import json

with open('./ShowsData.json', 'r') as fr:
    sr = fr.read()

data = json.loads(sr)

while True:

    os.system('clear')
    command = raw_input('What would you like to do?\n\n1: List Current Shows\n2: Add New Show\n3: Update Show Status\n4: Search Shows\n5: Quit\n\n')

    if command == '1':
        os.system('clear')
        showCount = 0
        for show in data['showIndex']:
            print data["showIndex"][showCount]["Name"] + ', Season ' + str(data["showIndex"][showCount]["Season"]) + ' Episode ' + str(data["showIndex"][showCount]["Episode"])
            showCount += 1
        wait = raw_input('\n')

    elif command == '2':
        os.system('clear')
        newShow = {}
        data["showIndex"].append(newShow)
        name = raw_input('Name: ')
        newShow["Name"] = name
        season = raw_input('Season: ')
        newShow["Season"] = season
        episode = raw_input('Episode: ')
        newShow["Episode"] = episode

    elif command == '3':
        os.system('clear')
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

    elif command == '4':
        continueWaiting = True
        while continueWaiting:
            os.system('clear')
            query = raw_input()
            shows = list(filter(lambda s: query in s["Name"].lower(), data["showIndex"]))
            for s in shows:
                print s["Name"]
            continueWaiting = raw_input() != '\\'

    elif command == "Test":
        print data["showIndex"]
        wait = raw_input('')

    elif command == '5':
        os.system('clear')
        break

sw = json.dumps(data)

with open('./ShowsData.json', 'w') as fw:
    fw.write(sw)
