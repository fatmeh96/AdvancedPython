#Assume that the input is always consist from parentheses only.
def valid(sstr):
    dic1={"[":"]","{":"}","(":")"}
    listEven=[]
    listOdd=[]
    for i in range(len(sstr)):
        if i%2==0:
            listEven.append(sstr[i])
        else:
            listOdd.append(sstr[i])
    dic2={}
    if len(listEven)!=len(listOdd):
        print("Flase")
        return
    for i in range(len(listEven)):
        dic2[listEven[i]]=listOdd[i]
    dicVal=dic2.values()
    dicKey=dic2.keys()
    for k in dicKey:
        if dic1.keys().__contains__(k):
            if dic1[k]!=dic2[k]:
                print("False")
                return
    print("True")

valid("{}()[]")#true
valid("{}([]")#flase
valid("{}(}[]")#false
valid("({[)]")#false
valid("{{{")#false
valid("[)")#false
valid("()")#true


