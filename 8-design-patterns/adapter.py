# like a screw that's too small to fit a hole, use an adapter to fit

# adapter pattern

# usbCables can plug directly into usb ports

class usbCable:
    def __init__(self) -> None:
        self.isPlugged = False
    
    def plugUsb(self):
        self.isPlugged = True

class usbPort:
    def __init__(self) -> None:
        self.portAvailable = True

    def plug(self, usb):
        if self.portAvailable:
            usb.plugUsb()
            self.portAvailable = False

usbcable = usbCable()
usbPort1 = usbPort()
usbPort1.plug(usbcable)

# micro usb cable is not compatible 
class MicroUsbCable:
    def __init__(self) -> None:
        self.isPlugged = False

    def plugMicroUsb(self):
        self.isPlugged = True


# microusb needs an adapter

class MicroToUsbAdapter(usbCable):
    def __init__(self, microUsbCable) -> None:
        self.microUsbCable = microUsbCable
        self.microUsbCable.plugMicroUsb()
    
    # can override UsbCable.plugUsb() if needed

# MircoUsbCables can plug into usb ports via an adapter

microToUsbAdapter = MicroToUsbAdapter(MicroUsbCable())
usbPort2 = usbPort()
usbPort2.plug(microToUsbAdapter)