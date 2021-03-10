#pragma once
#include <stdio.h>
#include <process.h> 
#include <Windows.h>
#include "globals.h"
#include "sensor_list.h"

#define INPUT_SIZE 128
#define MAX_TOKENS 5
#define MAX_TOKEN_SIZE 16
int __exit;

//Console thread for handling input and output to console
unsigned int _stdcall console(void* sensor_list)
{
	SL* head = (SL*)sensor_list;
	SL* current = (SL*)sensor_list;
	int returnValue = 0;
	__exit = 0;
	char scanLength[16];
	char input[INPUT_SIZE] = { '\0' };
	char* token;
	char flag[MAX_TOKENS][MAX_TOKEN_SIZE] = {'\0'};

	sprintf(scanLength, "%%%d[^\n]", INPUT_SIZE);
	printf("Write 'senval #id #type #value' to change value of sensor with sensor id #id\nand type #type into value #value.\n\nWrite 'senlst' to see a list of all sensors.\n\nWrite 'exit' to exit program.\n\n");
	while (__exit != 1)
	{
		memset(flag, 0, sizeof flag);

		scanf(scanLength, input);
		while (getchar() != '\n')												//I don't even know, it just works
		{
			continue;
		}

		token = strtok(input, " ");												//Divide input with delimiter ' ' (space)
		for (int i = 0; token && i < MAX_TOKENS; i++) 
		{
			sprintf(flag[i], "%s", token);										//Put each part into the array of strings 'flag'
			token = strtok(NULL, " ");
		}

		if (!strcmp(flag[0], "senlst"))
		{
			while (current)
			{
				printf("id: %d\t\ttype: %s\n", current->id, current->type);
				current = current->next;
			}
		}
		if (!strcmp(flag[0], "exit"))
		{
			__exit = 1;															//Sets exit flag to 1 in order to signify that we want to quit the program
		}

		//Expects input: senval %id %property %value
		else if (!strcmp(flag[0], "senval"))
		{
			if (strcmp(flag[3], ""))																			//Checks if there's a 4th argument, if not there are not enough arguments
			{
				if (strcmp(flag[4], ""))																		//Checks if there's a 5th argument, it there is there are too many arguments
				{
					printf("\nToo many arguments.\n");
					Sleep(1000);
					continue;
				}
				else
				{
					returnValue = changeProperty(head, atoi(flag[1]), flag[2], (float) atof(flag[3]));
					if (returnValue == 1)
					{
						printf("\nSensor %s could not be found.\n", flag[1]);
						Sleep(1000);
						continue;
					}
					else if (returnValue == 2)
					{
						printf("\nProperty %s could not be found.\n", flag[2]);
						Sleep(1000);
						continue;
					}
					else
					{
						printf("\nProperty %s of sensor %s changed to value %s.\n", flag[1], flag[2], flag[3]);
						serializeNode(head, atoi(flag[1]));														//Turns node into JSon and prints to file
						Sleep(1000);
						continue;
					}
				}
			}
			else
			{
				printf("\nMissing arguments\n");
				Sleep(1000);
				continue;
			}
		}	
	}
	return 0;
}