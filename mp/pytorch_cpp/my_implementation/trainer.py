import torch
import torch.nn as nn
import torch.optim as opt
from model import SimpleGRU


def train(dataloaders, n_epochs):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    criterion = nn.CrossEntropyLoss()
    i2w0 = dataloaders["0"].dataset.i2w
    i2w1 = dataloaders["1"].dataset.i2w
    vocab_size0 = len(i2w0) + 1
    vocab_size1 = len(i2w1) + 1
    model0 = SimpleGRU(vocab_size0, 16, 0, 16).to(device)
    model1 = SimpleGRU(vocab_size1, 16, 0, 16).to(device)
    optim0 = opt.Adam(model0.parameters())
    optim1 = opt.Adam(model1.parameters())
    best_val_loss0 = float('inf')
    best_val_loss1 = float('inf')
    # -------------------------------------------------------------
    for epoch in range(1, n_epochs + 1):
        print(f"[{epoch:2d}/{n_epochs}]    ", end="")
        loss0 = train_step(model0, dataloaders["0"], criterion, optim0, device)
        loss1 = train_step(model1, dataloaders["1"], criterion, optim1, device)
        val_loss0, acc0 = eval_step(model0, dataloaders["0_val"], criterion, device)
        val_loss1, acc1 = eval_step(model1, dataloaders["1_val"], criterion, device)
        if val_loss0 < best_val_loss0:
            best_val_loss0 = val_loss0
            torch.save(model0.state_dict(), f'models/model0_epo{epoch}.pt')
        if val_loss1 < best_val_loss1:
            best_val_loss1 = val_loss1
            torch.save(model1.state_dict(), f'models/model1_epo{epoch}.pt')
        print(
            f"    {loss0:.3f}, {loss1:.3f}     {val_loss0:.3f} {val_loss1:.3f} {acc0*100:.2f}% {acc1*100:.2f}%"
        )
    # model save


def train_step(model, dataloader, criterion, optim, device):
    model.train()
    losses_batch = 0
    lendl = len(dataloader)
    print(f"Batches: {lendl} ", end="")
    for x, y, lens in dataloader:
        x, y = x.to(device), y.to(device)
        yhat = model(x, lens)
        loss = criterion(yhat, y)
        optim.zero_grad()
        loss.backward()
        optim.step()
        losses_batch += loss.item() / lendl
    return losses_batch


def eval_step(model, dataloader, criterion, device):
    model.eval()
    losses = 0
    lendl = len(dataloader)
    true, total = 0, 0
    with torch.no_grad():
        for x, y, lens in dataloader:
            x, y = x.to(device), y.to(device)
            yhat = model(x, lens)
            ypred = torch.argmax(yhat, -1)
            losses += criterion(yhat, y).item() / lendl
            true += torch.sum(ypred == y).item()
            total += len(y)
    acc = true / total
    return losses, acc
