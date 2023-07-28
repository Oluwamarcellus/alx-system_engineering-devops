#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

/**
 * infinite_while - Runs forever if not interrupted
 * Return: 0
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Program that creates 5 zombie processes
 * Return: 0
*/
int main(void)
{
	int c_p = 0;
	int pid;

	for (c_p = 0; c_p < 5; c_p++)
	{
		pid = fork();
		if (!pid)
			break;
		printf("Zombie process created, PID: %d\n", pid);
	}
	if (pid > 0)
		infinite_while();
	return (0);
}
