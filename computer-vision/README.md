# Computer Vision

## Data

Fashion-MNIST (1) is an image dataset compiled by Zalando Research to replace the MNIST dataset. It contains 70,000 28x28 grayscale images of clothing items from 10 labelled classes:
 - T-shirt/top - 0
 - Trouser - 1
 - Pullover - 2
 - Dress - 3
 - Coat - 4
 - Sandal - 5
 - Shirt - 6
 - Sneaker - 7
 - Bag - 8
 - Ankle boot - 9     
 
The dataset is divided into a 60,000-image train set and 10,000-image test set. More information can be found on the GitHub page.
The data is provided in 2 `.csv` files contained in `data.tar.gz` file. The provided reader can be used to import the data as Numpy arrays in Python.

```python
from reader import get_images
(x_train, y_train), (x_test, y_test) = get_images() 
```

## Guidance

This is not an exhaustive list of tasks, the points are provided in order to guide you:

### Visualize Classes

Try to visualize the differences between classes, e.g. using a dimensionality reduction technique.

### Model

Test the performance of different model architectures. Tune your model to improve its performance.

### Evaluation

Report your results using appropriate metrics. See if your model performs equally among classes. Suggest possible imporvements.

## References
1. Xiao H, Rasul K, Vollgraf R. Fashion-MNIST: a Novel Image Dataset for Benchmarking Machine Learning Algorithms. CoRR [Internet]. 2017;abs/1708.07747. Available from: http://arxiv.org/abs/1708.07747
