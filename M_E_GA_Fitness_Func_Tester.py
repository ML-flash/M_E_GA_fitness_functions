# ok so replace the leadingonesfitness class with your implimentation. and teplace the
assignment in line 59 with your class. 
class LeadingOnesFitness:
    def __init__(self, max_length, update_best_func):
        self.max_length = max_length
        self.update_best = update_best_func  # Function to update the best organism

    def compute(self, encoded_individual, ga_instance):
        # Decode the individual
        decoded_individual = ga_instance.decode_organism(encoded_individual)

        # Initialize fitness score
        fitness_score = 0
        # Count the number of leading '1's until the first '0'
        for gene in decoded_individual:
            if gene == '1':
                fitness_score += 1
            else:
                break

        # Calculate the penalty based on the organism's length
        if len(decoded_individual) < self.max_length:
            penalty = 1.008 ** (self.max_length - len(decoded_individual))
        else:
            penalty = len(decoded_individual) - self.max_length

        # Compute final fitness score
        final_fitness = fitness_score - penalty

        # Update the best organism if necessary
        self.update_best(encoded_individual, final_fitness)

        return final_fitness

class MockGA:
    @staticmethod
    def decode_organism(encoded_individual):
        # Assume the organism is already in decoded form for simplicity
        return encoded_individual

def generate_random_organism(gene_set, length):
    """Generate a random organism from the given gene set."""
    return [random.choice(gene_set) for _ in range(length)]

def update_best_organism(encoded_individual, fitness_score):
    """Update the global record of the best organism based on fitness."""
    global best_organism
    if fitness_score > best_organism['fitness']:
        best_organism['genome'] = encoded_individual
        best_organism['fitness'] = fitness_score
        print(f"New best organism found with fitness: {fitness_score}")

# Configuration
MAX_LENGTH = 300
genes = ['0', '1']  # Gene set for the organisms
best_organism = {"genome": None, "fitness": float('-inf')}  # Initialize the best organism

# Initialize the fitness function
fitness_function = LeadingOnesFitness(MAX_LENGTH, update_best_organism)

# Generate a random organism and evaluate its fitness
random_organism = generate_random_organism(genes, 50)  # Generate a random organism of length 50
mock_ga = MockGA()  # Mock GA instance for decoding
fitness_score = fitness_function.compute(random_organism, mock_ga)

# Output the results
(random_organism, fitness_score, best_organism)
