#  File: Bowling.py
#  Description: Calculates Bowling Scores
#  Student's Name: Julio Gonzalez
#  Student's UT EID: jcg3245
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 9/3/16
#  Date Last Modified:

def main():

    in_file = open ("./scores.txt", "r")
    
    score = 0
    for line in in_file:
        print("  1   2   3   4   5   6   7   8   9    10")
        print("+---+---+---+---+---+---+---+---+---+-----+")
        print("|",end='')
        line = line.strip()
        line = line.split()
        day = []
        number = 0
        for i in line:
            day.append(i)
            number +=1
            if i == "X" and (number != 19 and number !=20 and number !=21):
                day.append(" ")
                number +=1
        for i in range(len(day)):
            if i%2==0 and i<19:
                print(day[i],end=' ')
            else:
                if i<18:
                    print(day[i],end='|')
                elif i ==19:
                    print(day[i],end=' ')
                elif i ==20:
                    print(day[i],end='')
        if len(day)==20:
            print(" |")
        else:
            print("|")
        print("|",end='')
        fay=[]
        for i in range(len(day)):
            if day[i]=='-':
                fay.append(int(0))
            elif day[i]=='/' or day[i]==' ':
                fay.append(day[i])
            elif day[i]=='X':
                fay.append(int(10))
            else:
                fay.append(int(day[i]))

        score = 0
        for i in range(len(fay)):
            if i%2!=0 and i <19:
                if fay[i]=='/':
                    score = score+10+fay[i+1]
                    print('%3s'%score,end='|')
                elif fay[i]==' ':
                    if fay[i+2]==' ':
                        score = score+10+fay[i+1]+fay[i+3]
                        print('%3s'%score,end='|')
                    elif fay[i+2]=='/':
                        score = score+20
                        print('%3s'%score,end='|')
                    else:
                        score = score+10+fay[i+1]+fay[i+2]
                        print('%3s'%score,end='|')
                else:
                    score = score+fay[i]+fay[i-1]
                    print('%3s'%score,end='|')
            elif len(fay)==20 and i>18:
                score=score+fay[18]+fay[19]
                print('%5s'%score,end='|')
            elif len(fay)==21 and i>19:
                if fay[i-1]=='/':
                    score=score+10+fay[i]
                    print('%5s'%score,end='|')
                elif fay[i]=='/':
                    score=score+20
                    print('%5s'%score,end='|')
                else:
                    score=score+fay[i-2]+fay[i-1]+fay[i]
                    print('%5s'%score,end='|')
        print()
        print("+---+---+---+---+---+---+---+---+---+-----+")
        print()

            
    





main()

