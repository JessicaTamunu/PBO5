class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_data(self):
        print(f"Nama      : {self.name}")
        print(f"Jabatan   : {self.position}")
        print(f"Gaji      : Rp{self.salary:,.0f}")


class Company:
    def __init__(self, name):
        self.name = name
        self.__employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.__employees.append(employee)
            print(f"{employee.name} berhasil ditambahkan.")
        else:
            print("Error: Data yang dimasukkan bukan objek Employee.")

    def show_employees(self):
        print(f"\n=== DATA KARYAWAN {self.name.upper()} ===")

        if not self.__employees:
            print("Belum ada data karyawan.")
            return

        for i, employee in enumerate(self.__employees, 1):
            print(f"\nKaryawan {i}")
            employee.display_data()

    def __calculate_payroll(self):
        total = 0

        for employee in self.__employees:
            total += employee.salary

        return total

    def show_payroll(self):
        total = self.__calculate_payroll()

        print("\n=== TOTAL PAYROLL ===")
        print(f"Perusahaan : {self.name}")
        print(f"Jumlah Karyawan : {len(self.__employees)}")
        print(f"Total Gaji : Rp{total:,.0f}")


# Membuat objek perusahaan
company = Company("Tech Indonesia")

# Membuat objek karyawan
employee1 = Employee("Jessica", "Programmer", 5000000)
employee2 = Employee("Maria", "UI/UX Designer", 4500000)
employee3 = Employee("Daniel", "System Analyst", 6000000)

# Menambahkan karyawan ke perusahaan
company.add_employee(employee1)
company.add_employee(employee2)
company.add_employee(employee3)

# Menampilkan data karyawan
company.show_employees()

# Menghitung dan menampilkan total payroll
company.show_payroll()

# Percobaan memasukkan objek yang bukan Employee
print("\n=== VALIDASI OBJECT ===")
company.add_employee("Bukan objek Employee")