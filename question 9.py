L = []
kilos = []
N = int(input("enter the number of students :"))
for i in range(0,N):
    pounds = int(input())
    kilograms = pounds * 0.4535923
    L.append(pounds) # adding weights to the list
    kilos.append(kilograms)
    print("L",pounds)
    print(kilos)
