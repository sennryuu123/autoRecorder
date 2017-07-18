import pickle
from server.config import CONF
from server.solenoide_out import solenoide_out


def run():
    """ Control RaspberryPi """
    with open(CONF['pickle_path'], mode='rb') as f:
        solenoide = [0 for i in range(10)]
        data = pickle.load(f)
        solenoide_out(data, solenoide)

    print(data)

if __name__ == '__main__':
    run()
