# Import RPi.gpio as GPIO
# Import time


def solenoide_out(expect, sout, test):
    BPM = 80
    bars = 0
    note = 0
    notemax = 0
    barsmax = 0
    count = 0
    barsmax = len(expect)
    for bars in range(barsmax):
        notemax = len(expect[bars])
        for note in range(notemax):
            temp = expect[bars][note]["pitch"]
            octave = temp["octave"]
            step = temp["step"]
            duration = expect[bars][note]["duration"]
            table = pitch(octave, step, test, count)
            count = count + 1
            output(table, sout)
            if sout[0] == 2:
                print("PitchError")
            print(sout)
            time = duration*60/BPM
            print(time)
            # Print("solenoid=", end = "")
            # For i in range(10):
            # Print(sout[i], end = "")
            # Print()
            # Ras_out(sout,time)
            sout = [0 for i in range(10)]

"""
def ras_out (X,dtime):
    pin_list = [1,2,3,4,5,6,7,8,9,10]
    GPIO.setmode(GPIO.BCM)
    for i in range(10):
        GPIO.setup(pin_list[i],GPIO.OUT)

    for i in range(10):
        GPIO.output(pin_list[i],X[i])
    time.sleep(dtime)

"""


def pitch(octave, step, test1, count1):
    list_step = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    list_octave = [4, 5]
    for i in range(2):
        for j in range(7):
            if octave == list_octave[i]:
                if step == list_step[j]:
                    test1[count1] = step
                    return i*7+j+1
                else:
                    return_num = 0
            else:
                return_num = 0
    return return_num


def output(num1, out):
    i = 0
    if num1 == 1:
        for i in range(10):
            out[i] = 1
    elif num1 == 2:
        for i in range(8):
            out[i] = 1
    elif num1 == 3:
        for i in range(6):
            out[i] = 1
    elif num1 == 4:
        for i in range(5):
            out[i] = 1
    elif num1 == 5:
        for i in range(4):
            out[i] = 1
    elif num1 == 6:
        for i in range(3):
            out[i] = 1
    elif num1 == 7:
        for i in range(2):
            out[i] = 1
    elif num1 == 8:
        out[0] = 1
        out[2] = 1
    elif num1 == 9:
        out[2] = 1
    else:
        out[0] = 2
