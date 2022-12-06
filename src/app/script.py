import sys

if __name__ == "__main__":
    print ("Привет :)")
    
    mes = int(input("Введите число для возведения в степень: "))
    n = int(input("Введите степень: "))
    mes = mes ** n
  
    print(f"Результат: " + str(mes))