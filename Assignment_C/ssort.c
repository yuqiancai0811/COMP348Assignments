#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "fileread.h"
#include "wordtype.h"
#include "output.h"
//Yuqian Cai(40187954)
//comp438 assignment1
//for executing this program you could choose to compile from the command line using the following simple gcc command
// gcc –Wall ssort.c fileread.c wordtype.c output.c
//Then my program will be called a.out by default, when you test my program
// please follow ./a.out <n> <wtype> [<sorttype>] [<skipword1> <skipword2> ...]

// Function to compare words for ascending order
int compareAsc(const void *a, const void *b) {
    const char *strA = *(const char **)a;
    const char *strB = *(const char **)b;
    return strcmp(strA, strB);
}

// Function to compare words for descending order
int compareDesc(const void *a, const void *b) {
    const char *strA = *(const char **)a;
    const char *strB = *(const char **)b;
    return strcmp(strB, strA);
}

int main(int argc, char *argv[]) {
    // Check for sufficient command line arguments
    if (argc < 4) {
        fprintf(stderr, "Usage: %s <inputfile> <n> <wtype> [<sorttype>] [<skipword1> <skipword2> ...]\n", argv[0]);
        return 2;
    }

    int n = atoi(argv[2]);  // Converts n to an integer
    if (n <= 0) {
        fprintf(stderr, "Error: Invalid number of words specified.\n");
        return 1;
    }

    // Determine sort type and check if the fourth argument is a sort type or a skip word
    char *sorttype = "ASC";  // Default sort type
    int sorttypeIndex = 4;

    if (argc > 4 && (strcmp(argv[4], "ASC") == 0 || strcmp(argv[4], "DESC") == 0)) {
        sorttype = argv[4];
        sorttypeIndex = 5;  // Adjust the index for skip words if sort type is provided
    }

    // Process the file and obtain the array of words 
     // argv + sorttypeIndex points to the first skip word
    // argc - sorttypeIndex is the number of skip words
    char **words = readAndProcessFile(argv[1], n, argv[3], sorttype, argv + sorttypeIndex, argc - sorttypeIndex);

    // Sort words based on the sorttype
    if (strcmp(sorttype, "ASC") == 0) {
        qsort(words, n, sizeof(char *), compareAsc);
    } else if (strcmp(sorttype, "DESC") == 0) {
        qsort(words, n, sizeof(char *), compareDesc);
    } else {
        fprintf(stderr, "Error: Invalid sort type specified.\n");
        return 1;
    }

    // Display the sorted words
    printWords(words, n);

    // Clean up dynamically allocated memory
    for (int i = 0; i < n; i++) {
        free(words[i]);  // Free each individual string
    }
    free(words);  // Free the array of pointers

    return 0;
}

