st=input("Enter the message :")
words=st.split(" ")
coding=input("1 for coding or 0 for decoding :")
coding=True if (coding=="1") else False
if(coding):
    nwords=[]
    for word in words:
        if(len(word)>=3):
          import random
          item=['q','w','e','r','t','y','u','i','o','p','z','x','c','v','b','n','m','a','s','d','f','g','h','j','k','l']
          st1=random.choice(item)
          st2=random.choice(item)
          st3=random.choice(item)
          st4=random.choice(item)
          st5=random.choice(item)
          st6=random.choice(item)
          stnew= st1 + st3 + st5 + word[1:] + word[0] + st2 +st4 + st6
          nwords.append(stnew)
        else:
          nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords=[]
    for word in words:
        if(len(word)>=3):
          stnew=word[3:-3]
          stnew= stnew[-1] + stnew[:-1]
          nwords.append(stnew)
        else:
          nwords.append(word[::-1])
    print(" ".join(nwords))
    
          