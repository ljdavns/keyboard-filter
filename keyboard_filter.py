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
    def __init__(self, min_interval=0.3, output_interval=1.0):
        self.min_interval = min_interval        # 最小允许间隔(t1)
        self.output_interval = output_interval  # 输出间隔(t2)
        self.last_key_time = {}                # 记录每个按键的最后触发时间
        self.last_output_time = {}             # 记录每个按键的最后输出时间
        self.previous_key = None
        
    def on_key_event(self, event):
        current_time = time.time()
        key = event.name
        
        # 处理按键按下事件
        if event.event_type == 'down':
            # 如果是不同的键，直接允许通过
            if key != self.previous_key:
                logger.info(f"允许按键 {key} 通过 - 新按键")
                self.last_key_time[key] = current_time
                self.last_output_time[key] = current_time
                self.previous_key = key
                return True
                
            # 获取上次按键和上次输出的时间
            last_key_time = self.last_key_time.get(key, 0)
            last_output_time = self.last_output_time.get(key, 0)
            
            # 计算时间间隔
            time_since_last_key = current_time - last_key_time
            time_since_last_output = current_time - last_output_time
            
            # 更新最后按键时间
            self.last_key_time[key] = current_time
            
            # 第一层检查：如果按键间隔小于最小间隔，直接屏蔽
            if time_since_last_key < self.min_interval:
                logger.warning(f"屏蔽按键 {key} - 间隔太短 ({time_since_last_key:.3f}s < {self.min_interval}s)")
                return False
                
            # 第二层检查：如果距离上次输出超过输出间隔，允许通过
            if time_since_last_output >= self.output_interval:
                logger.info(f"允许按键 {key} 通过 - 达到输出间隔 ({time_since_last_output:.3f}s >= {self.output_interval}s)")
                self.last_output_time[key] = current_time
                return True
            else:
                logger.warning(f"屏蔽按键 {key} - 输出间隔未到 ({time_since_last_output:.3f}s < {self.output_interval}s)")
                return False
                
        # 处理按键释放事件
        elif event.event_type == 'up':
            logger.debug(f"检测到按键释放 - 键名: {key}")
            return True

    def start(self):
        logger.info(f"启动键盘监听程序...")
        logger.info(f"最小允许间隔(t1)：{self.min_interval}秒")
        logger.info(f"输出间隔(t2)：{self.output_interval}秒")
        keyboard.hook(self.on_key_event, suppress=True)
        keyboard.wait('esc')  # 按ESC键退出程序

def parse_arguments():
    parser = argparse.ArgumentParser(description='键盘防抖程序')
    parser.add_argument('--t1', type=float, default=0.1,
                      help='最小允许间隔，小于此间隔的按键将被屏蔽 (秒)')
    parser.add_argument('--t2', type=float, default=0.15,
                      help='输出间隔，满足最小间隔的按键将按此间隔输出 (秒)')
    return parser.parse_args()

def main():
    try:
        args = parse_arguments()
        handler = KeyboardHandler(
            min_interval=args.t1,
            output_interval=args.t2
        )
        logger.info("程序已启动，按 ESC 键退出")
        handler.start()
    except KeyboardInterrupt:
        logger.info("程序已停止")
    except Exception as e:
        logger.error(f"发生错误: {e}")

if __name__ == "__main__":
    main()