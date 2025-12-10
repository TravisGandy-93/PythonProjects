"""A discount calculator that applies various discount strategies to products 
based on user tiers."""
from abc import ABC, abstractmethod
from typing import List


class Product:
    """Class representing a product with a name and price."""
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.name} - ${self.price}'


class DiscountStrategy(ABC):
    """Abstract base class for discount strategies."""
    @abstractmethod
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        """Check if the discount strategy is applicable to the product and user tier."""
        pass

    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        """Apply the discount to the product and return the discounted price."""
        pass


class PercentageDiscount(DiscountStrategy):
    """Discount strategy that applies a percentage discount."""
    def __init__(self, percent: int) -> None:
        self.percent = percent

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return self.percent <= 70

    def apply_discount(self, product: Product) -> float:
        return product.price * (1 - self.percent / 100)


class FixedAmountDiscount(DiscountStrategy):
    """Discount strategy that applies a fixed amount discount."""
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return product.price * 0.9 > self.amount

    def apply_discount(self, product: Product) -> float:
        return product.price - self.amount


class PremiumUserDiscount(DiscountStrategy):
    """Discount strategy for premium users."""
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return user_tier.lower() == 'premium'

    def apply_discount(self, product: Product) -> float:
        return product.price * 0.8


class DiscountEngine:
    """Engine to calculate the best discount for a product based on user tier."""
    def __init__(self, strategies: List[DiscountStrategy]) -> None:
        self.strategies = strategies

    def calculate_best_price(self, product: Product, user_tier: str) -> float:
        """Calculate the best price for the product based on applicable discounts."""
        prices = [product.price]

        for strategy in self.strategies:
            if strategy.is_applicable(product, user_tier):
                discounted = strategy.apply_discount(product)
                prices.append(discounted)

        return min(prices)


if __name__ == '__main__':
    product = Product('Wireless Mouse', 50.0)
    user_tier = 'Premium'

    strategies = [
        PercentageDiscount(10),
        FixedAmountDiscount(5),
        PremiumUserDiscount()
    ]

    engine = DiscountEngine(strategies)
    best_price = engine.calculate_best_price(product, user_tier)
    print(
        f'Best price for {product.name} for {user_tier} user: ${best_price:.2f}')
