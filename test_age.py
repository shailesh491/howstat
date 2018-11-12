import requests
from bs4 import BeautifulSoup


def player_age_details(ID):
	url = 'http://www.howstat.com/cricket/Statistics/Players/PlayerProgressSummary.asp?PlayerID=' + str(ID)
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text,features="lxml")

	age = soup.find_all('td',{'align':'left'})
	dat_odd = soup.find_all('tr', {'bgcolor':'#E3FBE9'})
	dat_even = soup.find_all('tr', {'bgcolor':'#FFFFFF'})
	arr_odd=[]
	for i in dat_odd:
		ls_odd=[]
		arr_ls = i.find_all('td')
		k=arr_ls[0].contents
		ag=arr_ls[16].contents
		agg=arr_ls[6].contents
		av = arr_ls[7].contents
		gg =k[0].strip()
		aggr=agg[0].strip()
		avg=av[0].strip()
		age=ag[0].strip()
	
		ls_odd.append(ID)
		ls_odd.append(gg)
		ls_odd.append(aggr)
		ls_odd.append(avg)
		ls_odd.append(age)
		arr_odd.append(ls_odd)

	arr_even=[]
	for i in dat_even:
		ls_odd=[]
		arr_ls = i.find_all('td')
		k=arr_ls[0].contents
		ag = arr_ls[16].contents
		agg=arr_ls[6].contents
		av = arr_ls[7].contents
		gg =k[0].strip()
		aggr=agg[0].strip()
		avg=av[0].strip()
		age=ag[0].strip()
	
		ls_odd.append(ID)
		ls_odd.append(gg)
		ls_odd.append(aggr)
		ls_odd.append(avg)
		ls_odd.append(age)
		arr_even.append(ls_odd)


	arr_even = [c for c in arr_even if c[4] != ''] 
	arr_odd = [c for c in arr_odd if c[4] != '']


	result = [None]*(len(arr_odd)+len(arr_even))
	result[::2] = arr_odd
	result[1::2] = arr_even
	return result

ids=[1735,3600]
arr_final=[]
for i in range(len(ids)):
	t=[]
	if not t:
		t = player_age_details(ids[i])
		arr_final.extend(t)

print(arr_final)


#print (tot_len)
#print (arr_even)




