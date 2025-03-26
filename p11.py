payslip=(125,"raj","account",10000)

basicpay=payslip[3]
hra=basicpay*20/100;
pf=basicpay*12/100;

total_ded=hra+pf

da=basicpay*15/100;
ta=basicpay*18/100;

total_earnings = da+hra+ta

netpay = total_earnings - total_ded

netpay = total_earnings - total_ded

print("employee id-",payslip[0])
print("employee name -",payslip[1])
print("department -",payslip[2])
print("basic pay in INR-",payslip[3])
print("total earnings:",total_earnings)
print("total deduction:",total_ded)
print("net salary:",netpay)