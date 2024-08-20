#include "output.h"
#include <stdio.h>

void printWords(char **words, int count) {
    for (int i = 0; i < count; i++) {
    //separate words using a whitespace, for every 10th word which must follow a single newline
        printf("%s%s", words[i], (i % 10 == 9) ? "\n" : " ");
        
    }
    printf("\n");
    
}




