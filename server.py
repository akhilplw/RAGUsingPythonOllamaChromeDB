import ollama,sys,chromadb
from utilities import getconfig

embedmodel = getconfig()["embedmodel"]
mainmodel = getconfig()["mainmodel"]

chroma = chromadb.HttpClient(host="localhost", port=8000)
collection = chroma.get_or_create_collection("buildragwithpython")


print(chroma)
