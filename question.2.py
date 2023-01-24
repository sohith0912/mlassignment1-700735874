#creating dog dictionary
dog=dict()
dog["Name"]="Puppy"
dog["Color"]="White"
dog["Breed"]="Bulldog"
dog["legs"]=4
dog["Age"]=5
print("Dog dictionary is : ",dog)
print()

#creating student dictionary
student=dict()
student["first_name"]="Sohith"
student["last_name"]="Soma"
student["Gender"]="Male"
student["Age"]=23
student["Martal status"]="single"
student["Skills"]=["python","Java","Artificial intelligence"]
student["Country"]="India"
student["City"]="Padkal"
student["Address"]="street no 1"
print("Student dictionary is : ",student)
print()

#length of student dictionary
print("length of student dictionary is : ",str(len(student)));

#value of student skills and datatype
print("student skills are : ",end='')
print(student["Skills"])
print("type of student skills is : ",type(student["Skills"]))

#modifying student skills
student["Skills"].append("Problem solving")
student["Skills"].append("Analytical skills")
print("modified student skills : ",student["Skills"])

#getting dictionary keys as list
dog_keys=list(dog.keys())
print("dog dictionary keys : ",dog_keys)
student_keys=list(student.keys())
print("student dictionary keys : ",student_keys)
dog_values=list(dog.values())
print("dog dictionary values : ",dog_values)
student_values=list(student.values())
print("student dictionary values : ",student_values)

