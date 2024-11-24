# !/usr/bin/env python3.10
# Created by [The8Woodcutter] with help from the [https://slixmpp.readthedocs.io] documentation.
# # -- [March 19 2023 - Project Start Date] -- # #
# README:
    # To start the bot, in your virtualenv use `python3.10 main.py -d -j $JID -n $NICKNAME -r $ROOM -p $PASSWD`
    # Or optionally just `python3.10 main.py -d` to input your information (as above) on commandline with debug 
    # logging (-d_)...  I use an alias to set my venv and another alias that includes -j for bot JID and -n for NICK...

# =====================================================================================================================================================
# =====================================================================================================================================================
# =====================================================================================================================================================

from getpass import getpass
from argparse import ArgumentParser
from ipaddress import ip_address

import slixmpp
import logging
import shelve
import random
import re
import os
import sys
import ipaddress
import socket
import urllib3

# =====================================================================================================================================================
# =====================================================================================================================================================
# =====================================================================================================================================================
# =====================================================================================================================================================

class mrBot(slixmpp.ClientXMPP):

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

# =====================================================================================================================================================
# =====================================================================================================================================================
# =====================================================================================================================================================
# =====================================================================================================================================================

    def muc_message(self, msg):
# =====================================================================================================================
# variables for this function
        nicklist = self.plugin['xep_0045'].get_roster(self.room)
        nicklist_string = ' '.join(nicklist)        
        body = msg['body']
        frm = msg['from'].bare
        mt = 'groupchat'
        mucnick = msg['mucnick']
        admins = ["cmdr_coconut","chunk"]

    # attack function:
        arfs = [
            "arF ARf ARF ARFFRFUF RFUFUFFUFUFUFFUFFUFU!@!@!!!@@@!!!!",
            "ARFARFARFARFARFARFARFUFUARFARFUFARFUFARFUFRUFF!!!!",
            f"Arf?  *starts to chew on {mucnick}'s pants*",
            "o_o",
            "Grrrrrrrr ..",
            "ArF ArF ARF ARFFF ARRFRUFRF !!!",
            "fruuffuufufuufuarfufaruffrarufrufrufffARf @_@",
        ]
        arf = random.choice(arfs)

# =====================================================================================================================
# Python Shelve settings:
        db = shelve.open('muc_message.db')

        if db.get('i') == 0 or db.get('i') == 1:
            i = db.get('i')
        else:
            db['i'] = 0
            i = db.get('i')

        if db.get('victims'):
            victims = db.get('victims')
        else:
            db['victims'] = []
            victims = db['victims']

        if db.get('friends'):
            friends = db.get('friends')
        else:
            db['friends'] = []
            friends = db['friends']

        if db.get('pluses'):
            pluses = db['pluses']
        else:
            db['pluses'] = {}
            pluses = db['pluses']

        if db.get(f'muclog.{self.room}'):
            muclog = db[f'muclog.{self.room}']
        else:
            db[f'muclog.{self.room}'] = []
            muclog = db[f'muclog.{self.room}']

        if db.get('mofos'):
            mofos = db['mofos']
        else:
            db['mofos'] = 7
            mofos = db['mofos']

        if db.get('txt'):
            txt = db.get('txt')
        else:
            db['txt'] = ""
            txt = db.get('txt')

# =====================================================================================================================
# test db:
    # read db first level:
        def test_first_db(self):
            message = []
            for each in db:
                thisdb = db.get(each)
                message.append(f"Name: {each}, Type: {type(thisdb)}\r\n")
            message = "".join(message)
            return message

        def test_second_db(self, dbthing):
            for each in db:
                if each == dbthing:
                    iam = db.get(each)
                    newmessage = []
                    for ech in iam:
                        newmessage.append(f"{ech}\r\n")
                    newnewmessage = "".join(newmessage)
                    message = f"Name: '{each}'\r\n" + newnewmessage + "\r\n"
                    return message
                    # if isinstance(each, __builtins__.list):
                        # iam = db.get(each)
                        # newmessage = []
                        # for ech in iam:
                        #     newmessage.append(f"{ech}\r\n")
                        # newmessage = "".join(message)
                        # newmessage = "Name:\r\n" + message + "\r\n"
                    # elif isinstance(each, __builtins__.dict):
                    #     newmessage = "\r\nWe're not handling dict() yet\r\n"
                    # elif isinstance(each, __builtins__.str) or isinstance(each, __builtins__.int):
                    #     iam = db.get(each)
                    #     newmessage = f"Name: {each}\r\n{iam}\r\n"
                    # message.append(newmessage)
                # return message

    # return functions:
        if "testdb1" == body and mucnick in admins:
            while True:
                self.send_message(mto=frm, mbody=test_first_db(self), mtype=mt)
                break
        for each in db:
            if body == f"testdb2 {each}" and mucnick in admins:
                while True:
                    self.send_message(mto=frm, mbody=test_second_db(self, each), mtype=mt)
                    break

