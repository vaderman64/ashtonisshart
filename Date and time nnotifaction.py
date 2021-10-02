import datetime

x = datetime.datetime.now()

from win10toast import ToastNotifier

toaster = ToastNotifier()
toaster.show_toast(str(x), duration=10)
