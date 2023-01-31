from statistics import mean

class Process:
    def __init__(self,name,arrival_time,burst_time,priority):
        self.name= name
        self.arrival_time= arrival_time
        self.burst_time = burst_time
        self.priority= priority

print("Priority Scheduling")
n = int(input("Enter number of processes : "))
process_list = list()

for i in range(n):
    process_name = "P" + str(i + 1)
    a = int(input("Enter arrival time for " + process_name + " : "))
    b = int(input("Enter burst time for " + process_name + " : "))
    pr = int(input("Enter priority for " + process_name + " : "))
    process = Process(process_name, a, b,pr)
    process_list.append(process)

process_list_final=[]
exit_times = []
completed_processes=0
order="0"
current_time=0



while completed_processes != n:

    ready_processes = list(filter(lambda p: p.arrival_time <= current_time, process_list))
    ready_processes.sort(key=lambda p: p.priority)
    if len(ready_processes)>0:
        process_to_run = ready_processes[0]
        current_time += process_to_run.burst_time
        exit_times.append(current_time)

        completed_processes+=1
        process_list.remove(process_to_run)
        process_list_final.append(process_to_run)

        order+= "__" + process_to_run.name + "__" + str(current_time)

    else:
        current_time += 1
        order += "_✕_" + str(current_time)


arrival_times = [p.arrival_time for p in process_list_final]
burst_times = [p.burst_time for p in process_list_final]

turnAround_times = [exit_times[i] - arrival_times[i] for i in range(n)]
wait_times = [ exit_times[i] - burst_times[i] - arrival_times[i] for i in range(n) ]

print("\n Execution order : \n " + order)
print("\n Average TurnAround Time = ", mean(turnAround_times))
print(" Average Wait Time = ", mean(wait_times))

input()