# =====================================================================================================================
# functions in the functions:
    def w_msg(self, msgbody, admin=False):
        s_msg = str(msgbody)
        if admin:
            a = True
        else:
            a = False
        while True:
            if not a:
                if mucnick != self.nick:
                    self.send_message(mto=frm, mbody=s_msg, mtype=mt)
            elif a:
                if mucnick != self.nick and mucnick in admins:
                    self.send_message(mto=frm, mbody=s_msg, mtype=mt)
            break

    def t_admin_msg(self, msgbody, admin=True):
        s1_msg = "is mofo a admin: \r\n"
        s2_msg = "yes" if mucnick in admins else "no"
        s_msg = s1_msg + s2_msg

# =====================================================================================================================
# muclog function:



    # # saving logs:
    #     if len(muclog) < 20:
    #         entry = f"{mucnick}: " + body
    #         muclog.append(entry.encode("utf_8","ignore").decode("utf_8","ignore"))
    #         db[f'muclog.{self.room}'] = muclog
    #     elif len(muclog) == 20:
    #         del muclog[0]
    #         entry = f"{mucnick}: " + body
    #         muclog.append(entry.encode("utf_8","ignore").decode("utf_8","ignore"))
    #         db[f'muclog.{self.room}'] = muclog
    #     else:
    #         muclog = []
    #         muclog = muclog.append(str(f"{mucnick}: " + body).encode("utf_8","ignore").decode("utf_8","ignore"))
    #         db[f'muclog.{self.room}'] = muclog

    # # testing muclog:
    #     if "testlog" == body and mucnick in admins:
    #         for x in muclog:
    #             message = f'> {x}'
    #             n = 1
    #             while n > 0:
    #                 self.send_message(mto=frm, mbody=message, mtype=mt)
    #                 n = 0
    #                 break

    #     if "testlograw" == body and mucnick in admins:
    #         while True:
    #             self.send_message(mto=frm, mbody=f"{muclog}", mtype=mt)
    #             break

    # # testing muc room:
    #     if "testroom" == body and mucnick in admins:
    #             message = self.room
    #             while True:
    #                 self.send_message(mto=frm, mbody=f"{message}", mtype=mt)
    #                 break

    # # delete muclog:
    #     if "dellog" == body and mucnick in admins:
    #         db[f'muclog.{self.room}'] = []

# =====================================================================================================================
# quote grab function:
    # Like: `Grab {frm}`
    # Like: `Grab {frm} 2`
        


        # def grab(self):
        #     for n in nicklist:
        #         if body == f"Grab {n}":
        #             matches = []
        #             for line in muclog:
        #                 if f"{n}: " in line and ">" not in line:
        #                     matches.append(line)
        #             if matches[0]:
        #                 pre = len(n) + 2
        #                 quote = matches[-1:][pre:]
        #                 quote = list(quote)
        #                 if db.get(f"grabbed.{n}"):
        #                     dbquote = db.get(f"grabbed.{n}")
        #                     dbquote.append(quote)
        #                     db[f"grabbed.{n}"] = dbquote
        #                     while True:
        #                         self.send_message(mto=frm, mbody="Quote Saved!", mtype=mt)
        #                         break
        #                 else:
        #                     db[f"grabbed.{n}"] = []
        #                     dbquote = db.get(f"grabbed.{n}")
        #                     dbquote.append(quote)
        #                     db[f"grabbed.{n}"] = dbquote
        #                     while True:
        #                         self.send_message(mto=frm, mbody="Quote Saved!", mtype=mt)
        #                         break

        #         if body == f"Grab {n} 2":
        #             matches = []
        #             for line in muclog:
        #                 if f"{n}: " in line and ">" not in line:
        #                     matches.append(line)
        #             if matches[1]:
        #                 pre = len(n) + 2
        #                 matches = matches[-2:]
        #                 quotes = []
        #                 for match in matches:
        #                     match = match[pre:]
        #                     quotes.append(match)
        #             if quotes[1]:
        #                 if db.get(f"grabbed.{n}"):
        #                     dbquote = db.get(f"grabbed.{n}")
        #                     dbquote.append(quotes)
        #                     db[f"grabbed.{n}"] = dbquote
        #                 else:
        #                     db[f"grabbed.{n}"] = []
        #                     dbquote = db.get(f"grabbed.{n}")
        #                     dbquote.append(quotes)
        #                     db[f"grabbed.{n}"] = dbquote
        #                     while True:
        #                         self.send_message(mto=frm, mbody="Quotes Added!", mtype=mt)
        #                         break

        #         if body == f"Grab {n} 3":
        #             matches = []
        #             for line in muclog:
        #                 if f"{n}: " in line and ">" not in line:
        #                     matches.append(line)
        #             if matches[2]:
        #                 pre = len(n) + 2
        #                 matches = matches[-3:]
        #                 quotes = []
        #                 for match in matches:
        #                     match = match[pre:]
        #                     quotes.append(match)
        #             if quotes[2]:
        #                 if db.get(f"grabbed.{n}"):
        #                     dbquote = db.get(f"grabbed.{n}")
        #                     dbquote.append(quotes)
        #                     db[f"grabbed.{n}"] = dbquote
        #                 else:
        #                     db[f"grabbed.{n}"] = []
        #                     dbquote = db.get(f"grabbed.{n}")
        #                     dbquote.append(quotes)
        #                     db[f"grabbed.{n}"] = dbquote
        #                     while True:
        #                         self.send_message(mto=frm, mbody="Quotes Added!", mtype=mt)
        #                         break
                
    # testing:
        # actually run the grab function:
        # grab(self)

        # test what the shelve took from grab()



        # def test_grab(self):
        #     try:
        #         dbquote = db.get(f"grabbed.{mucnick}")
        #         message = str(dbquote)
        #         while True:
        #             self.send_message(mto=frm, mbody=message, mtype=mt)
        #             break
        #     except:
        #         while True:
        #             self.send_message(mto=frm, mbody="We are a nope houston", mtype=mt)
        #             break

        # def test_grab_chunk(self):
        #     try:
        #         dbquote = db.get(f"grabbed.chunk")
        #         message = str(dbquote)
        #         while True:
        #             self.send_message(mto=frm, mbody=message, mtype=mt)
        #             break
        #     except:
        #         while True:
        #             self.send_message(mto=frm, mbody="We are a nope houston", mtype=mt)
        #             break

        # if body == "testgrab" and mucnick in admins:
        #     test_grab(self)
        # elif body == "testgrabchunk" and mucnick in admins:
        #     test_grab_chunk(self)

        # grab(self)




