# s = ['name','charge','sym']
s = ['Hydroxide',-1,'H','Flouride',-1,'Fl','Chloride',-1,'Cl','Bromide',-1,'Br','Iodide',-1,'I','Oxide',-2,'O','Sulfide',-2,'S','Nitride',-3,'N','Phosphide',-3,'P']
# print(len(s))
for x in range(int(len(s)/3)):
    d = f''''{s[x*3]}':{{
    'charge':{s[x*3+1]},
    'symbol':'{s[x*3+2]}'
}},'''
    print(d)