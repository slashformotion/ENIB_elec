##
# This file is subject to the terms and conditions defined in file 'LICENSE', which is part of this source code package.
#
# @authors: vincentchoqueuse, slashformotion
##
import numpy as np


def export_csv(data_list, filename="data.csv", header=""):
    data_2D = np.vstack(data_list)
    data_2D = np.transpose(data_2D)
    np.savetxt(filename, data_2D, delimiter=",", header=header)


def test():
    pass