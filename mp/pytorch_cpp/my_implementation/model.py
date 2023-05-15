import torch
import torch.nn as nn
import torch.nn.functional as F


class SimpleGRU(nn.Module):
    def __init__(this, vocab_size, emb_size, padding_idx, hidden_size):
        super().__init__()
        this.embedding_layer = nn.Embedding(
            vocab_size,
            emb_size,
            padding_idx=padding_idx,
        )
        this.gru = nn.GRU(
            input_size=emb_size,
            hidden_size=hidden_size,
            batch_first=True,
        )
        this.h0 = nn.Parameter(torch.zeros(1, hidden_size))
        this.classify = nn.Linear(hidden_size, vocab_size)

    def forward(this, xs, ls):
        hs = this.embedding_layer(xs)
        hs = nn.utils.rnn.pack_padded_sequence(
            hs,
            lengths=ls,
            batch_first=True,
            enforce_sorted=False,
        )
        bs = xs.shape[0]
        h0 = this.h0.repeat(bs, 1, 1)
        h0 = h0.permute(1, 0, 2)
        ys, _ = this.gru(hs, h0)
        ys, ls = nn.utils.rnn.pad_packed_sequence(ys, batch_first=True)
        ys = ys[torch.arange(ls.shape[0]), ls - 1]
        ys = this.classify(ys)
        return ys