# =====================================================================================================================
# friends function:
    # NOTES: later on we can use this function to start on a social credit score where certain activities by nicks in muc can grow or shrink their friendship with mrBot...
    # ...and they'll maintain a score for certain terms in a message sent with certain phrases to match mrBot mentions.  The responses throughout this script should vary...
    # ...based on their existing score, if any...
        # for x in nicklist:
        #     hint = f"mrBot {x} is a friend"
        #     cf = "clrfriends"
        #     if body == hint:
        #         friends.append(x)
        #         db['friends'] = friends
        #         while True:
        #             self.send_message(mto=frm, mbody=f"Okay {x} is ma buddey :P", mtype=mt)
        #             break
        #         for v in victims:
        #             if v == x:
        #                 victims.remove(v)
        #                 db['victims'] = victims
        #     elif cf == body and mucnick in admins:
        #         friends = []
        #         db['friends'] = friends
        #         while True:
        #             self.send_message(mto=frm, mbody="No more friends ...", mtype=mt)
        #             break

        # try:
        #     if db.get('friends'):
        #         for x in friends:
        #             if mucnick == x and self.nick in body:
        #                 while True:
        #                     self.send_message(mto=frm, mbody=f"Arff {x}! :D", mtype=mt)
        #                     break

        #         for x in friends:
        #             lst = ["pats mrBot","pats mrbot","pets mrBot","pets mrbot","hugs mrBot","hugs mrBot"]
        #             for i in lst:
        #                 if i in body and x == mucnick:
        #                     while True:
        #                         self.send_message(mto=frm, mbody=f"lllluulzlz..,,.,.  :D", mtype=mt)
        #                         break
        # except:
        #     pass

