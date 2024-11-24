#!/usr/bin/env python3
import os
from pathlib import Path
import mimetypes

with os.scandir('/var/www/html/stash') as entries:
	entries = Path('/var/www/html/stash')
	html_doc = "<html><head><title>TooFast.vip Gallery of Random Stash Pics</title></head><body style='background-color: #323415'><div style='width: 90vw; margin-left: 5vw; margin-right: 5vw; background-color: black; border-left: dotted 2px darkgray; border-right: dotted 2px darkgray; padding-left: 3vw; padding-right: 3vw;'>"
	for entry in entries.iterdir():
		if "image/" in mimetypes.guess_type(entry)[0]:
			img_tag = f"<img src='{entry}' alt='' style='width: 94vw; height: auto; border: 1px solid darkorange; border-radius: 5px;'><br/><br/>"
			html_doc = html_doc + img_tag
	index = html_doc + "</div></body></html>"
print(index)