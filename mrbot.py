#!/usr/bin/env /usr/bin/python3
## ^ this is in the even that on your debian system is package `python3-slixmpp` and mrBot is run without venv...

# from getpass import getpass
# from argparse import ArgumentParser
# from ipaddress import ip_address

import slixmpp
import logging
import shelve
import random
import re
import os
import sys

# import ipaddress
# import socket
# import urllib3


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

    def muc_message(self, msg):
    # VARIABLES:
    ## -------------------------------------------------------------------------
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
# mrBot ATTACK function:
    # setting the trigger:

    # set to NOT Attack:
        if mucnick != self.nick:
            if "mrBot Whoa Boy!" == body:
                db['i'] = 0
                i = db.get('i')
                while True:
                    self.send_message(mto=frm, mbody=f"/me Stares blankly at {mucnick}", mtype=mt)
                    break

        if mucnick != self.nick:
            for x in nicklist:
                hint = f"mrBot Free {x}!"
                if hint == body and x != self.nick:
                    victims.remove(x)
                    db['victims'] = victims
                    victims = db['victims']
                    while True:
                        self.send_message(mto=frm, mbody="/me runs over to the other side of the yard as if chasing a tennis ball that never was ... ..", mtype=mt)
                        break

    # set TO ATTACK!
        if mucnick != self.nick:
            if mucnick in admins:
                if "mrBot Attack!" == body:
                    db['i'] = 1
                    i = db.get('i')
                    while True:
                        self.send_message(mto=frm, mbody="Set to ATTACK >:]", mtype=mt)
                        break

        if mucnick != self.nick:
            for x in nicklist:
                hint = f"mrBot Attack {x}!"
                if hint == body and mucnick in admins and x != self.nick:
                    victims.append(x)
                    db['victims'] = victims
                    victims = db['victims']
                    while True:
                        self.send_message(mto=frm, mbody=f"{x} grrrrrr", mtype=mt)
                        break

    # TESTING Attack Status:
        if mucnick != self.nick:
            if "Test The Attack!" == body:
                if i == 0:
                    while True:
                        self.send_message(mto=frm, mbody=f"Parameter:{i}: No Attack.", mtype=mt)
                        break
                if i == 1:
                    while True:
                        self.send_message(mto=frm, mbody=f"Parameter:{i}: ATTACK!!", mtype=mt)
                        break

        if mucnick != self.nick:
            if "mrBot's Victims" == body:
                while True:
                    self.send_message(mto=frm, mbody=f"I will chew on: {victims}", mtype=mt)
                    break

    # if the trigger is 1 then Attack:
        if mucnick != self.nick:
            if i == 1 and mucnick in victims:
                while True:
                    self.send_message(mto=frm, mbody=f"{mucnick}: {arf}", mtype=mt)
                    break

# =====================================================================================================================
# Other responses:
        if mucnick != self.nick:
            if "Oi" in body or "oi" in body:
                ois = re.findall(r'Oi', body)
                if ois[0]:
                    semd = []
                    for x in ois:
                        semd.append("oi")
                    semd = " ".join(semd)
                    while True:
                        self.send_message(mto=frm, mbody=semd, mtype=mt)
                        break

        if mucnick != self.nick:
            if "Yay" in body or body == "yay" or body == "yay!":
                while True:
                    self.send_message(mto=frm, mbody="YAY! :D", mtype=mt)
                    break

        greetings = ["hello mrBot","Hello mrBot","Hi mrBot","hi mrBot","pats mrBot"]

        if mucnick != self.nick:
            for x in greetings:
                if x in body:
                    while True:
                        self.send_message(mto=frm, mbody=f"{mucnick}: Arf :P", mtype=mt)
                        break

        if mucnick != self.nick:
            if body == "test" or body == "Test" or "testing" in body:
                while True:
                    self.send_message(mto=frm, mbody="Test Success!", mtype=mt)
                    break

        if mucnick != self.nick:
            if mucnick in admins:
                if "nicklist" == body:
                    while True:
                        self.send_message(mto=frm, mbody=nicklist_string, mtype=mt)
                        break

# # =====================================================================================================================
# # chunk was here function:
#         def chunk_was_here(self):
#             self.send_message(mto=frm, mbody="chunk wuz here", mtype=mt)

#         if "mofo" in body:
#             if mofos <= 1:
#                 db['mofos'] = 12
#                 mofs = db['mofos']
#                 chunk_was_here(self)
#             else:
#                 db['mofos'] -= 1
#                 mofos = db['mofos']

#         if "Chunk's mofos?" == body and mucnick in admins:
#             while True:
#                 self.send_message(mto=frm, mbody=f"{mofos}", mtype=mt)
#                 break

#         if "mofoe" in body:
#             db['mofoes'] = True
#             mofoes = db['mofoes']

#         if "No Mofoes" == body and mucnick != self.nick and mucnick in admins:
#             db['mofoes'] = False
#             mofoes = db['mofoes']
#             while True:
#                 self.send_message(mto=frm, mbody="No mofoes, AAAAAAAAND SAFE!!!", mtype=mt)
#                 break

