#Needed imports
from views.utils import (
    clear_screen, #To clear the screen
)

import random


#Function of the simulations
def simulation(context: dict, bonus: int) -> dict:

    clear_screen()
    
    initialAmount = int(input('Ingrese el monto inicial de su cartera: '))
    initialBet = int(input('Ingrese el monto de la apuesta mínima: '))
    target = int(input('Ingrese el monto en el cual se ganará el juego: '))
    rounds = int(input('Ingrese el número de rondas a jugar: '))
    plays = []
    consecutiveLosses = 0
    numBets = 0
    simulation = []
    bet = initialBet
    amount = initialAmount

    for i in range(rounds):

        while 0 < initialAmount < target:
            plays.append({
                'monto_antes': initialAmount,
                'bet': (bet := min(bet, initialAmount)),
                'rand': (rand := random.uniform(0,1)),
                'victoria': (victory := rand < 0.5),
                'nuevo_monto': (initialAmount := min(target, initialAmount + bet) if victory else max(initialAmount - bet, 0)),
            })
            print(plays)
            input()
            consecutiveLosses = 0 if victory else consecutiveLosses + 1
            bet = initialBet if victory else bet * 2 ** consecutiveLosses
            numBets = numBets + 1

        
        simulation.append( {
            'meta_alcanzada': 'SI' if initialAmount == target else 'QUIEBRA',
            'num_bets': numBets,
            'jugadas': plays
        })

        plays = []
        numBets = 0
        consecutiveLosses = 0
        bet = initialBet
        initialAmount = amount
        print(simulation)
        print('\n\n')
        input()

    return context


    print(simulation)
    input()
    return context