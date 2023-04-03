import random
import tkinter as tk

thungPhieu = set()
thungPhieu = {"0865518636","0977585816","0977565628","0986044925"}

def add_number():
    soDienThoai = num_entry.get()
    thungPhieu.add(soDienThoai)
    num_entry.delete(0, tk.END)
    result_label.config(text="SDT: {0} đã được thêm vào danh sách trúng thưởng".format(soDienThoai))

def remove_number():
    soDienThoai = num_entry.get()
    if soDienThoai in thungPhieu:
        thungPhieu.discard(soDienThoai)
        num_entry.delete(0, tk.END)
        result_label.config(text="SDT: {0} đã được xóa khỏi danh sách trúng thưởng".format(soDienThoai))
    else:
        result_label.config(text="Không tìm thấy SDT này trong danh sách trúng thưởng")

def draw_winner():
    if len(thungPhieu) == 0:
        result_label.config(text="Không có số điện thoại nào trong danh sách trúng thưởng")
    else:
        soNgauNhien = random.randint(0,len(thungPhieu) -1)
        thungPhieuList = list(thungPhieu)
        winner_label.config(text='Số Điện Thoại chúng thưởng là {0}'.format(thungPhieuList[soNgauNhien]))

window = tk.Tk()
window.title("Chương trình rút thăm chúng thưởng")

# create labels and entry widgets
num_label = tk.Label(window, text="Nhập số điện thoại:")
num_entry = tk.Entry(window)
num_label.grid(row=0, column=0, padx=5, pady=5)
num_entry.grid(row=0, column=1, padx=5, pady=5)

# create buttons for adding, removing and drawing winners
add_button = tk.Button(window, text="Thêm", command=add_number)
remove_button = tk.Button(window, text="Xóa", command=remove_number)
draw_button = tk.Button(window, text="Rút thăm", command=draw_winner)
add_button.grid(row=1, column=0, padx=5, pady=5)
remove_button.grid(row=1, column=1, padx=5, pady=5)
draw_button.grid(row=1, column=2, padx=5, pady=5)

# create label for displaying results
result_label = tk.Label(window, text="")
result_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# create label for displaying the winner
winner_label = tk.Label(window, text="", font=("Helvetica", 16), fg="red")
winner_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

window.mainloop()
