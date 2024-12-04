class Student:
    def __init__(self, nama, umur, nilai):
        self.name = nama
        self.age = umur
        self.score = nilai

    def __str__(self):
        return f"Nama: {self.name}, Umur: {self.age}, Nilai: {self.score}"


class Kelas:
    def __init__(self, nama):
        self.name = nama
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        student_list = "\n".join([str(student) for student in self.students])
        return f"Nama Kelas: {self.name}\nJumlah Mahasiswa: {len(self.students)}\nDaftar Murid:\n{student_list}"


class University:
    def __init__(self, nama):
        self.name = nama
        self.classes = []

    def add_class(self, class_):
        self.classes.append(class_)

    def __str__(self):
        class_list = "\n".join([str(class_) for class_ in self.classes])
        return f"Nama Universitas: {self.name}\nJumlah Kelas: {len(self.classes)}\nDaftar Kelas:\n{class_list}"


def jadi():
    # Proses Pembuatan Universitas
    while True :
        university_name = input("Masukkan nama universitas: ")
        if university_name:
            university = University(university_name)
            break
        else :
            print ("Nama Universitas harus di isi, silahkan coba lagi")

    # Proses Pembuatan Kelas    
    while True:
        class_name = input("Masukkan nama kelas: ")
        if class_name :
            class_ = Kelas(class_name)
            university.add_class(class_)
        else :
            print ("Nama Kelas harus di isi, Silahkan coba lagi")
            continue 
        
        while True:
            more_classes = input("Apakah Anda ingin menambahkan kelas lagi? (Ya/Tidak): ")
            if more_classes in ["Ya","Tidak"]:
                break
            else:
                print("Jawaban Tidak Valid, Jawab Iya atau Tidak")
        if more_classes == "Tidak":
            break
        
    # Proses Pembuatan Data Siswa dalam kelas
    for class_ in university.classes:
        while True:
            #input Nama Mahasiswa
            student_name = input(f"Masukkan nama Mahasiswa untuk kelas {class_.name}: ")
            if not student_name:
                print ("Nama Mahasiswa harus di isi, Silahkan coba lagi")
                continue
            #input Usia Mahasiswa
            try:
                student_age = int(input(f"Masukkan umur Mahasiswa untuk kelas {class_.name}: "))
            except ValueError:
                print("Masukan Usia Mahasiswa Berupa Angka, Silahkan Coba Lagi")
                continue
            
            #input Nilai Mahasiswa
            try:
                student_score = float(input(f"Masukkan nilai Mahasiswa untuk kelas {class_.name}: "))
            except ValueError:
                print("Masukan Nilai Mahasiswa Berupa Angka, Silahkan Coba lagi")
                continue
                
            student = Student(student_name, student_age, student_score)
            class_.add_student(student)

            while True:
                more_students = input("Apakah Anda ingin menambahkan Mahasiswa lagi? (Ya/Tidak): ")
                if more_students in ["Ya","Tidak"]:
                    break
                else:
                    print("Jawaban Tidak Valid, Jawab Iya atau Tidak")
            if more_students == "Tidak":
                break

    print("\n"*2)
    print(university)


print(jadi())
