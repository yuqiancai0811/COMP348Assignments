#include "fileread.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "wordtype.h"

// Function: Check if a word is valid based on type and some to skip
bool isWordValid(const char *word, const char *wtype, char **skipwords, int skipcount) {
    // Check against skip words
    for (int i = 0; i < skipcount; i++) {
        if (strcmp(word, skipwords[i]) == 0) {
            return false;  // Skip this word
        }
    }

    // Check word type
    if (strcmp(wtype, "ALPHA") == 0 && !isAlpha(word)) {
        return false;
    } else if (strcmp(wtype, "ALPHANUM") == 0 && !isAlphanum(word)) {
        return false;
    } else if (strcmp(wtype, "ALL") == 0 && !isAll(word)) {
        return false;
    }

    return true;  // The word is valid
}

// Read and process the file according to the word type and skip words
char **readAndProcessFile(const char *filename, int n, const char *wtype, const char *sorttype, char **skipwords, int skipcount) {
    FILE *fptr = fopen(filename, "r");
    if (!fptr) {
        fprintf(stderr, "Failed to open file: %s\n", filename);
        return NULL;
    }

    char **words = (char **)malloc(sizeof(char *) * n); // dynamically allocated array of pointers
    if (!words) {
        fprintf(stderr, "Memory allocation failed\n");
        fclose(fptr);
        return NULL;
    }

    char line[1024]; // Buffer to hold each line read from the file
    int count = 0;  // Count of valid words stored in the array
    while (count < n && fgets(line, sizeof(line), fptr)) {
        char *token = strtok(line, ", \t\n");  // Tokenize the line using comma, space, tab, and newline as delimiters
        while (token && count < n) {
            if (isWordValid(token, wtype, skipwords, skipcount)) {
                words[count] = strdup(token);  // Duplicate the word and store in the array
                count++;
            }
            token = strtok(NULL, ", \t\n");  // Continue tokenizing the line
        }
    }

    fclose(fptr);  // Close the file after reading

    // If fewer words than expected are read and valid, adjust the size of the array
    if (count < n) {
        char **temp = realloc(words, sizeof(char *) * count);
        if (temp) {
            words = temp;
        } else {
            // If realloc fails, continue with the original size but note the actual count
            fprintf(stderr, "Could not reallocate memory, processing what was read\n");
        }
    }

    return words;  // Return the array of words
}

