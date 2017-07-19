import pickle
from server.config import CONF
from server.solenoide_out import solenoide_out
from server.counter import counter


def run():
    """ Control RaspberryPi """
    with open(CONF['pickle_path'], mode='rb') as f:
        data = pickle.load(f)
        num = counter(data)
        solenoide = [0 for i in range(10)]
        pitch = [0 for i in range(num)]
        solenoide_out(data, solenoide, pitch)

    print(pitch)
    return pitch
if __name__ == '__main__':
    run()
