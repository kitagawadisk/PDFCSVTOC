import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

"""
01.PDFから栞のリストを取出す
02.取出したリスト通りに栞を挿入しなおす。
"""

import fitz
import csv
from PyPDF2 import PdfFileWriter, PdfFileReader

def pdf_to_csv(pdf_in,csv_out):
    """
    以下PDFの栞の読み込み
    とcsvへの書き出し
    NOTE t.koba(2021.3.9)
    https://note.com/uranus_xii_jp/n/nbf8c42c0625b
    """
    doc = fitz.open(pdf_in)
    # 総ページ数
    page_count = doc.page_count
    print('Page count: ', page_count)
    toc_list = doc.get_toc()

    #空白行をなくすためnewline追加(220329)
    with open(csv_out, 'w',newline="") as f: 
        writer = csv.writer(f)
        writer.writerows(toc_list) #org
    f.close()
    return()

def csv_to_pdf(pdf_in, csv_out):
    """
    以下PDFの栞の書き込み
    参考 https://jablogs.com/detail/49869

    pdfcsv_toc.py
    """
    with open(csv_out) as f: #csvの読込み
        reader = csv.reader(f, delimiter=',')
        l = [row for row in reader]
    
    l2 = [] #csvの空データ行削除
    for i in range(len(l)):
        if l[i] == []:
            pass
        else:
            #print(l[i])
            l2.append(l[i])

    output = PdfFileWriter() # open output
    input1 = PdfFileReader(open(pdf_in, 'rb')) # open input
    
    n = input1.getNumPages()
    for i in range(n):
        output.addPage(input1.getPage(i)) # insert page

    par_list = [] #階層のある場合のための階層親リスト
    kaiso_list = [] #階層番号のリスト

    for i in l2:
        kaiso = int(i[0])
        kaiso_list.append(kaiso)
        name = i[1]
        page = int(i[2])
        #print(kaiso,name,page)
        #page は -1 しないとずれる(2022.03.28)
        if kaiso == 1:
            par_list.append(output.addBookmark(name, page-1, parent=None))
        else:
            ln = len(kaiso_list)
            par_kaiso = kaiso-1 #親の階層
            r_kaiso = kaiso_list[::-1] #階層リストの逆順
            ind = r_kaiso.index(par_kaiso) #逆から親の階層検索
            p_ind = ln - ind - 1 #par_listの親階層インデクス
            par = par_list[p_ind]
            par_list.append(output.addBookmark(name, page-1, parent=par))

    outputStream = open('result.pdf','wb') #creating result pdf JCT
    output.write(outputStream) #writing to result pdf JCT
    outputStream.close() #closing result JCT

def pdfFiles():
    '''
     Return a list of files ending with .pdf
    '''
    pdfs = []
    for i in os.listdir():
        if i[-4:] == ".pdf":
            pdfs.append(i)
    return pdfs

def multisearch():
    '''
                    Search in all selected pdf's
    '''
    docs = [lb.get(i) for i in lb.curselection()]
    term = e.get()
    console.delete('1.0', END)
    for d in docs:
        search(term, d)


def filedialog_clicked(): #INPUT FILE
    fTyp = [("", "*")]
    iFile = os.path.abspath(os.path.dirname(__file__))
    iFilePath = filedialog.askopenfilename(filetype = fTyp, initialdir = iFile)
    entry1.set(iFilePath)

def filedialog_clicked2(): #POST FILE
    fTyp = [("", "*")]
    iFile = os.path.abspath(os.path.dirname(__file__))
    iFilePath = filedialog.askopenfilename(filetype = fTyp, initialdir = iFile)
    entry3.set(iFilePath)

def conductMain(): # 実行ボタン押下時の実行関数
    filePath1 = entry1.get() #INPUT FILE
    filePath2 = entry3.get() #POST FILE
    method = combobox.get() #補間方法

    print(filePath1)
    print(filePath2)
    GUI_main(filePath1,filePath2,method)

def select_combo(event):
    print(combobox.get())

def getTextInput():
    result=textExample.get(1.0, tk.END+"-1c")
    print(result)

def quit(): #ウィンドウの完全な削除
    root.quit()

def GUI_main(file_pdf,file_csv,method):
    """
    入力
    """
    #書き込み先はresult.pdfとしている。
    if method == "pdf->csv":
        pdf_to_csv(file_pdf,file_csv) #01. PDFから付箋データをcsvに変換する場合に使用
    elif method == "csv->pdf":
        csv_to_pdf(file_pdf,file_csv) #02. csv付箋データをPDFに書き込む時使用。書き込んだファイルはrsult.pdfで保存とした。
    else:
        print("なにもしない")
    print("実行完了",method)

# ここの1行を変更　fTyp = [("","*")] →　fTyp = [("","*.csv")]
iDir = os.path.abspath(os.path.dirname(__file__))
fTyp = [("","*.pdf")]

# rootの作成
root = Tk()
root.title("PDF栞csv変換プログラム_ver1.0 by_kitagawa")

# Frame1の作成
frame1 = ttk.Frame(root, padding=10)
frame1.grid(row=1, column=1, sticky=E)
# 「ファイル参照」ラベルの作成
IFileLabel = ttk.Label(frame1, text="ファイル参照(pdf)＞＞", padding=(5, 2))
IFileLabel.pack(side=LEFT)
# 「ファイル参照」エントリーの作成
entry1 = StringVar()
IFileEntry = ttk.Entry(frame1, textvariable=entry1, width=30)
IFileEntry.pack(side=LEFT)
# 「ファイル参照」ボタンの作成
IFileButton = ttk.Button(frame1, text="参照pdf", command=filedialog_clicked)
IFileButton.pack(side=LEFT)

# Frame2の作成
frame2 = ttk.Frame(root, padding=10)
frame2.grid(row=2, column=1, sticky=E)
IFileLabel = ttk.Label(frame2, text="変換＞＞", padding=(5, 2))
IFileLabel.pack(side=LEFT)
style = ttk.Style()
style.theme_use("winnative")
style.configure("office.TCombobox", selectbackground="blue", padding=5)
module = ("pdf->csv", "csv->pdf")
v = StringVar()
combobox = ttk.Combobox(frame2,textvariable= v, values=module, style="office.TCombobox")
combobox.bind('<<ComboboxSelected>>', select_combo)
combobox.pack()
combobox.set("pdf->csv")

# Frame6の作成
frame6 = ttk.Frame(root, padding=10)
frame6.grid(row=7, column=1, sticky=E)
# 「ファイル参照」ラベルの作成
IFileLabel = ttk.Label(frame6, text="ファイル参照(csv)＞＞", padding=(5, 2))
IFileLabel.pack(side=LEFT)
# 「ファイル参照」エントリーの作成
entry3 = StringVar()
IFileEntry = ttk.Entry(frame6, textvariable=entry3, width=30)
IFileEntry.pack(side=LEFT)
# 「ファイル参照」ボタンの作成
IFileButton = ttk.Button(frame6, text="参照csv", command=filedialog_clicked2)
IFileButton.pack(side=LEFT)

# Frame7の作成
frame7 = ttk.Frame(root, padding=10)
frame7.grid(row=9,column=1,sticky=W)
# 実行ボタンの設置
button1 = ttk.Button(frame7, text="実行", command=conductMain)
button1.pack(fill = "x", padx=30, side = "left")
# キャンセルボタンの設置
button2 = ttk.Button(frame7, text=("閉じる"), command=quit)
button2.pack(fill = "x", padx=30, side = "left")
root.mainloop()
    
#if __name__ == "__main__":
#    main()