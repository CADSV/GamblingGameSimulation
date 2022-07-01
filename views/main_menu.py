#Needed imports
from views.utils import (
    create_menu, #To create the menu
    clear_screen, #To clear the screen
    exit_system, #To exit the system
)

from views.simulation_menu import simulation_menu #To call the simulation menu

from exceptions.menu_exceptions import InexistentMenuOptionError #Exception of an inexistent menu option selected


#Function use to create the main menu
def main():
    context = {}
    selected_option = None
    main_menu_options = ['Simulación', 'Salir del Programa']

    while(True):
        try:
            clear_screen()

            print('\n')
            print('Bienvenidos al Simulador del Juego de Apuestas de Investigación de Operaciones\n')
            print('Desarrollado por: Alejandro Pestana y Carlos Doffiny S-V')

            create_menu(main_menu_options, '            MENÚ PRINCIPAL')

            selected_option = int(input('Por favor seleccione una opción: '))

            if (selected_option == 1):
                simulation_menu(context)

            elif (selected_option == 2):
                exit_system()

            else:
                raise InexistentMenuOptionError('¡ERORR! La opción seleccionada no existe. Por favor seleccione una opción válida :(')

        except ValueError:
            print('\n\n¡ERROR! El valor ingresado no es valido, por favor intente nuevamente con un número entero :(\n')	
            input('Por favor presione cualquier tecla para continuar...')
        
        except (InexistentMenuOptionError) as e:
            print(f'\n\n{e}\n')
            input('Por favor presione cualquier tecla para continuar...')
