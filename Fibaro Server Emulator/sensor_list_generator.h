#pragma once
#include "sensor_list.h"
#include <stdio.h>
#include <string.h>
#include "globals.h"

//Generates linked list from entities specified in sensor_list.txt
SL* fetchList()
{
	SL* list = (SL*)malloc(sizeof(SL));
	init_SL(list, 0, NULL, 0, NULL);
	FILE* fp;
	int id, id2;
	char type[30];


	if (list)
	{
		if (fp = fopen("sensor_list.txt", "r"))
		{
			if (fscanf(fp, "%d %s", &id, type))													//Reads first line from file expecting an integer for id and a string for type and creates the head of the linked list
			{
				list->id = id;
				if (!strcmp(type, "switch_sensor"))
				{
					list->type = switch_sensor;
				}
				else if (!strcmp(type, "power_sensor"))
				{
					list->type = power_sensor;
				}
				else if (!strcmp(type, "state_sensor"))
				{
					list->type = state_sensor;
				}
				else if (!strcmp(type, "other_sensor"))
				{
					list->type = other_sensor;
				}
				else if (!strcmp(type, "dual_sensor"))
				{
					list->type = dual_sensor;
					fscanf(fp, "%d", &id2);
					list->id2 = id2;
					addSensor(list, id2, dual_sensor);
				}
				else
				{
					list->type = NULL;
				}
			}

			while (fscanf(fp, "%d %s", &id, type) != EOF)										//Reads rest of file and creates nodes
			{
				if (!strcmp(type, "switch_sensor"))
				{
					addSensor(list, id, switch_sensor);
				}
				else if (!strcmp(type, "power_sensor"))
				{
					addSensor(list, id, power_sensor);
				}
				else if (!strcmp(type, "state_sensor"))
				{
					addSensor(list, id, state_sensor);
				}
				else if (!strcmp(type, "other_sensor"))
				{
					addSensor(list, id, other_sensor);
				}
				else if (!strcmp(type, "dual_sensor"))
				{
					fscanf(fp, "%d", &id2);
					addDualSensor(list, id, dual_sensor, id2);
				}
				else
				{
					addSensor(list, id, NULL);
				}
			}
			fclose(fp);
			return list;
		}
		else
		{
			printf("list fetch failed.");
		}
	}
	else
	{
		return NULL;
	}
	return NULL;
}