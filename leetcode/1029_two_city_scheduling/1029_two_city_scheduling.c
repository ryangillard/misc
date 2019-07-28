struct CostDifference
{
    int index;
    int diff;
};

int isGreater(const void *a, const void *b)
{
    return (*(struct CostDifference*)a).diff > (*(struct CostDifference*)b).diff ? 1 : -1;
}

int twoCitySchedCost(int** costs, int costsSize, int* costsColSize){
    int i, min_cost = 0;
    
    struct CostDifference* person;
    person = malloc(sizeof(person) * costsSize);
    
    for (i = 0; i < costsSize; i++)
    {
        person[i].index = i;
        person[i].diff = costs[i][1] - costs[i][0];
    }
    
    qsort(person, costsSize, sizeof(struct CostDifference), isGreater);
    
    for (i = 0; i < costsSize / 2; i++)
    {
        min_cost += costs[person[i].index][1] + costs[person[i + costsSize / 2].index][0];
    }
    
    free(person);
    
    return min_cost;
}