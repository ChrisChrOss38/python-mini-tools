import sys 
print("Schaltjahr Rechner")
print("Geben Sie ein Jahr ein, um zu prüfen, ob es ein Schaltjahr ist.")
print("Zum Beenden geben Sie 0 ein.")

while True:
    year = int(input('Jahr eingeben : '))
    if year == 0:
       print('Goodbye')
       sys.exit()   
       
    if (year %4==0 and year % 100 !=0) or year    %400 ==0:
        print(f'Das Jahr {year} ist ein Schaltjahr.')
        print('-------------------------------')
        print('For exit enter 0')
    else:
        print('Das Jahr ' + str(year) + ' ist kein Schaltjahr')
        print('-------------------------------')
        print('For exit enter 0')