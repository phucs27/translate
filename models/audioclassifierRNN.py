import torch
import torch.nn as nn
import torchaudio

class AudioClassifierRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super(AudioClassifierRNN, self).__init__()
        
        # LSTM layer
        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size, 
                            num_layers=num_layers, batch_first=True, bidirectional=True)
        
        # Fully connected layer
        self.fc = nn.Linear(hidden_size * 2, num_classes)  # nhân 2 do LSTM bidirectional
        
        # Activation
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        # LSTM layer
        out, _ = self.lstm(x)
        
        # Select the last time step output (many-to-one)
        out = out[:, -1, :]  # lấy output của time step cuối cùng
        
        # Fully connected layer
        out = self.fc(out)
        
        # Apply softmax activation
        out = self.softmax(out)
        
        return out
