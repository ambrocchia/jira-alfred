# coding=utf-8

from feedback import Feedback
import urllib2
import urllib
import json
import sys
import os.path

import costants

if len(sys.argv) == 2:
	query = urllib.quote(sys.argv[1])

	feeds = Feedback()

	for project in costants.PROJECTS:
		ticket_url = "%s-%s" % (project, query)
		feeds.add_item(title="%s-%s" % (project, query), subtitle=ticket_url, valid='YES', arg=ticket_url, icon='icon.png')

	print feeds
