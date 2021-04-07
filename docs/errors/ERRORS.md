### Problem:

```
File with a trained model is not exists
``` 

### Solution:

```
Add to project's root the file with trained model
```

### Problem:

```
RuntimeError: Attempting to deserialize object on a CUDA device but torch.cuda.is_available() is False. If you are running on a CPU-only machine, please use torch.load with map_location=torch.device('cpu') to map your storages to the CPU.
``` 

### Solution:

```
Replace your machine or model (You can train a model with your machine or replace your machine with another)
```