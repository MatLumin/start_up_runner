import os;
from typing import *;
import pyautogui;
import time;

target_exe_path:Final[str] = r"C:\Program Files\Mozilla Firefox\firefox.exe";
const_arg:Final[str] = r"http://whocares.pythonanywhere.com/main";

def press_f11()->None:
	pyautogui.press("f11");

def run_target_exe_with_const_arg()->None:
	cmd:Final[str] = f"\"{target_exe_path}\" \"{const_arg}\"";
	print(cmd);
	os.popen(cmd);


if __name__ == "__main__":
	time.sleep(1);
	run_target_exe_with_const_arg();
	time.sleep(5);
	pyautogui.moveTo(500, 500);
	pyautogui.click();
	press_f11();


