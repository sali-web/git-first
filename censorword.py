#censoring a word
 
text = input("Enter your text: ")
word = input("Choose a word from the previously entered text to be censored: ")

def censor(text,word):
    t=text.split()
    n=[]
    for i in t:
        if(i==word):
            n.append("*"*len(word))
        else:
            n.append(i)
    return " ".join(n)
   
file = open("censored.txt","w")
file.write(censor(text,word))
