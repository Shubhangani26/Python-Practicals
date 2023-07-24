def saleCalc(l):
    monthlySales=0
    commision=0
    remark=""
    data=()      #commision,remark
    for i in l:
        monthlySales+=i
    print("Monthly Sales :",monthlySales)
    if(monthlySales<40000):
        commision=0
        remark="Work Hard"
        data=commision,remark
    elif(40000<monthlySales<60000):
         if(monthlySales<50000):
            commision=0
            remark="Average Sales"
         else:
               commision=0.05*monthlySales
               remark="Average Sales"
         data=commision,remark

    elif(60000<=monthlySales<80000):
        commision=0.05*monthlySales
        remark="Good"
        data=commision,remark

    else:
       commision=0.05*monthlySales
       remark="Excellent"
       data=commision,remark

    return data



print("Enter the sales per week as a list.")
sales=eval(input())
data=saleCalc(sales)
print("Commission Amount :",data[0])
print("Remark :",data[1])