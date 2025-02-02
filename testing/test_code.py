# This is input data
n = int(input("input num of rows"))  # Number of rows
m = int(input("input num of cols"))  # Number of rows

# This is the solution to my problem:
matrix = [[0] * m for _ in range(n)]


# For each row in the matrix
counter = 0
for row in range(n):
    for col in range(m):
        matrix[row][col] = counter
        counter += 1

print(matrix)
# 3
# 1 2 3
# 4 5 6
# 7 8 9


# StaffName = ["John", "Alice", "Bob", "Anthony"]
# StaffPhone = ["12345", "67890", "54321", "56432"]
# StaffOffice = ["A1", "B1", "A1", "C3"]
# TotalStaff = len(StaffName)
#
#
# def display_sorted_by_name(StaffName, StaffPhone, StaffOffice):
#     # This procedure runs bubble sort to sort arrays by names
#     for i in range(0, len(StaffName)):
#         for j in range(0, len(StaffName) - 1):
#             if StaffName[j] > StaffName[j+1]:
#                 # swap staff names
#                 temp = StaffName[j+1]
#                 StaffName[j+1] = StaffName[j]
#                 StaffName[j] = temp
#
#                 # swap staff phone
#                 temp = StaffPhone[j+1]
#                 StaffPhone[j+1] = StaffPhone[j]
#                 StaffPhone[j] = temp
#
#     for i in range(0, len(StaffName)):
#         print(StaffName[i], StaffPhone[i])
#
#
# def group_by_office():
#     print("Staff Grouped by Office:")
#     for i in range(TotalStaff):
#         office = StaffOffice[i]
#         print(f"Office {office}:", end=" --> ")
#         for j in range(TotalStaff):
#             if StaffOffice[j] == office:
#                 print(f"{StaffName[j]} - {StaffPhone[j]}", end=", ")
#         print()
#
#
# def display_staff_details(name):
#     for i in range(TotalStaff):
#         if StaffName[i] == name:
#             print("Staff Details:")
#             print(f"Name: {StaffName[i]}")  # print name
#             print(f"Phone: {StaffPhone[i]}")  # print phone number
#             print(f"Office: {StaffOffice[i]}") # print office number
#             return
#     print("Staff member not found.")
#
#
# def update_staff_details(name):
#     for i in range(TotalStaff):
#         if StaffName[i] == name:
#             new_phone = input("Enter new phone number: ")
#             new_office = input("Enter new office: ")
#             StaffPhone[i] = new_phone
#             StaffOffice[i] = new_office
#             print("Details updated successfully.")
#             return
#     print("Staff member not found.")
#
#
# #
# # def display_sorted_by_name():
# #     for i in range(0, TotalStaff - 1):
# #         for j in range(0, TotalStaff - 1):
# #             if StaffName[j] > StaffName[j + 1]:
# #                 # Swap StaffName
# #                 StaffName[j], StaffName[j + 1] = StaffName[j + 1], StaffName[j]
# #                 # Swap corresponding StaffPhone and StaffOffice
# #                 StaffPhone[j], StaffPhone[j + 1] = StaffPhone[j + 1], StaffPhone[j]
# #                 StaffOffice[j], StaffOffice[j + 1] = StaffOffice[j + 1], StaffOffice[j]
# #     # Display sorted staff names and phone numbers
# #     print("Staff Phone Numbers and Names in Alphabetical Order:")
# #     for i in range(TotalStaff):
# #         print(StaffName[i], StaffPhone[i])
# #
# # # Function to group staff by office
# # def group_by_office():
# #     print("Staff Grouped by Office:")
# #     for i in range(TotalStaff):
# #         office = StaffOffice[i]
# #         print(f"Office {office}:")
# #         for j in range(TotalStaff):
# #             if StaffOffice[j] == office:
# #                 print(f"  {StaffName[j]} - {StaffPhone[j]}")
# #
# # # Function to display staff details by name
# # def display_staff_details(name):
# #     for i in range(TotalStaff):
# #         if StaffName[i] == name:
# #             print("Staff Details:")
# #             print(f"Name: {StaffName[i]}")
# #             print(f"Phone: {StaffPhone[i]}")
# #             print(f"Office: {StaffOffice[i]}")
# #             return
# #     print("Staff member not found.")
#
# # # Function to update staff details by name
# # def update_staff_details(name):
# #     for i in range(TotalStaff):
# #         if StaffName[i] == name:
# #             new_phone = input("Enter new phone number: ")
# #             new_office = input("Enter new office: ")
# #             StaffPhone[i] = new_phone
# #             StaffOffice[i] = new_office
# #             print("Details updated successfully.")
# #             return
# #     print("Staff member not found.")
# #
# # display_sorted_by_name()
#
#
# #
# # # Main Program
# # while True:
# #     print("\n1. Display Staff Names and Phone Numbers Sorted")
# #     print("2. Display Staff Grouped by Office")
# #     print("3. Display Details of a Staff Member")
# #     print("4. Update Staff Details")
# #     print("5. Exit")
# #     choice = int(input("Enter your choice: "))
# #
# #     if choice == 1:
# #         display_sorted_by_name()
# #     elif choice == 2:
# #         group_by_office()
# #     elif choice == 3:
# #         name = input("Enter staff name: ")
# #         display_staff_details(name)
# #     elif choice == 4:
# #         name = input("Enter staff name: ")
# #         update_staff_details(name)
# #     elif choice == 5:
# #         print("Program Terminated.")
# #         break
# #     else:
# #         print("Invalid choice. Please try again.")

