import pandas as pd

x = int(input("Please enter an integer value greater than 0: "))

if x > 0:
    even = []
    odd = []
    fibo = [0,1]

    for i in range(x):
        even.append(2*i)
        odd.append(2*i + 1)
        if i > 1:
            fibo.append(fibo[i-2] + fibo[i-1])
    
    dict1 = {'Even':even,
             'Odd':odd,
             'Fibonacci':fibo}
    df = pd.DataFrame(dict1)
    print(df)


