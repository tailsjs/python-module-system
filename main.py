import os
import json 
import importlib
import sys

def clear():
    if "debug" not in sys.argv:
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)
if os.path.isdir("./modules") == False:
    print("modules folder not found! creating...")
    os.mkdir("./modules")

modules = os.listdir("modules")
init_modules = []
string_modules = ""
print(f"initializing modules... {len(modules)} modules has been found")
for i in modules:
    try:
        if os.path.isfile(f"./modules/{i}/info.json"): 
            file = open(f"./modules/{i}/info.json")
            module = json.loads(file.read())
            module["dir"] = i
            init_modules.append(module)
            string_modules += f'{len(init_modules)}. {module["name"]} — {module["desc"]} (./modules/{i}/{module["main"]}) [author: {module["author"]}]\n'
            file.close()
            print(f"./modules/{i} successfully init!")
        else:
            print(f"./modules/{i} does not have info.json file. this module will not be initialized")
    except Exception as e:
        print(f"some error with {i} module!")
        print(e)

print(f"modules initialized. {len(init_modules)} success. {len(modules)-len(init_modules)} failed")

def start(somewords=""):
    clear()
    choose = input(
        somewords+"\n"+ 
        "hello. this is cringe modulation system!\n\n" + 
        string_modules +
        "\n0 - Leave\n" + 
        "\n>>> "
        )
    if int(choose) == 0:
        return sys.exit(0)
    if type(int(choose)) is not int or int(choose) < 1 or int(choose) > len(init_modules):
        start("incorrect choice!")
    choosed = init_modules[int(choose)-1]
    module = importlib.import_module("modules." + choosed["dir"] + "." + choosed["main"])
    clear()
    r = module.Import.init()
    start("Module resp: " + str(r))
start()
