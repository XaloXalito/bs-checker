from abc import ABC, abstractmethod

class BaseScraper(ABC):
    @abstractmethod
    def extract(self) -> float:
        pass