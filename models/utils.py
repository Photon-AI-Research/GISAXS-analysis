from torch.nn import Module

class View(Module):
    def __init__(self, size):
        super(View, self).__init__()
        self.size = size

    def forward(self, tensor):
        return tensor.view(self.size)
    
class ToSymmetric(Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x):
        middle = x.shape[-1]//2
        x[:,:,:,middle:] = x.flip(-1)[:,:,:,middle:]
        return x