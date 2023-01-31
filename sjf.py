from statistics import mean

print("SJF Scheduling")
n = int(input("Enter number of processes ? : "))
process_list = list()

for i in range(n):
    b = int(input("Enter burst time for P" + str(i + 1) + " : "))
    process = ("P"+str(i+1), b)
    process_list.append(process)

process_list.sort(key=lambda item: item[1])

burst_times = [ i[1] for i in process_list ]
exit_times= [ sum(burst_times[0:i+1]) for i in range(n) ]
turnAround_times = exit_times
wait_times = [ exit_times[i]-burst_times[i] for i in range(n) ]

order = "0"
for i in range(n):
    order += "__"+process_list[i][0]+"__"+str(exit_times[i])
print("\n Execution order : \n " + order)

print("\n Average TurnAround Time = ",mean(turnAround_times))
print(" Average Wait Time = ",mean(wait_times))

input()
