import os
import pkgutil
import importlib
import json

with open('./ShowsData.json', 'r') as fr:
    data = json.loads(fr.read())

commands = map(lambda n: importlib.import_module("commands.%s" % n), [name for _, name, _ in pkgutil.iter_modules(['commands'])])

prompt = 'Select an option:\n'
for idx, command in enumerate(commands):
    prompt += ('%s. ' % (idx + 1)) + command.getDescription() + '\n'
prompt += '\n'

while True:
    os.system('clear')
    selection = raw_input(prompt)
    try:
        index = int(selection) - 1
        if index <= len(commands):
            data = commands[index].execute(data)
    except ValueError:
        if command == "Test":
            print data["showIndex"]
            wait = raw_input('')
        else:
            os.system('clear')
            break

with open('./ShowsData.json', 'w') as fw:
    fw.write(json.dumps(data))
