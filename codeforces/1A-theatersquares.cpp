#include <stdio.h>

int main(int argc, char *argv[]){
	unsigned int m,n,a;
	unsigned long long int squaresm, squaresn;
	unsigned long long int totalsquares;
	scanf("%u %u %u", &m, &n, &a);

	squaresn= (m%a == 0) ? m/a : (m/a) + 1;
	squaresm= (n%a == 0) ? n/a : (n/a) + 1;
	totalsquares = squaresn*squaresm;
	printf("%llu\n", totalsquares);
}