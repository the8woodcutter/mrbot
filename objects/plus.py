# !/usr/bin/env python3.10
import re
import shelve

class Plus():

	def give_pluses(self, awesome, count=1):
		db = shelve.open(plus.db)
		try:
			cc = db.get(awesome).get('pluses', 0)
			cc += 1
			db[awesome] = { 'pluses': cc }
		except AttributeError:
			db[awesome] = {}
			cc = count
			db[awesome] = { 'pluses': cc }

	def give_minuses(self, awesome):
		pass

	def is_plus(self, body):
		match = re.match(r'[\bA-Za-z0-9\_\-\=\:\;\[\]\(\)\{\}\%\$\#\@\&\*\!\<\>]+\+{2}', body)
		if match[0]:
			rgx = str(match[0])
			awesome = rgx.rstrip('++')
			l = len(awesome)
			if l > 1 and l < 28:
				self.give_pluses(awesome)
				cp = self.db.get(awesome).get('pluses')
				result = [awesome, cp]
				return result
			else:
				result = ['NOPE', 0]
				return result

	def is_minus(self, body):
		pass