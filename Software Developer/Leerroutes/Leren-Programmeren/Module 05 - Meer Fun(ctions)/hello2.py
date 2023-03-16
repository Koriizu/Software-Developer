def hello(test):
    iets = ''
    for x in range(1,test+1):
        iets += f'{x}.Hello From Function Town.\n'
    return iets

iets = hello(8)

print(iets)