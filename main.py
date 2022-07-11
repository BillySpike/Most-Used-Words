from functions import most_words
from functions import combine_files
import matplotlib.pyplot as plt
import sys

league = ["AskRiot.txt", "LoLChampRoad.txt", "LoLQuickThoughts.txt", "LoLSlashDev.txt"]
valorant = ["AskValorant.txt", "ValoGuns.txt", "ValoHealth.txt", "ValoMaps.txt", "ValoRandom.txt", "ValoStateAgent.txt"]
all_files = ["LoRDev.txt", "AllValo.txt", "AllLoL.txt"]

files = league + valorant + all_files

combine_files(league, "AllLoL.txt")
combine_files(valorant, "AllValo.txt")
combine_files(all_files, "AllDocs.txt")

sys.stdout = open("OutputData.txt", 'w')

for i in files:
    most_words(i, i)
    plt.savefig(i + ".png")

sys.stdout.close()
