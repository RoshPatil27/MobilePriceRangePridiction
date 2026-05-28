"""Simple mobile price range prediction demo.

This script uses a lightweight heuristic model to estimate a mobile
phone price range from common specifications such as RAM, battery power,
internal memory, and screen resolution.
"""

from __future__ import annotations


def predict_price_range(ram: int, battery_power: int, internal_memory: int,
                        px_height: int, px_width: int,
                        clock_speed: float = 0.0, n_cores: int = 0) -> int:
    """Return a price-range class from 0 to 3.

    Higher values mean more expensive mobiles.
    """
    resolution = px_height * px_width
    score = 0

    score += ram * 1.2
    score += battery_power * 0.02
    score += internal_memory * 0.8
    score += resolution / 100000.0
    score += clock_speed * 20
    score += n_cores * 5

    if score < 220:
        return 0
    if score < 420:
        return 1
    if score < 650:
        return 2
    return 3


def explain_prediction(ram: int, battery_power: int, internal_memory: int,
                       px_height: int, px_width: int) -> str:
    """Create a short explanation for the predicted range."""
    range_name = {
        0: "budget",
        1: "low-mid",
        2: "mid-high",
        3: "premium",
    }[predict_price_range(ram, battery_power, internal_memory, px_height, px_width)]

    return (
        f"Using RAM={ram} GB, battery={battery_power} mAh, memory={internal_memory} GB, "
        f"resolution={px_height}x{px_width}, the phone is predicted to fall in the "
        f"{range_name} price range."
    )


def main() -> None:
    """Run a simple demonstration of the price-range prediction logic."""
    sample_specs = {
        "ram": 6,
        "battery_power": 4000,
        "internal_memory": 128,
        "px_height": 1920,
        "px_width": 1080,
        "clock_speed": 2.4,
        "n_cores": 8,
    }

    predicted_range = predict_price_range(**sample_specs)
    print("Mobile Price Range Prediction")
    print("=" * 32)
    print(explain_prediction(
        sample_specs["ram"],
        sample_specs["battery_power"],
        sample_specs["internal_memory"],
        sample_specs["px_height"],
        sample_specs["px_width"],
    ))
    print(f"Predicted price range class: {predicted_range}")


if __name__ == "__main__":
    main()