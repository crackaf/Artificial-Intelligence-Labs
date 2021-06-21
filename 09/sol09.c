#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define _CRT_SECURE_NO_WARNINGS 0

#define PSIZE nqueens *nqueens //population row

typedef int node_t; //node_t can be char etc

const double mutationp = 0.85; //mutation probability

int nqueens = 0;    //size of array, poluation col size
int maxfitness = 0; //max fitness score

int getrand(int lower, int upper)
{
  return (rand() % (upper - lower + 1)) + lower;
}

int *random_arr(int lower, int upper, int size)
{
  int *ret = (int *)calloc(size, sizeof(int));
  for (int i = 0; i < size; ++i)
    ret[i] = getrand(lower, upper);
  return ret;
}

int fitness(const int *chrom)
{
  double horizontal_collisions = 0, diagonal_collisions = 0;

  //horizontal
  for (int i = 0; i < nqueens; ++i)
  {
    int count = 0;
    for (int j = 0; j < nqueens; ++j)
      if (chrom[j] == chrom[i])
        ++count;
    horizontal_collisions += count - 1;
  }
  horizontal_collisions /= 2;

  //printf("hori:%4.4f \n", horizontal_collisions);
  //printf("diag:%4.4f \n", diagonal_collisions);

  //diagnol
  int *left_diagonal = (int *)calloc(nqueens * 2, sizeof(int));
  int *right_diagonal = (int *)calloc(nqueens * 2, sizeof(int));
  for (int i = 0; i < nqueens; ++i)
  {
    left_diagonal[i + chrom[i] - 1] += 1;
    right_diagonal[nqueens - i + chrom[i] - 2] += 1;
  }
  //for (int i = 0; i < nqueens * 2; ++i)
  //{
  //  printf("%i  %i", left_diagonal[i], right_diagonal[i]);
  //  printf("\n");
  //}

  for (int i = 0; i < 2 * nqueens - 1; ++i)
  {
    int counter = 0;
    if (left_diagonal[i] > 1)
      counter += left_diagonal[i] - 1;
    if (right_diagonal[i] > 1)
      counter += right_diagonal[i] - 1;
    diagonal_collisions += (double)counter / (double)(nqueens - abs(i - nqueens + 1));
  }

  free(left_diagonal);
  free(right_diagonal);

  //printf("hori:%4.4f \n", horizontal_collisions);
  //printf("diag:%4.4f \n", diagonal_collisions);

  return (maxfitness - (horizontal_collisions + diagonal_collisions));
}

void print(const int *chrom)
{
  printf("Chromosome: ");
  for (int i = 0; i < nqueens; ++i)
    printf("%d, ", chrom[i]);
  printf(" | Fittness: %d\n", fitness(chrom));
}

int *Reproduce(const int *chromx, const int *chromy)
{
  int rnum = getrand(0, nqueens);
  int *ret = (int *)calloc(nqueens, sizeof(int));

  for (int i = 0; i < rnum; ++i)
    ret[i] = chromx[i];
  for (int i = rnum; i < nqueens; ++i)
    ret[i] = chromy[i];
  return ret;
}

void Mutate(int *chrom)
{
  int rindex = getrand(0, nqueens);
  int rval = getrand(0, nqueens);
  chrom[rindex] = rval;
}

int *RandomPick(const int **population, const double *probs)
{
  double sum = 0;
  for (int i = 0; i < PSIZE; ++i)
    sum += probs[i];

  double rval = (double)(getrand(0, (int)(sum * 1000)) / 1000);
  double upto = 0;

  for (int i = 0; i < PSIZE; ++i)
  {
    if (upto + probs[i] >= rval)
    {
      int *p = malloc(nqueens * sizeof(int));
      memcpy(p, population[i], nqueens * sizeof(int));
      return p;
    }
    upto += probs[i];
  }
  printf("Error! Should not reach here.\n");
  exit(1);
}

void GeneticAlgo(int **population)
{
  int **new_population = (int **)calloc(PSIZE, sizeof(int *)); //new population arr
  double *probs = (double *)calloc(PSIZE, sizeof(double));     //probabilties

  //calculation all probabilites
  for (int i = 0; i < PSIZE; ++i)
    probs[i] = (double)fitness(population[i]) / (double)maxfitness;

  int *chromx = NULL, *chromy = NULL;

  for (int i = 0; i < PSIZE; ++i)
  {
    chromx = RandomPick((const int **)population, (const double *)probs);
    chromy = RandomPick((const int **)population, (const double *)probs);

    //mating and creating child
    int *child = Reproduce((const int *)chromx, (const int *)chromy);

    //free
    free(chromx);
    free(chromy);

    //checking for mutation
    if ((double)(getrand(0, 1000) / 1000) < mutationp)
      Mutate(child);

    new_population[i] = child;

    //check for breaking point
    if (fitness((const int *)child) >= maxfitness)
      break;
  }

  //updating the orignal population array and free memory
  for (int i = 0; i < PSIZE; ++i)
  {
    free(population[i]);
    population[i] = new_population[i];
    new_population[i] = NULL;
  }
  free(probs);
  free(new_population);
}

//true or false
int findfitness(const int **population, int elem)
{
  for (int i = 0; i < PSIZE; ++i)
    if (fitness(population[i]) == elem)
      return 1;
  return 0;
}

int main(int argc, char *argv[])
{
  srand((unsigned)time(NULL)); //Intializes random number generator

  if (argc > 1)
    nqueens = (int)((argv[1]));
  else
  {
    printf("Enter number of queens: ");
    scanf("%i", &nqueens);
  }

  maxfitness = (nqueens * (nqueens - 1)) / 2; //max fitness calculation

  int **population = (int **)calloc(PSIZE, sizeof(int *)); //new population arr
  for (int i = 0; i < PSIZE; ++i)
  {
    population[i] = random_arr(1, nqueens, nqueens);
    print(population[i]);
  }

  int generation = 1;

  while (!findfitness((const int **)population, maxfitness))
  {
    printf("Generation: %d", generation);
    GeneticAlgo(population);
    for (int i = 0; i < PSIZE; ++i)
      if (fitness(population[i]) == maxfitness)
        print(population[i]);
    ++generation;
  }

  for (int i = 0; i < PSIZE; ++i)
    if (fitness(population[i]) == maxfitness)
      print(population[i]);
  printf("Generation: %d", generation);

  for (int i = 0; i < PSIZE; ++i)
    free(population[i]);
  free(population);

  return 0;
}