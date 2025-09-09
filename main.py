from machine import Pin
import time
import neopixel

# ========== HX711 CLASS ==========
class HX711:
    def __init__(self, dt, sck):
        self.dt = Pin(dt, Pin.IN, pull=Pin.PULL_UP)
        self.sck = Pin(sck, Pin.OUT)

    def is_ready(self):
        return self.dt.value() == 0

    def read(self):
        while not self.is_ready():
            pass
        val = 0
        for _ in range(24):
            self.sck.value(1)
            val = (val << 1) | self.dt.value()
            self.sck.value(0)
        self.sck.value(1)
        self.sck.value(0)
        if val & 0x800000:
            val |= ~0xffffff
        return val

    def read_average(self, times=10):
        total = 0
        for _ in range(times):
            total += self.read()
        return total // times

# ========== LED SETUP ==========
np = neopixel.NeoPixel(Pin(16), 1)

def set_led(r, g, b):
    np[0] = (r, g, b)
    np.write()

# ========== PIN SETUP ==========
hx = HX711(dt=10, sck=11)
trigger_pin = Pin(7, Pin.IN, Pin.PULL_DOWN)
output_pin = Pin(6, Pin.OUT)
mode_select_pin = Pin(1, Pin.IN, Pin.PULL_DOWN)  # NEW: Mode selection pin
output_pin.value(0)

# ========== CONFIG PROFILES ==========
threshold_a = 1000
offset_a = 1100

threshold_b = 2000
offset_b = 10000

# Initialize active config
threshold = threshold_a
offset = offset_a

required_trigger_count = 2
pulse_duration_ms = 50
debounce_time_ms = 50

# ========== STATE VARIABLES ==========
baseline = 0
armed = False
triggered = False
trigger_count = 0
last_trigger_time = 0
last_pulse_time = 0
last_disarm_time = 0

# ========== TRIGGER CALLBACK ==========
def trigger_callback(pin):
    global armed, baseline, last_trigger_time, last_disarm_time
    global threshold, offset

    now = time.ticks_ms()
    if time.ticks_diff(now, last_trigger_time) < 100:
        return
    last_trigger_time = now

    if pin.value() == 1:
        if time.ticks_diff(now, last_disarm_time) < debounce_time_ms:
            return

        # Select config profile based on mode pin
        if mode_select_pin.value() == 1:
            threshold = threshold_b
            offset = offset_b
            
            print("Mode B selected.")
        else:
            threshold = threshold_a
            offset = offset_a
            print("Mode A selected.")

        baseline = hx.read_average(10) + offset
        armed = True
        set_led(0, 0, 50)  # Blue = Armed
        print("Trigger HIGH: armed. Baseline =", baseline)
    else:
        armed = False
        output_pin.value(0)
        last_disarm_time = now
        set_led(0, 50, 0)  # Green = Disarmed
        print("Trigger LOW: disarmed.")

trigger_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=trigger_callback)

# ========== BOOT LOGIC ==========
print("Booting...")

if trigger_pin.value() == 1:
    if mode_select_pin.value() == 1:
        threshold = threshold_b
        offset = offset_b
        
        print("Mode B selected at boot.")
    else:
        threshold = threshold_a
        offset = offset_a
        print("Mode A selected at boot.")

    armed = True
    baseline = hx.read_average(10) + offset
    set_led(0, 0, 50)  # Blue = Armed
    print("Trigger already HIGH at boot. Armed. Baseline =", baseline)
else:
    set_led(0, 50, 0)  # Green = Disarmed
    print("System disarmed. Waiting for trigger HIGH...")

# ========== MAIN LOOP ==========
while True:
    if armed:
        current = hx.read()
        print("Raw reading:", current)

        if not triggered and current > (baseline + threshold):
            trigger_count += 1
            print(f"Over threshold: {trigger_count}/{required_trigger_count}")
            set_led(50, 50, 0)  # Yellow = approaching trigger
            if trigger_count >= required_trigger_count:
                output_pin.value(1)
                triggered = True
                last_pulse_time = time.ticks_ms()
                print("Output pin HIGH")
                set_led(50, 0, 0)  # Red = triggered
        elif current <= (baseline + threshold):
            trigger_count = 0
            if not triggered:
                set_led(0, 0, 50)  # Blue = armed and under threshold

        if triggered and time.ticks_diff(time.ticks_ms(), last_pulse_time) >= pulse_duration_ms:
            output_pin.value(0)
            triggered = False
            print("Output pin LOW")
            baseline = hx.read_average(10) + offset
            set_led(0, 0, 50)  # Return to armed (blue)
    else:
        time.sleep(0.1)
