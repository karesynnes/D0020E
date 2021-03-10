#pragma once
#include <stdio.h>
#include <process.h> 
#include <Windows.h>

//Used for storing pointer to a thread
typedef struct thrd
{
    HANDLE thread;
    unsigned int id;
} thrd;


//Allocates memory for and starts specified process and then returns a pointer to that thread
thrd* newthread(unsigned int (__stdcall* func)(void*), void* arguments)
{
    thrd* thread = (thrd*)malloc(sizeof(thrd));

    if (!thread)
    {
        printf("Memory for thread could not be allocated. Shutting down.");
        return 0;
    }

    thread->thread = (HANDLE)_beginthreadex(0, 0, func, arguments, 0, &(thread->id));

    return thread;
}

//Waits for thread to finish and then frees the memory allocated by it
void join(thrd* thread)
{
    if (thread && thread->thread != 0)
    {
        WaitForSingleObject((thread->thread), INFINITE);
        free(thread);
    }
}