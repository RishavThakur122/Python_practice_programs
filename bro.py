prices=[7,1,5,3,6,4]
prices1=prices
prices1=sorted(prices1,reverse=True)
print("prices : ",prices)
print("prices1 : ",prices1)
if prices==[]:
    print("0")
if prices1==prices:
    print("0")
else:
    temp=prices.index(min(prices))
    prices=prices[temp:len(prices)]
    print( max(prices)-min(prices))
