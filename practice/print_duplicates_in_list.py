l = ['hello', 10, 20, 40, 20, 60, 40, 30]
#[20,40]
q = [ i for i in l if l.count(i)>1]
print(list(set(q)))
