from csv import DictReader, reader, writer, DictWriter

print("\n--- 1 ---")
with open("files/file1.txt") as file:
    print(file.read())
    print("---")
    file.seek(0)
    print(file.readline())
    print("---")
    file.seek(0)
    print(file.readlines())
print("---")
file = open("files/file1.txt")
print(file.read())
file.close()


print("\n--- 2 ---")
with open("files/file1.txt", "w") as file:
    file.write("Irasyta pirma eilute\n")
    file.write("Irasyta antra eilute\n")

with open("files/file1.txt", 'a') as file:
    file.write("prideta nauja eilute\n")

with open("files/file1.txt") as file:
    file_content = file.read()
    print(file_content)
    with open("files/file2.txt", "w") as file2:
        file2.write(file_content)

print("\n--- 3 ---")
with open("files/cars.txt") as file:
    print(file.read())
    file.seek(0)
    lines = file.readlines()
    year_list= [int(line.split(" - ")[1].rstrip("\n")) for line in lines]
    avg_years = sum(year_list)/len(year_list)
    print(f"Vidutinis automobilio amžius: {avg_years} metai")


print("\n--- 4 ---")
with open("files/students.csv") as file:
    csv_reader = DictReader(file, delimiter=",")
    student_list = list(csv_reader)
    student_list.sort(key= lambda x: x["Vidurkis"], reverse=True)
    list_of_averages = [float(student["Vidurkis"]) for student in student_list]
    print(f"Pažangiausias studentas: {student_list[0]['Vardas']} {student_list[0]["Pavardė"]}. Vidurkis: {student_list[0]['Vidurkis']}")
    print(f"Studentų pažymių vidurkis: {round(sum(list_of_averages)/len(list_of_averages),1)}")


print("n\--- 5 ---")
with open("files/data.csv") as file:
    csv_reader = DictReader(file, delimiter=";")
    housing_list = list(csv_reader)
    for row in housing_list:
        print(row)
    plotai = [int(housing['Plotas']) for housing in housing_list]
    kainos = [int(housing['Kaina']) for housing in housing_list]
    print(f"Vidutinis būsto plotas: {round(sum(plotai)/len(plotai))}")
    print(f"Vidutinė būsto kaina: {round(sum(kainos)/len(kainos))}")

print("\n--- 6 ---")
with open("files/students.csv") as file:
    csv_reader = DictReader(file, delimiter=",")
    student_list = list(csv_reader)

student_list.sort(key= lambda x: x["Vidurkis"], reverse=True)
print(student_list)
best = student_list[0]
worst = student_list[-1]
best_student_str = f"Geriausias studentas {best['Vardas']} {best['Pavardė']} (Vidurkis {best['Vidurkis']})\n"
worst_student_str = f"Prasčiausias studentas {worst['Vardas']} {worst['Pavardė']} (Vidurkis {worst['Vidurkis']})\n"
grades = [float(student["Vidurkis"]) for student in student_list]
avg_grade = round(sum(grades)/len(grades),1)
avg_grade_str = f"Studentų vidurkis: {avg_grade}\n"
print(best_student_str)
print(worst_student_str)
print(avg_grade_str)

with open("files/students_summary.txt", "w") as file:
    file.write(best_student_str)
    file.write(worst_student_str)
    file.write(avg_grade_str)

print("\n--- 7 ---")
with open("files/students.csv") as file:
    students = DictReader(file, delimiter=",")
    student_list = list(students)
    good_students = [student for student in student_list if float(student["Vidurkis"])>9]
    [print(student) for student in good_students]

with open("files/students_filtered.csv", 'w', newline="") as file:
    headers = list(good_students[0].keys())
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for student in good_students:
        csv_writer.writerow(student)








