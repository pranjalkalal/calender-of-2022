days=['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
a_months=['January','February','March','April','May','June','July','August','September','October','November','December']
def first_day(month):
    days=0
    for i in range(1,month):
        if i==2:
            days=days+28
        elif i<=7:
            if i%2==0:
             days=days+30
            else:
             days=days+31
        else:
            if i%2==0:
             days=days+31
            else:
             days=days+30        
    months_first_day=days%7
    return months_first_day
def calender(month,months_first_day):
    total_days=0
    if month==2:
        total_days=28
    elif month<=7:
        if month%2==0:
           total_days=30
        else:
           total_days=31
    else:
        if month%2==0:
           total_days=31
        else:
           total_days=30
    #i=months_first_day
    for i in range(0,total_days,7):
        x=months_first_day
        temp=i+1
        for cnt in range(0,7):
            if(temp!=total_days+1):
              print('{} : {}'.format(temp,days[x]))
              x=x+1
              z=x%7
              x=z
              temp=temp+1
            else:
               exit

month=int(input("enter month in number:"))
f_day=first_day(month)
print(f_day)
print("Calender of {} 2022".format(a_months[month]))
calender(month,f_day)

