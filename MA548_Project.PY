import numpy as np
import csv
import pandas as pd 



# Input value
my_data = pd.read_excel('UEFA_Champions_League.xlsx',header=None)

print('[Inital Value]\n')
print(my_data,'\n')
# print('\n',my_data.iloc[0,2])

# Initial Value
Group1 = np.array([[my_data.iloc[0,2],my_data.iloc[0,1],my_data.iloc[0,3]],
                    [my_data.iloc[1,2],my_data.iloc[1,1],my_data.iloc[1,3]],
                    [my_data.iloc[2,2],my_data.iloc[2,1],my_data.iloc[2,3]],
                    [my_data.iloc[3,2],my_data.iloc[3,1],my_data.iloc[3,3]],
                    [my_data.iloc[4,2],my_data.iloc[4,1],my_data.iloc[4,3]],
                    [my_data.iloc[5,2],my_data.iloc[5,1],my_data.iloc[5,3]],
                    [my_data.iloc[6,2],my_data.iloc[6,1],my_data.iloc[6,3]],
                    [my_data.iloc[7,2],my_data.iloc[7,1],my_data.iloc[7,3]],
                    ])

Group2 = np.array([[my_data.iloc[8,2],my_data.iloc[8,1],my_data.iloc[8,3]],
                    [my_data.iloc[9,2],my_data.iloc[9,1],my_data.iloc[9,3]],
                    [my_data.iloc[10,2],my_data.iloc[10,1],my_data.iloc[10,3]],
                    [my_data.iloc[11,2],my_data.iloc[11,1],my_data.iloc[11,3]],
                    [my_data.iloc[12,2],my_data.iloc[12,1],my_data.iloc[12,3]],
                    [my_data.iloc[13,2],my_data.iloc[13,1],my_data.iloc[13,3]],
                    [my_data.iloc[14,2],my_data.iloc[14,1],my_data.iloc[14,3]],
                    [my_data.iloc[15,2],my_data.iloc[15,1],my_data.iloc[15,3]],
                    ])

Table_initial = np.zeros(64).reshape(8,8)
# You can change value as below:
# Table_initial[0,1] =1
print('[INITAL TABLE]\n')
print(Table_initial)

print('\n[Group1]\n')
print(Group1)
print('\n[Group2]\n')
print(Group2)

# We check traps as below
# print(Group1[0,2]==Group2[2,2])
def trap2(list_input,keep_list):
    '''Club of Group1 that Group2 can choose '''
    global Group1, Group2
    in_trap2 = 0
    choose_1 = 99
    choose_2 = 99
    count = 0
    for i in keep_list:
        if len(list_input[i]) <= 1:
            in_trap2 = 1
            choose_1 = i
            choose_2 = list_input[i][0]
            count += 1
    if count >=2:
        in_trap2 = 3
        choose_1 = 99
        choose_2 = 99
    # We will return booln that if it is in trap or not(means all len of list1 is larger than 1 or not)
    return in_trap2, choose_1, choose_2

def trap3(list_input,left_list):
    '''Club of Group2 that Group1 can choose '''
    global Group1,Group2
    # for dongda and yuxiang
    in_trap3 = 0
    choose_1 = 99
    choose_2 = 99
    count = 0
    for i in left_list:
        if len(list_input[i]) <= 1:
            in_trap3 = 1
            choose_1 = list_input[i][0]
            choose_2 = i
            count += 1
    if count >=2:
        in_trap2 = 3
        choose_1 = 99
        choose_2 = 99
      # We will return booln that if it is in trap or not(means all len of list2 is larger than 1 or not)
    return in_trap3, choose_1, choose_2

