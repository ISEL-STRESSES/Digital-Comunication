#include <stdio.h>

/**
 * Function that counts a symbol present in a file.
 * @param file_name name of the file to read.
 * @param symbol symbol to look for and count its occurrences.
 * @return Number of occurrences of a symbol.
 */
int count_symbol(char *file_name, char symbol)
{
    int SOF = 0;
	int chunk = 16;
	unsigned char buffer[chunk];
	int char_index;
    int counter = 0;

    FILE *file = fopen(file_name, "r");

    while (!feof(file))
    {
        char char_chunck = fread(buffer, sizeof(unsigned char), chunk, file);
        if (char_chunck == 0)
		{
			SOF += char_index;
			break;
		}

        for (char_index = 0; char_index<char_chunck; char_index++)
		{
            if(buffer[char_index] == symbol)
            {
                counter++;
            }
		}
    }
    return counter;
}

/**
 * Main function for testing the program.
 */
int main(int argc, char *argv[])
{
    int counter_of_a = count_symbol(argv[1], 'a');
	printf("number of a %d \n", counter_of_a);

}
