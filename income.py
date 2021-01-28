#income tax calculation
income=int(input("enter your income"))
NETPAY=0
PAYE=0
if income<=25000:
    tax=0
elif income<=40000:
    tax=12500+(income-40000)*0.15
elif income<=57333:
    tax=12500+(income-57333)*0.20
else:
    tax=12500+57333+(income-57333)*0.25
PAYE=tax*0.30
NETPAY=tax+PAYE
print("incometax=", tax)
print("Pay as you earn=", PAYE)
print("net per pay=", NETPAY)

