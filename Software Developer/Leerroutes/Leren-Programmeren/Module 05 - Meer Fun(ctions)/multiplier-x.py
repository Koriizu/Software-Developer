
def multiply(getal):
    iets = ''
    for nummer in range(1, 11):
        print(nummer, "x" ,getal , "=",  nummer * getal)
        iets += f'{nummer} x {getal} = {nummer * getal} \n' 
    return iets
    

iets = multiply(10)
print (iets)
