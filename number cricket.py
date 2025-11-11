from random import *
def bumrah(k): 
    a = str(randint(0,10))
    b=str(max(set(k), key=k.count))
    f= randint(0,1)
    if f==0:
        return a
    else:
        return b
def dhoni(k):
    f=1
    while f==1:
        a = str(randint(0,10))
        b=max(set(k), key=k.count)
        if a==b:
            continue
        else:
            return a
print('welcome to number cricket')
print('if the numbers are same the batsman is out')
print('here is the binary flip')
sides=['0','1']
user_toss= ''
comp_toss=''
while True:
    value1=input('choose 0 or 1: ')
    if value1=='0'or value1=='1':
        print('great')
        user_toss = int(value1)
        sides.remove(value1)
        comp_toss = int(sides[0])
        break
    else:
        print('try again')

#toss
toss=randint(0,1)
bat = ''
bowl = ''
if user_toss==toss:
    print('you won the toss')
else:
    print('computer won the toss')
us_choose = ''
if user_toss==toss:
    while True:
        value2 =input('choose bat or bowl: ')
        if value2=='bat'or value2=='bowl':
            us_choose = value2
            break
        else:
           print('try again')
    if us_choose=='bat':
        bat='user'
        bowl='comp'
    else:
        bat='comp'
        bowl='user'
else:
    ch=randint(0,1)
    if ch == 0:
        bat='user'
        bowl='comp'
    else:
        bat='comp'
        bowl='user'
#------------------------------------------------------------
if bat=='user':
    print('the game has 6 overs and 1 wicket (0-10 allowed)')
    ball=0
    user_score=0
    ball1=0
    comp_score = 0
    batter=['10']
    bowler=['10']
    while True:
        print(f"you're score: {user_score} computer score: {comp_score}")
        ba = bumrah(batter)
        bat= input('bat:')
        if bat=='0' or bat =='1'or bat=='2' or bat=='3' or bat=='4' or bat=='5' or bat=='6' or bat=='7' or bat=='8' or bat=='9' or bat=='10':
            print(ba)
            batter.append(bat)
            if ba == bat:
                print('out!')
                ball+=1
                if ball==1:
                    print('duck duck duck')
                break
            elif bat == '0':
                user_score+=int(ba)
                ball+=1
            else:
                user_score+=int(bat)
                ball+=1
        else:
            print('try again')
        if ball == 36:
            break
    
    
    while True:
        print(f"you're score: {user_score} computer score: {comp_score}")
        ba = dhoni(bowler)
        bat= input('bowl:')
        print(ba)
        if bat=='0' or bat =='1'or bat=='2' or bat=='3' or bat=='4' or bat=='5' or bat=='6' or bat=='7' or bat=='8' or bat=='9' or bat=='10':
            if ba == bat:
                print('out!')
                ball+=1
                if ball==1:
                    print('duck duck duck')
                break
            elif ba == '0':
                comp_score+=int(bat)
                ball1+=1
            else:
                comp_score+=int(ba)
                ball1+=1
        else:
            print('try again')
        if comp_score>user_score:
            break
        if ball1 == 36:
            break
if bowl=='user':
    ball1=0
    comp_score = 0
    ball=0
    user_score=0
    batter=['10']
    bowler=['10']
    while True:
        print(f"you're score: {user_score} computer score: {comp_score}")
        ba = dhoni(bowler)
        bat= input('bowl:')
        print(ba)
        if bat=='0' or bat =='1'or bat=='2' or bat=='3' or bat=='4' or bat=='5' or bat=='6' or bat=='7' or bat=='8' or bat=='9' or bat=='10':
            if ba == bat:
                print('out!')
                ball+=1
                if ball==1:
                    print('duck duck duck')
                break
            elif ba == '0':
                comp_score+=int(bat)
                ball1+=1
            else:
                comp_score+=int(ba)
                ball1+=1
        else:
            print('try again')
        if ball1 == 36:
            break
    print(f'{comp_score+1} runs to win')
    print('the game has 6 overs and 1 wicket (0-10 allowed)')
    

    while True:
        print(f"you're score: {user_score} computer score: {comp_score}")
        ba = bumrah(batter)
        bat= input('bat:')
        if bat=='0' or bat =='1'or bat=='2' or bat=='3' or bat=='4' or bat=='5' or bat=='6' or bat=='7' or bat=='8' or bat=='9' or bat=='10':
            print(ba)
            batter.append(bat)
            if ba == bat:
                print('out!')
                ball+=1
                if ball==1:
                    print('duck duck duck')
                break
            elif bat == '0':
                user_score+=int(ba)
                ball+=1
            else:
                user_score+=int(bat)
                ball+=1
        else:
            print('try again')
        if user_score>comp_score:
            break
        if ball == 36:
            break
print(f'your score : {user_score}')
print(f'Computer score : {comp_score} ')
if user_score>comp_score:
    win = user_score-comp_score
    print(f'you won by {win} scores')
elif user_score==comp_score:
    print('it is a draw')
else:
    win = comp_score-user_score
    print(f'computer won by {win} scores')