# =====================================================================================================================
# mrBot ATTACK function:
    # setting the trigger:

    # set to NOT Attack:
        if "mrBot Whoa Boy!" == body and mucnick != self.nick:
            db['i'] = 0
            i = db.get('i')
            msgbody = f"/me Stares blankly at {mucnick}"
            w_msg(self, msgbody)
            # self.send_message(mto=frm, mbody=f"/me Stares blankly at {mucnick}", mtype=mt)

        for x in nicklist:
            hint = f"mrBot Free {x}!"
            if hint == body and x != self.nick:
                victims.remove(x)
                db['victims'] = victims
                victims = db['victims']
                msgbody = "/me runs over to the other side of the yard as if chasing a tennis ball that never was ... .."
                w_msg(self, msgbody)
                # self.send_message(mto=frm, mbody="/me runs over to the other side of the yard as if chasing a tennis ball that never was ... ..", mtype=mt)

    # set TO ATTACK!
        if "mrBot Attack!" == body and mucnick in admins and mucnick != self.nick:
            db['i'] = 1
            i = db.get('i')
            msgbody = "Set to ATTACK >:]"
            w_msg(self, msgbody)
            # self.send_message(mto=frm, mbody="Set to ATTACK >:]", mtype=mt)

        for x in nicklist:
            hint = f"mrBot Attack {x}!"
            if hint == body and x != self.nick:
                victims.append(x)
                db['victims'] = victims
                victims = db['victims']
                msgbody = f"{x} grrrrrr!"
                w_msg(self, msgbody, admin=True)
                # self.send_message(mto=frm, mbody=f"{x} grrrrrr", mtype=mt)

    # TESTING Attack Status:
        if "Test The Attack!" == body:
            if i == 0:
                msgbody = f"Parameter: {i}: No Attack."
                w_msg(self, msgbody)
                # self.send_message(mto=frm, mbody=f"Parameter:{i}: No Attack.", mtype=mt)
            if i == 1:
                msgbody = f"Parameter:{i}: ATTACK!!"
                w_msg(self, msgbody)
                # self.send_message(mto=frm, mbody=f"Parameter:{i}: ATTACK!!", mtype=mt)

        if "mrBot's Victims" == body:
            msgbody = f"I will chew on: {victims}"
            w_msg(self, msgbody)
            # self.send_message(mto=frm, mbody=f"I will chew on: {victims}", mtype=mt)

    # if the trigger is 1 then Attack:
        if i == 1 and mucnick in victims:
            msgbody = f"{mucnick}: {arf}"
            w_msg(self, msgbody)
            # self.send_message(mto=frm, mbody=f"{mucnick}: {arf}", mtype=mt)

# =====================================================================================================================
# Other responses:

        if "Oi" in body or "oi" in body:
            ois = re.findall(r'Oi', body)
            if ois[0]:
                semd = []
                for x in ois:
                    semd.append("oi")
                semd = " ".join(semd)
                msgbody = semd + " !!!"
                w_msg(self, msgbody)
                # self.send_message(mto=frm, mbody=semd, mtype=mt)
        if "Yay" == body or "yay" == body:
            msgbody = "YAY!"
            w_msg(self, msgbody)
            # self.send_message(mto=frm, mbody="YAY!", mtype=mt)

        greetings = ["hello mrBot","Hello mrBot","Hi mrBot","hi mrBot","pats mrBot"]
        for x in range(1):
            for x in greetings:
                if x in body:
                    msgbody = f"{mucnick}: Arffruf! :P"
                    w_msg(self, msgbody)
                    # self.send_message(mto=frm, mbody=f"{mucnick}: Arf :P", mtype=mt)
                    break

        if "test" == body:
            msgbody = "Test Success!"
            w_msg(self, msgbody)
            # self.send_message(mto=frm, mbody="Test Success!", mtype=mt)

        if "nicklist" == body:
            msgbody = "Hi: " + nicklist_string
            w_msg(self, msgbody, admin=True)
            # self.send_message(mto=frm, mbody=nicklist_string, mtype=mt)

# =====================================================================================================================
# chunk was here function:
        def chunk_was_here(self):
            self.send_message(mto=frm, mbody="chunk wuz here", mtype=mt)

        if "mofo" in body:
            if mofos <= 1:
                db['mofos'] = 12
                mofs = db['mofos']
                chunk_was_here(self)
            else:
                db['mofos'] -= 1
                mofos = db['mofos']

        if "Chunk is how many mofos?" == body:
            msgbody = f"Now breaching x{mofos}"
            w_msg(self, msgbody, admin=True)
            # self.send_message(mto=frm, mbody=f"{mofos}", mtype=mt)


# =====================================================================================================================
# yell function:
        rgx = re.match(r'[A-Z0-9\ \,\!\.\?\:]{22,}', body) 
        rnd = random.randint(1,7)
        if rgx:
            if rnd == 2 or rnd == 3 or rnd == 5:
                rgx = rgx[0]
                l = len(rgx)
                r = random.randint(9,33)
                a = l + r
                a = ("A" * a) + ("!" * r)
                msgbody = str(a)
                w_msg(self, msgbody)
                # self.send_message(mto=frm, mbody=a, mtype=mt)

# =====================================================================================================================
# dice function:
        def dice(count):
            dice = ["⚀","⚁","⚂","⚃","⚄","⚅"]
            if isinstance(count, __builtins__.str):
                while True:
                    self.send_message(mto=frm, mbody="Arf??", mtype=mt)
                    break
            elif isinstance(count, __builtins__.int):
                if count > 0 and count <= 100:
                    dices = []
                    while count > 0:
                        r = random.randint(1,6)
                        r -= 1
                        dices.append(dice[r])
                        count -= 1
                    dices = " ".join(dices)
                    while True:
                        self.send_message(mto=frm, mbody=f"{dices}", mtype=mt)
                        break
                elif count < 0:
                    while True:
                        self.send_message(mto=frm, mbody="What are you going to do, roll invisible dice?!", mtype=mt)
                        break
                elif count > 100:
                    while True:
                        self.send_message(mto=frm, mbody="More than 100 dice?  How big are your hands that you could roll > 100 dice??!", mtype=mt)
                        break
                elif count == 0:
                    while True:
                        self.send_message(mto=frm, mbody="ArfufWat?", mtype=mt)
                        break

        pattern = '^Roll [0-9]*$'
        negpattern = '^Roll -[0-9]*$'
        result = re.findall(pattern, body)
        negresult = re.findall(negpattern, body)
        if result:
            match = int(result[0][5:])
            dice(match)
        elif negresult:
            match = int(negresult[0][5:])
            dice(match)
        elif body.startswith("Roll "):
            count = body[5:]
            dice(count)