# We run 10 times 
N1 = 100000
# Deep copy that I will not copy the address 
# The copy method makes a complete copy of the array and its data.
TABLE = Table_initial.copy()
wrong = 0
for i in range(N1):
    print('\n[ Round',i,']:')
    # Initial Table at first
    Table_bug = np.zeros(64).reshape(8,8)
    # Initial List1 for group1 and group2, ones they are in same country, corresponding coordinate just remove it 
    # Two ways, one is below, other is use np.ones.reshape and become to 0 one in trap
    List1 = [[1,2,3,4,5,6,7],
             [0,2,3,4,5,6,7],
             [0,1,3,4,5,6,7],
             [0,1,2,4,5,6,7],
             [0,1,2,3,5,6,7],
             [0,1,2,3,4,6,7],
             [0,1,2,3,4,5,7],
             [0,1,2,3,4,5,6]]

    List2 = [[1,2,3,4,5,6,7],
             [0,2,3,4,5,6,7],
             [0,1,3,4,5,6,7],
             [0,1,2,4,5,6,7],
             [0,1,2,3,5,6,7],
             [0,1,2,3,4,6,7],
             [0,1,2,3,4,5,7],
             [0,1,2,3,4,5,6]]

    # First DELETE all elements that are in same country
    # List 1
    for j in range(8):
        for k in range(8):
            if Group1[j,2]==Group2[k,2]:
                List1[j].remove(k)
    # List 2
    for j in range(8):
        for k in range(8):
            if Group2[j,2]==Group1[k,2]:
                List2[j].remove(k)
    # This is a indicator for checking Group2 leave which didnt chosed
    Group_leave = [0,1,2,3,4,5,6,7]
    # This is a indicator for checking Group1 leave which didnt chosed
    Group_keep = [0,1,2,3,4,5,6,7]
    # print('\n',List1,'\n',List2)
    # For Group1 1st and 2nd choose
    
    for j in range(2):
        # So for here, we choose randomly and ignore the trap2 and trap3
        random_choose = np.random.randint(len(List1[j]))
        TABLE[j][List1[j][random_choose]] += 1
        Table_bug[j][List1[j][random_choose]] += 1
        remove_club = List1[j][random_choose]
        # print(remove_club)
        Group_leave.remove(remove_club)
        Group_keep.remove(j)

        
        # print('Group_keep:',Group_keep,'\n')
        # print('Group_leave:',Group_leave,'\n')
        # print(Group_leave)
        # remove all elements in list 1 and list 2 that has just been chosed
        for l in range(8):
            if remove_club in List1[l]:
                List1[l].remove(remove_club)
            if j in List2[l]:
                List2[l].remove(j)
        
        # print(j,remove_club)
        # print('\n',List1,'\n',List2)
        # print('\n',TABLE)
    for j in range(2,8):
        index2 = trap2(List1,Group_keep)
        index3 = trap3(List2,Group_leave)
        if (index2[0]==3):
            TABLE -= Table_bug
            wrong += 1
            break
        elif (index2[0]==1):
            TABLE[index2[1]][index2[2]] += 1
            Table_bug[index2[1]][index2[2]] +=1
            Group_leave.remove(index2[2])
            Group_keep.remove(index2[1])
            # print('Group_keep:',Group_keep,'\n')
            # print('Group_leave:',Group_leave,'\n')
            # remove all elements in list 1 and list 2 that has just been chosed
            for l in range(8):
                if  index2[2] in List1[l]:
                    List1[l].remove(index2[2])
                if index2[1] in List2[l]:
                    List2[l].remove(index2[1])
            # print(index2[1],index2[2])
            # print('\n',List1,'\n',List2)
            # print('\n',TABLE)
        elif(index3[0]==3):
            TABLE -= Table_bug
            wrong += 1
            break
        elif(index3[0]==1):
            TABLE[index3[1]][index3[2]] += 1
            Table_bug[index3[1]][index3[2]] += 1
            Group_leave.remove(index3[2])
            Group_keep.remove(index3[1])
            # print('Group_keep:',Group_keep,'\n')
            # print('Group_leave:',Group_leave,'\n')
            # remove all elements in list 1 and list 2 that has just been chosed
            for l in range(8):
                if index3[2] in List1[l]:
                    List1[l].remove(index3[2])
                if index3[1] in List2[l]:
                    List2[l].remove(index3[1])
            # print(index3[1],index3[2])
            # print('\n',List1,'\n',List2)
            # print('\n',TABLE)

        else:
            # So for here, we choose randomly 
            # we remove the first element in Gruop 1 left
            left_else = Group_keep[0]
            random_choose = np.random.randint(len(List1[left_else]))
            TABLE[left_else][List1[left_else][random_choose]] += 1
            Table_bug[left_else][List1[left_else][random_choose]] += 1
            remove_club = List1[left_else][random_choose]
            
            
            Group_leave.remove(remove_club)
            Group_keep.remove(left_else)
            # print('Group_keep:',Group_keep,'\n')
            # print('Group_leave:',Group_leave,'\n')
            # remove all elements in list 1 and list 2 that has just been chosen
            for l in range(8):
                if remove_club in List1[l]:
                    List1[l].remove(remove_club)
                if left_else in List2[l]:
                    List2[l].remove(left_else)
            # print(j,remove_club,'\n')
            # print('\n',List1,'\n',List2)
            # print('\n',TABLE)

    #     print('\n',remove_club,List1[0])
    # print('\n',List1,'\n',List2)

    # print('\n',TABLE)
    

result = TABLE/(N1-wrong)

print('\n',result)         

np.savetxt('2017-2018Result.csv',result, delimiter = ',')

