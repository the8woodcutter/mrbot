import os
from ipaddress import ip_address
def host(hostname):
    s = hostname
    s1 = "".join(c for c in s if c.isalpha() or c == "." or c.isdecimal())
    # s1 = re.sub('[^A-Za-z0–9.]','',s)
    hostname = s1
    lengthdiff0 = 13
    lengthdiff1 = 18
    hostnamelen = len(hostname)
    cmd = f"host {hostname} > host.{hostname}.txt"
    if os.system(cmd) == 0:
        f = open(f"host.{hostname}.txt", "r")
        r = f.read()
        l = r.split("\n")
        diff0 = int(hostnamelen + lengthdiff0)
        diff1 = int(hostnamelen + lengthdiff1)
        message = f"{hostname} has:"
        ipv4s = []
        ipv6s = []
        for each in l:
            if " has address " in each:
                addr = each[diff0:]
                ipv4s.append(addr)
            elif " has IPv6 address " in each:
                addr = each[diff1:]
                ipv6s.append(addr)
        message = [f"{hostname} has:"]
        if ipv4s:
            for four in ipv4s:
                message.append(f"IPv4: {four}")
        if ipv6s:
            for six in ipv6s:
                message.append(f"IPv6: {six}")
        end = "\r\n".join(message)
        return end
    else:
        return "Hostname Did Not Resolve!"

def ping(target):
	s = target
	try:
		target_ip = ip_address(s)
	except:
		target = "".join(c for c in s if c.isalpha() or c == "." or c.isdecimal())
	cmd = f"ping -c8 -4 {target} > ping.c8.v4.{target}.txt"
	if os.system(cmd) == 0:
		f = open(f"ping.c8.v4.{target}.txt","r")
		r = f.read()
		l = r.split("\n")
		pings = []
		for x in l:
			if " icmp_seq=" in x:
				pings.append(x)
		if pings[7]:
			message = f"Pinging {target}, IPv4, Count x8:\r\n" + "\r\n".join(pings)
			return message
		else:
			return "Error in specifying target for ping"

def ping6(target):
	s = target
	try:
		target_ip = ip_address(s)
	except:
		target = "".join(c for c in s if c.isalpha() or c == "." or c.isdecimal())
	cmd = f"ping -c8 -6 {target} > ping.c8.v6.{target}.txt"
	if os.system(cmd) == 0:
		f = open(f"ping.c8.v6.{target}.txt","r")
		r = f.read()
		l = r.split("\n")
		pings = []
		for x in l:
			if " icmp_seq=" in x:
				pings.append(x)
		if pings[7]:
			message = f"Pinging {target}, IPv6, Count x8:\r\n" + "\r\n".join(pings)
			return message
		else:
			return "Error in specifying target for ping"