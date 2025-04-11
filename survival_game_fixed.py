import os
import random















class SurvivalGame:
    def __init__(self):
        self.player = {
            "health": 100,
            "hunger": 0,
            "energy": 100,
            "inventory": {
                "food": 3,
                "water": 5,
                "medicine": 1,
                "wood": 0,
                "tools": 0
            },
            "days_survived": 0,
            "shelter_level": 0
        }
        self.game_over = False
        self.message = ""
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def display_status(self):
        """Display the current player status"""
        self.clear_screen()
        print("\n===== WILDERNESS SURVIVAL =====")
        print(f"Days Survived: {self.player['days_survived']}")
        print("\n----- PLAYER STATUS -----")
        print(f"Health: {self.player['health']}/100")
        print(f"Hunger: {self.player['hunger']}/100")
        print(f"Energy: {self.player['energy']}/100")
        print(f"Shelter Level: {self.player['shelter_level']}")
        
        print("\n----- INVENTORY -----")
        for item, amount in self.player['inventory'].items():
            print(f"{item.capitalize()}: {amount}")
            
        if self.message:
            print(f"\nLAST EVENT: {self.message}")
            self.message = ""
            
    def get_action(self):
        """Get player action choice"""
        print("\n----- ACTIONS -----")
        print("1. Search for food")
        print("2. Collect water")
        print("3. Rest")
        print("4. Build/improve shelter")
        print("5. Craft tools")
        print("6. Use medicine")
        print("7. Eat food")
        print("8. Drink water")
        print("9. End day")
        
        while True:
            try:
                choice = int(input("\nWhat would you like to do? (1-9): "))
                if 1 <= choice <= 9:
                    return choice
                else:
                    print("Please enter a number between 1 and 9.")
            except ValueError:
                print("Please enter a valid number.")
    
    def search_for_food(self):
        """Search for food in the wilderness"""
        if self.player["energy"] < 20:
            self.message = "You're too tired to search for food."
            return
            
        self.player["energy"] -= 15
        self.player["hunger"] += 10
        
        success_chance = random.random()
        if success_chance < 0.6:  # 60% chance to find food
            amount = random.randint(1, 3)
            self.player["inventory"]["food"] += amount
            self.message = f"You found {amount} food!"
        else:
            self.message = "You searched but couldn't find any food."
            
        # Random event
        if random.random() < 0.2:  # 20% chance for injury
            damage = random.randint(5, 15)
            self.player["health"] -= damage
            self.message += f" You got injured while searching (-{damage} health)."
    
    def collect_water(self):
        """Collect water from nearby sources"""
        if self.player["energy"] < 15:
            self.message = "You're too tired to collect water."
            return
            
        self.player["energy"] -= 10
        self.player["hunger"] += 5
        
        success_chance = random.random()
        if success_chance < 0.7:  # 70% chance to find water
            amount = random.randint(1, 4)
            self.player["inventory"]["water"] += amount
            self.message = f"You collected {amount} water!"
        else:
            self.message = "You couldn't find a clean water source."
    
    def rest(self):
        """Rest to regain energy"""
        energy_gain = 30
        if self.player["shelter_level"] > 0:
            energy_gain += 10 * self.player["shelter_level"]
            
        self.player["energy"] = min(100, self.player["energy"] + energy_gain)
        self.player["hunger"] += 15
        
        self.message = f"You rested and regained energy. (+{energy_gain} energy)"
    
    def build_shelter(self):
        """Build or improve shelter"""
        if self.player["energy"] < 25:
            self.message = "You're too tired to build a shelter."
            return
            
        if self.player["inventory"]["wood"] < 3:
            self.message = "You need at least 3 wood to improve your shelter."
            return
            
        self.player["energy"] -= 25
        self.player["hunger"] += 20
        self.player["inventory"]["wood"] -= 3
        
        self.player["shelter_level"] += 1
        self.message = f"You improved your shelter to level {self.player['shelter_level']}!"
    
    def craft_tools(self):
        """Craft tools to improve efficiency"""
        if self.player["energy"] < 20:
            self.message = "You're too tired to craft tools."
            return
            
        if self.player["inventory"]["wood"] < 2:
            self.message = "You need at least 2 wood to craft tools."
            return
            
        self.player["energy"] -= 20
        self.player["hunger"] += 10
        self.player["inventory"]["wood"] -= 2
        
        self.player["inventory"]["tools"] += 1
        self.message = "You crafted a new tool! This will help you gather resources."
    
    def use_medicine(self):
        """Use medicine to heal"""
        if self.player["inventory"]["medicine"] <= 0:
            self.message = "You don't have any medicine."
            return
            
        self.player["inventory"]["medicine"] -= 1
        health_gain = random.randint(20, 35)
        self.player["health"] = min(100, self.player["health"] + health_gain)
        
        self.message = f"You used medicine and healed {health_gain} health points."
    
    def eat_food(self):
        """Eat food to reduce hunger"""
        if self.player["inventory"]["food"] <= 0:
            self.message = "You don't have any food to eat."
            return
            
        self.player["inventory"]["food"] -= 1
        hunger_reduction = random.randint(20, 30)
        self.player["hunger"] = max(0, self.player["hunger"] - hunger_reduction)
        
        self.message = f"You ate some food and reduced your hunger by {hunger_reduction}."
    
    def drink_water(self):
        """Drink water to reduce thirst and slightly recover health"""
        if self.player["inventory"]["water"] <= 0:
            self.message = "You don't have any water to drink."
            return
            
        self.player["inventory"]["water"] -= 1
        self.player["health"] = min(100, self.player["health"] + 5)
        
        self.message = "You drank some water and feel a bit better. (+5 health)"
    
    def end_day(self):
        """End the current day and update stats"""
        # Gather random resources
        if random.random() < 0.5:
            wood_amount = random.randint(1, 3)
            self.player["inventory"]["wood"] += wood_amount
            self.message = f"While setting up camp, you collected {wood_amount} wood."
        
        # Shelter protection effects
        if self.player["shelter_level"] > 0:
            shelter_protection = random.randint(0, 5) * self.player["shelter_level"]
            self.message += f"\nYour shelter protected you from harsh conditions (+{shelter_protection} health)."
            self.player["health"] = min(100, self.player["health"] + shelter_protection)
        
        # Night events
        if random.random() < 0.3:  # 30% chance for a night event
            event_type = random.random()
            if event_type < 0.4:  # 40% chance for animal attack
                damage = random.randint(10, 25)
                reduced_damage = max(5, damage - self.player["shelter_level"] * 3)
                self.player["health"] -= reduced_damage
                self.message += f"\nA wild animal attacked during the night! (-{reduced_damage} health)"
                
            elif event_type < 0.7:  # 30% chance for bad weather
                damage = random.randint(5, 15)
                reduced_damage = max(0, damage - self.player["shelter_level"] * 4)
                self.player["health"] -= reduced_damage
                if reduced_damage > 0:
                    self.message += f"\nBad weather made you sick! (-{reduced_damage} health)"
                else:
                    self.message += "\nYour shelter protected you completely from the bad weather!"
                    
            else:  # 30% chance to find something
                if random.random() < 0.5:
                    self.player["inventory"]["food"] += 1
                    self.message += "\nYou found some food near your camp!"
                else:
                    self.player["inventory"]["medicine"] += 1
                    self.message += "\nYou found medicinal herbs near your camp!"
        
        # Update day count
        self.player["days_survived"] += 1
        
        # Daily stat changes
        self.player["hunger"] += 30
        self.player["energy"] = min(100, self.player["energy"] + 20)
        
        # Check hunger effects
        if self.player["hunger"] >= 100:
            damage = random.randint(10, 20)
            self.player["health"] -= damage
            self.message += f"\nYou're starving! (-{damage} health)"
            self.player["hunger"] = 100
    
    def check_game_state(self):
        """Check if the game should continue or end"""
        if self.player["health"] <= 0:
            self.game_over = True
            self.message = "You have died. Game Over."
            return
            
        if self.player["days_survived"] >= 30:
            self.game_over = True
            self.message = "Congratulations! You survived for 30 days and have been rescued!"
    
    def process_action(self, action):
        """Process the chosen action"""
        if action == 1:
            self.search_for_food()
        elif action == 2:
            self.collect_water()
        elif action == 3:
            self.rest()
        elif action == 4:
            self.build_shelter()
        elif action == 5:
            self.craft_tools()
        elif action == 6:
            self.use_medicine()
        elif action == 7:
            self.eat_food()
        elif action == 8:
            self.drink_water()
        elif action == 9:
            self.end_day()
        
        # Check game state after each action
        self.check_game_state()
    
    def play(self):
        """Main game loop"""
        print("Welcome to Wilderness Survival!")
        print("You have been stranded in the wilderness. Survive for 30 days to win.")
        print("Press Enter to start...")
        input()
        
        while not self.game_over:
            self.display_status()
            action = self.get_action()
            self.process_action(action)
            
        # Final display
        self.display_status()
        print("\nGame over! You survived for", self.player["days_survived"], "days.")
        if self.player["health"] <= 0:
            print("You died in the wilderness.")
        else:
            print("You have been rescued! Congratulations!")

if __name__ == "__main__":
    game = SurvivalGame()
    game.play() 