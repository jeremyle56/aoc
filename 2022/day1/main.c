#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static void part1();
static void part2();

int main(void) {
    part1();
    part2();

    return 0;
}

static void part1() {
    FILE *fp = fopen("input.txt", "r");
    int max = 0;
    char line[20];
    
    while (fgets(line, 20, fp) != NULL) {
        int total = atoi(line);
        while (fgets(line, 20, fp) != NULL && strcmp(line, "\n")) {
            total += atoi(line);
        }

        if (total > max) {
            max = total;
        }
    }

    printf("Largest: %d\n", max);
    fclose(fp);
}

static void part2() {
    FILE *fp = fopen("input.txt", "r");
    
    int max, max2, max3;
    max = max2 = max3 = 0;
    char line[20];

    while (fgets(line, 20, fp) != NULL) {
        int total = atoi(line);
        while (fgets(line, 20, fp) != NULL && strcmp(line, "\n")) {
            total += atoi(line);
        }

        if (total > max) {
            max3 = max2;
            max2 = max;
            max = total;
        } else if (total > max2) {
            max3 = max2;
            max2 = total;
        } else if (total > max3) {
            max3 = total;
        }
    }

    printf("Sum of Largest 3: %d\n", max + max2 + max3);
    fclose(fp);
}
