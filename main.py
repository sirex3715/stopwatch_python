import time
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("StopWatch")

        # 表示盤の描画
        self.upper_frame = tk.Frame(self, bg="black")
        self.text = tk.StringVar()
        self.text.set("0.0")
        self.Label = tk.Label(self.upper_frame, textvariable=self.text, width=20,
                              background="black", foreground="white").pack(fill=tk.X)
        self.upper_frame.pack(padx=10, pady=10)

        # ボタンの描画
        self.lower_frame = tk.Frame(self, bg="black")
        self.button1 = tk.Button(self.lower_frame, text="開始", width=8, command=self.click_start).pack(side=tk.LEFT)
        self.button2 = tk.Button(self.lower_frame, text="停止", width=8, command=self.click_stop).pack(side=tk.LEFT)
        self.button3 = tk.Button(self.lower_frame, text="リセット", width=8, command=self.click_reset).pack(side=tk.LEFT)
        self.lower_frame.pack()

        # 状態の初期化
        self.play_time = False
        self.start_time = None
        self.now_time = None
        self.count_time = 0.0
        self.text_time = 0.0

        # 10msごとに表示盤を更新
        self.after(10, self.update_time)

    def click_start(self):
        if not self.play_time:
            # 現在の時間をstart_timeに格納
            self.start_time = time.time()
            # ストップウォッチの起動フラグ
            self.play_time = True
        print("start")

    def click_stop(self):
        if self.play_time:
            # 開始のたびにリセットされないよう、現在カウントしている数字を格納
            self.count_time = self.now_time - self.start_time
            self.play_time = False
        print("stop")

    def click_reset(self):
        if self.play_time:
            self.play_time = True
        self.start_time = None
        self.count_time = 0.0
        self.text.set("0.0")

    def update_time(self):
        if self.play_time:
            self.now_time = time.time()

            # 現在の時間 - 開始時間 + 蓄積時間を表示盤へ反映
            self.text_time = self.now_time - self.start_time + self.count_time
            self.text.set('{:.2f}'.format(self.text_time))

        # 自身を呼び出して定期的に表示盤を更新する
        self.after(10, self.update_time)


if __name__ == "__main__":
    app = App()
    app.mainloop()
