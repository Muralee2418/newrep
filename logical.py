age=int(input("Enter your age"))
qual=input("Enter your Qualification")
status=(age>20 and age<30) and (qual=="BE" or qual=="BSC" or qual=="MCA")
print("Am i Eligible for the course:", status)