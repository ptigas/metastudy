Metastudy
===

This study depends on [oscarknagg/few-shot](https://github.com/oscarknagg/few-shot/tree/master/few_shot) which has been cloned in [/fewshot](https://github.com/ptigas/metastudy/tree/master/fewshot). Read [README](https://github.com/ptigas/metastudy/blob/master/fewshot/README.md) for installation instructions.


## Few shot experiments

For the fashion dataset, download from [Kaggle](https://www.kaggle.com/paramaggarwal/fashion-product-images-dataset/version/1) the dataset and use `fewshot\scripts\prepare_fashion.py [fashion dataset folder]` to prepare the examples for the few shot experiments.


### Resnet50

Resnet-50 has been used for the fashion dataset. The encoder has been defined as:


```python
def get_few_shot_resnet_encoder() -> nn.Module:
    resnet = torchvision.models.resnet50(pretrained=True)
    modules = list(resnet.children())[:-1]
    for p in resnet.parameters():
        p.requires_grad = False

    modules.append(Flatten())
    modules.append(nn.Linear(2048, 512))

    return nn.Sequential(*modules)
```

### Prototypical Network experiments

The following experiments have been conducted. To reproduce the results use the following commands:

K=2, N=5
```
python -m experiments.proto_nets --dataset fashion --k-train 25 --k-test 2 --n-test 5 --n-train 5
```

K=10, N=5
```
python -m experiments.proto_nets --dataset fashion --k-train 25 --k-test 10 --n-test 5 --n-train 5
```

K=10, N=1
```
python -m experiments.proto_nets --dataset fashion --k-train 25 --k-test 10 --n-test 1 --n-train 1
```

K=2, N=1
```
python -m experiments.proto_nets --dataset fashion --k-train 25 --k-test 2 --n-test 1 --n-train 1
```

### Results


| **N**       | **K**  | Top-1 Accuracy (val) | Categorical Accuracy      | Network  |
| ----------: |------: | -------------------: | ----------------: | :------: |
| 5           | 10     | .858                 | .943              | Resnet50 |
| 5           | 2      | .975                 | .942              | Resnet50 |
| 1           | 10     | .668                 | .874              | Resnet50 |
| 1           | 2      | .935                 | .879              | Resnet50 |
