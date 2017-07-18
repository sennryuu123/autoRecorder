import pickle


from server.config import CONF
from server.solenoide_out import solenoide_out


def run(test):
    """ Control RaspberryPi """
    with open(CONF['pickle_path'], mode='rb') as f:
        solenoide = [0 for i in range(10)]
        data = pickle.load(f)
        solenoide_out(data, solenoide, test)

    print(test)

if __name__ == '__main__':
    pitch_data = [0 for i in range(6)]
    run(pitch_data)
