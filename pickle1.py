import pickle

a=open("one.txt","rb")

try:
    while True:
        
        print(pickle.load(a))
except:
    print("Complete program...")
    
a.close()