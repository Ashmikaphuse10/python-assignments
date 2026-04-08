from Temperature import celsius_to_fahrenheit,fahrenheit_to_celsius
def main():
    print("Temperature conversion choices:")
    print("1.Celsius to Fahrenheit")
    print("2.Fahrenheit to Celsius")
    choice= int(input("Enter your choice:"))

    if choice==1:
        celsius=float(input("Enter temperature in Celsius:"))
        print(f"{celsius}°C ={celsius_to_fahrenheit(celsius)}°F")
    elif choice==2:
        fahrenheit=float(input("Enter temperature in Fahrenheit:"))
        print(f"{fahrenheit}°F={fahrenheit_to_celsius(fahrenheit)}°C")
    else:
        print("Invalid choice")

if __name__=="__main__":
    main()