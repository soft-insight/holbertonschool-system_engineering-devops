#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while -Is a infinite while with sleep
 *
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
 * main - main function
 *
 * Return: when is sucess
 */


int main(void)
{
	pid_t pid;
	int i;

	while (i < 5)
	{
		pid = fork();
		if (pid)
			printf("Zombie process created, PID: %d\n", pid);
		else
			return (0);
		i++;
	}
	infinite_while();
	return (0);
}
