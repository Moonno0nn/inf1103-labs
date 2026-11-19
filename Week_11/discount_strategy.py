from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        """Calculate and return the discounted total."""
        pass


class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100.")
        self.percentage = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self.percentage / 100)


class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, discount_amount: float):
        if threshold < 0 or discount_amount < 0:
            raise ValueError("Threshold and discount amount must be non-negative.")
        self.threshold = threshold
        self.discount_amount = discount_amount

    def apply(self, total: float) -> float:
        if total >= self.threshold:
            return max(0.0, total - self.discount_amount)
        return total


class StudentDiscount(DiscountStrategy):
    def __init__(self, percentage: float = 5.0):
        self.percentage = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self.percentage / 100)
