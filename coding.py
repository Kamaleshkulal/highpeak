def findMaxEarnings(jobs):
    n = len(jobs)
    jobs.sort(key=lambda x: x[2], reverse=True)
    totalEarnings = 0
    taskCounter = 0
    endTime = 0
    for i in range(n):
        if jobs[i][0] >= endTime:
            endTime = jobs[i][1]
            taskCounter += 1
        else:
            totalEarnings += jobs[i][2]
    return [n - taskCounter, totalEarnings]

def main():
    numJobs = int(input("Enter the number of Jobs: "))
    print("Enter job  start time, end time,and earning")
    jobs = []
    for i in range(numJobs):
        startTime = int(input())
        endTime = int(input())
        earnings = int(input())
        jobs.append([startTime, endTime, earnings])
    result = findMaxEarnings(jobs)
    print("The number of tasks and earnings available for others")
    print("Task:", result[0])
    print("Earnings:", result[1])

if __name__ == '__main__':
    main()