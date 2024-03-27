def rezultats(sk1, sk2):
    if sk1<6 and sk2<6:
        rez = sk1*sk2
    else:
        rez = sk1+sk2
    
    return rez

for skaitlis in range(1, 11, 2):      #range - funkcija, kas skaita skaitļus
    for otrs in range(2,11, 2):
        print("mūsu skaitlis:", skaitlis, "otrais skaitlis:", otrs, "rezultāts: ", rezultats(skaitlis, otrs))

 




skaitlis1 = 7
skaitlis2 = 3



print("pirmais skaitlis:", skaitlis1)
print("otrais skaitlis", skaitlis2)
print("rezultats:", rezultats(skaitlis1,skaitlis2))