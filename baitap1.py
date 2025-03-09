"""
Đề bài:
  - Nhận một dữ liệu string từ input
  - Làm cho string di chuyển từ trái sang phải
"""

# Import các thư viện
import os
import time

# Các hằng số
IS_WINDOW = True  # Nếu chạy trên mac hoặc linux thì chỉnh thành False
# lệnh clear command prompt trên mac là clear trên window là cls
CLEAR_SCREEN_COMMAND = "cls" if IS_WINDOW else "clear"
SPACES = 50  # số khoảng trắng
DURATION = 10  # thời lượng (giây) chuyển động theo một hướng
TIME_PER_SPACE = DURATION / SPACES  # thời gian tăng một khoảng trắng

# Nhận string từ người dùng
a = input()

# Tạo một hàm nhận tham số x mô phỏng vị trí trong hệ trục Ox


def print_(x, string):
    """
    giả sử string = "nam"
    x = 0 => print("nam")
    x = 1 => print(" nam")
    x = 2 => print("  nam")
    x = 3 => print("   nam")
    """
    print(" " * x + string)


# Lặp khi x thuộc đoạn [0, SPACES - 1]
for x in range(SPACES):
    print_(x, a)
    time.sleep(TIME_PER_SPACE)
    print(x)
    os.system(CLEAR_SCREEN_COMMAND)

""" 
Giải thích các dòng code:
time.sleep(x) dừng trong môt khoảng thời gian x(giây)
os.system(x) thực hiên câu lệnh x trong terminal ví dụ cls, cd Desktop, rmdir abcdef (xóa thự mục)
"""
