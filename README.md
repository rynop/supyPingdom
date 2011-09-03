supyPingdom
=====================
This is a [Pingdom](http://pingdom.com) IRC plugin for supybot

Version 0.01

Currently, the library supports:

* list check(s)

Requirements
--------------------
- Pingdom account
- [pingdom-python](https://github.com/EA2D/pingdom-python)
- simplejson (Python 2.5 and earlier)


Installation
--------------------
* clone, copy plugins/Pingdom dir to your bot's plugin directory
* modify Pingdom/config.py and put in your api-key, username and password
* load the plugin in your bot
* run Pingdom getcheck or Pingdom getcheck "my check name" 
* replies will always be private messages


Note: This is my 1st supybot plugin AND I'm a total python noob, so any suggestions/fixes are appreciated