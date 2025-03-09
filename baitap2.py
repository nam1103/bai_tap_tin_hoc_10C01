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
SPACES_PER_DIRECTION = 20  # số khoảng trắng theo một hướng
"""
NẾU MUỐN CÓ SỰ khác biệt về số khoảng trắng và hàng theo hướng thì có thể làm như sau:
SPACES_PER_DIRECTIONS = {
    "left": 50,
    "right": 50,
    "down": 20,
    "up": 20
}
SPACES_PER_DIRECTION["left"]
"""

DURATION = 5  # thời lượng (giây) chuyển động theo một hướng
# thời gian tăng một khoảng trắng
TIME_PER_SPACE = DURATION / SPACES_PER_DIRECTION

# Các biến
a = input()  # Nhận string từ người dùng
x = y = 0  # vị trí khởi đầu string ở A(0, 0)

# Tạo một hàm nhận tham số x mô phỏng vị trí trong hệ trục Oxy


def print_(x, y, string):
    """
    giả sử string = "nam"
    x = 0 => print("nam")
    x = 1 => print(" nam")
    x = 2 => print("  nam")
    x = 3 => print("   nam")
    y = 4 => print("\n\n\n\nnam")
    """
    print("\n" * y + " " * x + string)


# Lặp từ trái sang phải
for _ in range(SPACES_PER_DIRECTION):
    print_(x, y, a)
    time.sleep(TIME_PER_SPACE)
    os.system(CLEAR_SCREEN_COMMAND)
    x += 1

# Lặp từ trễn xuống dưới
for _ in range(SPACES_PER_DIRECTION):
    print_(x, y, a)
    time.sleep(TIME_PER_SPACE)
    os.system(CLEAR_SCREEN_COMMAND)
    y += 1

# Lặp từ phải sang trái
for _ in range(SPACES_PER_DIRECTION):
    print_(x, y, a)
    time.sleep(TIME_PER_SPACE)
    os.system(CLEAR_SCREEN_COMMAND)
    x -= 1

# Lặp từ phải sang trái
for _ in range(SPACES_PER_DIRECTION):
    print_(x, y, a)
    time.sleep(TIME_PER_SPACE)
    os.system(CLEAR_SCREEN_COMMAND)
    y -= 1


""" 
Giải thích các dòng code:
time.sleep(x) dừng trong môt khoảng thời gian x(giây)
os.system(x) thực hiên câu lệnh x trong terminal ví dụ cls, cd Desktop, rmdir abcdef (xóa thự mục)
\n kí hiệu tạo một hàng mới trong văn bản
"""
