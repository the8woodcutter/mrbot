# # =====================================================================================================================
# # test db:
#     # read db first level:
#         def test_first_db(self):
#             message = []
#             for each in db:
#                 thisdb = db.get(each)
#                 message.append(f"Name: {each}, Type: {type(thisdb)}\r\n")
#             message = "".join(message)
#             return message

#         def test_second_db(self, dbthing):
#             for each in db:
#                 if each == dbthing:
#                     iam = db.get(each)
#                     newmessage = []
#                     for ech in iam:
#                         newmessage.append(f"{ech}\r\n")
#                     newnewmessage = "".join(newmessage)
#                     message = f"Name: '{each}'\r\n" + newnewmessage + "\r\n"
#                     return message
#                     # if isinstance(each, __builtins__.list):
#                         # iam = db.get(each)
#                         # newmessage = []
#                         # for ech in iam:
#                         #     newmessage.append(f"{ech}\r\n")
#                         # newmessage = "".join(message)
#                         # newmessage = "Name:\r\n" + message + "\r\n"
#                     # elif isinstance(each, __builtins__.dict):
#                     #     newmessage = "\r\nWe're not handling dict() yet\r\n"
#                     # elif isinstance(each, __builtins__.str) or isinstance(each, __builtins__.int):
#                     #     iam = db.get(each)
#                     #     newmessage = f"Name: {each}\r\n{iam}\r\n"
#                     # message.append(newmessage)
#                 # return message

#     # return functions:
#         if "testdb1" == body and mucnick in admins:
#             while True:
#                 self.send_message(mto=frm, mbody=test_first_db(self), mtype=mt)
#                 break
#         for each in db:
#             if body == f"testdb2 {each}" and mucnick in admins:
#                 while True:
#                     self.send_message(mto=frm, mbody=test_second_db(self, each), mtype=mt)
#                     break

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




# # =====================================================================================================================
# # friends function:
#     # NOTES: later on we can use this function to start on a social credit score where certain activities by nicks in muc can grow or shrink their friendship with mrBot...
#     # ...and they'll maintain a score for certain terms in a message sent with certain phrases to match mrBot mentions.  The responses throughout this script should vary...
#     # ...based on their existing score, if any...
#         for x in nicklist:
#             hint = f"mrBot {x} is a friend"
#             cf = "clrfriends"
#             if body == hint:
#                 friends.append(x)
#                 db['friends'] = friends
#                 while True:
#                     self.send_message(mto=frm, mbody=f"Okay {x} is ma buddey :P", mtype=mt)
#                     break
#                 for v in victims:
#                     if v == x:
#                         victims.remove(v)
#                         db['victims'] = victims
#             elif cf == body and mucnick in admins:
#                 friends = []
#                 db['friends'] = friends
#                 while True:
#                     self.send_message(mto=frm, mbody="No more friends ...", mtype=mt)
#                     break

#         try:
#             if db.get('friends'):
#                 for x in friends:
#                     if mucnick == x and self.nick in body:
#                         while True:
#                             self.send_message(mto=frm, mbody=f"Arff {x}! :D", mtype=mt)
#                             break

#                 for x in friends:
#                     lst = ["pats mrBot","pats mrbot","pets mrBot","pets mrbot","hugs mrBot","hugs mrBot"]
#                     for i in lst:
#                         if i in body and x == mucnick:
#                             while True:
#                                 self.send_message(mto=frm, mbody=f"lllluulzlz..,,.,.  :D", mtype=mt)
#                                 break
#         except:
#             pass








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
    
# =====================================================================================================================================================
# =====================================================================================================================================================
# =====================================================================================================================================================
