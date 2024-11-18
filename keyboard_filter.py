import keyboard
import time
import logging
import argparse
from datetime import datetime

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class KeyboardHandler:
    def __init__(self, debounce_time):
        self.last_key_time = {}
        self.debounce_time = debounce_time
        self.previous_key = None
        
    def on_key_event(self, event):
        current_time = time.time()
        key = event.name
        
        if event.event_type == 'down':
            last_time = self.last_key_time.get(key, 0)
            time_diff = current_time - last_time
            
            logger.debug(f"检测到按键按下 - 键名: {key}, 距离上次: {time_diff:.3f}秒")
            
            if (key != self.previous_key) or (time_diff >= self.debounce_time):
                self.last_key_time[key] = current_time
                self.previous_key = key
                logger.info(f"允许按键 {key} 通过 - {'新按键' if key != self.previous_key else f'间隔{time_diff:.3f}秒'}")
                return True
            else:
                logger.warning(f"屏蔽按键 {key} - 间隔仅 {time_diff:.3f}秒，需要等待 {self.debounce_time}秒")
                return False
                
        elif event.event_type == 'up':
            logger.debug(f"检测到按键释放 - 键名: {key}")
            return True

    def start(self):
        logger.info(f"启动键盘监听程序... （按键防抖时间：{self.debounce_time}秒）")
        keyboard.hook(self.on_key_event, suppress=True)
        keyboard.wait('esc')

def main():
    parser = argparse.ArgumentParser(description='键盘防连发程序')
    parser.add_argument('time', type=float, help='防连发时间(秒)')
    args = parser.parse_args()

    try:
        handler = KeyboardHandler(debounce_time=args.time)
        logger.info(f"程序已启动，防连发时间设为{args.time}秒。按ESC键退出。")
        handler.start()
    except KeyboardInterrupt:
        logger.info("程序已停止")
    except Exception as e:
        logger.error(f"发生错误: {e}")

if __name__ == "__main__":
    main()