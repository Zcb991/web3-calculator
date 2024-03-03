import tkinter as tk

class web3_calculator:
    root = None
    button_frame = None
    calculate_button1 = None
    calculate_button2 = None
    calculate_button3 = None
    calculate_button4 = None
    calculate_temp = None
    label1 = None
    label2 = None
    input_entry1 = None
    input_entry2 = None
    calculate_button = None
    result_label = None

    # 全局按钮id
    global_btn_id = 1

    def __init__(self):
        # 创建主窗口
        self.root = tk.Tk()
        self.root.title("简易计算器")

        # 设置窗口为置顶
        self.root.attributes('-topmost', True)

        # 创建按钮框架
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()
        self.calculate_button1 = tk.Button(self.button_frame, text="多", command=lambda: self.switch_bg_color(1))
        self.calculate_button2 = tk.Button(self.button_frame, text="空", command=lambda: self.switch_bg_color(2))
        self.calculate_button3 = tk.Button(self.button_frame, text="分批进场", command=lambda: self.switch_bg_color(3))
        self.calculate_button4 = tk.Button(self.button_frame, text="分批出场", command=lambda: self.switch_bg_color(4))
        self.calculate_button1.pack(side="left")
        self.calculate_button2.pack(side="left")
        self.calculate_button3.pack(side="left")
        self.calculate_button4.pack(side="left")
        
        # 初始化，默认加载第一个按钮
        self.calculate_button1.config(bg='red')
        
        # 创建输入框和标签
        self.label1 = tk.Label(self.root, text="Costs:")
        self.label1.pack()

        self.input_entry1 = tk.Entry(self.root, width=40)
        self.input_entry1.pack()

        # 创建百分比输入框和标签
        self.label2 = tk.Label(self.root, text="止损位:")
        self.label2.pack()

        self.input_entry2 = tk.Entry(self.root, width=40)
        self.input_entry2.pack()

        # 创建计算按钮
        self.calculate_button = tk.Button(self.root, text="计算", command=self.calculate)
        self.calculate_button.pack()

        # 创建结果显示标签
        self.result_label = tk.Label(self.root, text="结果: ")
        self.result_label.pack(pady=10)

        self.root.mainloop()
        
    # 定义按钮点击事件
    def more(self):
        self.calculate_button1.config(bg="red")  # 设置按钮背景色为红色
        self.calculate_button2.config(bg=self.root.cget('bg'))  # 恢复原始颜色
        self.calculate_button3.config(bg=self.root.cget('bg'))  # 恢复原始颜色
        self.calculate_button4.config(bg=self.root.cget('bg'))  # 恢复原始颜色
        value1 = self.input_entry1.get()
        value2 = self.input_entry2.get()
        try:
            diff = float(value1)- float(value2)
            text = ''
            start = 1
            end = 2.5
            step = 0.5

            current_value = start
            while current_value < end:
                # Your operation using current_value
                # print(current_value)
                text += f'盈亏比 1:{current_value}，Price：{value1 + diff * current_value}\n'
                current_value += step

            # for i in range(1, 2.5, 0.5):
            #     text += f'盈亏比 1:{i}，Price：{value1 + diff * i}\n'
            self.result_label.config(text=text)
        except ValueError:
            self.result_label.config(text="请输入有效的数字")

    def less(self):
        self.calculate_button1.config(bg=self.root.cget('bg'))  # 设置按钮背景色为红色
        self.calculate_button2.config(bg="red")  # 恢复原始颜色
        self.calculate_button3.config(bg=self.root.cget('bg'))  # 恢复原始颜色
        self.calculate_button4.config(bg=self.root.cget('bg'))  # 恢复原始颜色

    def batch_buy(self):
        self.calculate_button1.config(bg=self.root.cget('bg'))  # 恢复原始颜色
        self.calculate_button2.config(bg=self.root.cget('bg'))  # 恢复原始颜色
        self.calculate_button3.config(bg="red")  # 设置按钮背景色为红色
        self.calculate_button4.config(bg=self.root.cget('bg'))  # 恢复原始颜色
        value1 = self.input_entry1.get()
        value2 = self.input_entry2.get()
        try:
            text = ''
            for i in range(3):
                result = float(value1) * (1 - float(value2) * 0.01 * (i + 1))
                text += f'Price{i+1}：{round(result, 4)}\n'
            self.result_label.config(text=text)
        except ValueError:
            self.result_label.config(text="请输入有效的数字")

    def batch_sell(self):
        self.calculate_button1.config(bg=self.root.cget('bg'))  # 恢复原始颜色
        self.calculate_button2.config(bg=self.root.cget('bg'))  # 恢复原始颜色
        self.calculate_button3.config(bg=self.root.cget('bg'))  # 恢复原始颜色
        self.calculate_button4.config(bg="red")  # 设置按钮背景色为红色
        value1 = self.input_entry1.get()
        value2 = self.input_entry2.get()
        try:
            text = ''
            for i in range(3):
                result = float(value1) * (1 + float(value2) * 0.01 * (i + 1))
                text += f'Price{i+1}：{round(result, 4)}\n'
            self.result_label.config(text=text)
        except ValueError:
            self.result_label.config(text="请输入有效的数字")

    def switch_bg_color(self, btn_id):
        # global global_btn_id
        self.global_btn_id = btn_id
        for i in range(1, 5):
            self.calculate_temp = getattr(self, f"calculate_button{i}")
            # self.calculate_temp = eval(self.calculate_temp)
            if i == btn_id:
                self.calculate_temp.config(bg='red')  # 设置按钮背景色为红色
            else:
                self.calculate_temp.config(bg=self.root.cget('bg'))   # 设置其他按钮恢复原始颜色
        if btn_id == 1 or btn_id == 2:
                self.label2.config(text="止损位:")
        else:
            self.label2.config(text="百分比:")
        # btn_id = f"calculate_button{btn_id}"
        # btn_id = eval(btn_id)
        # btn_id.config(bg="red")  # 设置按钮背景色为红色


    def calculate(self):
        # print(global_btn_id)
        # 根据全局id来判断当前按下的是哪一个按钮
        value1 = self.input_entry1.get()
        value2 = self.input_entry2.get()
        try:
            text = ''
            value1 = float(value1)
            value2 = float(value2)
            if self.global_btn_id == 1 or self.global_btn_id == 2:
                start = 1
                end = 2.5
                step = 0.5

                current_value = start
                while current_value < end:
                    if self.global_btn_id == 1:
                        diff = value1 - value2
                        text += f'盈亏比 1:{current_value}，Price：{value1 + diff * current_value}\n'
                    else:
                        diff = value2 - value1
                        text += f'盈亏比 1:{current_value}，Price：{value1 - diff * current_value}\n'
                    current_value += step

                self.result_label.config(text=text)
            else:
                for i in range(3):
                    if self.global_btn_id == 3:
                        result = float(value1) * (1 - float(value2) * 0.01 * (i + 1))
                    else:
                        result = float(value1) * (1 + float(value2) * 0.01 * (i + 1))
                    text += f'Price{i+1}：{round(result, 4)}\n'
                self.result_label.config(text=text)
        except ValueError:
            self.result_label.config(text="请输入有效的数字")


if __name__ == "__main__":
    wc = web3_calculator()