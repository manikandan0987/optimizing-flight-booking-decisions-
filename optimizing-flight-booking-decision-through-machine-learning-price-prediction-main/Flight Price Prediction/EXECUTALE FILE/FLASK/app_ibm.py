import pickle 
 
note = {'so long': 'and thanks for all the fish'} 
 
with open('filename.pkl', 'wb') as handle: 
    pickle.dump(note, handle) 
 
with open('filename.pkl', 'rb') as handle: 
    read_back = pickle.load(handle) 
 
print(note == read_back)