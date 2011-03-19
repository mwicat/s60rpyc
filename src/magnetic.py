from threading import Thread
import e32


def my_callback():
    azimuth = str(magnetic_north.azimuth)
    print azimuth

def start_magnetic():
    import sensor
    global magnetic_north
    magnetic_north = sensor.MagneticNorthData()
    magnetic_north.set_callback(data_callback=my_callback)
    magnetic_north.start_listening()
    print 'jedziemy'


sm = e32.ao_callgate(start_magnetic)

t = Thread(target=sm)
t.start()

e32.ao_sleep(8)