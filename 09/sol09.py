import random as rnd

# returns the random array


def random_arr(lower, upper, size):
    return [rnd.randrange(lower, upper+1) for _ in range(size)]

# cross over between chromosomes


def reproduce(x, y):
    tmp = rnd.randint(0, len(x)-1)
    return x[:tmp]+y[tmp:]

# randomly change the value of index


def mutate(x):
    inp = rnd.randint(1, len(x))
    x[rnd.randrange(0, len(x))] = inp
    return x

# pick the random chromosome from population while seeing the probabilities


def random_pick(population, probs):
    r = rnd.uniform(0, sum(probs))
    endpoint = 0
    for pop, prob in zip(population, probs):
        if endpoint+prob >= r:
            return pop  # picking random chromosome
        endpoint += prob
    print("Error!")
    exit()

# def random_pick(population, probs):
#     totalprob = sum(probs)
#     percentage_arr = []

#     for chrom, prob in zip(population, probs):
#         percent = int((prob*100)/totalprob)
#         [percentage_arr.append(chrom) for _ in range(percent)]
#     if len(percentage_arr) == 0:
#         dummy = 10
#     r = rnd.randrange(0, len(percentage_arr))
#     onerand = percentage_arr[r]
#     tworand = percentage_arr[r-len(percentage_arr)]
#     return onerand, tworand


def genetic_algo(population, maxfitness):
    mutation_prob = 0.85  # mutation 85%
    new_population = []
    # all probabilites or percentages
    probs = [fitness(pop)/maxfitness for pop in population]
    for _ in range(len(population)):
        x = random_pick(population, probs)  # one best chromosome
        y = random_pick(population, probs)  # two best chromosome

        # creating child
        child = reproduce(x, y)
        if rnd.random() < mutation_prob:
            child = mutate(child)  # rarely mutate

        new_population.append(child)
        if fitness(child) >= maxfitness:
            break
    return new_population


def fitness(x):  # checking the chromosome for fitness
    horizontal_collisions = sum(
        [x.count(queen)-1 for queen in x])/2
    diagonal_collisions = 0

    n = len(x)
    left_diagonal = [0] * 2*n
    right_diagonal = [0] * 2*n
    for i in range(n):
        left_diagonal[i + x[i] - 1] += 1
        right_diagonal[len(x) - i + x[i] - 2] += 1

    diagonal_collisions = 0
    for i in range(2*n-1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i]-1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i]-1
        diagonal_collisions += counter / (n-abs(i-n+1))

    # 28-(2+3)=23
    return int((n*(n-1))/2 - (horizontal_collisions + diagonal_collisions))


if __name__ == "__main__":
    nq = int(input("Enter number of queens: "))  # number of queens
    maxfitness = (nq*(nq-1))/2

    population = [random_arr(1, nq, nq) for _ in range(nq*nq)]

    generation = 1

    while not maxfitness in [fitness(chrom) for chrom in population]:
        population = genetic_algo(population, maxfitness)
        generation += 1

    print("generation:  ", generation)
    for chrom in population:
        if fitness(chrom) == maxfitness:
            chrom_out = chrom
            print(chrom)
            print("score: ", fitness(chrom))
            exit()
