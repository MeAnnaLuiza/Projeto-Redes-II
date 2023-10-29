import time
import random
import argparse
import numpy as np
import rasterio
from rasterio.plot import show
from PIL import Image
from scipy.io import arff
import pandas as pd
from scipy.io import arff
from gng import GrowingNeuralGas
import plotly.offline as py
import plotly.graph_objs as go
from sklearn.preprocessing import StandardScaler

def get_parametro(seed):
    random.seed(seed)
    ortofoto = rasterio.open("imagem_recortada.tif")
    show(ortofoto)

    bandas = np.zeros((ortofoto.height, ortofoto.width, ortofoto.count), np.uint8)

    for b in range(ortofoto.count):
        bandas[:, :, b] = ortofoto.read(b+1)

    novo_shape = (bandas.shape[0] * bandas.shape[1], bandas.shape[2])
    X = bandas[:, :, :ortofoto.count].reshape(novo_shape)

    training(X, int(seed))

def training(data, seed):
    print('Generating data...')
    print('Done.\n')
    print('Fitting neural network...\n')
    inicio = time.time()
    gng = GrowingNeuralGas(data, seed)
    gng.fit_network(e_b=0.05, e_n=0.0036, a_max=10, l=200, a=0.9, d=0.995, passes=8, plot_evolution=False)
    print('Found %d clusters.' % gng.number_of_clusters())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Projeto Redes II")
    parser.add_argument("seed", type=int, help="Semente")

    args = parser.parse_args()
    get_parametro(args.seed)