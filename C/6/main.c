#include <stdio.h>
#include <time.h>
#include <stdint.h>
#include <omp.h>

#define uint128_t __uint128_t

int main()
{
    clock_t start = clock();

    int days = 1000000;
    int initial[] = {1,1,1,2,1,1,2,1,1,1,5,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,4,1,1,1,1,3,1,1,3,1,1,1,4,1,5,1,3,1,1,1,1,1,5,1,1,1,1,1,5,5,2,5,1,1,2,1,1,1,1,3,4,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,5,4,1,1,1,1,1,5,1,2,4,1,1,1,1,1,3,3,2,1,1,4,1,1,5,5,1,1,1,1,1,2,5,1,4,1,1,1,1,1,1,2,1,1,5,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,3,1,1,3,1,3,1,4,1,5,4,1,1,2,1,1,5,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,4,1,1,4,1,1,1,1,1,1,1,5,4,1,2,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,4,1,1,1,2,1,4,1,1,1,1,1,1,1,1,1,4,2,1,2,1,1,4,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,3,2,1,4,1,5,1,1,1,4,5,1,1,1,1,1,1,5,1,1,5,1,2,1,1,2,4,1,1,2,1,5,5,3};
    uint128_t fish[] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
    size_t n = sizeof(initial) / sizeof(initial[0]);
    for (int i = 0; i < n; i++)
    {
        fish[initial[i]]++;
    }

    for (int t = 0; t <= days; t++)
    {
        uint128_t newFish = fish[0];
        fish[0] = fish[1];
        for (int i = 0; i <= 8; i++)
        {
            if (i != 0 && i != 8)
            {
                fish[i] = fish[i + 1];
            }
        }
        fish[8] = newFish;
        fish[6] += newFish;
    }

    uint128_t totalFish = 0;
    for (int i = 0; i < 8; i++)
    {
        totalFish += fish[i];
    }
    printf("%llx\n", (unsigned long long)(totalFish & 0xFFFFFFFFFFFFFFFF));
    clock_t end = clock();
    double duration = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Took %f seconds", duration);
    return 0;
//    395627
}
