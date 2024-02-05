In general there are two use cases for ABCs, as a pure ABC that defines an "interface" and as a tool for code re-use via the Framework Design Pattern or through Mixins.

Requires @abstractmethod decorator to be put on methods that must be implemented.

```python
from abc import ABC, abstractmethod
from typing import List, TypeVar

import numpy as np

T = TypeVar("T", bound="Model")


class Model(ABC):
    def __init__(self):
        self._is_fitted = False

    def fit(self: T, data: np.ndarray, target: np.ndarray) -> T:
        fitted_model = self._fit(data, target)
        self._is_fitted = True
        return fitted_model

    def predict(self, data: np.ndarray) -> List[float]:
        if not self._is_fitted:
            raise ValueError(f"{self.__class__.__name__} must be fit before calling predict")
        return self._predict(data)

    @property
    def is_fitted(self) -> bool:
        return self._is_fitted

    @abstractmethod
    def _fit(self: T, data: np.ndarray, target: np.ndarray) -> T:
        pass

    @abstractmethod
    def _predict(self, data: np.ndarray) -> List[float]:
        pass
```