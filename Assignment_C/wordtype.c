#include "wordtype.h"
#include <ctype.h>  // For character checking functions


// Check if all characters in the word are alphabetic ([a-z] or [A-Z])
bool isAlpha(const char *word) {
    if (!*word) // Check for an empty string
        return false;
    
    for (int i = 0; word[i] != '\0'; i++) {  // Iterate over each character until '\0'
        if (!isalpha((unsigned char)word[i])) {
            return false;  // Return false if the character is not alphabetic
        }
    }
    return true;
}

// Check if all characters in the word are alphanumeric ([a-z], [A-Z], [0-9])
bool isAlphanum(const char *word) {
    if (!*word) // Check for an empty string
        return false;
    
    for (; *word; word++) {
        if (!isalnum((unsigned char)*word)) {
            return false;
        }
    }
    return true;
}

// Check if the word is non-empty (since 'ALL' seems to include any non-empty string)
bool isAll(const char *word) {
    return *word != '\0'; // Return true if the string is not empty
}

