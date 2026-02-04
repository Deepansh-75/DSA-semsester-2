#include <stdio.h>

int removeElement(int* nums, int numsSize, int val) {
    // k will track the index of the next position for a non-val element
    int k = 0;

    for (int i = 0; i < numsSize; i++) {
        // If the current element is not the value we want to remove
        if (nums[i] != val) {
            // Move it to the 'k' position and increment k
            nums[k] = nums[i];
            k++;
        }
    }

    // k represents the count of elements not equal to val
    return k;
}

// Example usage
int main() {
    int nums[] = {0, 1, 2, 2, 3, 0, 4, 2};
    int val = 2;
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    int k = removeElement(nums, numsSize, val);

    printf("k = %d\n", k);
    printf("Modified array: ");
    for (int i = 0; i < k; i++) {
        printf("%d ", nums[i]);
    }
    
    return 0;
}