#B. Order Book
#Codeforces problem number 572.

n,s = [int(i) for i in input().split()]

buys = {}
sells = {}

#read orders
for i in range(n):
	order = input().split()
	d = order[0]
	p = int(order[1])
	q = int(order[2])
	if d == 'B': #buys
		if p in buys:
			buys[p] += q
		else:
			buys[p] = q
	elif d == 'S': #sells
		if p in sells:
			sells[p] += q
		else:
			sells[p] = q

#order orders
buys_list = sorted([(k, v) for k, v in buys.items()], reverse=True)
sells_list = sorted([(k,v) for k,v in sells.items()]) #sells orders are not reversed 'cause a sell is better if it has lower price

l_sells_list = len(sells_list)
l_buys_list = len(buys_list)
#best aggregated sells
if l_sells_list > s:
	if l_sells_list > 0:
		for i in range(s-1, -1, -1):
			print("S " + str(sells_list[i][0]) + " " + str(sells_list[i][1]))
elif l_sells_list > 0:
	#print all
	for i in range(l_sells_list-1, -1, -1):
		print("S " + str(sells_list[i][0]) + " " + str(sells_list[i][1]))

#best aggregated buys
if l_buys_list > s:
	if l_buys_list > 0:
		for i in range(s):
			print("B "+ str(buys_list[i][0]) + " " + str(buys_list[i][1]))
elif l_buys_list > 0:
	#print all
	if l_buys_list > 0:
		for i in range(l_buys_list):
			print("B "+ str(buys_list[i][0]) + " " + str(buys_list[i][1]))

