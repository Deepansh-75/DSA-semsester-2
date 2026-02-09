#include <stdio.h>
#include <string.h>

int main() {
    char str[1001]; // Buffer to hold the string (adjust size as needed)
    
    // Read the input string
    scanf("%s", str);

    // Get the length of the string
    int len = strlen(str);
    
    // Loop only up to half the length of the string
    for (int i = 0; i < len / 2; i++) {
        // Store the character at the current index in a temporary variable
        char temp = str[i];
        
        // Replace the character at the start with the character from the end
        str[i] = str[len - 1 - i];
        
        // Put the stored character at the end position
        str[len - 1 - i] = temp;
    }

    // Print the transformed string
    printf("%s", str);

    return 0;
}