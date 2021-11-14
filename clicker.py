# Once an hour click a specific location on the window "AFK Arena"
import time
import win32gui
import win32api
import win32con
import ctypes
import sys
def get_cursor_coordinates_in_window(window_handle):
    """
    Get the cursor coordinates in a window
    :param window_handle: The window handle
    :return: The cursor coordinates
    :rtype: tuple
    """
    cursor_pos = win32gui.GetCursorPos()
    cursor_pos = win32gui.ScreenToClient(window_handle, cursor_pos)
    
    return cursor_pos

def get_cursor_coordinates() -> tuple:
    """
    Get the cursor coordinates
    :return: The cursor coordinates
    :rtype: tuple
    """
    cursor_pos = win32gui.GetCursorPos()
    return cursor_pos

def do_click_on_window(window_name, x, y) -> bool:
    """
    Click on a window
    :param window_name: The name of the window
    :param x: The x coordinate
    :param y: The y coordinate
    :return: True if the click was successful, False otherwise
    :rtype: bool
    """
    hwnd = win32gui.FindWindow(None, window_name)
    current_hwnd = win32gui.GetForegroundWindow()
    print(win32gui.GetWindowText(current_hwnd))
    current_cursor_pos = win32gui.GetCursorPos()
    
    current_x, current_y = current_cursor_pos
    print(current_x, current_y)
    
    if hwnd == 0:
        print("Window not found")
        return
    win32gui.SetForegroundWindow(hwnd)
    win32api.SetCursorPos((x, y))
    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    win32gui.SetForegroundWindow(current_hwnd)    
    win32api.SetCursorPos((current_x, current_y))
    
hwnd = win32gui.FindWindow(None, "AFK Arena")

#while(True):
#    print(get_cursor_coordinates())

def is_admin():
    """
    Check if the current user is an admin
    :return: True if the current user is an admin, False otherwise
    :rtype: bool
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
run = True
if is_admin():
    while(run==True):
        do_click_on_window("AFK Arena", 3824, 1042)
        #sleep 30 minutes
        time.sleep(1800)
        
        #If space bar pressed run = False
        if(win32api.GetAsyncKeyState(0x20)):
            run = False
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

