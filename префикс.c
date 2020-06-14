#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LENGHT (1000001)


int main() {
    char string[MAX_LENGHT];
    scanf("%s", string);
    int len = strlen(string);

    int *prefixes = (int *)calloc(len, sizeof(int));

    for (int i = 1; i < len; i++) {
        int p = prefixes[i - 1];
        while (p > 0 && string[i] != string[p]) {
            p = prefixes[p - 1];
        }
        if (string[i] == string[p]) {
            p += 1;
        }
        prefixes[i] = p;
    }

    for (int i = 0; i < len; i++) {
        printf("%d ", prefixes[i]);
    }

    return 0;
}