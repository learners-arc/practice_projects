a=open("/home/ansh-kumar/Documents/tx.txt",'r')
for x in a:
    if x[0]=='H':
        print(x)
    else:
        print('Not Found')
