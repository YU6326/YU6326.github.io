frfrom pyautocad import Autocad,APoint
import tkinter.filedialog as tkFileDialog

def wtPoint(start):
    """
    将文件中的点写入autocad，start表示起始行数
    """
    acad=Autocad()
    # f=open(r'D:\学习\摄影测量\摄影测量实验数据-后方交会、前方交会\point.txt')
    fname = tkFileDialog.askopenfilename(title=u"选择文件",filetypes=[("text file", "*.txt"), ("all", "*.*")],initialdir=r"D:\学习\摄影测量\摄影测量实验数据-后方交会、前方交会")
    f=open(fname)
    lines=f.readlines()
    for i in range(1,len(lines)):
        t=lines[i].split(',')
        ap=APoint(float(t[0]),float(t[1]))
        acad.model.AddPoint(ap)

if __name__=="__main__":
    wtPoint(0)
