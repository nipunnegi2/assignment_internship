

employees = [
    {"name": "Nipun", "organization": "QuickHeal"},
    {"name": "Faizan", "organization": "GrayMatter"},
    {"name": "Shobin", "organization": "SecureBlink"},
    {"name": "Chhankar", "organization": "QuickHeal"},
    {"name": "Arvind", "organization": "Yahoo"}
]



def search_quickheal_employees(employee_list):
    quickheal_employees = []
    for employee in employee_list:
        if employee["organization"] == "QuickHeal":
            quickheal_employees.append(employee)
    return quickheal_employees


result = search_quickheal_employees(employees)

if result:
    print("Employees from QuickHeal:")
    for emp in result:
        print(f"Name: {emp['name']}, Organization: {emp['organization']}")
else:
    print("No employees from QuickHeal found.")
