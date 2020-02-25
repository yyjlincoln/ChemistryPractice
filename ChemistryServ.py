# Chem

import random
import os
import time
import flask
import flask_cors
import threading

app = flask.Flask(__name__)
flask_cors.CORS(app)
command = ''
scores = {}

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
            'Fluoride': {
                'charge': -1,
                'symbol': 'F'
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



# c = []
# e = []
# corr, wrong = 0 , 0
# for x in Substance['Pure substance']['Compounds']:
#     c.append(x)
# for x in Substance['Pure substance']['Elements']:
#     e.append(x)

# while True:
#     if corr+wrong>0:
#         print(corr,'/',corr+wrong,100*corr/(corr+wrong),'% Correct')
#     if random.randint(0,1):
#         r=random.choice(c)
#         ans=Substance['Pure substance']['Compounds'][r]
#         print(r)
#     else:
#         r=random.choice(e)
#         ans=Substance['Pure substance']['Elements'][r]
#         print(r)
#     ri=input('>')
#     if ri=='ans':
#         print(ans)
#     else:
#         i=ri.split('+')
#         if len(i)==2:
#             if i[1]=='':
#                 i[1]='1'
#             if ans['symbol']==i[0] and ans['charge'] == int(i[1]):
#                 print('correct!')
#                 corr+=1
#             else:
#                 print('wrong')
#                 print(ans)
#                 wrong+=1
#         else:
#             i = ri.split('-')
#             if len(i)==2:
#                 if i[1]=='':
#                     i[1]='1'
#                 if ans['symbol']==i[0] and ans['charge'] == -int(i[1]):
#                     corr+=1
#                     print('correct!')
#                 else:
#                     print('wrong')
#                     print(ans)
#                     wrong+=1
#     time.sleep(1)
#     os.system('clear')


c = []
e = []
corr, wrong = 0 , 0
for x in Substance['Pure substance']['Compounds']:
    c.append(x)
for x in Substance['Pure substance']['Elements']:
    e.append(x)

@app.route('/next')
def nextWord():
    # 
    ip = flask.request.headers.get('X-Real-IP')
    # 
    t = flask.request.values.get('type')
    if t:
        try:
            t=int(t)
        except:
            return {
                'code':-1,
                'msg':'Invalid type. Should be int'
            }
    else:
        t=-1
    
    #
    if ip not in scores:
        scores[ip] = {
            'correct':0,
            'incorrect':0
        }
    #
    if t==0:
        r=random.choice(e)
        return {
            'code':0,
            'word':r,
            'setcorrect':scores[ip]['correct'],
            'setincorrect':scores[ip]['incorrect']            
        }
    elif t==1:
        r=random.choice(c)
        return {
            'code':0,
            'word':r,
            'setcorrect':scores[ip]['correct'],
            'setincorrect':scores[ip]['incorrect']
        }
    elif t==-1:
        r=random.choice(e+c)
        return {
            'code':0,
            'word':r,
            'setcorrect':scores[ip]['correct'],
            'setincorrect':scores[ip]['incorrect']
        }

@app.route('/check', methods = ['GET','POST'])
def check():
    # 
    ip = flask.request.headers.get('X-Real-IP')
    # 
    w = flask.request.values.get('word')
    f = flask.request.values.get('equation')
    if w in Substance['Pure substance']['Compounds']:
        ifc = False
        ans = Substance['Pure substance']['Compounds'][w]
        i=f.split('+')
        if len(i)==2:
            if i[1]=='':
                i[1]='1'
            if ans['symbol']==i[0] and ans['charge'] == int(i[1]):
                ifc=True
            else:
                ifc=False
        else:
            i = f.split('-')
            if len(i)==2:
                if i[1]=='':
                    i[1]='1'
                if ans['symbol']==i[0] and ans['charge'] == -int(i[1]):
                    ifc=True
                else:
                    ifc=False
        #
        if ifc:
            if ip in scores:
                scores[ip]['correct']+=1
            else:
                scores[ip] = {
                    'correct':0,
                    'incorrect':0
                }
                scores[ip]['correct']=1
        else:
            if ip in scores:
                scores[ip]['incorrect']+=1
            else:
                scores[ip] = {
                    'correct':0,
                    'incorrect':0
                }
                scores[ip]['incorrect']=1
        #
        return {
            'code':0,
            'word':w,
            'type':1,
            'symbol':Substance['Pure substance']['Compounds'][w]['symbol'],
            'charge':Substance['Pure substance']['Compounds'][w]['charge'],
            'correct':ifc,
            'setcorrect':scores[ip]['correct'],
            'setincorrect':scores[ip]['incorrect']
        }

    elif w in Substance['Pure substance']['Elements']:
        ifc = False
        ans = Substance['Pure substance']['Elements'][w]
        i=f.split('+')
        if len(i)==2:
            if i[1]=='':
                i[1]='1'
            if ans['symbol']==i[0] and ans['charge'] == int(i[1]):
                ifc=True
            else:
                ifc=False
        else:
            i = f.split('-')
            if len(i)==2:
                if i[1]=='':
                    i[1]='1'
                if ans['symbol']==i[0] and ans['charge'] == -int(i[1]):
                    ifc=True
                else:
                    ifc=False
        #
        if ifc:
            if ip in scores:
                scores[ip]['correct']+=1
            else:
                scores[ip] = {
                    'correct':0,
                    'incorrect':0
                }
                scores[ip]['correct']=1
        else:
            if ip in scores:
                scores[ip]['incorrect']+=1
            else:
                scores[ip] = {
                    'correct':0,
                    'incorrect':0
                }
                scores[ip]['incorrect']=1
        #

        return {
            'code':0,
            'word':w,
            'type':0,
            'symbol':Substance['Pure substance']['Elements'][w]['symbol'],
            'charge':Substance['Pure substance']['Elements'][w]['charge'],
            'correct':ifc,
            'setcorrect':scores[ip]['correct'],
            'setincorrect':scores[ip]['incorrect']
        }
    else:
        return {
            'code':-1,
            'msg':'Not found'
        }

@app.route('/getEvents')
def getEvents():
    ip = flask.request.headers.get('X-Real-IP')
    c,i = 0,0
    if ip in scores:
        c, i = scores[ip]['correct'], scores[ip]['incorrect']
    return {
        'code':0,
        'command':command,
        'setcorrect': c,
        'setincorrect': i
    }

def autotype(string):
    try:
        if str(int(string)) == string:
            return int(string)
    except:
        pass
    
    try:
        if str(float(string)) == string:
            return float(string)
    except:
        pass
    
    try:
        if string == 'True':
            return True
    except:
        pass

    try:
        if string == 'False':
            return False
    except:
        pass

    return string

class getCommand(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        global command, scores
        while True:
            rc = input('Input Command >')
            c = rc.split(' ')
            # print(c)
            if c[0]=='score':
                if len(c)>1:
                    for x in range(1,len(c)):
                        if c[x] in scores:
                            print(scores[c[x]])
                        else:
                            print(c[x],'not found.')
                else:
                    print(scores)
            elif c[0]=='reset':
                if len(c)>1:
                    for x in range(1,len(c)):
                        if c[x] in scores:
                            print(scores[c[x]],'=>','{}')
                            scores[c[x]] = {
                                'correct':0,
                                'incorrect':0
                            }
                        else:
                            print(c[x],'not found.')                    
                else:
                    scores={}
            elif c[0]=='set':
                if len(c)>2:
                    if c[1] in scores:
                        i = 2
                        print('Altering',c[1])
                        for x in scores[c[1]]:
                            if i<len(c):
                                print('{',x,':',scores[c[1]][x],'} => {',x,':',autotype(c[i]),'}')
                                i+=1
                        if input('Accepted? [Y / N]: ').lower() == 'y':
                            i = 2
                            for x in scores[c[1]]:
                                if i<len(c):
                                    scores[c[1]][x] = autotype(c[i])
                                    print('Updated','{',x,':',c[i],'}')
                                    i+=1
                    else:
                        print('set: error -',c[1],'is not found.')
                else:
                    print('set: error - no target specified.')
            
            elif c[0]=='repl':
                print('Entering REPL, type .exit or exit() to exit')
                while True:
                    try:
                        cmd = input('REPL >')
                        if cmd == '.exit' or cmd == 'exit()':
                            break
                        else:
                            print(eval(cmd))
                    except Exception as e:
                        print('Exception:',e)

            if rc.startswith('send '):
                command = rc[5:]

g = getCommand()
g.setDaemon(True)
g.start()
