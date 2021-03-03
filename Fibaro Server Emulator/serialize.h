#pragma once
#include "sensor_list.h"
#include <stdio.h>
#include <string.h>


//Turns each node in the linked list into a json object and then puts it into it's own file.
void serializeAll(SL* sensor_list)
{
	int id;																												//Used to create the file path
	char fileName[100];																									//Stores the file path for each iteration
	FILE* fp;																											//File pointer

	while (sensor_list)																									//Goes through the list in order to serialize each node
	{
		id = sensor_list->id;
		sprintf(fileName, "sensors\\%d.json", sensor_list->id);															//Stores the complete path in fileName
		if (fp = fopen(fileName, "w"))
		{
			fprintf(fp, "{\n");																							//Prints to file
			fprintf(fp, "\t\"properties\": [\n\t{\n");																	//Hardcoded to be properties
			if (sensor_list->prop->energy)
			{
				fprintf(fp, "\t\t\"energy\": %.2f", sensor_list->prop->energy);
				if (sensor_list->prop->lastBreached || sensor_list->prop->power || sensor_list->prop->value)			//Adds comma and newline if there are more elements to write
				{
					fprintf(fp, ",\n");
				}
			}
			if (sensor_list->prop->lastBreached)
			{
				fprintf(fp, "\t\t\"lastBreached\": %.2f", sensor_list->prop->lastBreached);								//Adds comma and newline if there are more elements to write
				if (sensor_list->prop->power || sensor_list->prop->value)
				{
					fprintf(fp, ",\n");
				}
			}
			if (sensor_list->prop->power)
			{
				fprintf(fp, "\t\t\"power\": %.2f", sensor_list->prop->power);											//Adds comma and newline if there are more elements to write
				if (sensor_list->prop->value)
				{
					fprintf(fp, ",\n");
				}
			}
			if (sensor_list->prop->value)
			{
				fprintf(fp, "\t\t\"value\": %.2f", sensor_list->prop->value);
			}
			fprintf(fp, "\n\t}\n\t]\n}");																				//Prints closing stuff
		}
		if (fp)
		{
			fclose(fp);
		}
		sensor_list = sensor_list->next;																				//Make the pointer point to the next node
	}
}

void serializeNode(SL* sensor_list, int id)
{																														//id is used to create the file path
	char fileName[100];																									//Stores the file path for each iteration
	FILE* fp;																											//File pointer

	sensor_list = findSensor(sensor_list, id);
	if (sensor_list)																									//Checks if node was found
	{
		sprintf(fileName, "sensors\\%d.json", sensor_list->id);															//Stores the complete path in fileName
		if (fp = fopen(fileName, "w"))
		{
			fprintf(fp, "{\n");																							//Prints to file
			fprintf(fp, "\t\"properties\": [\n\t{\n");																	//Hardcoded to be properties
			if (sensor_list->prop->energy)
			{
				fprintf(fp, "\t\t\"energy\": %.2f", sensor_list->prop->energy);
				if (sensor_list->prop->lastBreached || sensor_list->prop->power || sensor_list->prop->value)			//Adds comma and newline if there are more elements to write
				{
					fprintf(fp, ",\n");
				}
			}
			if (sensor_list->prop->lastBreached)
			{
				fprintf(fp, "\t\t\"lastBreached\": %.2f", sensor_list->prop->lastBreached);								//Adds comma and newline if there are more elements to write
				if (sensor_list->prop->power || sensor_list->prop->value)
				{
					fprintf(fp, ",\n");
				}
			}
			if (sensor_list->prop->power)
			{
				fprintf(fp, "\t\t\"power\": %.2f", sensor_list->prop->power);											//Adds comma and newline if there are more elements to write
				if (sensor_list->prop->value)
				{
					fprintf(fp, ",\n");
				}
			}
			if (sensor_list->prop->value)
			{
				fprintf(fp, "\t\t\"value\": %.2f", sensor_list->prop->value);
			}
			fprintf(fp, "\n\t}\n\t]\n}");																				//Prints closing stuff
		}
		if (fp)
		{
			fclose(fp);
		}
	}
}