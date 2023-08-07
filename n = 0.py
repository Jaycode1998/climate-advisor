def get_rating(temperature):
    if temperature > 75:
        return "It's hot out!"
    elif 75 >= temperature > 60:
        return "It's warm out today"
    elif 60 >= temperature > 50:
        return "It's a pleasant day"
    elif 50 >= temperature >= 40:
        return "It's cool out"
    elif 40 > temperature >= 30:
        return "It's chilly, wear a jacket"
    elif 30 > temperature >= 20:
        return "It's cold, bundle up!"
    elif 20 > temperature >= 0:
        return "It's freezing! Stay indoors!"
    else:
        return "The temperature is extreme. Please take caution."

def main():
    try:
        temperature = float(input("Enter the temperature in Fahrenheit: "))
        rating = get_rating(temperature)
        print(rating)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()