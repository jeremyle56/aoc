#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    FILE *fp = fopen("input.txt", "r");

    int score = 0;
    char player1;
    char player2;
    while (fscanf(fp, "%c ", &player1) != EOF) {
        fscanf(fp, "%c ", &player2);
        if ((player1 == 'C' && player2 == 'X') || (player1 == 'B' && player2 == 'Z') || (player1 == 'A' && player2 == 'Y')) {
            score += 6;
        } else if ((player1 == 'A' && player2 == 'X') || (player1 == 'B' && player2 == 'Y') || (player1 == 'C' && player2 == 'Z')) {
            score += 3;
        }

        if (player2 == 'X') {
            score += 1;
        } else if (player2 == 'Y') {
            score += 2;
        } else if (player2 == 'Z') {
            score += 3;
        }
    } 
    
    printf("score: %d\n", score);
}