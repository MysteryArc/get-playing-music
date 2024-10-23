'''
@File       :  getMusicInfo.py
@Time       :  2024/10/22 17:50:51
@Author     :  Wang Hengyu (wanghyuuuuu@163.com)
@Description:  
'''

# here put the import lib
import win32process
import win32gui
import psutil

def getProcessIDByName(pname):
    pid_list = []
    for penum in psutil.process_iter(['pid', 'name']):
        if penum.info['name'] == pname:
            pid_list.append(penum.info['pid'])
    return pid_list

# 获取指定进程 PID 的窗口标题
def getTitleByPid(pid):
    def enum_windows_callback(hwnd, pid_list):
        tid, current_pid = win32process.GetWindowThreadProcessId(hwnd)
        if current_pid == pid:
            title = win32gui.GetWindowText(hwnd)
            if title:  # 窗口标题不为空
                pid_list.append(title)
        return True

    titles = []
    win32gui.EnumWindows(enum_windows_callback, titles)
    return titles

if __name__ == "__main__":
    processName = 'QQMusic.exe'
    processId = getProcessIDByName(processName)
    print(getTitleByPid(processId[0])[1])