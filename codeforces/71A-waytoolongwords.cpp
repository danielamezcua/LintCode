#include <stdio.h>
#include <iostream>

#define MAXLENGTH 101 /* 100 chars + null terminating char */
int main(int argc, char *argv[]){
	int number_of_lines;
	char s[MAXLENGTH];

	scanf("%d", &number_of_lines);

	for (int i = 0; i<number_of_lines; i++){
		scanf("%s", s);
		int j = 0;
		while (s[j] != '\0'){
			j++;
		}
		if (j>10){
			printf("%c%d%c\n", s[0], j-2, s[j-1]);
		}
		else {
			printf("%s\n", s);
		}
	}
}