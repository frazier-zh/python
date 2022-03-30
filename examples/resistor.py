import memboard as mb
from memboard import board
import memboard.unit as unit

top_pin = [1,2,3]
bottom_pin = [84,83,82]
voltage = 1 *unit.V
pulse_width = 1 *unit.ms
repeat = 1 *unit.s # Repeat interval, unit.ms, unit.s, unit.us, unit.min
end = 10 *unit.s # Repeat for 10 seconds

def main(output):
    output['time'] = mb.time()
    for i in range(len(top_pin)):
        output[str(top_pin[i])+'to'+str(bottom_pin[i])] = mb.measure(pin=top_pin[i], drive_pin=bottom_pin[i], v=voltage, width=pulse_width)

board.open()
mb.execute(main, every=repeat, total=end, out='../PCB measurements/test')
board.close()