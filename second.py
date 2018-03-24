from nltk.tokenize import word_tokenize
import nltk
def main():
    sent =input('enter a sentence')
    word = nltk.word_tokenize(sent)
    #print(word)
    list1=nltk.pos_tag(word)
    #print(list1[0])
    #print(list1[1])
    for i in list1:
        str=""
        str1=""
        str=",".join(i)
        print(str)
        a=str.split(',')
        print(a[0])
        print(a[1])
        str=str.join(a[0])
        str1=str1.join(a[1])
        print("str1"+str1)
        if str1 == "VBG":
             try:
                file=open("verb.txt",'r')
                i=1
                b=[]
                while True:
                    line=file.readline().strip()
                    if not line:
                        break
                    b=line.split(':')
                         #print(i,b)
                    print(b[0])
                    print(b[1])
                    i=i+1
                    dict={b[0],b[1]}

                    if str in dict:
                        print(b[1])
             finally:
                    file.close()

    return

if __name__=="__main__":
    main()





























































































































