#include "sensor_list.h"
#include "sensor_list_generator.h"
#include "serialize.h"
#include <stdio.h>
#include <process.h> 
#include <Windows.h>
#include "newthread.h"
#include "input.h"
#include "readSensorFileScript.h"


//Creates a linked list of all sensors specified in sensor_list.txt and then creates a thread for the console input.
int main(int argc, char** argv)
{
    char* scriptname = "sensor_script.txt";
    SL* sensor_list = fetchList();
    readSensorFileScript(sensor_list, scriptname);
    thrd* consoleThrd = newthread(&console, sensor_list);

    join(consoleThrd);
    return 0;
}