# =====================================================================================================================
# plus/minus functions:
    # awesomes variables:
        q = 0

    # get an awesome:
        for x in pluses:
            cmd = f"How awesome is {x}?"
            if cmd == body and mucnick != self.nick:
                v = pluses[x]
                str = f"{x} is {v} awesome!"
                while True:
                    self.send_message(mto=frm, mbody=str, mtype=mt)
                    break

    # print awesomes:
        cmd = "What's awesome?"
        if cmd == body and mucnick != self.nick:
            awesomes = []
            for x in pluses:
                v = pluses[x]
                my_string = f"-→{x}:{v}"
                awesomes.append(my_string)
            # composite_list = [awesomes[x:x+15] for x in range(0, len(awesomes), 15)]
            awesome_chunk = " ".join(awesomes)
            while True:
                self.send_message(mto=frm, mbody=awesome_chunk, mtype=mt)
                break

    # clear all awesomes:
        cmd = "clrpluses"
        if cmd == body and mucnick in admins and mucnick != self.nick:
            pluses = {}
            db['pluses'] = pluses

    # delete an awesome:
        for x in pluses:
            try:
                if body == f"Remove {x}" and mucnick in admins and mucnick != self.nick:
                    pluses.pop(x)
                    while True:
                        self.send_message(mto=frm, mbody=f"Removed {x} as an awesome!", mtype=mt)
                        break
            except:
                pass

    # test awesomes:
        if body == "testpluses" and mucnick in admins:
            cs = ["test1","test2","test3"]
            for c in cs:
                if c in pluses:
                    del pluses[c]
                    db['pluses'] = pluses
            teststr = "test1++ test2++ test3++ 'test1'++ 'test2'++ 'test3'++ test1-- test2-- test3-- 'test1'-- 'test2'-- 'test3'--"
            while True:
                self.send_message(mto=frm, mbody=teststr, mtype=mt)
                break

    # add points:
        def add_point(match):
            if pluses.get(match):
                m = pluses.get(match)
                m += 1
                pluses[match] = m
                db['pluses'] = pluses
            else:
                pluses[match] = 1
                db['pluses'] = pluses

    # minus points:
        def minus_point(match):
            if pluses.get(match):
                m = pluses.get(match)
                m -= 1
                pluses[match] = m
                db['pluses'] = pluses
            else:
                pluses[match] = -1
                db['pluses'] = pluses

    # send awesomes update msg:
        # def awesomes_updated_msg(my_awesomes):
        #     try:
        #         if my_awesomes > 0:
        #             for x in my_awesomes:


    # simple ++'s
        if re.findall(r'[\w]+\+{2}', body):
            match = re.findall(r'[\w]+\+{2}', body)
            ms = []
            for m in match:
                m = m[0:-2]
                if len(m) < 128 and len(m) > 1:
                    add_point(m)
                    msi = f"'{m}'"
                    ms.append(msi)
            try:
                if ms[0]:
                    mstr = "Awesomes updated for " + " ".join(ms) + "!"
                if mstr:
                    while True:
                        self.send_message(mto=frm, mbody=mstr, mtype=mt)
                        break
            except:
                pass

    # complex ++'s
        if re.findall(r'([\'\"]{1}[a-zA-Z0-9=%/ &_.!?;:@#$\-><\+]{2,}[\'\"]{1}\+{2})', body):
            match = re.findall(r'([\'\"]{1}[a-zA-Z0-9=%/ &_.!?;:@#$\-><\+]{2,}[\'\"]{1}\+{2})', body)
            ms = []
            for m in match:
                m = m[1:-3]
                if len(m) < 128 and len(m) > 1:
                    add_point(m)
                    msi = f"'{m}'"
                    ms.append(msi)
            try:
                if ms[0]:
                    mstr = "Awesomes updated for " + ", ".join(ms) + "!"
                if mstr:
                    while True:
                        self.send_message(mto=frm, mbody=mstr, mtype=mt)
                        break
            except:
                pass

    # simple --'s
        if re.findall(r'[\w]+\-{2}', body):
            match = re.findall(r'[\w]+\-{2}', body)
            ms = []
            for m in match:
                m = m[0:-2]
                if len(m) < 128 and len(m) > 1:
                    minus_point(m)
                    msi = f"'{m}'"
                    ms.append(msi)
            try:
                if ms[0]:
                    mstr = "Awesomes updated for " + ", ".join(ms) + "!"
                if mstr:
                    while True:
                        self.send_message(mto=frm, mbody=mstr, mtype=mt)
                        break
            except:
                pass

    # complex --'s
        if re.findall(r'([\'\"]{1}[a-zA-Z0-9=%/ &_.!?;:@#$\-><\+]{2,}[\'\"]{1}\-{2})', body):
            match = re.findall(r'([\'\"]{1}[a-zA-Z0-9=%/ &_.!?;:@#$\-><\+]{2,}[\'\"]{1}\-{2})', body)
            ms = []
            for m in match:
                m = m[1:-3]
                if len(m) < 128 and len(m) > 1:
                    minus_point(m)
                    msi = f"'{m}'"
                    ms.append(msi)
            try:
                if ms[0]:
                    mstr = "Awesomes updated for " + ", ".join(ms) + "!"
                if mstr:
                    while True:
                        self.send_message(mto=frm, mbody=mstr, mtype=mt)
                        break
            except:
                pass

    # sort pluses by values in descending order:
        pluses = sorted(pluses.items(), key=lambda x:x[1], reverse=True)
        pluses = dict(pluses)
        db['pluses'] = pluses

