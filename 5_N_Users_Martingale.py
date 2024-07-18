import random
import matplotlib
import matplotlib.pyplot as plt
import time

def rolldice():
    roll = random.randint(1,100)
    
    if roll == 100:
        #print (roll,'roll was 100, you lose. What are the odds?! Play Again')
        return False
        
    elif roll <=50:
        #print (roll, 'roll was 1-50, you lose. Play Again')
        return False
        
    elif 100 > roll > 50:
        #print (roll, 'roll was 51-99, you win!')
        return True

def doubler_bettor(funds, initial_wager, wager_count):
    value = funds 
    wager = initial_wager
    global broke_count

    wX = []
    vY = []

    currentWager=1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        
        if previousWager == 'win':
            #print ('Ganamos la apuesta, genial!')
            
            if rolldice():
                
                value += wager
                #print (value)
                
                wX.append(currentWager)
                vY.append(value)
                
            else:
                
                value -= wager
                previousWager = 'loss'
                #print(value)
                previousWagerAmount = wager
                
                wX.append(currentWager)
                vY.append(value)
                
                if value < 0:
                    #print ('nos fuimos a bancarrota antes de ', currentWager, ' apuestas')
                    broke_count+=1
                    break
                    
        elif previousWager == 'loss':
            #print ('perdimos, por lo que debemos ser listos y doblar la apuesta')
            
            if rolldice():
                wager = previousWagerAmount * 2
                
                #print ('ganamos', wager)
                value += wager
                #print (value)
                
                wager = initial_wager
                previousWager = 'win'
                
                wX.append (currentWager)
                vY.append(value)
                
            else:
                wager = previousWagerAmount * 2
                
                #print ('perdimos', wager)
                value -= wager
                
                if value <0:
                    #print ('nos fuimos a bancarrota antes de ', currentWager, ' apuestas')
                    broke_count+=1
                    break

                #print (value)
                previousWager = 'loss' 

                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                
        currentWager +=1 
    #print (value)
    plt.plot (wX, vY)

xx = 0
broke_count=0
 
while xx <1000:
    doubler_bettor(10000, 100, 100)
    xx+=1

print ('Ratio de perder: ', (broke_count/float(xx)) * 100)
print ('Ratio de sobrevivir: ', 100 - (broke_count/float(xx)) * 100)

plt.axhline(0, color='r')
plt.show()

