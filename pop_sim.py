# Simulation of population (only one market for now)
import time

class PopulationSimulator:
    """Simulator for population"""
    def __init__(self):
        self.population = 10
        self.population_growth = 1
        self.population_growth_rate = 0.1
        # self.update_population() # Comment out when debugging

    def simulate_growth(self):
        """Simulate population growth"""
        self.population = self.population + self.population_growth
        self.population_growth += self.population_growth_rate
        return self.population

    def update_population(self):
        """Loop population growth"""
        while True:
            self.simulate_growth()
            time.sleep(1) # How fast growth happens
# Debugging
if __name__ == "__main__":
    pop_sim = PopulationSimulator()
    while True:
        print(pop_sim.simulate_growth())
        time.sleep(1) # How fast growth happens
