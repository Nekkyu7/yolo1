class Customer:
    def __init__(self, name):
        self.name = name
        self.points = 0

class LoyaltyProgram:
    def __init__(self):
        self.customers = {}

    def add_customer(self, name):
        if name in self.customers:
            print(f"Klient {name} już istnieje!")
            return False
        self.customers[name] = Customer(name)
        print(f"Dodano klienta: {name}")
        return True

    def add_points(self, name, points):
        if name not in self.customers:
            print(f"Klient {name} nie istnieje!")
            return False
        if points < 0:
            print("Nie można dodać ujemnych punktów!")
            return False
        self.customers[name].points += points
        print(f"Dodano {points} punktów dla {name}. Saldo: {self.customers[name].points}")
        return True

    def redeem_points(self, name, points):
        if name not in self.customers:
            print(f"Klient {name} nie istnieje!")
            return False
        if points > self.customers[name].points:
            print(f"Brak wystarczających punktów! Saldo: {self.customers[name].points}")
            return False
        self.customers[name].points -= points
        print(f"Zużyto {points} punktów dla {name}. Pozostało: {self.customers[name].points}")
        return True

    def check_balance(self, name):
        if name not in self.customers:
            print(f"Klient {name} nie istnieje!")
            return None
        return self.customers[name].points

# Przykład użycia
if __name__ == "__main__":
    program = LoyaltyProgram()
    
    while True:
        print("\nSystem Punktów Lojalnościowych")
        print("1. Dodaj klienta")
        print("2. Dodaj punkty")
        print("3. Wykorzystaj punkty")
        print("4. Sprawdź saldo")
        print("5. Wyjście")
        
        choice = input("Wybierz opcję (1-5): ")
        
        if choice == "1":
            name = input("Podaj imię klienta: ")
            program.add_customer(name)
            
        elif choice == "2":
            name = input("Podaj imię klienta: ")
            points = int(input("Ile punktów dodać: "))
            program.add_points(name, points)
            
        elif choice == "3":
            name = input("Podaj imię klienta: ")
            points = int(input("Ile punktów wykorzystać: "))
            program.redeem_points(name, points)
            
        elif choice == "4":
            name = input("Podaj imię klienta: ")
            balance = program.check_balance(name)
            if balance is not None:
                print(f"Saldo punktów dla {name}: {balance}")
                
        elif choice == "5":
            print("Zamykanie programu...")
            break
            
        else:
            print("Nieprawidłowy wybór! Proszę wybrać opcję 1-5")