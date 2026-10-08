# Bài 1: Chương trình quản lý điểm sinh viên bằng list và dictionary
# Mỗi sinh viên là 1 dictionary: {"id", "name", "score"}
# Tất cả sinh viên được lưu trong 1 list


# Hàm nhập số lượng sinh viên
# Điều kiện: Số nguyên > 0, nhập sai thì nhập lại
def input_number_of_students():
    while True:
        value = input("Enter the number of students: ")
        try:
            n = int(value)
            if n > 0:
                return n
            print("-> Invalid number! Please try again.")
        except ValueError:
            print("-> Invalid number! Please enter an integer.")

# Hàm nhập điểm Python
# Điều kiện: Số nằm trong khoảng 0 - 10, sai thì nhập lại
def input_score():
    while True:
        value = input("Student score (0 - 10): ")
        try:
            score = float(value)
            if 0 <= score <= 10:
                return score
            print("-> Score must be between 0 and 10. Please try again.")
        except ValueError:
            print("-> Invalid score. Please enter a number.")

# Hàm nhập thông tin 1 sinh viên, trả về 1 dictionary
def input_student(index):
    print(f"\nStudent #{index}")
    student_id = input("  Student ID: ")
    full_name = input("  Full name: ")
    score = input_score()

    # Tạo dictionary chứa thông tin sinh viên
    student = {
        "id": student_id,
        "name": full_name,
        "score": score
    }
    return student

# Hàm hiển thị danh sách sinh viên dạng bảng
def display_students(students):
    print(f"{'ID':<10}{'Full name':<25}{'Score':>6}")
    print("-" * 41)
    for s in students:
        print(f"{s['id']:<10}{s['name']:<25}{s['score']:>6.2f}")

# Hàm tìm tất cả sinh viên có điểm cao nhất
def find_highest_students(students):
    highest_score = students[0]["score"]
    for s in students:
        if s["score"] > highest_score:
            highest_score = s["score"]

    highest_students = []
    for s in students:
        if s["score"] == highest_score:
            highest_students.append(s)
    return highest_students

# Hàm tính điểm trung bình
def calculate_average(students):
    total = 0
    for s in students:
        total += s["score"]
    return total / len(students)

# Hàm lấy danh sách sinh viên đậu (score >= 5)
def find_passed_students(students):
    passed = []
    for s in students:
        if s["score"] >= 5:
            passed.append(s)
    return passed

# Hàm nhập dữ liệu -> Lưu vào list -> Hiển thị kết quả
def main():
# 1. Nhập số lượng sinh viên
    n = input_number_of_students()
# 2. Nhập thông tin từng sinh viên và lưu vào list
    students = []
    for i in range(1, n + 1):
        students.append(input_student(i))
# 3. Hiển thị tất cả sinh viên
    print("\n/===== ALL STUDENTS =====/")
    display_students(students)
# 4. Hiển thị sinh viên có điểm cao nhất (tất cả nếu bằng điểm)
    print("\n/===== STUDENT(S) WITH THE HIGHEST SCORE =====/")
    display_students(find_highest_students(students))
# 5. Hiển thị điểm trung bình (làm tròn 2 chữ số thập phân)
    print("\n/===== AVERAGE SCORE =====/")
    print(f"Average score: {calculate_average(students):.2f}")
# 6. Hiển thị sinh viên đậu (score >= 5)
    print("\n/===== PASSED STUDENTS (score >= 5) =====/")
    passed = find_passed_students(students)
    if len(passed) > 0:
        display_students(passed)
    else:
        print("No student passed.")

if __name__ == "__main__":
    main()
