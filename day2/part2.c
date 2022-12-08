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
        if (player2 == 'Y') {
            score += 3;
        } else if (player2 == 'Z') {
            score += 6;
        }

        if (player2 == 'Y' && player1 == 'A') {
            score += 1;
        } else if (player2 == 'Y' && player1 == 'B') {
            score += 2;
        } else if (player2 == 'Y' && player1 == 'C') {
            score += 3;
        } else if (player2 == 'X' && player1 == 'A') {
            score += 3;
        } else if (player2 == 'X' && player1 == 'B') {
            score += 1;
        } else if (player2 == 'X' && player1 == 'C') {
            score += 2;
        } else if (player2 == 'Z' && player1 == 'A') {
            score += 2;
        } else if (player2 == 'Z' && player1 == 'B') {
            score += 3;
        } else if (player2 == 'Z' && player1 == 'C') {
            score += 1;
        }
    } 
    
    printf("score: %d\n", score);
}