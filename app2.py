#tkintnerを導入し、「tk」に省略して使う
import tkinter as tk

#ボタンが押されたらラベルをこんにちはに変更
def displabel():
    lbl.configure(text="こんにちは")

root = tk.Tk() #ウィンドウ作成
root.geometry("300x200") #ウィンドウのサイズ調整

# 作成
lbl = tk.Label(text="LABEL") #ラベル作成
btn = tk.Button(text="PUSH",command = displabel) #ボタン作成

# 配置
lbl.pack() #ラベル配置
btn.pack() #ボタン配置
tk.mainloop() #ウィンドウを表示