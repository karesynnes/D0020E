#pragma once
#include <stdio.h>
#include <Windows.h>
#include "globals.h"
#include "sensor_list.h"
#include "serialize.h"

#define INPUT_SIZE 128
#define MAX_TOKENS 5
#define MAX_TOKEN_SIZE 16

void readSensorFileScript(SL* sensor_list, char* filename)
{
	SL* sl = (SL*)sensor_list;
	FILE* fp;
	int returnValue = 0;
	char input[INPUT_SIZE] = { '\0' };
	char flag[MAX_TOKENS][MAX_TOKEN_SIZE] = { '\0' };


	if (fp = fopen("sensor_script.txt", "r"))
	{
		memset(flag, 0, sizeof flag);
		while (fscanf(fp, "%s %s %s %s", flag[0], flag[1], flag[2], flag[3]) != EOF)
		{
			
			//Expects input: senval %id %property %value
			if (!strcmp(flag[0], "senval"))
			{
				if (strcmp(flag[3], ""))																			//Checks if there's a 4th argument, if not there are not enough arguments
				{
					if (strcmp(flag[4], ""))																		//Checks if there's a 5th argument, it there is there are too many arguments
					{
						memset(flag, 0, sizeof flag);
						continue;
					}
					else
					{
						returnValue = changeProperty(sl, atoi(flag[1]), flag[2], (float)atof(flag[3]));
					}
				}
				else
				{
					memset(flag, 0, sizeof flag);
					continue;
				}
			}
			else
			{
				memset(flag, 0, sizeof flag);
				continue;
			}
			memset(flag, 0, sizeof flag);
		}
		serializeAll(sl);
		fclose(fp);
	}
	
	return;
}