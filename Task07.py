attendance=[1,0,1,1,1,0,1,0,0,1]
print("attendance:",attendance)
present=attendance.count(1)
absent=attendance.count(0)
print("Present students:",present)
print("absent students:",absent)
percentage=(present/10)*100
print("Percentage:",percentage)
