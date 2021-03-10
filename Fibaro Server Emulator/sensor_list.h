#pragma once
#include <malloc.h>
#include <string.h>

//Forward declaration of struct for use in sensor_list struct
struct properties;

//Linked list node
typedef struct sensor_list {
	int id, id2;
	const char* type;
	struct properties* prop;
	struct sensor_list* next;
}SL;

//Used for storing values for sensors
typedef struct properties {
	float power;
	float value;
	float lastBreached;
	float energy;
}properties;

//Wrapper for allocation of memory for properties object
properties* new_properties(float power, float value, float lastBreached, float energy)
{
	properties* new =(properties*)malloc(sizeof(properties));
	if (new)
	{
		new->power = power;
		new->value = value;
		new->lastBreached = lastBreached;
		new->energy = energy;
	}
	else
	{
		new = NULL;
	}
	return new;
}

//Initialization of linked list node
void init_SL(SL* sl, int id, const char* type, properties* prop, SL* next)
{
	sl->id = id;
	sl->id2 = id;
	sl->type = type;
	if (prop != NULL)
	{
		sl->prop = prop;
	}
	else
	{
		sl->prop = new_properties(0.0F, 0.0F, 0.0F, 0.0F);
	}
	sl->next = next;
}

//Allocates memory for a new node and sets the values of its members
int addSensor(SL* list, int id, const char* type)
{
	if (list)
	{
		SL* last_node = list;
		while (last_node->next != NULL)
		{
			last_node = last_node->next;
		}
		last_node->next = (SL*)malloc(sizeof(SL));
		if (last_node->next)
		{
			last_node = last_node->next;
			init_SL(last_node, id, type, NULL, NULL);
		}
		return 0;
	}
	else
	{
		return 1;
	}
}

//Allocates memory for two nodes and sets the values of their members
int addDualSensor(SL* list, int id, const char* type, int id2)
{
	if (list)
	{
		SL* last_node = list;
		while (last_node->next != NULL)
		{
			last_node = last_node->next;
		}
		last_node->next = (SL*)malloc(sizeof(SL));
		if (last_node->next)
		{
			last_node = last_node->next;
			init_SL(last_node, id, type, NULL, NULL);
			last_node->id2 = id2;
		}
		last_node->next = (SL*)malloc(sizeof(SL));
		if (last_node->next)
		{
			last_node = last_node->next;
			init_SL(last_node, id2, type, NULL, NULL);
			last_node->id2 = id;
		}
		return 0;
	}
	else
	{
		return 1;
	}
}

//Traverses linked list in search of id
SL* findSensor(SL* list, int id)
{
	if (list)
	{
		if (list->id == id)
		{
			return list;
		}
		while (list->next)
		{
			if (list->next->id == id)
			{
				return list->next;
			}
			else
			{
				list = list->next;
			}
		}
		return NULL;
	}
	else
	{
		return NULL;
	}
}

//Used for changing properties of nodes
int changeProperty(SL* list, int id, char* property, float value)
{
	list = findSensor(list, id);
	if (list)
	{
		if (!strcmp(property, "energy"))
		{
			list->prop->energy = value;
			return 0;
		}
		else if (!strcmp(property, "lastBreached"))
		{
			list->prop->lastBreached = value;
			return 0;
		}
		else if (!strcmp(property, "power"))
		{
			list->prop->power = value;
			return 0;
		}
		else if (!strcmp(property, "value"))
		{
			list->prop->value = value;
			return 0;
		}
		else
		{
			return 2;
		}
	}
	else
	{
		return 1;
	}
}
