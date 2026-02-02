#include <stdio.h>

int main() {
    int n, pos, i;

    // Read the number of elements
    if (scanf("%d", &n) != 1) return 0;

    int arr[n];

    // Read the array elements
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Read the 1-based position to delete
    scanf("%d", &pos);

    // Logic to delete the element:
    // We start at the target index and move every element 
    // after it one step to the left.
    for (i = pos - 1; i < n - 1; i++) {
        arr[i] = arr[i + 1];
    }

    // Print the updated array (now containing n-1 elements)
    for (i = 0; i < n - 1; i++) {
        printf("%d", arr[i]);
        if (i < n - 2) {
            printf(" "); // Print space between elements
        }
    }

    return 0;
}