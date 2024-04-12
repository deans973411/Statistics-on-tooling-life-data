import tkinter as tk             #開啟檔案
from tkinter import filedialog
import pandas as pd              #讀取/編輯excel
import numpy as np               #計算
import matplotlib as mpl         #作圖
#from matplotlib.pyplot import*
import matplotlib.pyplot as plt
import warnings

#warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
root = tk.Tk()
root.title('開啟檔案')
root.geometry('150x60')

def show():
    file_path = filedialog.askopenfilename()   # 選擇檔案後回傳檔案路徑與名稱
    print(file_path)                           # 印出路徑
    #data = pd.read_csv(file_path)
    #讀取表格
    RawData0 = pd.read_excel(file_path, usecols=["儲位編號", "模治具編號", "模治具英文名稱", "進貨單價"], nrows=1)
    RawData1 = pd.read_excel(file_path, usecols=["報廢日期"])
    RawData2 = pd.read_excel(file_path, usecols=["備註"])


    RawData1 = RawData1["報廢日期"].str.split(' 上午',expand = True)
    RawData2 = RawData2["備註"].str.split(':',expand = True)
    RawData2 = RawData2[1].str.split('/',expand = True)


    RawData0 = np.array(RawData0).T
    RawData1 = np.array(RawData1).T #轉置數據
    RawData2 = np.array(RawData2).T #轉置數據
    RawData1 = np.delete(RawData1, 1, axis = 0)
    RawData2 = np.delete(RawData2, 1, axis = 0)
    RawData1 = RawData1[0]  #指定為可被轉換的整數
    RawData2 = RawData2[0]  #指定為可被轉換的整數
    print(RawData0)
    print(RawData1)
    print(RawData2)
    '''
    |參數|	    |預設|	        |說明|
    num	        None	        畫布的唯一標記，如果不指定 num，每次執行 figure() 方法時會自動增加 1，表示會產生新的畫布。
    figsize	    (6,4)	        畫布長寬尺寸，單位為「英吋」。
    dpi	        100	            畫布分辨率，表示一英吋裡有幾個像素。
    facecolor	white	        背景色。
    edgecolor	white	        外框顏色。
    linewidth	0	            外框粗細。
    frameon	    True	        是否顯示外框和背景色，設定 False 表示不顯示。
    '''
    x = [1,2,3,4,5]
    fig = plt.figure(edgecolor='#E6D7D4', facecolor='#D1EBED', linewidth=5, figsize=(12,6)) #edge: outside, face = tital color, color code= Hex
    plt.subplot()
    plt.xticks(ticks=RawData1,  rotation=30)
    plt.plot(RawData2)
    plt.show()
    
    


# Button 設定 command 參數，點擊按鈕時執行 show 函式
btn = tk.Button(root,
                text='Open file',
                font=('Microsoft JhengHei UI Light',15,'bold'),
                command=show
              )





btn.pack()
root.mainloop()

#f = pd.read_excel(file_path)


