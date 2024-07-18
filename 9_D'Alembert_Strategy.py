import random
import matplotlib
import matplotlib.pyplot as plt
import time

#Este programa emplea la estrategía D'Alambert para una probabilidad 50/50

lower_bust=31.235
higher_profit = 63.208

sampleSize = 1000

startingFunds = 100000
wagerSize = 100
wagercount = 100000

'''def rolldice():
    roll = random.randint(1,100)
    
    if roll == 100:
        #print (roll,'roll was 100, you lose. What are the odds?! Play Again')
        return False
        
    elif roll <=50:
        #print (roll, 'roll was 1-50, you lose. Play Again')
        return False
        
    elif 100 > roll > 50:
        #print (roll, 'roll was 51-99, you win!')
        return True'''

def rolldice():
    roll = random.randint(1,100)
    
    if roll <=50:
        #print (roll, 'roll was 1-50, you lose. Play Again')
        return False
        
    elif roll >= 51:
        #print (roll, 'roll was 51-100, you win!')
        return True
    

    

def dalembert(funds, initial_wager, wager_count):
    
    global Ret
    global da_busts
    global da_profits

    value = funds
    wager = initial_wager
    currentWager = 1
    previousWager =  'win'
    previousWageramount = initial_wager

    while currentWager <= wager_count:

        if previousWager =='win':

            if wager == initial_wager:
                pass
            else:
                wager -= initial_wager

            #print("\nApuesta actual: ", wager, "Value: ", value)

            if rolldice():
                value += wager

                #print("we won, current value: ", value)

                previousWageramount = wager

            else:
                value -= wager
                previousWager = 'loss'

                #print("We loss, current value: ",value)

                previousWageramount = wager

            if value <=0:
                #print("\t\t\tBANCARROTA.")
                da_busts += 1
                break
        
        elif previousWager == 'loss':
            wager = previousWageramount + initial_wager
            if (value - wager) <= 0:
                wager = value 

            #print("\nWe lost the last wager, current wager: ", wager, "value: ", value)

            if rolldice():
                value += wager
                #print ("we won, current value: ", value)
                previousWageramount = wager
                previousWager = 'win'
            
            else:
                value -= wager
                #print("we lost, current value: ", value)
                previousWageramount = wager

                if value <=0 :
                    #print("\t\t\tBANCARROTA.")
                    da_busts += 1
                    break

        currentWager+=1
    
    if value > funds:
        da_profits += 1
    
    #print (value)

    Ret+=value





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

Ret = 0.0
da_busts = 0.0
da_profits = 0.0
daSampSize = 1000000

counter = 1
while counter <= daSampSize:
    dalembert(startingFunds, wagerSize, wagercount)
    counter +=1

print ("Total invested: ", daSampSize*startingFunds)
print ("Total Return: ", Ret)
print ("ROI: ", Ret-daSampSize*startingFunds)

print("Bust rate: ", (da_busts/daSampSize)*100.00)
print("Profit rate: ", (da_profits/daSampSize)*100.00)