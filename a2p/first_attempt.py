import pandas as pd
import numpy as np
import os
import re

df = pd.read_csv(f"{os.getcwd()}/a2p/data.csv")
print(df)

class Node():
    def __init__(self, userid, idea, time):
        # userid är emailadress
        self.userid = userid
        # idea är iden i råtext
        self.idea = idea
        # time  är time submitted
        self.time = time
        self.highlights = self.makehighlights()

    def makehighlights(self):
        # OBS EJ KLAR MÅSTE GÖRAS
        returnset = set()
        return returnset