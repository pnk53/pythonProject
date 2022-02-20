x= (input('Enter your String:'))
alpha='abcdefghijklmnopqrstuvwxyz'
t=''
i=0
k=1
t=t+alpha[((alpha.index(x[i]))+k)%26]
t=t+alpha[((alpha.index(x[i+1]))+k)%26]
t=t+alpha[((alpha.index(x[i+2]))+k)%26]
t=t+alpha[((alpha.index(x[i+3]))+k)%26]
t=t+alpha[((alpha.index(x[i+4]))+k)%26]
print(t)