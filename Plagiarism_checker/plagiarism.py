
from difflib import SequenceMatcher

with open('fails1.txt') as file1, open('fails2.txt') as file2:
    file1_data = file1.read()
    file2_data = file2.read()
    similarity = SequenceMatcher(None, file1_data, file2_data).ratio()
    
    percentage = str(round(similarity*100)) + '%'
    print("Teksti ir", percentage, "līdzīgi")