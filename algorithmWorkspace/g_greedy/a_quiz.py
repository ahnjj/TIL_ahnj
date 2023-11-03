# 동전 찍기
def q1(change):
    coins = {500: 0, 100:0, 50:0, 10:0, 1: 0}

    for coin in coins:
        coins[coin] = change // coin
        change %= coin
    return coins

print(q1(3465))



def q2(meetings):
    meetings = sorted(meetings,key = lambda x: x['end'])
    res = []
    res.append(meetings)
    # 빨리끝나는 애를 먼저 선택한다고 가정
    fin = meetings[0]['end']

    for i in range(1,len(meetings)):
        if meetings[i]['start'] >= fin:
            fin = meetings[i]['end']
            res.append(i)

    for mtg in res:
        print(meetings[mtg])


meetings = [
      {'idx':1,'start':1, 'end':10}
     ,{'idx':2,'start':5, 'end':6}
     ,{'idx':3,'start':13,'end':15}
     ,{'idx':4,'start':14,'end':17}
     ,{'idx':5,'start':8, 'end':14}
     ,{'idx':6,'start':3, 'end':12}
     ]

q2(meetings)
