#include <stdio.h>
#include <stdlib.h>

int thereAreReplaces(int N);

int main()
{
    int N;
    // открытие файла
    FILE* inputFile = fopen("../files/input.txt", "r");
    if (inputFile == NULL)
    {
        printf("File not opened\n");
        return 0;
    }
    fscanf(inputFile, "%d", &N);
    fclose(inputFile);
    // алгоритм
    int k = 1; //для того, чтобы увеличивать когда число не имеет одинаковые числа, чтобы попасть в условие останова
    int i = 1; // для итерация
    while (k <= N)
    {
        if (!thereAreReplaces(i))
        {
            k += 1;
        }
        i += 1;
    }
    // сохранение результата в файл
    FILE* outputFile = fopen("../files/output.txt", "w");
    fprintf(outputFile, "%d", i - 1);
    fclose(outputFile);
    return 0;
}

int thereAreReplaces(int N)
{
    // число в строку
    int size = 0;
    char* str = (char*) calloc(size, sizeof(char));
    do
    {
        size += 1;
        str = (char*) realloc(str, size * sizeof(char));
        str[size - 1] = 48 + N % 10;
    }
    while((N /= 10) > 0);
    // строку нужно перевернуть
    char* reverseStr = (char*) calloc(size, sizeof(char));
    for (int i = 0; i < size; i += 1)
    {
        reverseStr[i] = str[size - i - 1];
    }
    free(str);
    // считаем количество цифр
    int index = 0;
    int* arr = (int*) calloc(10, sizeof(int));
    for (int i = 0; i < size; i += 1)
    {
        index = (int) reverseStr[i] - 48;
        arr[index] += 1;
    }
    free(reverseStr);
    // если количество цифр больше 1, то пропускаем это число в алгоритме
    for (int i = 0; i < 10; i += 1)
    {
        if (arr[i] > 1)
        {
            free(arr);
            return 1;
        }
    }
    // если чисел 0 или 1, то алгоритм его не выбрасыват
    free(arr);
    return 0;
}
