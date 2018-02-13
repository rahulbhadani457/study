def wrap(new):
    def insiderap(*args):
        #sum=new(*args)
        return new.__name__+" {}".format(str(new(*args)))
    return insiderap
    
@wrap
def add(a,b):
    print("TESTING")
    print(a+b)
    #return sum
    
    
op=add(2,4)
print(op)