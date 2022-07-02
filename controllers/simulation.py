#Needed imports
from fileinput import filename
from views.utils import (
    clear_screen, #To clear the screen
)

import random
import numpy as np
import pandas as pd
from datetime import datetime


#Function of the simulations
def simulation(context: dict, bonus: int) -> dict:

    clear_screen()
    
    initialAmount = int(input('Ingrese el monto inicial de su cartera: '))
    initialBet = int(input('Ingrese el monto de la apuesta mínima: '))
    target = int(input('Ingrese el monto en el cual se ganará el juego: '))
    rounds = int(input('Ingrese el número de rondas a jugar: '))
    plays = []
    consecutiveLosses = 0
    consecutiveWins = 0
    numBets = 0
    simulation = []
    bet = initialBet
    amount = initialAmount

    for i in range(rounds):

        while 0 < initialAmount < target:
            plays.append({
                'monto_antes': initialAmount,
                'apuesta': (bet := min(bet, initialAmount)),
                'rand': (rand := random.uniform(0,1)),
                'victoria': (victory := rand < 0.5),
                'nuevo_monto': (initialAmount := min(target, initialAmount + bet) if victory else max(initialAmount - bet, 0)),
            })
            # print(plays)
            # print('\n')
            # input()

            if(bonus):
                consecutiveWins = consecutiveWins + 1 if victory else 0
                bet = bet * 2  if victory else initialBet
            else:
                consecutiveLosses = 0 if victory else consecutiveLosses + 1
                bet = initialBet if victory else bet * 2 

            numBets = numBets + 1

        
        simulation.append( {
            'meta_alcanzada': 'SI' if initialAmount == target else 'QUIEBRA',
            'numero_apuestas': numBets,
            'jugadas': plays
        })

        plays = []
        numBets = 0
        consecutiveLosses = 0
        consecutiveWins = 0
        bet = initialBet
        initialAmount = amount
        # print(simulation)
        # print('\n\n')
        # input()
        
    context['simulation'] = simulation

    calculations(context, rounds, initialAmount, target)

    return context


def calculations(context: dict, rounds: int, initialAmount: int, target: int) -> dict:

    clear_screen()

    victories: int = np.count_nonzero([1 if simulation['meta_alcanzada'] == 'SI' else 0 for simulation in context['simulation']])
    average = victories / rounds
    print(f"\nLa probabilidad porcentual de llegar a la meta es de: {average:.0%}")
    hope: float =  ( (target - initialAmount)*average - initialAmount * (1 - average) )
    print(f"\nLa ganancia esperada es de: {hope:.2g} u.m.")


    xlsx_file = export_excel(context['simulation'])
    print(f'\nSe ha guardado la simulación en el excel ubicado en "{xlsx_file}"')



    return context




def export_excel(resultados: list[dict]) -> str:

    filename = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}'

    dataset = []
    for index, simulation in enumerate(resultados):
        for play in simulation['jugadas']:
            dataset.append((index + 1, play['monto_antes'], play['apuesta'], play['rand'],
                            'sí' if play['victoria'] else 'no', play['nuevo_monto'], simulation['meta_alcanzada']))
    cols = [
        'Número de la corrida',
        'Cantidad antes de jugar',
        'Monto de la Apuesta',
        'Número aleatorio',
        '¿Se ganó el juego?',
        'Cantidad luego de jugar',
        '¿Se llegó a la meta?'
    ]


    df = pd.DataFrame(dataset, columns=cols)

    df.to_excel(xlsx_file := f'{filename}.xlsx', index=False)


    return xlsx_file