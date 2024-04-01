#開啟檔案
import tkinter as tk
from tkinter import filedialog
#讀取/編輯excel
import pandas as pd
#計算
import numpy as np
#作圖
import matplotlib as mpl
#from matplotlib.pyplot import*
import matplotlib.pyplot as plt

root = tk.Tk()
root.title('開啟檔案')
root.geometry('150x60')

def show():
    file_path = filedialog.askopenfilename()   # 選擇檔案後回傳檔案路徑與名稱
    print(file_path)                           # 印出路徑
    #讀取表格
    '''
    RawData0 = pd.read_excel(file_path, usecols=["儲位編號", "模治具編號", "模治具英文名稱", "進貨單價"], nrows=1)
    RawData1 = pd.read_excel(file_path, usecols=["報廢日期"])
    RawData2 = pd.read_excel(file_path, usecols=["備註"])
    '''
    #RawData0 = pd.DataFrame(file_path, usecols=["儲位編號", "模治具編號", "模治具英文名稱", "進貨單價"], nrows=1)
    RawData1 = pd.DataFrame(file_path, usecols=["報廢日期"])
    #RawData2 = pd.DataFrame(file_path, usecols=["備註"])
    RawData1 = RawData1.values
    RawData2 = RawData2.values
    print(RawData0)
    print(RawData1)
    print(RawData2)
    
    


# Button 設定 command 參數，點擊按鈕時執行 show 函式
btn = tk.Button(root,
                text='Open file',
                font=('Microsoft JhengHei UI Light',15,'bold'),
                command=show
              )





btn.pack()
root.mainloop()

#df = pd.read_excel(file_path)


