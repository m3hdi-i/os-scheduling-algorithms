from statistics import mean

class Process:
    def __init__(self,name,burst_time):
        self.name=name
        self.remaining_time = burst_time

print("FCFS Scheduling")
n = int(input("Enter number of processes : "))
process_list = list()

for i in range(n):
    process_name = "P" + str(i + 1)
    a = int(input("Enter arrival time for " + process_name + " : "))
    b = int(input("Enter burst time for " + process_name + " : "))
    process = (process_name, a, b)
    process_list.append(process)

process_list.sort(key=lambda item: item[1])

arrival_times = [i[1] for i in process_list]
burst_times = [i[2] for i in process_list]

exit_times = []
for i in range(n):
    if i == 0:
        et = arrival_times[0] + burst_times[0]
    else:
        if arrival_times[i] <= exit_times[i - 1]:
            et = exit_times[i - 1] + burst_times[i]
        else:
            et = arrival_times[i] + burst_times[i]

    exit_times.append(et)

turnAround_times = [exit_times[i] - arrival_times[i] for i in range(n)]
wait_times = [exit_times[i] - burst_times[i] - arrival_times[i] for i in range(n)]

order = str(process_list[0][1])
for i in range(n):
    if i!=0 and arrival_times[i]>exit_times[i-1]:
        order += "__✕__" + str(arrival_times[i])

    order += "__" + process_list[i][0] + "__" + str(exit_times[i])

print("\n Execution order : \n " + order)

print("\n Average TurnAround Time = ", mean(turnAround_times))
print(" Average Wait Time = ", mean(wait_times))

input()
