#!/usr/bin/env python3
""" Read a bunch of data from all the HDF5 files in the current folder, and plot aggregated view of the simulation data."""

import glob
import numpy as np
import matplotlib.pyplot as plt
import h5py


def main():
    list_of_files = glob.glob("*.hdf5")
    dict_of_envs = {
        itspath: hdf5.File(itspath)['env_0']
        for itspath in list_of_files
    }
    

if __name__ == "__main__":
    main()