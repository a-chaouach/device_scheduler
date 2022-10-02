import time 


TIME_UNIT = 1 #This is simply to set the regime of the clock (in seconds)

class Task: 
    """ Task

    Small class that saves the properties of each task as well as temporal state
    . (Task identifier, task period, and time since last execution.)
    """    

    def __init__(self,period, task_letter,first_run = True):
        """__init__ 
        Initializes task properties. 
        Args:
            period (int): period in time units between each execution.
            task_letter (char): Task letter.
            first_run (bool, optional): Says whether initial execution before first periodl is allowed.Defaults to True.
        """        
        self.period = period
        self.time_since_last_exec = 0
        self.time_last_exec = 0
        self.task_letter = task_letter
        self.first_run = first_run
        
    def inc_last_time_exec(self):
        """inc_last_time_exec 
        Increments time for this task by one time unit.
        """        
        self.time_since_last_exec += TIME_UNIT

    def reset_time(self):
        """reset_time 
        Resets time for this task.
        """        
        self.time_since_last_exec = 0

tasks= []
letters = ['A','B','C','D','E']
periods = [1,5,5,10,10]
     


def main():
    print("Time (sec) -> Tasks")

    # Intializes each task.
    for i, letter in enumerate(letters):
        tasks.append(Task(periods[i],letter))
    start =time.time()

    while(True):
        time.sleep(TIME_UNIT)
        curr_time = round(time.time()-start) 
        scheduled_tasks=[]
        for task in tasks:
            #Increments the time for each task.
            task.inc_last_time_exec()

            #Makes sure that no more than two tasks are scheduled for running #at the same time.
            if len(scheduled_tasks)<2:
                #Simple check whether we're at new period or the task can be #run regardless (B,C,D,E).
                if task.time_since_last_exec>=task.period or task.first_run:
                        scheduled_tasks.append(task.task_letter)
                        task.reset_time()
                        task.first_run=False
        
        # Printing of the scheduled tasks for this loop. 
        print("{} -> {}".format(curr_time, ' '.join(scheduled_tasks)))


if __name__=="__main__":
    main()