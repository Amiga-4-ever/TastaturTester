import keyboard
import os

def on_key_pressed(event):


    # Lösche vor dem Drucken den Bildschirm
    # für UNIX:
    # os.system('clear' if os.name == 'posix' else 'cls')
    os.system('cls')


    print("######################################################################")
    print("############ K  E  Y  B  O  A  R  D  - T  E  S  T  E  R  #############")
    print("")
    print(". -------------------------------------------------------------------.")        
    print("| [Esc] [F1][F2][F3][F4][F5][F6][F7][F8][F9][F0][F10][F11][F12] o o o|")        
    print("|                                                                    |")     
    print("| [^][1][2][3][4][5][6][7][8][9][0][ß][´][_<_] [I][H][U] [N][/][*][-]|")        
    print("| [|-][Q][W][E][R][T][Z][U][I][O][P][Ü][+] | | [D][E][D] [7][8][9]|+||")        
    print("| [CAP][A][S][D][F][G][H][J][K][L][Ö][Ä][#]|_|           [4][5][6]|_||")        
    print("| [^][<][Y][X][C][V][B][N][M][,][.][-] [__^__]    [^]    [1][2][3]| ||")        
    print("| [c]   [a][________________________][a]   [c] [<][V][>] [ 0  ][,]|_||")        
    print("`--------------------------------------------------------------------'")
    print("")
    print("#####################################################################")
    print("# Drücke eine Taste: (ESC zum beenden)...")

    if event is not None:
        print(f"Folgende Taste wurde gedrückt: {event.name}")

# Startbildschirm einmalig anzeigen
# für UNIX:
# os.system('clear' if os.name == 'posix' else 'cls')
os.system('cls')
on_key_pressed(None)


keyboard.on_press(on_key_pressed)

keyboard.wait('esc')

# ausführbare Datei: pyinstaller.exe --onefile --icon=icon.ico main.py