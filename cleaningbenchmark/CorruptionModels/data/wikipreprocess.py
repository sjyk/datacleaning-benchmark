#!/usr/bin/env python
import re
import pickle
import itertools

def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', name.replace("_"," ").replace("'",""))
    return ' '.join(re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1).lower().split())

redirects = {}
f = open('wikiredirects.txt', 'rb+')
line = f.readline()

while line != "":
	comps = line.split(',')

	try:
		pid = int(comps[0])
		title = comps[2].lower().replace("'","").replace("_"," ")
		if title not in redirects:
			redirects[title] = []
		redirects[title].append(pid)
		
	except ValueError:
		pass
	except IndexError:
		pass

	line = f.readline()

titles = {}
f = open('wikititles.txt', 'rb+')
line = f.readline()

while line != "":
	comps = line.split(',')

	try:
		pid = int(comps[0])
		print pid
		titles[pid] = convert(comps[2])
		
	except ValueError:
		pass
	except IndexError:
		pass

	line = f.readline()

pickle.dump( [redirects, titles], open( "save.p", "wb" ) )

data = pickle.load(open( "save.p", "rb" ))
redirects = data[0]
titles = data[1]
lookup_set = {}

for k in redirects:
	
	title_list = [k]
	for j in redirects[k]:
		if j in titles:
			title_list.append(titles[j])

	for j in title_list:
		lookup_set[j] = title_list

	print k, title_list

pickle.dump(lookup_set, open( "lookup.p", "wb" ) )


