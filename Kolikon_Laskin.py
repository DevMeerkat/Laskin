import pandas as pd
from pathlib import Path
import glob
import os
import time
import sys
################# CONFIG #####################
#
#
rounding = True
animation = True
#
#
##############################################


def prints(str):
    if animation:
       for c in str + '\n':
         sys.stdout.write(c)
         sys.stdout.flush()
         time.sleep(3./90)
    else:
        print(str)


# Finding the newest file
prints("Paina 1, jos haluat automaattisen tiedoston etsinnän. Paina 2 jos haluat syöttää itse tiedoston sijainin.\n")
valinta = input("")

def laskin():
    # Gathering the necessary information
    df = pd.read_csv(file) # Reads the csv file
    sheetTotal = df['Words'].sum() # Counts the words in the csv file
    translator_joona = df.loc[df['Translator'] == 297410829589020673, 'Words'].sum()
    translator_siri = df.loc[df['Translator'] == 696421760890962061, 'Words'].sum()
    translator_susmot = df.loc[df['Translator'] == 404554986396319744, 'Words'].sum()
    translator_nuclide = df.loc[df['Translator'] == 541652140687360010, 'Words'].sum()
    proofreader_susmot = df.loc[df['Proofreader(s)'] == 404554986396319744, 'Words'].sum()
    proofreader_nuclide = df.loc[df['Proofreader(s)'] == 541652140687360010, 'Words'].sum()

    # Presenting user with information
    prints(f"Sheetin sanamäärä: {sheetTotal}")
    prints("Käännetyt sanat")
    print("Masterjoona:",translator_joona, "\nSiri:",translator_siri, "\nSusmot:", translator_susmot, "\nNuclide:",translator_nuclide)
    prints("---------------------")
    prints("Proofreadatut sanat:")
    print("Susmot:", proofreader_susmot, "\nNuclide:", proofreader_nuclide)
    prints("---------------------")

    # Taking proofreaders into the calculation
    totalWords = int(sheetTotal) + (int(sheetTotal) * 0.85)
    proofreader_susmot = proofreader_susmot * 0.85
    proofreader_nuclide = proofreader_nuclide * 0.85

    # Combining proofread and Translated
    reward_susmot = int(proofreader_susmot) + int(translator_susmot)
    reward_nuclide = int(proofreader_nuclide) + int(translator_nuclide)

    # Calculating rewards
    reward_joona = translator_joona * 7.5 / int(totalWords)
    reward_siri = int(translator_siri) * 7.5 / int(totalWords) 
    reward_nuclide = reward_nuclide * 7.5 / int(totalWords) 
    reward_susmot = reward_susmot * 7.5 / int(totalWords) 

    if rounding: # If rounding is turned ON in the config, rounds the answers to 2 decimals.

        # Rounding up to 2 decimals
        reward_joona = str(round(reward_joona, 2))
        reward_siri = str(round(reward_siri, 2))
        reward_nuclide = str(round(reward_nuclide, 2))
        reward_susmot = str(round(reward_susmot, 2))
    # Showing rewards to the user
    prints("\n")
    prints("     Palkinnot")
    prints("---------------------")
    prints('Masterjoona ' + reward_joona)
    prints('Siri '+ reward_siri)
    prints('Susmot '+ reward_susmot)
    prints('Nuclide '+ reward_nuclide)
    prints("---------------------")
    time.sleep(10)
    input("Paina ENTER sulkeaksesi laskimen")

def autoFindCsv():
    prints("Etsitään uusinta sheettiä")
    downloads_path = str(Path.home() / "Downloads") # Goes to %userprofile%\Downloads
    list_of_files = glob.glob(downloads_path + "\\*.csv") # Finds all .csv files
    global file
    file = max(list_of_files, key=os.path.getmtime) # Finds the newest one
    # Telling the user whats happening
    prints("Uusin sheetti löytynyt: " + file)
    prints("---------------------")
    laskin()
if valinta == "1":
    autoFindCsv()
if valinta == "2":
    global file
    file = input("Anna tiedoston sijainti\n")
    laskin()
else:
    time.sleep(1)
    prints(valinta + " ei ole 1 tai 2")
    time.sleep(1)
    prints("Otetaan käyttöön automaattinen valinta")
    time.sleep(1)
    prints("\n")
    autoFindCsv()
