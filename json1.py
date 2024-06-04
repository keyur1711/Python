import json

a=open("write.txt","r")

print(json.load(a))

a.close()