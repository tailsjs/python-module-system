# Python LocalModule System
Cringe, but works.

## So, what's the point?
* idk

## Module example
Every module must have *.py file and info.json<br>
Also, modules must be in folder "modules" and have their folders (./modules/test/)<br>
* info.json
```json
{
    "name": "Test!", // Module name
    "mainFile": "test", // Module file (without .py)
    "mainClass": "Import", // class to be imported.
    "mainFunction": "init", // function to be executed from the "Import" class
    "author": "tailsjs", // Module author
    "desc": "Test module." // Module description
}
```
* test.py
```py
class Import: # the class to be used in the program.
    def init(): # main func (need to be synced with info.json)
        return "Hello world!"

class SomeClassLol: # this class will not be used in the program. only in the module.
    def help():
        return "real"
```

## Need to install:
 * importlib