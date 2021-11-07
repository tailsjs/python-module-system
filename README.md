# Python LocalModule System
Cringe, but works.

## So, what's the point?
* idk

## Module example
Every module must have *.py file and info.json<br>
Also, modules must be in folder "modules" and have their folders (./modules/test/)
* info.json
```json
{
    "name": "Test!",
    "main": "test",
    "author": "tailsjs",
    "desc": "Test module."
}
```
* test.py
```py
class Import: # modules must be in class Import
    def init(): # main func
        return "Hello world!"
```

## Need imports:
* os
* json
* importlib
* sys