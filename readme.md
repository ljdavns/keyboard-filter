# 键盘防连发工具 / Keyboard Anti-Repeat Tool

一个解决键盘连发问题的实用小工具，特别适用于KVM等设备导致的连发按键问题。  
A practical tool to prevent keyboard key repetition issues, especially useful for KVM-related key repeat problems.

*gpt4o+o1改了两个小时没改对，claude 3.5 sonnet几分钟就做好了。*  
*Spent two hours with GPT4 without success, Claude 3.5 Sonnet solved it in minutes.*

## 使用说明 / Usage

```bash
# 运行可执行文件 / Run executable
KeyFilter.exe 5.0  # 设置5秒防连发间隔 / Set 5-second anti-repeat interval

# 源码运行 / Run from source
pip install keyboard
python keyboard_filter.py 5.0
```

## 构建方法 / Build

```bash
pip install pyinstaller
python build.py
```

## 应用场景 / Use Cases

- KVM切换器引起的连发问题 / Key repetition issues caused by KVM switches
- 键盘本身的重复触发 / Keyboard's own repeat triggering issues
- 快速输入造成的意外重复 / Accidental repetition from fast typing

## 注意事项 / Notes
- 需要管理员权限运行 / Requires administrator privileges to run
- 支持Windows系统 / Supports Windows systems
