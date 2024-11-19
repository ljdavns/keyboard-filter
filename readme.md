# 键盘防连发工具 / Keyboard Anti-Repeat Tool

一个解决键盘连发问题的实用小工具，特别适用于KVM等设备导致的连发按键问题。  
A practical tool to prevent keyboard key repetition issues, especially useful for KVM-related key repeat problems.

## 使用说明 / Usage Instructions

```bash
# 源码运行 / Run from source
pip install keyboard
python keyboard_filter.py --t1 0.1 --t2 0.15
```

## 构建方法 / Build Instructions

```bash
pip install pyinstaller
python build.py

# 运行可执行文件 / Run executable
cd dist
KeyFilter.exe --t1 0.1 --t2 0.15
```

### 参数说明 / Parameters

- `--t1`: 最小允许间隔（秒），小于此间隔的按键将被屏蔽  
  Minimum allowed interval (seconds), keys pressed within this interval will be blocked
- `--t2`: 输出间隔（秒），满足最小间隔的按键将按此间隔输出  
  Output interval (seconds), keys that meet the minimum interval will be output at this interval

## 应用场景 / Use Cases

- KVM切换器等设备引起的连发问题 / Key repetition issues caused by KVM switches or similar devices
- 键盘本身的重复触发 / Keyboard's own repeat triggering issues
- 快速输入造成的意外重复 / Accidental repetition from fast typing

## 注意事项 / Notes

- 需要管理员权限运行 / Requires administrator privileges to run
- 支持Windows系统 / Supports Windows systems
- 按ESC或Ctrl+C退出程序 / Press ESC or Ctrl+C to exit the program
