email=input("Can you please provide your email\n")
wordlist=email.split('@')
names=wordlist[0].split('.')
fname=names[0]
domain=wordlist[1].split('.')
if(domain[0]=='gmail'):
    company='Google'
    print("Hey",fname,"I see your email is registered with ",company,". Thats so cool !")
else:
    company=domain[0]
    print("Hey",fname,",I see your email is registered with ",company,". U have got your own custom setup, Amazing !")
