#pragma once
//File used for storing global variables that are to be used by several other files

#include "sensor_list.h"


extern int __exit;													//Flag to signify that the program should close down.
const char* switch_sensor = "switch_sensor";						//Used to specify type
const char* power_sensor = "power_sensor";							//Used to specify type
const char* state_sensor = "state_sensor";							//Used to specify type
const char* other_sensor = "other_sensor";							//Used to specify type
const char* dual_sensor = "dual_sensor";							//Used to specify type
