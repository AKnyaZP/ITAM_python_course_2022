def summation(start, end):
    summ = 0 
    for i in range (start, end+1):
        summ += i
    return summ
start_end = (input())
start_end = start_end.split(" ")
start = int(start_end[0])
end = int(start_end[1])

print (summation(start, end))