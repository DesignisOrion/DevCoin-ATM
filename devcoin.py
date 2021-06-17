# DevCoin Project


import time

devCoinBal = 1000

print("WELCOME TO DEVCOIN ATM")
print("How many DEVCOIN would you like to withdrawl today?")
print("Please type in the amount please")
user_wd_input = input()
devCoinBal = int(devCoinBal) - int(user_wd_input)
if int(user_wd_input) <= devCoinBal:
    print(f"Ok great! We will process the amount: {user_wd_input} DEVCOINS right away.")
    print("PLEASE HOLD!")
    time.sleep(5)
    print("TRANSACTION COMPLETE")
    time.sleep(2)
    print(f"Your new balance is {devCoinBal} DEVCOINS")
    print(f"THANKS FOR USING DEVCOIN ATM")
elif int(user_wd_input) > devCoinBal:
    print(f"INSUFFICENT DEVCOINS.")
    time.sleep(2)
    print(f"THANKS FOR USING DEVCOIN ATM")
    