#         if "How many mofos?" == body and mucnick != self.nick:
#             mofos_count = len(nicklist)
#             if mofoes == True:
#                 msgbody = f"{mofos_count} mofos present with possible mofoes >_>  ...  suspicious"
#                 while True:
#                     self.send_message(mto=frm, mbody=msgbody, mtype=mt)
#                     break
#             elif mofoes == False:
#                 msgbody = f"{mofos_count} mofos present"
#                 while True:
#                     self.send_message(mto=frm, mbody=msgbody, mtype=mt)
#                     break


# # =====================================================================================================================
# # yell function:
#         if mucnick != self.nick:
#             rgx = re.match(r'[A-Z\ \,\!\.\?\:]{22,}', body) 
#             rnd = random.randint(1,7)
#             if rgx:
#                 if rnd == 2 or rnd == 3 or rnd == 5:
#                     rgx = rgx[0]
#                     l = len(rgx)
#                     r = random.randint(9,33)
#                     a = l + r
#                     a = ("A" * a) + ("!" * r)
#                     while True:
#                         self.send_message(mto=frm, mbody=a, mtype=mt)
#                         break

# # =====================================================================================================================
# # dice function:
#         def dice(count):
#             dice = ["⚀","⚁","⚂","⚃","⚄","⚅"]
#             if isinstance(count, __builtins__.str):
#                 while True:
#                     self.send_message(mto=frm, mbody="Arf??", mtype=mt)
#                     break
#             elif isinstance(count, __builtins__.int):
#                 if count > 0 and count <= 100:
#                     dices = []
#                     while count > 0:
#                         r = random.randint(1,6)
#                         r -= 1
#                         dices.append(dice[r])
#                         count -= 1
#                     dices = " ".join(dices)
#                     while True:
#                         self.send_message(mto=frm, mbody=f"{dices}", mtype=mt)
#                         break
#                 elif count < 0:
#                     while True:
#                         self.send_message(mto=frm, mbody="What are you going to do, roll invisible dice?!", mtype=mt)
#                         break
#                 elif count > 100:
#                     while True:
#                         self.send_message(mto=frm, mbody="More than 100 dice?  How big are your hands that you could roll > 100 dice??!", mtype=mt)
#                         break
#                 elif count == 0:
#                     while True:
#                         self.send_message(mto=frm, mbody="ArfufWat?", mtype=mt)
#                         break

#         pattern = '^Roll [0-9]*$'
#         negpattern = '^Roll -[0-9]*$'
#         result = re.findall(pattern, body)
#         negresult = re.findall(negpattern, body)
#         if result:
#             match = int(result[0][5:])
#             dice(match)
#         elif negresult:
#             match = int(negresult[0][5:])
#             dice(match)
#         elif body.startswith("Roll "):
#             count = body[5:]
#             dice(count)

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
#     # Help function, ask what mrBot's hobbies are:
#         list_of_commands = []
#         # list_of_commands.append(["mrBot food no","mrBot food like","mrBot food luv","mrBot food crazy","mrBot food {food}"])
#         list_of_commands.append(["clrpluses [admin]","testpluses [admin]","What's awesome?","How awesome is {awesome}?"])
#         list_of_commands.append(["Roll {int(range(1,100))}","How many mofos? [admin]"])
#         list_of_commands.append(["mrBot {mucnick} is a friend","clrfriends [admin]"])
#         list_of_commands.append(["mrBot Whoa Boy!","mrBot Free {mucnick}!","mrBot Attack!","mrBot Attack {mucnick}!","Test The Attack!","mrBot's Victims"])
#         how_awesomes_work = "Awesomes are counted positive or negative in two manners:\r\nOne is a single regex word appended by two minus or two plus signs, the other, which allows spaces and a small amount of special characters is to wrap the string with quotations and then immediately append two minuses or pluses."
#         if body == "mrBot Help" or body == "mrBot help" or body == "help mrBot" or body == "mrBot help me":
#             while True:
#                 self.send_message(mto=frm, mbody="To know how Awesomes! work type mrBot Help Awesomes!\r\nTo know mrBot's commands type mrBot Help Commands\r\n\r\nmrBot will only ever respond to his name written as mrBot, fyi, and use proper english for commands, including punctuation, however there's still tiny imperfections, and chunk is a melon, what can you expect from a melon, like seriously...", mtype=mt)
#                 break
#         elif body == "mrBot Help Awesomes!":
#             while True:
#                 self.send_message(mto=frm, mbody=f"{how_awesomes_work}", mtype=mt)
#                 break
#         elif body == "mrBot Help Commands":
#             iteros = []
#             for command_sngl_list in list_of_commands:
#                 for command in command_sngl_list:
#                     iteros.append(" ".join(command))
#                 tosend = "\r\n".join(iteros)
#             while True:
#                 self.send_message(mto=frm, mbody=tosend, mtype=mt)
#                 break


if __name__ == '__main__':
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
