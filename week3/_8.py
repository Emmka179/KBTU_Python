def temperature(farenheits):
    return (5 / 9) * (farenheits - 32)

farenheits = int(input("Enter amount of farenheit: "))
print("Celsius: ", temperature(farenheits))