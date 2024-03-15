import random
al = ['a' , 'b' , 'c' ,'d' , 'e' ,'f' , 'g' , 'h', 'i' ,'j' ,'k' , 'l' ,'m' ,'n', 'o' ,'p','q' , 'r','s', 't','u','v', 'w','x', 'y' ,'z']
AL = ['A' ,'B' ,'C' ,'D' ,'E', 'F', 'G', 'H' , 'I', 'G' , 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R','S', 'T','U','V','W','X','Y','Z']
num = ['0','1','2','3','4','5','6','7','8','9']
    
i = 1
while True:
    ia = random.randint(0,23)
    ia2 = random.randint(0,23) 
    iA = random.randint(0,23)
    iA2 = random.randint(0,23)
    inn = random.randint(0,9)
    inn2 = random.randint(0,9)
    iqu = random.randint(0,2)

    alph = al[ia]
    alph2 = al[ia2]
    Alph = AL[iA]
    Alph2 = AL[iA2]
    Num = num[inn]
    Num2 = num[inn2]
        
    if i > 2:
        paAssq = Alph + alph + Num 
    else:
        psAsq =   Alph + Alph2 + Num2 + Num +alph + alph2
    if i >= 3:
        break
    else:
        i = i+1
        continue 
    
    
pp = psAsq + paAssq
print(pp)