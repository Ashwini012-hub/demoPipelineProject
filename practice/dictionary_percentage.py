student_data = {'jay':{'details':{'roll_no':101, 'marks':[92,80,90]}}}
for s in student_data:
    result = sum(student_data[s]['details']['marks'])/len(student_data[s]['details']['marks'])
print(f"{result}")