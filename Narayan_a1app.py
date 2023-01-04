# Application main script 
import Narayan_a1

# Receiving  the required data from the user

old = input("Enter original currency : ").upper()
new = input("Enter desired currency : ").upper()
amt = float(input("Enter Original amount : "))

if(not(Narayan_a1.is_currency(old))):        # if the source currency is not valid, quit
	print(old, " is not a valid currency")
	quit()

if(not(Narayan_a1.is_currency(new))):               # if the target currency is not valid, quit
	print(new, " is not a valid currency")
	quit()
print(f"You can exchange {amt} {old} for {Narayan_a1.exchange(old ,new ,amt )} {new}.")   # Giving exchanged amount in new curency