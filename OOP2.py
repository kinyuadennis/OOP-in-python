# Base class
class FuelPump:
    def __init__(self, fuel_type, price_per_litre, quantity_litres):
        self.fuel_type = fuel_type
        self.price_per_litre = price_per_litre
        self.quantity_litres = quantity_litres

    def dispense_fuel(self, litres):
        if litres <= self.quantity_litres:
            self.quantity_litres -= litres
            total_cost = litres * self.price_per_litre
            print(f"Dispensed {litres}L of {self.fuel_type}. Total cost: Ksh {total_cost}")
        else:
            print(f"Not enough {self.fuel_type} available.")

    def get_status(self):
        return f"{self.fuel_type}: {self.quantity_litres}L left at Ksh {self.price_per_litre}/L"

# Subclasses
class PetrolPump(FuelPump):
    def __init__(self, quantity_litres):
        super().__init__('Petrol', 185.0, quantity_litres)

class DieselPump(FuelPump):
    def __init__(self, quantity_litres):
        super().__init__('Diesel', 170.0, quantity_litres)

# FuelStation to manage pumps
class FuelStation:
    def __init__(self):
        self.pumps = []

    def add_pump(self, pump):
        self.pumps.append(pump)

    def show_status(self):
        print("\n--- Fuel Station Status ---")
        for pump in self.pumps:
            print(pump.get_status())

# Main
if __name__ == "__main__":
    petrol_pump = PetrolPump(500)  # 500L Petrol
    diesel_pump = DieselPump(800)  # 800L Diesel

    station = FuelStation()
    station.add_pump(petrol_pump)
    station.add_pump(diesel_pump)

    station.show_status()
    petrol_pump.dispense_fuel(40)   # Simulate a sale
    diesel_pump.dispense_fuel(100)
    station.show_status()
