// Contar os symbols do ficheiro
// Contar a probabilidade de cada symbolo no ficheiro
// Calcular a função FMP de cada symbolo
// Ordenar do mais provavel para o menos provavel
// Ir atribuindo um código binário do mais provável para menos

#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>
#include <string.h>

#define LIBRARY_SIZE 256
#define NUMBER_OF_FILES 6
#define FILENAME_SIZE 32
#define UNARY_MAX_SIZE 64
#define TOTAL_PROBABILITY 1

unsigned char charArrayToByte(char *buffer)
{
    unsigned char binaryBuffer = 0;
    int i = 0;

    while (1)
    {
        if (buffer[i] == '0' || buffer[i] == '1')
        {
            break;
        }
        i++;
    }

    int size = i + 7;
    for (; i <= size; i++)
    {
        if (buffer[i] == '0')
        {
            if (i != size)
            {
                binaryBuffer = binaryBuffer << 1;
            }
        }
        else
        {
            binaryBuffer++;
            if (i != size)
            {
                binaryBuffer = binaryBuffer << 1;
            }
        }
    }
    return binaryBuffer;
}

void encoder(const char *file_name)
{
    char encoded_file[64] = "";
    strcat(encoded_file, file_name);
    strcat(encoded_file, "_encoded");

    // Array dos chars e as suas ocorrencias
    unsigned int dictionary[2][LIBRARY_SIZE];
    float fmp[LIBRARY_SIZE];
    float fmp_sum = 0;
    unsigned int nr_total_symb = 0;
    unsigned int nr_dif_symb = 0;
    unsigned char *modelo[LIBRARY_SIZE];

    for (int i = 0; i < LIBRARY_SIZE; i++)
    {
        dictionary[0][i] = i;
        dictionary[1][i] = 0;
    }

    // Contar o numero de ocorrencias de cada symbol por ficheiro
    FILE *source_file;
    source_file = fopen(file_name, "r");
    unsigned char cur_char = fgetc(source_file);
    while (!feof(source_file))
    {
        dictionary[1][cur_char]++;
        cur_char = fgetc(source_file);
    }
    fclose(source_file);

    // Contar o total de symbols por ficheiro
    for (int k = 0; k < LIBRARY_SIZE; k++)
    {
        nr_total_symb += dictionary[1][k];
        if (dictionary[1][k] != 0)
        {
            nr_dif_symb++;
        }
    }

    // Ordenar os symbols pela quantidade de ocurrencias
    for (int x = 0; x < LIBRARY_SIZE - 1; x++)
    {
        for (int y = 0; y < LIBRARY_SIZE - x - 1; y++)
        {
            if (dictionary[1][y] > dictionary[1][y + 1])
            {
                int tempN = dictionary[1][y];
                dictionary[1][y] = dictionary[1][y + 1];
                dictionary[1][y + 1] = tempN;

                int tempChar = dictionary[0][y];
                dictionary[0][y] = dictionary[0][y + 1];
                dictionary[0][y + 1] = tempChar;
            }
        }
    }

    // Calcular a funçao massa de probabilidade de cada symbol no ficheiro
    for (int f = 0; f < LIBRARY_SIZE; f++)
    {
        fmp[f] = dictionary[1][f] / (float)nr_total_symb;
        fmp_sum += fmp[f];
    }

    if (fmp_sum != TOTAL_PROBABILITY)
    {
        return;
    }

    // for para a escrita em modo semi-adaptativo no ficheiro saída
    FILE *dest_file, *file;
    file = fopen(file_name, "r");
    dest_file = fopen(encoded_file, "w+b");

    // Criar a string modelo para colocar no ficheiro encoded
    int f = LIBRARY_SIZE-1;
    for (; fmp[f] != 0; f--)
    {
        modelo[f] = dictionary[0][f];
        fputc(modelo[f], dest_file);
    }
    fputc(modelo[++f], dest_file);

    //--------------------------------------------------------

    cur_char = getc(file);
    unsigned char bin_buffer = 0x0;
    char char_buffer[10] = " ";
    unsigned char bit_counter = 0;
    while (!feof(file))
    {
        if (dictionary[0][255] == cur_char)
        {
            strcat(char_buffer, "0");
            bit_counter++;
            if (bit_counter != 0)
            {
                if (bit_counter % 8 == 0)
                {
                    bin_buffer = charArrayToByte(&char_buffer);
                    fwrite(&bin_buffer, 1, 1, dest_file);
                    memset(char_buffer, '\0', sizeof char_buffer);
                    bit_counter = 0;
                }
            }

            cur_char = getc(file);
        }
        else
        {
            for (int c = 255; dictionary[0][c] != cur_char; c--)
            {

                strcat(char_buffer, "1");
                bit_counter++;
                if (bit_counter != 0)
                {
                    if (bit_counter % 8 == 0)
                    {
                        bin_buffer = charArrayToByte(&char_buffer);
                        fwrite(&bin_buffer, 1, 1, dest_file);
                        memset(char_buffer, '\0', sizeof char_buffer);
                        bit_counter = 0;
                    }
                }
            }
            strcat(char_buffer, "0");
            bit_counter++;
            if (bit_counter != 0)
            {
                if ((bit_counter % 8) == 0)
                {
                    bin_buffer = charArrayToByte(&char_buffer);
                    fwrite(&bin_buffer, 1, 1, dest_file);
                    memset(char_buffer, '\0', sizeof char_buffer);
                    bit_counter = 0;
                }
            }
            cur_char = getc(file);
        }
    }
    while (bit_counter < 7)
    {
        strcat(char_buffer, "1");
        bit_counter++;
    }
    strcat(char_buffer, "1");
    bin_buffer = charArrayToByte(&char_buffer);
    fwrite(&bin_buffer, 1, 1, dest_file);
    memset(char_buffer, '\0', sizeof char_buffer);

    printf("\n");

    fclose(dest_file);
    fclose(file);
}

int main()
{
    // Array de nomes dos ficheiros
    char filename[NUMBER_OF_FILES][FILENAME_SIZE] = {
        "a.txt",
        "alice29.txt",
        "cp.htm",
        "lena.bmp",
        "Person.java",
        "progc.c"};

    for (size_t i = 0; i < NUMBER_OF_FILES; i++)
    {
        printf("%p", &filename[i]);
        encoder(&filename[i][0]);
    }
}