#include <stdio.h>
#include <stdlib.h>

int cube(int number) {
    return number * number * number;
}

int main() {
    int n;
    scanf("%d", &n);

    int *dp = (int *)malloc(sizeof(int) * (n + 1));

    for (int i = 1; i < n + 1; i++) {
        dp[i] = dp[i - 1] + 1;
        int j = 2;
        while (cube(j) <= i) {
            if (dp[i - cube(j)] < dp[i]) {
                dp[i] = dp[i - cube(j)] + 1;
            }
            j++;
        }
    }

    printf("%d", dp[n]);

    return 0;
}