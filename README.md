# Python-Background-Website-Blocker
Demo: https://www.youtube.com/watch?v=G8x3HEla7Vo  
  
Program that blocks certain websites on windows machines and runs in the background. Does this by modifying the hosts file and redirecting specifed websites such as facebook and reddit to localhost. Can be set to run on startup on PC or laptop.

HOW TO RUN FILE ON START UP
Open Task Scheduler and click on create task
provide a name for the task such as "website blocker"
check 'run with highest priorities' as the script needs admin rights to modify the host file
under configure for, select your version of windows
then goto triggers, new and select run at startup from the drop down menu
then goto actions, new, browse and select the .pyw file, not the .py file and the .pyw file is the one that runs in the background
then goto conditions and uncheck start only if plugged in and charging.

Add websites you want to block to the list and can change redirect to some other site or change blocked times if needed.
