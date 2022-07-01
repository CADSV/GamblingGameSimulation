#Needed imports
from views.utils import (
    create_menu, #To create the menu
    clear_screen, #To clear the screen
    exit_system, #To exit the system
)

from exceptions.menu_exceptions import InexistentMenuOptionError #Exception of an inexistent menu option selected
from controllers.simulation import simulation #To call the simulation function

#Function use to create the simulation menu
def simulation_menu(context: dict) -> dict:

    selected_option = None
    simulation_menu_options = ['Simular una partida', 'Simular BONUS', 'Volver al Menú Principal','Salir del Programa']


    while(True):
        try:
            clear_screen()

            create_menu(simulation_menu_options, '            MENÚ SIMULACIÓN')

            selected_option = int(input('Por favor seleccione una opción: '))


            if (selected_option == 1):
                simulation(context,False)
            
            elif (selected_option == 2):
                simulation(context,True)

            elif (selected_option == 3):
                break

            elif (selected_option == 4):
                exit_system()

            else:
                raise InexistentMenuOptionError('¡ERORR! La opción seleccionada no existe. Por favor seleccione una opción válida :(')


        except InexistentMenuOptionError as e:
                print(f'\n\n{e}\n')
                input('Por favor presione cualquier tecla para continuar...')

        except ValueError:
                print('\n\n¡ERROR! El valor ingresado no es valido, por favor intente nuevamente con un número entero :(\n')	
                input('Por favor presione cualquier tecla para continuar...')

    return context