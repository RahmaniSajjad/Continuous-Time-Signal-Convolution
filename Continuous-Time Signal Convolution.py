import matplotlib.pyplot as plt
import numpy as np


# continuous time signal convolution
# Sajjad Rahmani

def conv(x_value, x_start, h_value, h_start, accuracy):
    x_start *= accuracy
    h_start *= accuracy

    # calculate multiplication two signal (result in keeper)
    keeper = []
    for num in h_value:
        keeper.append([num * i for i in x_value])

    # insert zero in empty place
    for i in range(len(h_value)):
        keeper[i] = [0] * i + keeper[i] + [0] * (len(h_value) - 1 - i)

    # calculate sum of each columns (result in conv_res)
    keeper = list(zip(*keeper))
    conv_res = []
    for i in keeper:
        conv_res.append(sum(i))

    # calculate t for first conv_res value
    conv_start = x_start + h_start

    # add some zeros to start and end of each signals
    x_value = [0.0] * accuracy + x_value + [0.0] * accuracy
    h_value = [0.0] * accuracy + h_value + [0.0] * accuracy
    conv_res = [0.0] * accuracy + conv_res + [0.0] * accuracy

    plt.style.use('seaborn')
    fig, ax = plt.subplots(3, 1, sharex=True)

    ax[0].plot([i / accuracy for i in range(x_start - accuracy, x_start + len(x_value) - accuracy)], x_value,
               label='x(t)')
    ax[1].plot([i / accuracy for i in range(h_start - accuracy, h_start + len(h_value) - accuracy)], h_value,
               label='h(t)')
    ax[2].plot([i / accuracy for i in range(conv_start - accuracy, conv_start + len(conv_res) - accuracy)],
               [i / accuracy for i in conv_res], label='x(t) * h(t)')

    for axx in ax:
        axx.legend()
    plt.show()


accuracy = 100  # number of dt-signal per ct-signal's second

# for example if "accuracy = 100" it means :
# signal must have 100 value in per second


# example 1 :
# sig1_start = 0
# sig1_end = 2
# sig1 = []
# for t in np.arange(sig1_start, sig1_end, 1 / accuracy):
#     sig1_value = 2.0
#     sig1.append(sig1_value)
#
# sig2_start = 0
# sig2_end = 1
# sig2 = []
# for t in np.arange(sig2_start, sig2_end, 1 / accuracy):
#     sig2_value = 3.0
#     sig2.append(sig2_value)
#
# conv(sig1, sig1_start, sig2, sig2_start, accuracy)


# example 2 :
# sig1_start = 1
# sig1_end = 10
# sig1 = []
# for t in np.arange(sig1_start, sig1_end, 1 / accuracy):
#     sig1_value = 1.0
#     sig1.append(sig1_value)
#
# sig2_start = 0
# sig2_end = 10
# sig2 = []
# for t in np.arange(sig2_start, sig2_end, 1 / accuracy):
#     sig2_value = pow(np.e, -t)
#     sig2.append(sig2_value)
#
# conv(sig1, sig1_start, sig2, sig2_start, accuracy)


# example 3
sig1_start = -2
sig1_end = 3
sig1 = []
for t in np.arange(sig1_start, sig1_end, 1 / accuracy):
    sig1_value = 1.0
    sig1.append(sig1_value)

sig2_start = -1
sig2_end = 2
sig2 = []
for t in np.arange(sig2_start, sig2_end, 1 / accuracy):
    sig2_value = 3 * t + 5
    sig2.append(sig2_value)

conv(sig1, sig1_start, sig2, sig2_start, accuracy)
