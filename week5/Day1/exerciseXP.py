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
from operator import countOf
import random

dna = {
    1: [random.choice([0,1]) for gene in range(10)] ,
    2: [random.choice([0,1]) for gene in range(10)] ,
    3: [random.choice([0,1]) for gene in range(10)] ,
    4: [random.choice([0,1]) for gene in range(10)] ,
    5: [random.choice([0,1]) for gene in range(10)] ,
    6: [random.choice([0,1]) for gene in range(10)] ,
    7: [random.choice([0,1]) for gene in range(10)] ,
    8: [random.choice([0,1]) for gene in range(10)] ,
    9: [random.choice([0,1]) for gene in range(10)] ,
    10: [random.choice([0,1]) for gene in range(10)] ,

}
class Organism():
    '''
    Accepts a DNA object and an environment parameter that sets the probability for its DNA to mutate.
     '''
    def __init__(self, dna, enviroment):
        self.dna = dna
        self.enviroment = enviroment
    
class Sea(Organism):
    for list in dna.values():
        new_list = [*list]
        count = 0
        if new_list[0] == 1:
            new_list[-1] = 1
        elif new_list[-1] == 1:
            new_list[0] = 1
    dna[1] = (new_list)
    print(f"these are the chromosomes an organism of the sea: {new_list}")
    print(f"this is the dna of an organism in the sea: {dna}")

    def perfect_dna(self):
        for list in dna.values():
            count = 0
            if list != [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                count += 1
                continue
            else:
                return count

class land(Organism):
    for list in dna.values():
        new_list = [*list]
        if new_list[0] == 0:
            new_list[-1] = 0
        elif new_list[-1] == 0:
            new_list[0] = 0
    dna[1] = (new_list)
    # dna.update({'1': new_list})
    # print(f"these are the genes of an organism from the land: {new_list}")
    def perfect_dna(self):
        for list in dna.values():
            count = 0
            if list != [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                count += 1
                continue
            else:
                return count

    print(f"these are the genes of an organism from the land: {dna}")

                    
                    


creature = Organism(dna, "sea")
sea_creature = Sea(creature, "sea")
land_creature = land(creature, "land")
# print(creature.land())