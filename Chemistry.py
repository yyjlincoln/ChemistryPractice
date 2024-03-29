# Chem

import random
import os
import time


Substance = {
    'Mixture': {
        'Heterogeneous mixture': {
        },
        'Homogeneous mixture': {
        }
    },
    'Pure substance': {
        'Elements': {
            'Hydrogen': {
                'charge': +1,
                'symbol': 'H'
            },
            'Lithium': {
                'charge': +1,
                'symbol': 'Li'
            },
            'Sodium': {
                'charge': +1,
                'symbol': 'Na'
            },
            'Potassium': {
                'charge': +1,
                'symbol': 'K'
            },
            'Silver': {
                'charge': +1,
                'symbol': 'Ag'
            },
            'Magnesium': {
                'charge': +2,
                'symbol': 'Mg'
            },
            'Calcium': {
                'charge': +2,
                'symbol': 'Ca'
            },
            'Strontium': {
                'charge': +2,
                'symbol': 'Sr'
            },
            'Barium': {
                'charge': +2,
                'symbol': 'Ba'
            },
            'Zinc': {
                'charge': +2,
                'symbol': 'Zn'
            },
            'Aluminium': {
                'charge': +3,
                'symbol': 'Al'
            },
            'Hydroxide': {
                'charge': -1,
                'symbol': 'OH'
            },
            'Flouride': {
                'charge': -1,
                'symbol': 'Fl'
            },
            'Chloride': {
                'charge': -1,
                'symbol': 'Cl'
            },
            'Bromide': {
                'charge': -1,
                'symbol': 'Br'
            },
            'Iodide': {
                'charge': -1,
                'symbol': 'I'
            },
            'Oxide': {
                'charge': -2,
                'symbol': 'O'
            },
            'Sulfide': {
                'charge': -2,
                'symbol': 'S'
            },
            'Nitride': {
                'charge': -3,
                'symbol': 'N'
            },
            'Phosphide': {
                'charge': -3,
                'symbol': 'P'
            }
        },
        'Compounds': {
            'Hydroxide': {
                'charge': -1,
                'symbol': 'OH'
            },
            'Nitrate': {
                'charge': -1,
                'symbol': 'NO3'
            },
            'Nitrite': {
                'charge': -1,
                'symbol': 'NO2'
            },
            'Hydrogencarbonate': {
                'charge': -1,
                'symbol': 'HCO3'
            },
            'Bicarbonate': {
                'charge': -1,
                'symbol': 'HCO3'
            },
            'Hydrogensulfate': {
                'charge': -1,
                'symbol': 'HSO4'
            },
            'Dihydrogenphosphate': {
                'charge': -1,
                'symbol': 'H2PO4'
            },
            'Ethanoate': {
                'charge': -1,
                'symbol': 'CH3COO'
            },
            'Acetate': {
                'charge': -1,
                'symbol': 'CH3COO'
            },
            'Hypochlorite': {
                'charge': -1,
                'symbol': 'ClO'
            },
            'Cyanide': {
                'charge': -1,
                'symbol': 'CN'
            },
            'Permanganate': {
                'charge': -1,
                'symbol': 'MnO4'
            },
            'Carbonate': {
                'charge': -2,
                'symbol': 'CO3'
            },
            'Sulfate': {
                'charge': -2,
                'symbol': 'SO4'
            },
            'Sulfite': {
                'charge': -2,
                'symbol': 'SO3'
            },
            'Peroxide': {
                'charge': -2,
                'symbol': 'O2'
            },
            'Hydrogenphosphate': {
                'charge': -2,
                'symbol': 'HPO4'
            },
            'Dichromate': {
                'charge': -2,
                'symbol': 'Cr2O7'
            },
            'Chromate': {
                'charge': -2,
                'symbol': 'CrO4'
            },
            'Oxalate': {
                'charge': -2,
                'symbol': 'C2O4'
            },
            'Phosphate': {
                'charge': -3,
                'symbol': 'PO4'
            },
            'Ammonium': {
                'charge': +1,
                'symbol': 'NH4'
            }

        }
    }

}

c = []
e = []
corr, wrong = 0 , 0
for x in Substance['Pure substance']['Compounds']:
    c.append(x)
for x in Substance['Pure substance']['Elements']:
    e.append(x)

while True:
    if corr+wrong>0:
        print(corr,'/',corr+wrong,100*corr/(corr+wrong),'% Correct')
    if random.randint(0,1):
        r=random.choice(c)
        ans=Substance['Pure substance']['Compounds'][r]
        print(r)
    else:
        r=random.choice(e)
        ans=Substance['Pure substance']['Elements'][r]
        print(r)
    ri=input('>')
    if ri=='ans':
        print(ans)
    else:
        i=ri.split('+')
        if len(i)==2:
            if i[1]=='':
                i[1]='1'
            if ans['symbol']==i[0] and ans['charge'] == int(i[1]):
                print('correct!')
                corr+=1
            else:
                print('wrong')
                print(ans)
                wrong+=1
        else:
            i = ri.split('-')
            if len(i)==2:
                if i[1]=='':
                    i[1]='1'
                if ans['symbol']==i[0] and ans['charge'] == -int(i[1]):
                    corr+=1
                    print('correct!')
                else:
                    print('wrong')
                    print(ans)
                    wrong+=1
    time.sleep(1)
    os.system('clear')

    