# # =====================================================================================================================
# # Food function, feed mrBot food:
#     # food function:
#         foods = {
#             "nos": ["cherry","onion","mrwoofs","chocolate","cat","rock","cement","f00d","food","plastic cement","booz","booze","cat","porcupine","fish","log","tree","boulder","snake"],
#             "likes": ["pizza","steak","spam","hotdog","drumstick","chicken","ham","sandwich","hamburger","apple","mail man","pie","noodles","orange","bugs","bug","beetle","rubber ball","bird","duck","tires","tire","stick"],
#             "luvs": ["chickens","salami","pepperoni","meatloaf","pear","pluses","bird","decibals","sheep","cake","cookies","magpie","rabbit","coconut","muskrat"],
#             "friends": ["g1n","chunk","cmdr_coconut","shokara","baobab","nova","anhydrous","thecanine","r1k","sneexy","mrwoofs","lohang","jrmu","bassgod","arcseconds","pete","tcache","altblex","cow","allie","mopar","moparisthebest","LohanG","lohangX","wgreenhouse","TheCoffeMaker","taba","crk","rozzin","Licaon_Kter","thecanines","ben"],
#             "crazys": ["nutmeg","catnip","nitrogen","bath salts","pcp","fairy dust"]
#         }

#         res_foods = {
#             "nos": "*stares at so called food blankly ( ._.)*",
#             "likes": "nom nom nom :3",
#             "luvs": "*drools, then gnaws and inhales f00d*",
#             "friends": "*wags his tail with his tounge out* :P",
#             "crazys": "\\@_@/~~~~~~ \r\n*rolls around in dirt*"
#         }


#         if body.startswith('mrBot food '):
#             if "mrBot food no" == body:
#                 my_nos = []
#                 for no in foods.get('nos'):
#                     my_nos.append(no)
#                 my_nos_string = ", ".join(my_nos)
#                 while True:
#                     self.send_message(mto=frm, mbody=my_nos_string, mtype=mt)
#                     break

#             if "mrBot food like" == body:
#                 my_likes = []
#                 for like in foods.get('likes'):
#                     my_likes.append(like)
#                 my_likes_string = ", ".join(my_likes)
#                 while True:
#                     self.send_message(mto=frm, mbody=my_likes_string, mtype=mt)
#                     break

#             if "mrBot food luv" == body:
#                 my_luvs = []
#                 for luv in foods.get('luvs'):
#                     my_luvs.append(luv)
#                 my_luvs_string = ", ".join(my_luvs)
#                 while True:
#                     self.send_message(mto=frm, mbody=my_luvs_string, mtype=mt)
#                     break

#             if "mrBot food crazy" == body:
#                 my_crazys = []
#                 for crazy in foods.get('crazys'):
#                     my_crazys.append(crazy)
#                 my_crazys_string = ", ".join(my_crazys)
#                 while True:
#                     self.send_message(mto=frm, mbody=my_crazys_string, mtype=mt)
#                     break

