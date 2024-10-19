class car:
    def __init__(self, mpg: float, miles_per_year: float) -> None:
        self.mpg: float = mpg
        self.miles_per_year: float = miles_per_year

    def annual_gas_cost(self, gas_price: float) -> float:
        return (self.miles_per_year / self.mpg) * gas_price

net_car_cost: float #had to do the type annotation here. If I tried it in the function, I got "SyntaxError: annotated name 'net_car_cost' can't be global". Kinda wierd!
def calculate_break_even(current_car: car, new_car: car, new_car_cost: float, gas_price: float) -> float:
    global net_car_cost
    net_car_cost = new_car_cost - car_value #Accounts for whatever you get for selling the old car

    if net_car_cost < 0:
        print(f"\nYou will earn ${-net_car_cost:.2f} by upgrading (downgrading?) to the new car.")

    current_annual_cost: float = current_car.annual_gas_cost(gas_price)
    new_annual_cost: float = new_car.annual_gas_cost(gas_price)
    
    annual_savings: float = current_annual_cost - new_annual_cost

    print(f"Current car's annual gas cost: ${current_annual_cost:,.2f}")
    print(f"New car's annual gas cost: ${new_annual_cost:,.2f}")
    
    if annual_savings > 0:
         print(f"Annual savings: ${annual_savings:,.2f}")
    elif annual_savings == 0:
        return "The new car doesn't save any money on gas."
    elif annual_savings < 0:
        return "You will pay more for gas with the new car."

    break_even_years: float = round((net_car_cost / annual_savings), 2)
    return break_even_years

def get_input(value: str) -> float: #allows for user to use commas or underscores if necessary when inputting their values
    while True:
        user_input: str = input(value)
        cleaned_input: str = user_input.replace('_', '').replace(',', '')
        try:
            return float(cleaned_input)
        except ValueError:
            print("Enter a number.")

#User inputs
current_mpg: float = get_input("Enter your current car's MPG: ")
new_mpg: float = get_input("Enter the new car's MPG: ")
car_value: float = get_input("Enter the sale value of your current car: ")
new_car_cost: float = get_input("Enter the cost of the new car: ")
gas_price: float = get_input("Enter the current gas price per gallon: ")
miles_per_year: float = get_input("Enter the average miles you drive per year: ")

#Create the 'car' objects
current_car: car = car(current_mpg, miles_per_year)
new_car: car = car(new_mpg, miles_per_year)

break_even: float = calculate_break_even(current_car, new_car, new_car_cost, gas_price)

#Checks if variable break_even is float. if it is, it prints the f-string. 
#If not, it will print that string from the function calculate_break_even to let you know you won't save money in the long run
if isinstance(break_even, float):
    years, fraction = divmod(break_even, 1)
    months = fraction * 12
    if years < 0:
        print(f"There is no break even time due to your current car being ${abs(net_car_cost):.2f} more expensive than the car you are looking to buy.")
    else:
        print(f"It will take {years:.0f} years and {months:.0f} months to break even.")
    print('')
else:
    print(break_even)
    print('')