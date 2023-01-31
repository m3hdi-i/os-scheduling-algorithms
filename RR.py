from statistics import mean

class Process:
    def __init__(self,name,burst_time):
        self.name=name
        self.remaining_time = burst_time

print("Round Robin Scheduling")
n = int(input("Enter number of processes : "))
process_list = list()

for i in range(n):
    process_name = "P" + str(i + 1)
    b = int(input("Enter burst time for " + process_name + " : "))
    process = Process(process_name,b)
    process_list.append(process)

q = int(input("Enter quantom : "))

burst_times = [ i.remaining_time for i in process_list ]

exit_times = [ 0 for i in range(n) ]

completed_processess=0
order="0"
current_time=0

while completed_processess != n:
    for i,p in enumerate(process_list):
        if p.remaining_time!=0:
            if p.remaining_time <= q:
                current_time+=p.remaining_time
                exit_times[i]=current_time
                process_list[i].remaining_time=0
                completed_processess+=1
            else:
                current_time+= q
                process_list[i].remaining_time -= q

            order += "__" + p.name + "__" + str(current_time)

turnAround_times = exit_times
wait_times = [ exit_times[i]-burst_times[i] for i in range(n) ]

print("\n Execution order : \n " + order)
print("\n Average TurnAround Time = ",mean(turnAround_times))
print(" Average Wait Time = ",mean(wait_times))

input()