#         def food():
#             if body.startswith("Food "):
#                 check = False
#                 for no in foods.get("nos"):
#                     if body[5:] == no:
#                         while True:
#                             self.send_message(mto=frm, mbody=f"{res_foods.get('nos')}", mtype=mt)
#                             break
#                         check = True
#                 for like in foods.get("likes"):
#                     if body[5:] == like:
#                         while True:
#                             self.send_message(mto=frm, mbody=f"{res_foods.get('likes')}", mtype=mt)
#                             break
#                         check = True
#                 for luv in foods.get("luvs"):
#                     if body[5:] == luv:
#                         while True:
#                             self.send_message(mto=frm, mbody=f"{res_foods.get('luvs')}", mtype=mt)
#                             break
#                         check = True
#                 for friend in foods.get("friends"):
#                     if body[5:] == friend:
#                         while True:
#                             self.send_message(mto=frm, mbody=f"{res_foods.get('friends')}", mtype=mt)
#                             break
#                         check = True
#                 for crazy in foods.get("crazys"):
#                     if body[5:] == crazy:
#                         while True:
#                             self.send_message(mto=frm, mbody=f"{res_foods.get('crazys')}", mtype=mt)
#                             break
#                         check = True
#                 if check == False:
#                     while True:
#                         self.send_message(mto=frm, mbody="Arf?!?!", mtype=mt)
#                         break

#         if body.startswith("Food "):
#             food()

# =====================================================================================================================
    # Help function, ask what mrBot's hobbies are:
        list_of_commands = []
        # list_of_commands.append(["mrBot food no","mrBot food like","mrBot food luv","mrBot food crazy","mrBot food {food}"])
        list_of_commands.append(["clrpluses [admin]","testpluses [admin]","What's awesome?","How awesome is {awesome}?"])
        list_of_commands.append(["Roll {int(range(1,100))}","How many mofos?","Chunk is how many mofos?"])
        # list_of_commands.append(["mrBot {mucnick} is a friend","clrfriends [admin]"])
        list_of_commands.append(["mrBot Whoa Boy!","mrBot Free {mucnick}!","mrBot Attack!","mrBot Attack {mucnick}!","Test The Attack!","mrBot's Victims"])
        how_awesomes_work = "Awesomes are counted positive or negative in two manners:\r\nOne is a single regex word appended by two minus or two plus signs, the other, which allows spaces and a small amount of special characters is to wrap the string with quotations and then immediately append two minuses or pluses."
        if body == "mrBot Help" or body == "mrBot help" or body == "help mrBot" or body == "mrBot help me" or body == "help me" or body == "help" or body == "halp":
            while True:
                self.send_message(mto=frm, mbody="To know how Awesomes! work type mrBot Help Awesomes!\r\nTo know mrBot's commands type mrBot Help Commands\r\n\r\nmrBot will only ever respond to his name written as mrBot, fyi, and use proper english for commands, including punctuation, however there's still tiny imperfections, and chunk is a melon, what can you expect from a melon, like seriously...", mtype=mt)
                break
        elif body == "mrBot Help Awesomes!":
            while True:
                self.send_message(mto=frm, mbody=f"{how_awesomes_work}", mtype=mt)
                break
        elif body == "mrBot Help Commands":
            iteros = []
            for command_sngl_list in list_of_commands:
                for command in command_sngl_list:
                    iteros.append(" ".join(command))
                tosend = "\r\n".join(iteros)
            while True:
                self.send_message(mto=frm, mbody=tosend, mtype=mt)
                break

# =====================================================================================================================================================
# net tools::functions:
    # # host command as if on bash command line
    #     def host(hostname):
    #         s = hostname
    #         s1 = "".join(c for c in s if c.isalpha() or c == "." or c.isdecimal())
    #         # s1 = re.sub('[^A-Za-z0–9.]','',s)
    #         hostname = s1
    #         lengthdiff0 = 13
    #         lengthdiff1 = 18
    #         hostnamelen = len(hostname)
    #         cmd = f"host {hostname} > host.{hostname}.txt"
    #         if os.system(cmd) == 0:
    #             f = open(f"host.{hostname}.txt", "r")
    #             r = f.read()
    #             l = r.split("\n")
    #             diff0 = int(hostnamelen + lengthdiff0)
    #             diff1 = int(hostnamelen + lengthdiff1)
    #             message = f"{hostname} has:"
    #             ipv4s = []
    #             ipv6s = []
    #             for each in l:
    #                 if " has address " in each:
    #                     addr = each[diff0:]
    #                     ipv4s.append(addr)
    #                 elif " has IPv6 address " in each:
    #                     addr = each[diff1:]
    #                     ipv6s.append(addr)
    #             message = [f"{hostname} has:"]
    #             if ipv4s:
    #                 for four in ipv4s:
    #                     message.append(f"IPv4: {four}")
    #             if ipv6s:
    #                 for six in ipv6s:
    #                     message.append(f"IPv6: {six}")
    #             end = "\r\n".join(message)
    #             return end
    #         else:
    #             return "Hostname Did Not Resolve!"

    #     def ping(target):
    #         s = target
    #         try:
    #             target_ip = ip_address(s)
    #         except:
    #             target = "".join(c for c in s if c.isalpha() or c == "." or c.isdecimal())
    #         cmd = f"ping -c4 -4 {target} > ping.c4.v4.{target}.txt"
    #         os.system(cmd)
    #         f = open(f"ping.c4.v4.{target}.txt","r")
    #         r = f.read()
    #         if len(r) > 0:
    #             l = r.split("\n")
    #             pings = []
    #             for x in l:
    #                 if " icmp_seq=" in x:
    #                     pings.append(x)
    #             if pings[3]:
    #                 message = f"Pinging {target}, IPv4, Count x4:\r\n" + "\r\n".join(pings)
    #                 return message
    #         return "Error in specifying target for ping"

    #     def ping6(target):
    #         s = target
    #         try:
    #             target_ip = ip_address(s)
    #         except:
    #             target = "".join(c for c in s if c.isalpha() or c == "." or c.isdecimal())
    #         cmd = f"ping -c4 -6 {target} > ping.c4.v6.{target}.txt"
    #         os.system(cmd)
    #         f = open(f"ping.c4.v6.{target}.txt","r")
    #         r = f.read()
    #         if len(r) > 0:
    #             l = r.split("\n")
    #             pings = []
    #             for x in l:
    #                 if " icmp_seq=" in x:
    #                     pings.append(x)
    #             if pings[3]:
    #                 message = f"Pinging {target}, IPv6, Count x4:\r\n" + "\r\n".join(pings)
    #                 return message
    #         return "Error in specifying target for ping"

