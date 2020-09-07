#include <stdio.h>
int __fastcall sum(int a, int b)
{
	int c = a + b;
	return c;
}
int main(int argc, char* argv[])
{
	sum(1,2);
	return 0;
}