P = input("Enter Amount:")
R = input("Enter roi:")
N = input("Enter duration:")

# amount = 123
# print(amount)
# print(P)
# print(type(amount))
# print(type(roi))
# print(type(duration))

def emiCalculation():
    pass

def homeLoanEmitCalculator(P,R,N):
    if P=='' or R =='' or N =='':
        print('Please Enter Values')
    else:
        P = int(P)
        R = float(R)
        N = int(N)

        R =R/12/100
        N =N*12

        emi = P*R*(1+R)**N / ( (1+R)**N-1)
        print(emi)
        print(round(emi))
        

        result = "Loan Amount : {0}, Rate of Interest: {1}, EMI: {2}".format(P,R,round(emi))
        print(result)

homeLoanEmitCalculator(P,R,N)        