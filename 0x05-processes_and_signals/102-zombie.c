#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>

/**
 * infinite_while - function for parent proccess get sleep
 * Return: (0)
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
 * main - Program that creates 5 zombie process.
 * Return: 0
 */

int main(void)
{
	int count;
	pid_t child_pid;

	for (count = 0; count < 5; count++)
	{
		child_pid = fork();
		if (child_pid > 0)
			printf("Zombie process created, PID: %d\n", child_pid);
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
