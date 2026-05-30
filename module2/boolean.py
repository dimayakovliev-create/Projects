point = (1, 0)

match point:
    case (0, 0):
        print("Точка в центрі координат")  
    case (0, y):
        print(f"Точка лежить на осі Y: y={y}")  
    case (x, 0):
        print(f"Точка лежить на осі X: x={x}") 
    case (x, y):
        print(f"Точка має координати:  x={x}, y={y}") 
    case _:
        print("Це не точка")




x = int(input("X: "))
y = int(input("Y: "))
if x == 0:
    print("X can`t be equal to zero")
    x = int(input("X: "))
result = y / x
print(result)