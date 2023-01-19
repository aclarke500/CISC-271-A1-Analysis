from lib import listToString


edges=[]



with open('21asc6.txt') as file:
    for f in file:
            line=f #get line from file


            num1 = []
            num2 = []

            for i in range(len(line) -1):
                if (i <= 4 and line[i] != ' '):
                    num1.append(line[i])
                elif ( i>=4 and line[i] != ' '):
                    num2.append(line[i])




            num1 = int(listToString(num1))
            num2 = int(listToString(num2))
            edges.append([num1, num2])

            
            # end=int(len(line)-1) 
            # line=line[0:end] #cut off '/n' that is stored in text file
            # averages.append(line)

# print(edges)

set_1 = [1, 2, 4, 6, 7, 11, 12, 14, 15, 18]
set_1_in_counts = []
set_1_out_counts = []


set_2 = [3, 5, 8, 9, 10, 13, 16, 17, 19, 20]
set_2_in_counts = []
set_2_out_counts = []

for i in range(10):
    set_1_in_counts.append(0)
    set_2_out_counts.append(0)
    set_1_out_counts.append(0)
    set_2_in_counts.append(0)


# get each time the set[i] occurs in edges

for e in edges:
    if set_1.count(e[0]) != 0: # in set 1
        index = set_1.index(e[0])

        if set_1.count(e[1]) != 0: # its in same set
            set_1_in_counts[index]+=1
        else:
            set_1_out_counts[index]+=1

    elif set_2.count(e[0]) != 0: # in set 1
        index = set_2.index(e[0])
        
        if set_2.count(e[1]) != 0: # its in same set
            set_2_in_counts[index]+=1
        else:
            set_2_out_counts[index]+=1

average_in_set_1_in = sum(set_1_in_counts)/len(set_1_in_counts)
# print(average_in_set_1_in)

average_in_set_1_out = sum(set_1_out_counts)/len(set_1_out_counts)
# print(average_in_set_1_out)


average_in_set_2_in = sum(set_2_in_counts)/len(set_2_in_counts)
# print(average_in_set_2_in)

average_in_set_2_out = sum(set_2_out_counts)/len(set_2_out_counts)
# print(average_in_set_2_out)


print("Average inside set 1: ", average_in_set_1_in)
print("Average outside set 1: ", average_in_set_1_out)
print("Average outside set 2: ", average_in_set_2_in)
print("Average inside set 2: ", average_in_set_2_out)



