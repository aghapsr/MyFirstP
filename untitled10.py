import random


secret = random.randint(1, 100)
guest = None
attempts = 0

print("🎯 I'm thinking of a number between 1 and 100.")
while guest != secret:
    guest = int(input("Enter your guest: "))
    attempts += 1
    
    if guest < secret:
        print("📈 Go higher!")
    elif guest > secret:
        print("📉 Go lower!")
    else:
        print(f"🎉 Congratulations! You got it in {attempts} attempts.")