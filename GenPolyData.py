import numpy as np
import pandas as pd


def generate_polynomial_dataset(n):
    np.random.seed(42)  # Setting seed for reproducibility

    # Generating X values with limited range and decimal points
    X = np.round(np.random.uniform(-11, 33, n), 4)

    # Generating Y values based on a polynomial formula
    Y = 2.95 * X - 3.25 * X ** 2 + 1.75 * X**3 + 5000 * np.round(np.random.randn(n), 4)

    # Creating a DataFrame
    data = {
        'X': X,
        'Y': Y
    }

    df = pd.DataFrame(data)

    # Save DataFrame to a CSV file
    df.to_csv('files/polyLR_dataset.csv', index=False, float_format='%.4f')  # Limit decimal points to 4
    print(f"Polynomial dataset saved as 'polyLR_dataset.csv' in the 'Files' folder.")
    return df


# Generating a polynomial dataset with 10000 rows and saving it to a CSV file
n = 20
polynomial_df = generate_polynomial_dataset(n)
print(polynomial_df)
