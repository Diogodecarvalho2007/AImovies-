import pandas as pd
import torch
from sklearn.preprocessing import LabelEncoder

def load_and_prepare_data(path):
    df = pd.read_csv(path)

    X = df.drop("movie", axis=1).values.astype("float32")
    y_raw = df["movie"].values

    le = LabelEncoder()
    y = le.fit_transform(y_raw)
    
    X_tensor = torch.tensor(X, dtype=torch.float32)
    y_tensor = torch.tensor(y, dtype=torch.long)

    return X_tensor, y_tensor, le
