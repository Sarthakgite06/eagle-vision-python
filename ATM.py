class BankATM:

    def __init__(self):
        self.pin = 0
        self.balance = 0

    def menu(self):
        print("1. Set PIN")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Change PIN")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        match choice:

            case 1:
                self.setpin()

            case 2:
                self.check_balance()

            case 3:
                self.deposit()

            case 4:
                self.withdraw()

            case 5:
                self.change_pin()

            case 6:
                print("Thank you for using ATM")

            case _:
                print("Invalid choice")
                self.menu()

    def setpin(self):

        if self.pin == 0:
            setpin = int(input("Enter PIN: "))
            self.pin = setpin
            print("PIN set successfully")

        else:
            print("PIN is already set")

        self.menu()

    def check_balance(self):

        setpin = int(input("Enter PIN: "))

        if setpin == self.pin:
            print("Bank balance:", self.balance)

        else:
            print("Invalid PIN")

        self.menu()

    def deposit(self):

        setpin = int(input("Enter PIN: "))

        if setpin == self.pin:
            amount = int(input("Enter amount to deposit: "))

            self.balance = self.balance + amount

            print("Amount deposited successfully")
            print("Bank balance:", self.balance)

        else:
            print("Invalid PIN")

        self.menu()

    def withdraw(self):

        setpin = int(input("Enter PIN: "))

        if setpin == self.pin:

            amount = int(input("Enter amount to withdraw: "))

            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Please collect your cash")
                print("Bank balance:", self.balance)

            else:
                print("Insufficient balance")

        else:
            print("Invalid PIN")

        self.menu()

    def change_pin(self):

        old_pin = int(input("Enter old PIN: "))

        if old_pin == self.pin:

            new_pin = int(input("Enter new PIN: "))
            self.pin = new_pin

            print("PIN changed successfully")

        else:
            print("Invalid PIN")

        self.menu()


obj = BankATM()
obj.menu()