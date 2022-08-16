#include <stdio.h>

/**
 * Function that prints in binary representation an array of integers.
 * @param array array of integer to print.
 * @param array_size size of the given array.
 */
void print_bits(int array[], size_t array_size)
{
    for (int i = 0; i < array_size; i++)
    {
        int value = array[i];
        printf("number %d in binary \t",value);
        for (int j = (sizeof(int)*8)-1; j >= 0; j--)
        {
            if((j+1) % 4 == 0)
            {
                putchar(' ');
            }
            unsigned char byte = (value >> j) & 1;
            printf("%u", byte);
        }
        putchar('\n');
    }
}

/**
 * Main function for testing the program.
 */
int main()
{
    int array[] = {1,2,3,4,5,6,7,8,9,10};
    print_bits(array, sizeof(array)/sizeof(array[0]));
}
