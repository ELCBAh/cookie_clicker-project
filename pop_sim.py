# Simulation of population (only one market for now)

class PopulationSimulator:
    """Simulator for population"""
    def __init__(self):
        self.population = 10
        self.population_growth = 1
        self.population_growth_rate = 0.1

    def simulate_growth(self):
        """Simulate population growth"""
        self.population += self.population_growth
        self.population_growth += self.population_growth_rate