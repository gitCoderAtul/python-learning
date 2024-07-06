P = input("Enter Amount:")
R = input("Enter roi:")
N = input("Enter duration:")
 

if P=='' or R =='' or N =='':
    print('Please Enter Values')
else:
    P = int(P)
    R = float(R)
    N = int(N)

    year=1
    openingBalance=0
    while year<=N:
        interest =(openingBalance+P)*R/100
        interest = round(interest)
        closingBalance = (openingBalance+P+interest)
        print(year, openingBalance, P, interest, closingBalance)
        year = year+1
        openingBalance = closingBalance
        

     