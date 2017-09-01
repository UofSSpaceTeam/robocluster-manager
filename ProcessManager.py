# File ProcessManager.py
# 
# THIS FILE IS SUBJECT TO THE LICENSE TERMS GRANTED BY THE UNIVERSITY OF SASKATCHEWAN SPACE TEAM (USST).

from threading import Thread # Threads are fully functional on Windows.
from multiprocessing.context import Process # Processes are fully functional on Windows.
import time
import sys
from subprocess import Popen

class RoboProcesses:
    def __init__(self, cmd):
        self.cmd = cmd
    def execute(self):
        Popen(self.cmd)



class ProcessManager:
    """
    Class: ProcessManager

    This class represents the pocessing module for the robocluster operating system.
    """
    process_dict = {}


    def __init__(self, **kwargs):
        """Initializes the process manager"""
        self.T = [] # Thread or process library (It is right now a list but it could be changed to something else other than a list).
        return super().__init__(**kwargs)

    def isEmpty(self):
        if T == []:
            return True
        else:
            return False

    def createProcess(self, name, command):
        """
        TODO create a function that takes in parameters and uses those parameters to
        ceate one single process. The process must then be stored in "self.T".
        """
        if type(command) == str:
            return True
        else:
            return False
        process_dict[name] = RoboProcesses(command)



    def createThread(self):
        """
        TODO create a function that takes in parameters and uses those parameters to
        ceate one single thread. The thread must then be stored in "self.T".
        """

    def startProcess(self, name):
        process_dict[name].execute()


    def startAllProcesses(self):
        """
        TODO: create a function that starts all processes or threads in "self.T" all at once.
        """

        for process in process_dict:
            startProcess(process)

    def stopAllProcesses(self):
        """
        TODO: create a function that stops all processes or threads in "self.T" all at once.
        """

        print ("Shutting down")

        for process in process_dict:
            process.execute.kill()
            process.execute.wait()

    def status(self, thread):
        if self.isEmpty():
            return None
        else:
            None
        """
        TODO: Return the status of a thread or process
        """

    def verify(self, thread):
        """
        TODO: Check the status of the thread or process and perform certain functions based on its status.
        """

    def fix(self, thread):
        """
        TODO: Fix a thread or process if its not running properly. 
        """

threadNames = [] # This list is currently used for testing purposes.
# Once the threading module is working fine, then we can begin connecting the proceses through 0mq.
if __name__ == "__main__":
    taskMgr=ProcessManager()
    for name in threadNames: # Create threads for each rover software
        taskMgr.createThread(name)

    taskMgr.startAllProcesses()

    try:
        while True: # Execute the processes.
            """
            TODO Run the processes as they should.
            """
            for task in taskMgr.T: # Verify tasks.
                taskMgr.verify(task.name)
            time.sleep(3)
    except KeyboardInterrupt:
        taskMgr.stopAllProcesses()
        sys.exit(0)