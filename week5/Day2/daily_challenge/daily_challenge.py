# Instructions :
# This challenge is about Biology that will put emphasis on your knowledge of classes, inheritance and polymorphism.
# Implement these classes as you see fit.
# Instantiate a number of Organism and let them mutate until one gets to a DNA which is only made of 1s. Then stop and record the number of generations (iterations) it took.
# Write your results in you personal biology research notebook and tell us your conclusion :).
# ------------------------------------------------------------------
# Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.
# A Gene is a single value 0 or 1, it can mutate (flip).
# A Chromosome is a series of 10 Genes. It also can mutate, meaning a random number of genes can randomly flip (1/2 chance to flip).
# A DNA is a series of 10 chromosomes, and it can also mutate the same way Chromosomes can mutate.
# from operator import countOf
# import random

dna = {
    1: [random.choice([0,1]) for gene in range(10)],
    2: [random.choice([0,1]) for gene in range(10)],
    3: [random.choice([0,1]) for gene in range(10)],
    4: [random.choice([0,1]) for gene in range(10)],
    5: [random.choice([0,1]) for gene in range(10)],
    6: [random.choice([0,1]) for gene in range(10)],
    7: [random.choice([0,1]) for gene in range(10)],
    8: [random.choice([0,1]) for gene in range(10)],
    9: [random.choice([0,1]) for gene in range(10)],
    10: [random.choice([0,1]) for gene in range(10)],
}
class Organism():
    '''
    Accepts a DNA object and an environment parameter that sets the probability for its DNA to mutate.
     '''
    def __init__(self, dna, enviroment):
        self.dna = dna
        self.enviroment = enviroment
    
class Sea(Organism):
    chromosome_lists =  dna.values()
    for chromosome in chromosome_lists:
        chromosome = [*chromosome]
        count = 0
        if chromosome[0] == 1:
            chromosome[-1] = 1
        elif chromosome[-1] == 1:
            chromosome[0] = 1
    dna[1] = (chromosome)
    # print(f"these are the chromosomes an organism of the sea: {new_list}")
    print(f"this is the dna of an organism in the sea: {dna}")

    def perfect_dna(self):
        chromosome_lists =  dna.values()
        for chromosome in chromosome_lists:
            count = 0
            if chromosome != [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                count += 1
                continue
            else:
                print(f"it only took {count} amount of times to find the perfect chromosomes!")

# class land(Organism):
#     chromosome_lists =  dna.values()
#     for chromosome in chromosome_lists:
#         chromosome = [*chromosome]
#         if chromosome[0] == 1 and chromosome[1] == 1:
#             chromosome[-1] = 1 and chromosome[-2] == 1
#         elif chromosome[-1] == 0:
#             chromosome[0] = 0
#     dna[1] = (chromosome)
#     # dna.update({'1': new_list})
#     # print(f"these are the genes of an organism from the land: {new_list}")
#     def perfect_dna(self):
#         chromosome_lists =  dna.values()
#         for chromosome in chromosome_lists:
#             count = 0
#             if list != [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
#                 count += 1
#                 continue
#             else:
#                 print(f"it only took {count} amount of times to find the perfect chromosomes!")

#     print(f"these are the genes of an organism from the land: {dna}")



creature = Organism(dna, "world")
# sea_creature = Sea(creature, "sea")
land_creature = land(creature, "land")
print(land_creature.perfect_dna())
# ---------------------------------------------------------------------------------------------


# Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.
# Implement these classes as you see fit.

# Create a new class called Organism that accepts a DNA object and an environment parameter that sets the probability for its DNA to mutate.

# Instantiate a number of Organism and let them mutate until one gets to a DNA which is only made of 1s. 
# Then stop and record the number of generations (iterations) it took.

# Write your results in you personal biology research notebook and tell us your conclusion :).

# ---------------------------------------------------------------------------
import random

class Gene():
    # A Gene is a single value 0 or 1, it can mutate (flip).
    def __init__(self):
        self.state = random.randint([0, 1])

    def flip(self):
    # It also can mutate, meaning a random number of genes can randomly flip (1/2 chance to flip).
        self.state == 0 if self.state == 1 else 1

class Chromosome():
    # A Chromosome is a series of 10 Genes.
    def __init__(self):
        self.genes = [Gene() for i in range(0, 10)]

    def mutate(self):
    #  It also can mutate, meaning a random number of genes can randomly flip (1/2 chance to flip).
        # selected_genes = random.sample(self.genes, random.randint(0, len(self.genes)))    #One line code that can do the same as lined 115 - 119.
        indexs = list(range(0, len(self.genes)))
        random.shuffle(indexs)
        sub_selection = self.genes[0:random.choice(indexs)]
        for gene in sub_selection:    
            if random.randint(0, 1):
                gene.flip()


class Dna():
    # A DNA is a series of 10 chromosomes, and it can also mutate the same way Chromosomes can mutate.
    def __init__(self):
        self.chromosomes = [Chromosome() for i in range(10)]

    def mutate(self):
        indexs = list(range(0, len(self.genes)))
        random.shuffle(indexs)
        selected_chromosomes = self.genes[0:random.choice(indexs)]
        for gene in selected_chromosomes:    
            if random.randint(0, 1):
                gene.flip()


