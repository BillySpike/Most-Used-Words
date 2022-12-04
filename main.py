from functions import most_words
from functions import combine_files
from combine import Combine
import matplotlib.pyplot as plt
import sys

league = ["AskRiot", "LoLChampRoad", "LoLQuickThoughts", "LoLSlashDev"]
valorant = ["AskValorant", "ValoGuns", "ValoHealth", "ValoMaps", "ValoRandom", "ValoStateAgent"]
all_files = ["LoRDev", "AllValo", "AllLoL"]
combined = "Combined"

files = league + valorant + all_files + ["AllDocs"]
combine_file = league + valorant + all_files

combine_files(league, "AllLoL.txt")
combine_files(valorant, "AllValo.txt")
combine_files(all_files, "AllDocs.txt")

for i in files:
    sys.stdout = open(i + ".csv", 'w')
    print("word" + "," + i + "Amount")
    most_words(i + ".txt", i)
    plt.savefig(i + ".png")
    sys.stdout.close()

Combine()

