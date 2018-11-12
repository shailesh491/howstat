import requests
from bs4 import BeautifulSoup
ID = 3600
ret = []
pd = {}
d = {}
def player_details(ida):
	url='http://howstat.com/cricket/Statistics/Players/PlayerOverview.asp?PlayerID='+str(ida)
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text)
	ret.append(ID)
	trs_1 = (soup.findAll('table')[6].findAll('tr'))

	for i_ in range(len(trs_1)):
		tr_1 = trs_1[i_]
		children = tr_1.findChildren(recursive=False)
		if 'Full Name' in children[0].text:
			try:
				pd['Full Name'] = str(children[1].text.strip())
			except:
				pd['Full Name'] = -1
		if 'Born' in children[0].text:
			try:
				pd['Born'] = int(children[1].text.strip()[-4:])
			except:
				pd['Born'] = -1

	for x in ['Full Name', 'Born']:
		if x in pd:
			ret.append(pd[x])
		else:
			ret.append(-1)

	trs = (soup.findAll('table')[8].findAll('tr'))
	i = 0

	for i_ in range(len(trs)):
		if 'Batting' in trs[i_].text:
			i = i_ + 1
	
	for i_ in range(i):
		tr = trs[i_]
		children = tr.findChildren(recursive=False)
		if 'Aggregate' in children[0].text:
			try:
				d['Aggregate'] = int(children[1].text.strip())
			except:
				d['Aggregate'] = -1

		elif 'Average' in children[0].text:
			try:
				d['Average'] = float(children[1].text.strip())
			except:
				d['Average'] = -1
		elif '50s' in children[0].text:
			try:
				d['50s'] = int(children[1].text.strip())
			except:
				d['50s'] = -1

		elif '100s' in children[0].text:
			try:
				d['100s'] = int(children[1].text.strip())
			except:
				d['100s'] = -1


	for x in ['Aggregate', 'Average', '50s', '100s']:
		if x in d:
			ret.append(d[x])
		else:
			ret.append(-1)
	return ret 

#print(player_details('http://howstat.com/cricket/Statistics/Players/PlayerOverview.asp?PlayerID=' + str(ID)))

ids = [1735,3600,2060]
arr_pl=[] 		
for j in range(len(ids)):
	t=[]
	if not t:
		t = player_details(ids[j])
		arr_pl.append(t)
#print (arr_pl)

ls = arr_pl[0]
arr=[]
badi_arr=[]
for i in range(len(ls)):
	arr.append(ls[i])
	if len(arr)==7:
		badi_arr.append(arr)
		arr=[]
for i in range(len(ids)):
	badi_arr[i][0]=ids[i]

print (badi_arr)		