# net tools::executes:
        # if body.startswith("mrBot host "):
        #     hostname = body[11:]
        #     message = host(hostname)
        #     while True:
        #         self.send_message(mto=frm, mbody=f"{message}", mtype=mt)
        #         break

        # if body.startswith("mrBot ping "):
        #     target = body[11:]
        #     message = ping(target)
        #     while True:
        #         self.send_message(mto=frm, mbody=f"{message}", mtype=mt)
        #         break

        # if body.startswith("mrBot ping6 "):
        #     target = body[12:]
        #     message = ping6(target)
        #     while True:
        #         self.send_message(mto=frm, mbody=f"{message}", mtype=mt)
        #         break

# net tools::tests:
    # tests:

# net tools::schedule:
    # flush the file list in cwd:
        # cmd = "rm host.*.txt ping.c*.txt"
        # os.system(cmd)

# =====================================================================================================================
# Tell mrBot to exit:
        # if "nn mrBot" == body and mucnick in admins and mucnick != self.nick:
        #     while True:
        #         self.send_message(mto=frm, mbody="zzz z zz...zzzzzz ....zzz z ...... x_x ..zzz", mtype=mt)
        #         break
        #     pause(3)
        #     exit()

# =====================================================================================================================================================
# =====================================================================================================================================================
# =====================================================================================================================================================

if __name__ == '__main__':
    # parser = ArgumentParser()

    # parser.add_argument("-q", "--quiet", help="set logging to ERROR",
    #                     action="store_const", dest="loglevel",
    #                     const=logging.ERROR, default=logging.INFO)
    # parser.add_argument("-d", "--debug", help="set logging to DEBUG",
    #                     action="store_const", dest="loglevel",
    #                     const=logging.DEBUG, default=logging.INFO)

    # parser.add_argument("-j", "--jid", dest="jid",
    #                     help="JID to use")
    # parser.add_argument("-p", "--password", dest="password",
    #                     help="password to use")
    # parser.add_argument("-r", "--room", dest="room",
    #                     help="MUC room to join")
    # parser.add_argument("-n", "--nick", dest="nick",
    #                     help="MUC nickname")

    # args = parser.parse_args()

    # logging.basicConfig(level=args.loglevel,
    #                     format='%(levelname)-8s %(message)s')

    # if args.jid is None:
    #     args.jid = input("Username: ")
    # if args.password is None:
    #     args.password = getpass("Password: ")
    # if args.room is None:
    #     args.room = input("MUC room: ")
    # if args.nick is None:
    #     args.nick = input("MUC nickname: ")

    # xmpp = mrBot(args.jid, args.password, args.room, args.nick)
    botjid_to_load_in = input("Bot's JID: ")
    botjid_to_load = str(botjid_to_load_in)

    passwd_to_load_in =  input("Password: ")
    passwd_to_load = str(passwd_to_load_in)

    botnick_to_load_in =  input("Bot's nickname: ")
    botnick_to_load = str(botnick_to_load_in)

    muc_to_load_in =  input("MUC's JID: ")
    muc_to_load = str(muc_to_load_in)

    # print(muc_to_load)

    xmpp = mrBot(botjid_to_load, passwd_to_load, muc_to_load, botnick_to_load)
    xmpp.register_plugin('xep_0030') # Service Discovery
    xmpp.register_plugin('xep_0045') # Multi-User Chat
    xmpp.register_plugin('xep_0199') # XMPP Ping
    xmpp.connect()
    xmpp.process()

# =====================================================================================================================================================
# =====================================================================================================================================================
# =====================================================================================================================================================
