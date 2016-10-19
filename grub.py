import json, requests, BeautifulSoup
session=requests.session()
headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

r=session.get('http://debate.grubhub.com/?utm_source=responsys&utm_medium=email_crm&utm_campaign=20161019_Brand_DebateRound3_Quiz',headers=headers)
soup = BeautifulSoup.BeautifulSoup(r.content)
init=str(soup.findAll(attrs={"id":"init"})[0]['data-initialization'])
data={
    'email':'zdw7287@rit.edu',
    'answer_1':'1',
    'answer_2':'0',
    'answer_3':'1',
    'answer_4':'0',
    'answer_5':'0',
    'answer_bonus':'1',
    'source':'grubhub',
    'initialization':init
}
r=session.post('http://debate.grubhub.com/scripts/submit.php',data=data,headers=headers)
print r.json()
