#include <stdio.h>

/**
 * Problem: Construct an array of length n where all elements
 * and all adjacent sums are pairwise distinct.
 *
 * Strategy: Use odd numbers (1, 3, 5, ...) for elements.
 * Elements will be odd, adjacent sums will be even.
 * This guarantees no element equals any sum.
 */

void solve() {
    int n;
    // Read the size of the array
    if (scanf("%d", &n) != 1) return;

    for (int i = 1; i <= n; i++) {
        // Generate the i-th odd number: 1, 3, 5, ...
        int element = 2 * i - 1;
       
        // Print the element followed by a space or newline
        if (i == n) {
            printf("%d\n", element);
        } else {
            printf("%d ", element);
        }
    }
}

int main() {
    int t;
    // Read the number of test cases
    if (scanf("%d", &t) != 1) return 0;

    while (t--) {
        solve();
    }

    return 0;
}
