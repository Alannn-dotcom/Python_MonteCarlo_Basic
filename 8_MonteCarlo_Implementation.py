import random
import matplotlib
import matplotlib.pyplot as plt
import time

#Este programa nos dice cual es el mejor número para multiplicar la apuesta cada que perdemos, (spoiler: este esta entre 1.6-1.7)

lower_bust=31.235
higher_profit = 63.208

sampleSize = 1000
startingFunds = 10000
wagerSize = 100
wagercount = 100

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
    


def multiple_bettor(funds, initial_wager, wager_count):
    global multiple_busts
    global multiple_profits

    value = funds
    wager = initial_wager
    wX=[]
    vY=[]
    currentWager = 1
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
                
                if value <= 0:
                    #print ('nos fuimos a bancarrota antes de ', currentWager, ' apuestas')
                    multiple_busts+=1
                    break
                    
        elif previousWager == 'loss':
            #print ('perdimos, por lo que debemos ser listos y doblar la apuesta')
            
            if rolldice():
                wager = previousWagerAmount * random_multiple

                if(value - wager) < 0:
                    wager = value
                
                #print ('ganamos', wager)
                value += wager
                #print (value)
                
                wager = initial_wager
                previousWager = 'win'
                
                wX.append (currentWager)
                vY.append(value)
                
            else:
                wager = previousWagerAmount * random_multiple

                if(value - wager) < 0:
                    wager = value

                #print ('perdimos', wager)
                value -= wager

                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                
                if value <=0:
                    #print ('nos fuimos a bancarrota antes de ', currentWager, ' apuestas')
                    multiple_busts+=1
                    break

                #print (value)
                previousWager = 'loss' 
  
        currentWager +=1 
    #print (value)
    #plt.plot (wX, vY, color)
    if value > funds:
        multiple_profits +=1    


def simple_bettor(funds, initial_wager, wager_count, color):
    global simple_busts
    global simple_profits

    value = funds 
    wager = initial_wager

    wX = [] 
    vY = []

    currentWager=1

    while currentWager <= wager_count:
        if rolldice():
            value += wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentWager)
            vY.append(value)
        currentWager +=1

    if value <= 0:
        #value = 'broke'
        simple_busts += 1

    #print ('Funds: ', value, '\n')
    plt.plot(wX, vY, color)

    if value > funds:
        simple_profits += 1

def doubler_bettor(funds, initial_wager, wager_count, color):
    value = funds 
    wager = initial_wager
    global doubler_busts
    global doubler_profits

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
                
                if value <= 0:
                    #print ('nos fuimos a bancarrota antes de ', currentWager, ' apuestas')
                    doubler_busts+=1
                    break
                    
        elif previousWager == 'loss':
            #print ('perdimos, por lo que debemos ser listos y doblar la apuesta')
            
            if rolldice():
                wager = previousWagerAmount * 2

                if(value - wager) < 0:
                    wager = value
                
                #print ('ganamos', wager)
                value += wager
                #print (value)
                
                wager = initial_wager
                previousWager = 'win'
                
                wX.append (currentWager)
                vY.append(value)
                
            else:
                wager = previousWagerAmount * 2

                if(value - wager) < 0:
                    wager = value

                #print ('perdimos', wager)
                value -= wager

                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                
                if value <=0:
                    #print ('nos fuimos a bancarrota antes de ', currentWager, ' apuestas')
                    doubler_busts+=1
                    break

                #print (value)
                previousWager = 'loss' 
  
        currentWager +=1 
    #print (value)
    plt.plot (wX, vY, color)
    if value > funds:
        doubler_profits +=1

while True:
    multiple_busts = 0.0
    multiple_profits = 0.0

    multipleSampSize = 100000 #vamos a correr el multiple_bettor esta cantidad de veces.
    currentSample = 1

    random_multiple=random.uniform(0.1, 10.0)

    while currentSample <= multipleSampSize:
        multiple_bettor(startingFunds,wagerSize,wagercount)
        currentSample += 1

    if ((multiple_busts/multipleSampSize)*100.00 < lower_bust) and ((multiple_profits/multipleSampSize)*100.00 > higher_profit):
        print ("############################################")

        print ("Found a WINWINWINER, the multiple was: ", random_multiple)
        print ("Lower bust to beat: ", lower_bust)
        print("Higher profit rate to beat: ", higher_profit)
        print("bust rate: ", (multiple_busts/multipleSampSize)*100.00)
        print("profit rate: ", (multiple_profits/multipleSampSize)*100.00)
 
        print ("############################################")
    
    else:
        pass
        '''print ("############################################")

        print ("Found a LOSER, the multiple was: ", random_multiple)
        print ("Lower bust to beat: ", lower_bust)
        print("Higher profit rate to beat: ", higher_profit)
        print("bust rate: ", (multiple_busts/multipleSampSize)*100.00)
        print("profit rate: ", (multiple_profits/multipleSampSize)*100.00)
 
        print ("############################################")'''

