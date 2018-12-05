/*
 * MIT License
 * 
 * Copyright (c) 2018 cz7asm
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

#include <ctype.h>
#include <stdio.h>

void hexdump(const void *src, size_t size)
{
    const unsigned char *src8 = src;
    const int CNT = 16;

    for (size_t i=0; i < size; i++) {
        int n = i % CNT;
        if (n == 0)
            printf("%04x: ", i);
        printf("%02X ", src8[i]);
        if ((i && n==CNT-1) || i+1==size) {
            int rem = CNT-1 - n;
            for (int j=0; j < rem; j++)
                printf("   ");
            printf("|");
            for (int j=n; j >= 0; j--)
                putchar(isprint(src8[i-j])?src8[i-j]:'.');
            printf("|\n");
        }
    }
}
