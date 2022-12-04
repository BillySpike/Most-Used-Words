import pandas as pd


class Combine:
    def __init__(self):
        files = ['AllDocs.csv', 'AllLoL.csv', 'AllValo.csv', 'AskRiot.csv', 'AskValorant.csv', 'LoLChampRoad.csv',
                 'LoLQuickThoughts.csv', 'LoLSlashDev.csv', 'LoRDev.csv', 'ValoGuns.csv', 'ValoHealth.csv',
                 'ValoMaps.csv', 'ValoRandom.csv', 'ValoStateAgent.csv']

        combined = "Combined.csv"

        self.combine_csv(files[0], files, combined, 1)

    def combine_csv(self, f1, f2, comb, count):
        if count == len(f2):
            return
        d1 = pd.read_csv(f1)
        d2 = pd.read_csv(f2[count])
        c1 = d1.merge(d2,
                      on="word",
                      how="outer")
        c1 = c1[c1.columns.drop(c1.filter(regex='Unnamed'))]
        c1.to_csv(comb)
        self.combine_csv(comb, f2, comb, count + 1)


