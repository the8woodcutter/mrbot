# !/usr/bin/env python3.10

# Created by The8Woodcutter with help from the slixmpp documentation.
# Inherits whatever Licence that slixmpp has.  For questions/comments/concerns
# email chunk@toofast.vip

# Chatbot is python project for The8Woodcutter to better learn how to program
# chatbots as well as python in general.  This is a personal project however
# fork or do what you wish with respects to the licence.
# # -- March 19 2023 - Project Start Date -- # #

# README:
# To start the bot, in your virtualenv use `python3.10 main.py -d -j $JID -n $NICKNAME -r $ROOM -p $PASSWD`
# Or optionally just `python3.10 main.py -d` to input your information (as above) on commandline with debug 
# logging.

from getpass import getpass
from argparse import ArgumentParser
import logging
import slixmpp
import shelve
import os
import re
import sys
import random
import requests
import ipaddress

class party_bot(slixmpp.ClientXMPP):

# Global Variables can go up here for this class
# Global variables can also be imported@
        # Todo:
            # gather all these variables and reuse them
            # See: section A1 below

    def __init__(self, jid, password, room, nick):
    # instantiate: `slixmpp.ClientXMPP`
        slixmpp.ClientXMPP.__init__(self, jid, password)
        self.room = room
        self.nick = nick
    # Learn more about `add_event_handler` !!!!
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("groupchat_message", self.muc_message)

# This sets an XMPP stream to persist to the `self.room`:
    async def start(self, event):
        await self.get_roster()
        self.send_presence()
        self.plugin['xep_0045'].join_muc(self.room, self.nick)
    
# Here we act on the "groupchat_message" event handler, this whole function is iterated over ...
# ... every new message event fired.  Inner functions and returns should be done from other functions:
    def muc_message(self, msg):
    # section A1
        nicklist = self.plugin['xep_0045'].get_roster(self.room)
        nicklist_string = ' '.join(nicklist)        
        body = msg['body']
        frm = msg['from'].bare
        mt = 'groupchat'
        mucnick = msg['mucnick']
        admins = ["cmdr_coconut","chunk"]
    # end section A1

# THE DIRECTIONS FOR THE REST OF THIS CLASS:

        # Now we will first: regex: find URLs
        # Second: strip URLs to domain portion
        # Third: run os.system(DNS_COMMANDS) to verify against a list of source platforms.
            # namely soundcloud and youtube and bandcamp if we can
            # special care will need to go into the more in depth soundcloud, with their API
        # Four: Reference another function @self to download the URL to /mnt/toofast.vip/jukebox as HQ
        # .. with the video stripped, the meta data, etc ....
        # LOOK FOR NCURSES APPLICATIONS FOR MANAGING PLAYING AND STREAMING AUDIO ie: MPV, CVLC
        # JWPlayer might be sufficient on an HTML5 page

if __name__ == '__main__': 
    xmpp.connect()
    xmpp.process()     ### Is this asyncio or stream??? ::