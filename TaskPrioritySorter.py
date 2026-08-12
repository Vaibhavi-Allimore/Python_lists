PMO=[("priority_1",1),("priority_2",2),("priority_3",3),
                                        ("priority_4",4),("priority_5",5)]
for priority in PMO:
    if priority[1]==1:
        print(priority[0],"Urgent")
    elif priority[1]==2 or priority[1]==3:
        print(priority[0],"Normal")
    else:
        print(priority[0],"Low")
