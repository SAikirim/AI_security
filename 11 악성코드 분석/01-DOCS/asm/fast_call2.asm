#include <stdio.h>
int __fastcall sum(int a, int b, int c, int d)
{
	int e = a + b + c + d;
	return e;
}
int main(int argc, char* argv[])
{
	sum(1,2,3,4);
	return 0;
}