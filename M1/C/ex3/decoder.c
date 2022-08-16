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

void decoder(const char *file_name)
{
    unsigned char encoded_file[32] = "";
    strcat(encoded_file, (char *)file_name);
    strcat(encoded_file, "_encoded");

    unsigned char decoded_file[32] = "";
    strcat(decoded_file, (char *)file_name);
    strcat(decoded_file, "_decoded");

    unsigned char modelo[LIBRARY_SIZE];

    FILE *source_file, *dest_file;
    dest_file = fopen(decoded_file, "w");
    source_file = fopen(encoded_file, "rb");
    unsigned char cur_char = fgetc(source_file);
    unsigned char buffer = 0;

    // Ler o modelo acaba quando encontro o primeiro caracter repetido
    unsigned char *pch;
    for (int i = 0;; i++)
    {
        pch = strchr(modelo, cur_char);
        if (pch != NULL)
        {
            pch = strchr(pch + 1, cur_char);
            break;
        }
        else
        {
            modelo[i] = cur_char;
            cur_char = fgetc(source_file);
        }
    }

    // Aqui já tenho modelo vou começar a ler o binário e escrever
    //  num ficheiro o descodificado

    buffer = fgetc(source_file);
    unsigned char ahead_buffer = fgetc(source_file);
    unsigned char bit = 128;
    unsigned int bit_counter = 0;
    size_t idx = 0;

    while (!feof(source_file))
    {
        if ((buffer & bit) == 0)
        {
            bit_counter++;
            bit = bit >> 1;
            if (bit_counter != 0)
            {
                if (bit_counter % 8 == 0)
                {
                    buffer = ahead_buffer;
                    ahead_buffer = fgetc(source_file);
                    bit_counter = 0;
                    bit = 128;
                }
            }
            fputc(modelo[idx], dest_file);
            printf("%c", modelo[idx]);
        }
        else
        {
            while ((buffer & bit) > 0)
            {
                bit = bit >> 1;
                bit_counter++;
                if (bit_counter != 0)
                {
                    if (bit_counter % 8 == 0)
                    {
                        buffer = ahead_buffer;
                        ahead_buffer = fgetc(source_file);
                        bit_counter = 0;
                        bit = 128;
                    }
                }
                idx++;
            }
            bit = bit >> 1;
            bit_counter++;

            if (bit_counter != 7)
            {
                bit = bit >> 1;
            }

            if (bit_counter != 0)
            {
                if (bit_counter % 8 == 0)
                {
                    buffer = fgetc(source_file);
                    bit_counter = 0;
                    bit = 128;
                }
            }
            fputc(modelo[idx], dest_file);
            printf("%c", modelo[idx]);
        }
    }
    printf("\n");
    printf("\n");

    fclose(source_file);
    fclose(dest_file);
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

    decoder(&filename[0][0]);
}
