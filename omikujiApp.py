import tkinter as tk #tkintnerを導入し、「tk」に省略して使う
import random

def displabel():
    kuji = ["大吉", "中吉", "小吉",  "凶"]
    lbl.configure(text=random.choice(kuji))

root = tk.Tk() #ウィンドウ作成
root.geometry("300x200") #ウィンドウのサイズ調整

# 作成
lbl = tk.Label(text="LABEL") #ラベル作成
btn = tk.Button(text="PUSH",command = displabel) #ボタン作成

# 配置
lbl.pack() #ラベル配置
btn.pack() #ボタン配置
tk.mainloop() #ウィンドウを表示