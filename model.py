import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd

class MovieRecommender(nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.fc1 = nn.Linear(input_size, 32)
        self.dropout = nn.Dropout(0.3)
        self.fc2 = nn.Linear(32, 16)
        self.out = nn.Linear(16, output_size)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        return self.out(x)

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = MovieRecommender(X.shape[1], len(set(y.tolist())))
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    loss_fn = nn.CrossEntropyLoss()

    for epoch in range(200):
        model.train()
        optimizer.zero_grad()
        output = model(X_train)
        loss = loss_fn(output, y_train)
        loss.backward()
        optimizer.step()

    # Avaliação simples
    model.eval()
    with torch.no_grad():
        preds = model(X_test)
        predicted = torch.argmax(preds, dim=1)
        acc = (predicted == y_test).float().mean().item()
        print(f"[✔] Test accuracy: {acc:.2f}")

    return model
