import math
import sys
import psutil
import igpu
from PySide6 import QtCore, QtWidgets

from ui.compiled.main import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.frequency_update = 1000

        self.load_cpu_info_timer = QtCore.QTimer()
        self.load_cpu_info_timer.setInterval(self.frequency_update)
        self.load_cpu_info_timer.timeout.connect(self.load_cpu_info)
        self.load_cpu_info_timer.start()

        self.load_mem_info_timer = QtCore.QTimer()
        self.load_mem_info_timer.setInterval(self.frequency_update)
        self.load_mem_info_timer.timeout.connect(self.load_mem_info)
        self.load_mem_info_timer.start()

        self.load_gpu_info_timer = QtCore.QTimer()
        self.load_gpu_info_timer.setInterval(self.frequency_update)
        self.load_gpu_info_timer.timeout.connect(self.load_gpu_info)
        self.load_gpu_info_timer.start()
        
        self.load_cpu_info()
        self.load_gpu_info()
        self.load_mem_info()

    def load_cpu_info(self):
        cpu_temp = psutil.sensors_temperatures().get("coretemp")[0].current
        cpu_percent = psutil.cpu_percent()
        self.pb_cpu_freq.setValue(cpu_percent)
        self.lbl_cpu_temp.setText(f"{cpu_temp} °C")

    def load_mem_info(self):
        mem = psutil.virtual_memory()
        self.lbl_mem_total.setText(self.convert_size(mem.total))
        self.lbl_mem_used.setText(self.convert_size(mem.used))
        self.lbl_mem_free.setText(self.convert_size(mem.free))

    def load_gpu_info(self):
        if len(igpu.devices()) == 1:
            card = igpu.devices()[0]
            self.pb_gpu_freq.setValue(card.utilization.gpu)
            self.pb_gpu_mem_percent.setValue(card.utilization.memory)
            self.lbl_gpu_men_total.setText(f"{int(card.memory.total)} MiB")
            self.lbl_gpu_men_used.setText(f"{int(card.memory.used)} MiB")
            self.lbl_gpu_mem_free.setText(f"{int(card.memory.free)} MiB")
            self.lbl_gpu_temp.setText(f"{card.utilization.temperature}°C")
            self.lbl_gpu_fan_speed.setText(f"{card.utilization.fan}%")


    def convert_size(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
