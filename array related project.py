# It will ask user to enter the no. of days for which user wants temperature data
def avgtem():
    temp= int(input("How many days average temperature you want: "))
    sum = 0
    templist =[]
    for i in range(1,  temp+1):
        daytemp = int(input("Enter Day" + str(i) + "'s temperature: "))
        templist.append(daytemp)
        sum +=daytemp
    avg = sum/temp
    print(avg)

    avgcount = 0
    for j in templist:
        if j>avg:
            avgcount+=1
    print(str(avgcount) +" days temperture is above average temperature")
    
avgtem()
    

