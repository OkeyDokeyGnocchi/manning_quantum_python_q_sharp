from interface import QuantumDevice
from simulator import SingleQubitSimulator

def qrng(device: QuantumDevice) -> bool:
    with device.using_qubit() as q:
        q.h()
        return q.measure()


if __name__ == '__main__':
    qsim = SingleQubitSimulator()
    # Run a bunch of times to see percentages
    coin_tosses = 1000000
    heads_count = 0
    tails_count = 0
    for i in range(coin_tosses):
        random_sample = qrng(qsim)
        #print(f'QRNG returned {random_sample}')
        if random_sample == True:
            heads_count += 1
        else:
            tails_count += 1

    print(f'Heads: {(heads_count / coin_tosses) * 100 }% // Tails: {(tails_count / coin_tosses) * 100}%')
