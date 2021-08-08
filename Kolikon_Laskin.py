import pandas as pd
from pathlib import Path
import glob
import os
print("Etsitään uusinta sheettiä")


################# CONFIG #####################
#
#
rounding = True
#
#
##############################################
# Finding the newest file
downloads_path = str(Path.home() / "Downloads") # Goes to %userprofile%\Downloads
list_of_files = glob.glob(downloads_path + "\\*.csv") # Finds all .csv files
file = max(list_of_files, key=os.path.getmtime) # Finds the newest one

# Telling the user whats happening
print("Uusin sheetti löytynyt:", file)
print("---------------------")

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
print(f"Sheetin sanamäärä: {sheetTotal}")
print("Käännetyt sanat")
print("Masterjoona:",translator_joona, "\nSiri:",translator_siri, "\nSusmot:", translator_susmot, "\nNuclide:",translator_nuclide)
print("---------------------")
print("Proofreadatut sanat:")
print("Susmot:", proofreader_susmot, "\nNuclide:", proofreader_nuclide)
print("---------------------")

# Taking proofreaders into the calculation
totalWords = int(sheetTotal) + (int(sheetTotal) * 0.85)
proofreader_susmot = proofreader_susmot * 0.85
proofreader_nuclide = proofreader_nuclide * 0.85

# Combining proofread and Translated
reward_susmot = int(proofreader_susmot) + int(translator_susmot)
reward_nuclide = int(proofreader_nuclide) + int(translator_nuclide)

# Calculating rewards
reward_joona = int(translator_joona) * 7.5 / int(totalWords)
reward_siri = int(translator_siri) * 7.5 / int(totalWords) 
reward_nuclide = reward_nuclide * 7.5 / int(totalWords) 
reward_susmot = reward_susmot * 7.5 / int(totalWords) 

if rounding: # If rounding is turned ON in the config, rounds the answers to 2 decimals.

    # Rounding up to 2 decimals
    reward_joona = str(round(reward_joona, 2))
    reward_siri = str(round(reward_siri, 2))
    reward_nuclide = str(round(reward_nuclide, 2))
    reward_susmot = str(round(reward_susmot, 2))
    total = float(reward_joona) + float(reward_susmot) + float(reward_nuclide) + float(reward_siri)

    
    # Making sure the total isnt higher than 7.5
    if float(7.5) == total:
        print("\n\n")
        print("---------------------")
        print("     Palkinnot")
        print("---------------------")
        print("")
        print('Masterjoona', reward_joona)
        print('Siri', reward_siri)
        print('Susmot ', reward_susmot)
        print('Nuclide', reward_nuclide)
        print("---------------------")
        print("\n\n")
        print(total)
        print("owo")
        input("Paina ENTER sulkeaksesi laskimen")
    elif float(7.5) < total:
        print(str(total) + " is more than 7.5")
    elif float(7.5) > total:
        print(str(total) + " is less than 7.5")
