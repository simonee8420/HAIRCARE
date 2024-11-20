import random


class HairCareRoutine:
    def __init__(self, hair_type, porosity, density, lifestyle, diet):
        self.hair_type = hair_type
        self.porosity = porosity
        self.density = density
        self.lifestyle = lifestyle
        self.diet = diet
        self.climate_data = self.get_climate_data()

    def get_climate_data(self):
        # Simulating climate data instead of fetching from an API
        return {
            "temperature": random.uniform(-10, 40),  # Simulating a random temperature
            "humidity": random.uniform(0, 100)  # Simulating a random humidity percentage
        }

    def generate_routine(self):
        routine = []

        if self.hair_type == "curly":
            routine.append("Use sulfate-free shampoo to avoid drying out your curls.")
        elif self.hair_type == "straight":
            routine.append("Use a volumizing shampoo to add body to your hair.")

        if self.porosity == "high":
            routine.append("Use protein treatments to strengthen your hair.")
        elif self.porosity == "low":
            routine.append("Use deep conditioning treatments to improve moisture retention.")

        if self.density == "thin":
            routine.append("Avoid heavy products that can weigh down your hair.")
        elif self.density == "thick":
            routine.append("Use rich conditioners to maintain moisture.")

        if self.lifestyle == "active":
            routine.append("Wash your hair more frequently to remove sweat and buildup.")
        elif self.lifestyle == "sedentary":
            routine.append("Opt for a gentle cleansing routine.")

        if self.diet == "balanced":
            routine.append("Your diet is good for hair health, continue with it.")
        else:
            routine.append("Consider incorporating more vitamins and proteins into your diet for better hair health.")

        if self.climate_data["humidity"] > 70:
            routine.append("Use anti-humidity hair products to control frizz.")
        elif self.climate_data["humidity"] < 30:
            routine.append("Use moisturizing products to combat dry air.")

        return routine


# Example Usage
user_profile = HairCareRoutine(
    hair_type="curly",
    porosity="high",
    density="thick",
    lifestyle="active",
    diet="balanced"
)

routine = user_profile.generate_routine()

print("Personalized Hair Care Routine:")
for step in routine:
    print("-", step)

