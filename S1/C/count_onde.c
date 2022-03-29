#include <stdio.h>

/**
 * Function that counts the number of ones of a given integer in its binary representation.
 * @param val value to count its ones.
 * @return Number of ones of an integer.
 */
int count_ones(int val)
{
    int one_mask = 1;
    int val_aux = val;
    int counter = 0;
    for (int i = 0; i < sizeof(int)*8; i++)
    {
        counter += val_aux & one_mask;
        val_aux >>= 1;
    }
    return counter;
}

/**
 * Main function for testing the program.
 */
int main()
{
    int array[] = {1,2,3,4,5,6,7,8,9};
    for (size_t i = 0; i < (sizeof(array)/sizeof(array[0])); i++)
    {
        printf("number of bits of %d -> %d \n",array[i], count_ones(array[i]));
    }
    return 0;
}
