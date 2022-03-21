import csv
from this import d
import pandas as pd
from connexion_tweet import Connexion


Connexion.create_table()
Connexion.load_infile_table()
procedure = Connexion.procedure("Guerre")

# print(procedure)
