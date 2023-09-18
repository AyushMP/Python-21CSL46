from difflib import SequenceMatcher
string1="Ayush"
string2="Ayush"
similarity=SequenceMatcher(None,string1,string2).ratio()
print("Original String: ")
print(string1)
print(string2)
print("Similarity: ",similarity)