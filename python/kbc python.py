que=[["what color is the sky?","pink","black","blue","green","none",3],
["what color is the sky?","pink","black","blue","green","none",3],
["what color is the sky?","pink","black","blue","green","none",3],
["what color is the sky?","pink","black","blue","green","none",3],
["what color is the sky?","pink","black","blue","green","none",3],
["what color is the sky?","pink","black","blue","green","none",3]]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money=0
for i in range(0,len(que)):
    que1=que[i]
    print(f"Question for Rs.{levels[i]}")
    print(f"A.{que1[1]}      B.{que1[2]}")
    print(f"C.{que1[3]}      D.{que1[4]}")
    reply=int(input("Enter your answer (1-4):"))
    if (reply==que1[-1]):
        print(f"Correct answer,you have won Rs.{levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
    else:
        print("Wrong Answer!!")
        break
print(f"You have won Rs.{money}")