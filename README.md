## About 
This is a briefly instruction to run a simple python application on kubernetes in order to hands-on exercises and live implementation.

## What's the purpose?
The main goal is be still learning and hands-on practice. Second one reson is be keep up to date because to master something new you'll have to play with it :) 

## Makefile
Makefile allows you to prepare dev environment and release app based on git tags.

```
$ make
version-next                   Create new version
version-save                   Create and save new version
version                        Show current version
```

### Release
To make a new release and create new version of app:
```
do-release
```
