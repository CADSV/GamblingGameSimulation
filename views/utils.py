# Needed imports
import os #To work with Operating System of the computer running the program
import sys

# Function use to create the program menu's
def create_menu(menu_options: list[str], title: str):
    print('\n')
    print(f'{title}') #Print the menu title

    for i in range(20): #Print a separator line
        print('**', end='')
    print('\n')

    for i in range(len(menu_options)): #Print the menu options
        print(f'  {i+1}- {menu_options[i]}') #Print the options with their number
    print('\n\n')

#Function use to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') #To clean the screen in windows or linux


# Function use to exit the program
def exit_system():
    clear_screen()
    print('\n')
    print('Espero que haya sido de su agrado. Hasta pronto :)')
    print('\n')
    input('Por favor presione cualquier tecla para salir...')
    sys.exit()