import pytorch_lightning as pl
import torch
import torch.nn as nn


def train_autoencoder():
    """Autoencoder 모델을 build한 후 train하는 함수."""
    class Autoencoder(pl.LightningModule):
        def __init__(self, input_shape, encoding_dim):
            super().__init__()
            
            self.encoder = nn.Sequential(
                nn.Linear(input_shape, 128),
                nn.ReLU(),
                nn.Linear(128, 64),
                nn.ReLU(),
                nn.Linear(64, encoding_dim)
            )
            
            self.decoder = nn.Sequential(
                nn.Linear(encoding_dim, 64),
                nn.ReLU(),
                nn.Linear(64, 128),
                nn.ReLU(),
                nn.Linear(128, input_shape)
            )

        def forward(self, x):
            encoded = self.encoder(x)
            decoded = self.decoder(encoded)
            return decoded
        
        def loss_function(self, recon_x, x):
            mse = nn.MSELoss()
            return mse(recon_x, x)
        
        def training_step(self, batch, batch_idx):
            x, _ = batch
            recon_batch = self(x)
            loss = self.loss_function(recon_batch, x)
            logs = {'loss': loss}
            self.log('train_loss', loss, on_step=True, on_epoch=True, prog_bar=True)
            return {'loss': loss, 'log': logs}


    model = Autoencoder(input_shape=28 * 28, encoding_dim=32)
    trainer = pl.Trainer(gpus=1)
    trainer.fit(model, train_dataloader=train_dataloader) 


def example():
    pass


if __name__ == "__main__":
    example()
