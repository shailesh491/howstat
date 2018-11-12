import mechanize, csv
from bs4 import BeautifulSoup

browser = mechanize.Browser()
browser.set_handle_robots(False)

def getAbcList():
	try:
		response = browser.open('http://www.howstat.com/cricket/Statistics/Players/PlayerMenu.asp')
	except:
		print 'Cannot connect to the internet!'
		sys.exit(1)

	l = []
	soup = BeautifulSoup(response)
	
	for a in soup.findAll('a', {'class' : 'abcList'}):
		l.append('http://www.howstat.com/cricket/Statistics/Players/' + str(a['href']))

	return l	

def getPlayers(link, f):

	try:
		response = browser.open(link)
	except:
		print 'Cannot connect to the internet!'
		sys.exit(1)

	print link

	ret = []
	soup = BeautifulSoup(response)
	concernedTrs = list(soup.findAll('table', {'class' : 'TableLined'})[0].findAll('tr'))

	for i in range(2, len(concernedTrs)-1):
		tds = list(concernedTrs[i].findAll('td'))
		l = []

		for j in range(3):
			try:
				l.append(tds[j].text.strip())
			except:
				l.append(None)
		
		try:
			l.append('http://www.howstat.com/cricket/Statistics/Players/' + tds[3].a['href'].strip())
		except:
			l.append(None)
		
		if l[1] is not None and l[3] is not None and int(l[1][-4:]) >= 1955:
			
			li = l[0:3] + [tds[3].text.strip()]
			playerId = l[3][l[3].index('=')+1:]

			print playerId

			li += collectPlayerData(playerId)

			f.writerow(li)


def collectPlayerData(playerId):
	try:
		response = browser.open('http://www.howstat.com/cricket/Statistics/Players/PlayerOverview.asp?PlayerID=' + playerId)
	except:
		print 'Cannot connect to the internet!'
		return

	soup = BeautifulSoup(response)
	trs = list(soup.findAll('table')[8].findAll('tr'))

	i, j = 0, 0

	for i_ in range(len(trs)):
		if 'Bowling' in trs[i_].text:
			i = i_ + 1
			
		if 'Fielding' in trs[i_].text:
			j = i_
			break

	d = {}
	for i_ in range(i, j):
		tr = trs[i_]
		children = tr.findChildren(recursive=False)
		if 'Overs' in children[0].text:
			try:
				d['Overs'] = float(children[1].text.strip())
			except:
				d['Overs'] = -1
	
		

	ret = []
	for x in ['Overs']:
		if x in d:
			ret.append(d[x])
		else:
			ret.append(-1)

	return [playerId] + ret	

if __name__ == '__main__':
	f = csv.writer(open('data_S.csv', 'w'))
	f.writerow(['Name', 'DOB', 'Country', 'Matches', 'Overs'])
	
	[getPlayers('http://www.howstat.com/cricket/Statistics/Players/PlayerList.asp?Group=' + str(c), f) for c in ['S']]
