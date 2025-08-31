from time import time
from rich.console import Console
console = Console()
def send_Msg(msg):
    if isinstance(msg, BaseMsg):
        console.print(msg, style=msg.style)
    else:
        print(msg)


class BaseMsg:
    def __init__(self, data: str):
        self._data = data
    
    @property
    def style(self):
        return 'cyan'
        
    @property
    def data(self):
        return self._data
    
    def __str__(self):
        return self._data
    
    def __len__(self):
        return len(self._data)
    
    def __eq__(self, other):
        if isinstance(other, BaseMsg):
            return self._data == other._data
        else:
            return False
    
    def __add__(self, other):
        if isinstance(other, BaseMsg):
            return BaseMsg(self._data + other._data)
        elif isinstance(other, str):
            return BaseMsg(self._data + other)
        else:
            return NotImplemented


class LogMsg(BaseMsg):
    def __init__(self, data):
        super().__init__(data)
        self._timestamp: int = int(time())

    def __str__(self):
        return f"[{self._timestamp}] {self._data}"
    
    @property
    def style(self):
        return "black on yellow"


class WarnMsg(LogMsg):
    def __str__(self):
        return f"[WARNING][{self._timestamp}] {self._data}"
    
    @property
    def style(self):
        return "white on red"


if __name__ == '__main__':
    m1 = BaseMsg('Normal message')
    m2 = LogMsg('Log')
    m3 = WarnMsg('Warning')
    send_Msg(m1)
    send_Msg(m2)
    send_Msg(m3)