# !/usr/bin/env python3.10
# This is written freehand by the hands of TheWoodcutter :: Ymail.com
# Copyright 2023 (C) Allan "The Woodcutter" S.
# Copying is inevitable, it is released open source under the [NEED LICENCE]
# No warranty, give a damn and no phone calls or emails answered by my clerk
# if you haven't gotten a proper requisite form from HR office on 3rd floor.
# `git init` coming soon!

#!/usr/bin/env python3.10

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

# for command line parameters at bottom of script:
from getpass import getpass
from argparse import ArgumentParser

import slixmpp
import logging
import shelve
import re
import random
# import plus
import os
import urllib.request
import requests
from bs4 import BeautifulSoup as soup
import mimetypes
#import youtube-dl
#import yt-dlp
# import ipaddress

class MUCBot(slixmpp.ClientXMPP):

    def __init__(self, jid, password, room, nick):
        slixmpp.ClientXMPP.__init__(self, jid, password)

        self.room = room
        self.nick = nick

        self.add_event_handler("session_start", self.start)
        self.add_event_handler("groupchat_message", self.muc_message)

    async def start(self, event):
        await self.get_roster()
        self.send_presence()
        self.plugin['xep_0045'].join_muc(self.room, self.nick)
    
    def muc_message(self, msg):
    # variables for this function
        nicklist = self.plugin['xep_0045'].get_roster(self.room)
        nicklist_string = ' '.join(nicklist)        
        body = msg['body']
        frm = msg['from'].bare
        mt = 'groupchat'
        frmnick = msg['from']
        mucnick = msg['mucnick']
        admins = ["cmdr_coconut","chunk"]
        accepted_domains = ["soundcloud.com","youtube.com","bandcamp.com","m.youtube.com","m.soundcloud.com"]

        for d in accepted_domains:
            if d in body:
                re0 = '((http|https)://)+(' + d + ')/[A-Za-z\=\?0-9\/\%\&\-]*'
                rgx = re.match(re0, body)
                url = rgx[0]
                self.rip_audio(self, url)

    def rip_audio(self, url):
        if not os.system('ls /home/$USER/rips/'):
            os.system('mkdir /home/$USER/rips')
        dir = "/home/$USER/rips"
        os.system('cd /tmp && mkdir rips && cd rips')
        if validators.url(url):
            import time
            ts = time.time()
            inner_command = 'mv {} %(dir)s/%(ts)s.mp3' % { "dir": dir, "ts": ts }
            download_command = "youtube-dl -x --audio-format mp3 --audio-quality 0 --embed-thumbnail --add-metadata --restrict-filenames -i %(url)s -exec %(inner_cormmand)s" % { "url": url, "inner_command": inner_command }
            try:
                os.system(download_command)

    ### now play it on a stream with vlc or mpv ###



# This: enables this module/file to be executed as a script on cli:
if __name__ == '__main__':
	logging.basicConfig(level=DEBUG, format='%(levelname)-8s %(message)s')

    # What other XEP's can we tinker with?
    xmpp = MUCBot("mrbot@toofast.vip", os.system('echo $MRBOTPASSWD'), "partyfolk@chat.toofast.vip", "mrDJ")
    xmpp.register_plugin('xep_0030') # Service Discovery
    xmpp.register_plugin('xep_0045') # Multi-User Chat
    xmpp.register_plugin('xep_0199') # XMPP Ping

    # HTTP Service Discovery?
    # pubsub microblog digests in news muc on tri-hourly rate?
    # Avatar manipulations?  Sqlite3 or text based gzip encrypted db including bin data for avatars w/ mimes

    xmpp.connect()
    xmpp.process()