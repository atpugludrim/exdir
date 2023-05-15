r"""Trains a simple tree generative model for molbace using GRU as a
generator. The code is distributed in trainer.py, model.py, and util.py.
This script takes a CLI argument that specifies the number of epochs.
The default value is 10.
"""
import argparse
from util import get_data
from trainer import train


def main():
    # -------------------------------------------------------------
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_epochs", "-ne", default=10, type=int,
                        help="number of epochs")
    args = parser.parse_args()
    # -------------------------------------------------------------
    dataset_name = "ogbg-molbace"
    freq_thresholds = {0: 5, 1: 10}
    dataloader0, dataloader1, vdataloader0, vdataloader1 = get_data(
        dataset_name, freq_thresholds
    )
    n_epochs = 10
    train(
        {
            "0": dataloader0,
            "1": dataloader1,
            "0_val": vdataloader0,
            "1_val": vdataloader1,
        },
        args.n_epochs,
    )


if __name__ == "__main__":
    main()
