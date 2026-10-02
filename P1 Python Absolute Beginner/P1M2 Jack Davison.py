# [ ] create, call and test fishstore() function 
def fishstore(fish, price):
    return"fish type:" + fish + "costs $" + price

fish_entry = input("Enter a fish type: ")
price_entry = input("Enter the price of the fish: ")
 

name = "Jack Davison"

print("Hi", name, fishstore(fish_entry, price_entry))