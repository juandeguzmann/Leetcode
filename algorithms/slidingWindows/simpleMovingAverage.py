import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulated data (replace with your real data)
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100),
    'Price': np.random.rand(100).cumsum() + 50
}
df = pd.DataFrame(data)

# Parameters for moving averages
short_window = 10  # Short-term SMA
long_window = 30   # Long-term SMA

# Calculate moving averages
df['Short_SMA'] = df['Price'].rolling(window=short_window, min_periods=1).mean()
df['Long_SMA'] = df['Price'].rolling(window=long_window, min_periods=1).mean()

# Generate buy/sell signals
df['Signal'] = 0
df['Signal'][short_window:] = np.where(
    df['Short_SMA'][short_window:] > df['Long_SMA'][short_window:], 1, -1
)

# Find where crossovers happen
df['Buy_Signal'] = (df['Signal'] == 1) & (df['Signal'].shift(1) == -1)
df['Sell_Signal'] = (df['Signal'] == -1) & (df['Signal'].shift(1) == 1)

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Price'], label='Price', color='blue', alpha=0.6)
plt.plot(df['Date'], df['Short_SMA'], label=f'{short_window}-day SMA', color='red', alpha=0.6)
plt.plot(df['Date'], df['Long_SMA'], label=f'{long_window}-day SMA', color='green', alpha=0.6)

# Plot buy/sell signals
plt.scatter(df['Date'][df['Buy_Signal']], df['Price'][df['Buy_Signal']],
            label='Buy Signal', marker='^', color='green', alpha=1)
plt.scatter(df['Date'][df['Sell_Signal']], df['Price'][df['Sell_Signal']],
            label='Sell Signal', marker='v', color='red', alpha=1)

plt.title('Price and Simple Moving Averages with Buy/Sell Signals')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()

# Print buy/sell signals
print("Buy Signals:")
print(df.loc[df['Buy_Signal'], ['Date', 'Price']])

print("\nSell Signals:")
print(df.loc[df['Sell_Signal'], ['Date', 'Price']])
