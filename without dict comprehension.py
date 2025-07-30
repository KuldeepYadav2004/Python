users={'rajeev verma':1,'mahima gupta':2,'manoj pandey ':3}
labels={}
print(users.items())
for key,values in users.items():
    labels[values]=key
    
print(labels)
