#include <stdio.h>

#define CHAR_MAX_SIZE 255


/**
 * Function that counts a symbol present in a file.
 * @param file_name name of the file to read.
 * @return a map of a file.
 */
char* count_symbols(char *file_name)
{
	int chunk = 16;
	unsigned char buffer[chunk];
    char array[CHAR_MAX_SIZE] = {};

    FILE *file = fopen(file_name, "r");
    
    while (!feof(file))
    {
        char char_chunck = fread(buffer, sizeof(unsigned char), chunk, file);
        if (char_chunck == 0) 
		{
			break;
        }

        for (size_t char_index = 0; char_index < char_chunck; char_index++)
		{
            array[buffer[char_index]]++;
		}
    }
    return array;
}

void sort()
{

}


int main(int argc, char *argv[])
{
    printf("%s", argv[1]);
    char *map = count_symbols(argv[1]);
    for (size_t i = 0; i < CHAR_MAX_SIZE; i++)
    {
        printf("ASCII value = %d, Character = %c\n", map[i], map[i]);
    }
}