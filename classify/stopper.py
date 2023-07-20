import numpy as np
class EarlyStopper:
    def __init__(self, patience=1, min_delta=0):
        self.patience = patience
        self.min_delta = min_delta
        self.counter = 0
        self.min_validation_loss = np.inf

    def early_stop(self, validation_loss):
        # tesnor comes in validation loss
        validation_loss = validation_loss.item()
        print(validation_loss < self.min_validation_loss, validation_loss, self.min_validation_loss)
        print( self.min_delta+ self.min_validation_loss )
        if validation_loss < self.min_validation_loss:
            print("inside if")
            self.min_validation_loss = validation_loss
            self.counter = 0
        elif validation_loss > (self.min_validation_loss + self.min_delta):
            self.counter += 1
            print(self.counter, "counter")
            if self.counter >= self.patience:
                return True
        return False