# Options Pricer

We are building a Black-Scholes model options pricer web application to learn more about quantitative finance, options pricing, and translating finance into an appealing web view.
I got the inspiration to build the app from this [video](https://www.youtube.com/watch?v=lY-NP4X455U)

## What is a Black-Scholes Model?

It's a mathematical model used for pricing options contracts. At its core, the model provides a theoretical estimate of the price of European-style options, helping determine the fair price of theoretical value for a call or put option based on factors like:

1. Current stock price
2. Option strike price
3. Time until expiration
4. Risk-free interest rate
5. Volatility of the stock

## Features

### Stage 1: Simple Data Input & Output

Takes in the 5 inputs (the five listed above) to an options price and spits out a call and a put value.

### Stage 2: Visualize the Output

- shocking (deliberately changing one or more variables to see how the output responds) the most sensitive inputs to an options price
  - volatility
  - actual stock price
- generating a visual that displays a heatmap that displays the call and put values at various different volatilities and stock prices

### Stage 3: Represent P&L

- Allow user to input a purchase price for the call and purchase price for the put
- We will then have a P&L (profit & loss) for the call and put given our inputs and given the purchase price
- The heatmap will not only display the value of the call, it can actual represent the p&l of the call and the put given the inputs and the purchase price
  - green = positive p&l
  - red = negative p&l

## Getting Started

### Dependencies

Install `fasthtml` Python library:

```sh
pip install python-fasthtml
```

### Usage

To start using the app, run:

```sh
python main.py
```

which will print out a link to the running app. Visiting this link in the browser will open the app.

<details>
<summary><h2>Understanding Black-Scholes Model at a high level</h2></summary>

To grasp the Black-Scholes Model, let's go over some preliminary terms and concepts.

### Options Basics

#### What are Options?

Options are financial contracts that give the buyer the right, but not the obligation, to buy or sell an underlying asset at a predetermined price within a specific time period. Think of them as financial insurance policies or reservations on an asset's price.

##### Key Terminology:

- **Call Option**: A contract giving the holder the right to buy an asset at a specified price within a specific time period. It's like having a coupon to buy something at a fixed price, regardless of how expensive it becomes.

- **Put Option**: A contract giving the holder the right to sell an asset at a specified price within a specific time period. This is like having insurance that guarantees you can sell at a certain price, even if the market value drops.

- **Strike Price**: The predetermined price at which the holder can buy (for calls) or sell (for puts) the underlying asset. Also called the "exercise price."

- **Expiration Date**: The date when the option contract ends and becomes void.

- **Premium**: The price paid to purchase an option contract. This is what the Black-Scholes model aims to calculate theoretically.

- **In-the-money**: When an option has intrinsic value. For calls, this means the stock price is above the strike price; for puts, the stock price is below the strike price.

- **Out-of-the-money**: When an option has no intrinsic value. For calls, this means the stock price is below the strike price; for puts, the stock price is above the strike price.

- **At-the-money**: When the stock price and strike price are approximately equal.

- **Intrinsic Value**: The amount an option would be worth if exercised immediately. For a call, it's max(0, stock price - strike price). For a put, it's max(0, strike price - stock price).

- **Time Value**: The premium minus the intrinsic value, representing the additional amount traders are willing to pay for the potential future value of the option.

#### Factors Affecting Option Pricing:

1. **Current stock price**: As the stock price increases, call options become more valuable and put options become less valuable.

2. **Strike price**: The higher the strike price, the less valuable a call option becomes; the higher the strike price, the more valuable a put option becomes.

3. **Time until expiration**: Generally, the longer the time until expiration, the more valuable the option (more time for favorable movement).

4. **Volatility**: Higher volatility increases option values (both calls and puts) as it increases the probability of the option finishing in-the-money.

5. **Risk-free interest rate**: Higher interest rates tend to increase call option values and decrease put option values.

6. **Dividends**: Expected dividends generally decrease call option values and increase put option values.

### The Intuition Behind Black-Scholes

While the mathematical formulation of Black-Scholes may seem complex, the underlying intuition is powerful and has transformed finance. Here's what the model really tells us:

#### Core Insights

The Black-Scholes model reveals that an option's price represents the cost of creating a perfectly hedged position that eliminates risk. This leads to several key insights:

1. **Risk-Neutral Valuation**: Remarkably, the option's fair price doesn't depend on investors' risk preferences or the expected return of the stock—only its volatility matters. This means regardless of whether you're bullish or bearish on a stock, you would theoretically agree on the same option price.

2. **No Arbitrage Principle**: The model is built on the idea that in efficient markets, risk-free profit opportunities cannot exist for long. The option price must be exactly what it would cost to replicate the option's payoff using a dynamic portfolio of stocks and bonds.

3. **Perfect Hedging**: Black-Scholes demonstrates that you can create a "perfect hedge" by continuously adjusting a portfolio of the underlying stock and a risk-free asset. This perfect hedge exactly replicates the option's payoff.

#### How Market Factors Affect Option Prices

The model quantifies several intuitive relationships that traders observe:

1. **Volatility Effect**: Higher volatility increases option values for both calls and puts. This makes intuitive sense because:

   - Options give you unlimited upside potential while limiting downside risk
   - Greater volatility increases the chance of large price movements
   - Since your losses are capped with options, more volatility only increases your chance of substantial gains

   This is why implied volatility often spikes before major announcements or events—the market is pricing in the potential for large moves.

2. **Time Value Decay**: Options lose value as expiration approaches (shown by negative theta). This decay accelerates as expiration nears, like an hourglass where sand falls faster at the end. This reflects the diminishing probability of significant price movements in shorter time frames.

3. **Interest Rate Effects**: Higher interest rates increase call option values but decrease put option values. This occurs because:
   - With calls, you're delaying payment for the stock, which becomes more valuable when interest rates are higher
   - With puts, you're postponing the receipt of funds from selling stock, which becomes less valuable when interest rates are higher

#### Real-World Example

Consider two stocks both trading at $100:

- Stock A barely fluctuates, moving just 0.5% per day on average
- Stock B is highly volatile, regularly moving 3% per day on average

A call option with strike price $110 expiring in three months would be much more valuable for Stock B, even though both stocks are currently at the same price. Why? Because Stock B has a much higher probability of exceeding $110 during the option's lifetime due to its greater volatility.

#### Limitations of the Model

After the 1987 market crash, traders observed that the model sometimes underprices extreme events. Real markets have "fat tails"—extreme price movements happen more frequently than a normal distribution would predict. This leads to phenomena like the "volatility smile," where out-of-the-money options trade at higher implied volatilities than the model would suggest.

Despite these limitations, the Black-Scholes model remains the foundation of options pricing theory and provides valuable insights into how options respond to changes in market conditions.

### Probability Concepts

#### Normal Distribution:

A symmetrical, bell-shaped distribution where most observations cluster around the central peak, and the probabilities of observations decrease the further they are from the mean. In simple terms, it's a pattern where most values are close to average, and extreme values are rare.

Key characteristics:

- It's symmetrical around the mean
- The mean, median, and mode are all equal
- About 68% of values fall within one standard deviation of the mean
- About 95% of values fall within two standard deviations
- About 99.7% of values fall within three standard deviations

#### Log-Normal Distribution:

A distribution of a random variable whose logarithm follows a normal distribution. Unlike the normal distribution, the log-normal distribution is skewed to the right.

Why it matters for stocks: Stock prices can't go below zero but can theoretically rise infinitely, creating an asymmetrical distribution. The log-normal distribution captures this behavior well, which is why stock prices are often modeled this way.

#### Random Walks:

A mathematical concept describing a path consisting of a succession of random steps. In finance, stock prices are often modeled as random walks, suggesting that future price movements are independent of past movements.

#### Brownian Motion:

A continuous-time random process named after botanist Robert Brown. It describes the random movement of particles suspended in a fluid. In financial mathematics, it's used to model the continuous random behavior of stock prices.

#### Standard Deviation and Volatility:

- **Standard Deviation**: A measure of the amount of variation or dispersion in a set of values. A low standard deviation indicates values tend to be close to the mean, while a high standard deviation indicates values are spread out over a wider range.

- **Volatility**: In finance, volatility refers to the degree of variation in a trading price series over time, typically measured by the standard deviation of returns. High volatility means prices change dramatically over short time periods, while low volatility means price stays relatively constant.

- **Historical Volatility**: Calculated from past market prices.

- **Implied Volatility**: The volatility value that, when input into an option pricing model like Black-Scholes, yields a theoretical value equal to the current market price of the option. It represents the market's forecast of future volatility.

### The Black-Scholes Formula

#### Key Assumptions:

1. The stock follows a log-normal distribution with constant volatility
2. No transaction costs or taxes
3. No dividends during the option's life
4. Markets are efficient (no arbitrage opportunities)
5. Risk-free interest rate is constant
6. Trading is continuous
7. Short selling is permitted

#### The Formula Components:

For a call option, the Black-Scholes formula is:

C = S₀N(d₁) - Ke^(-rT)N(d₂)

For a put option:

P = Ke^(-rT)N(-d₂) - S₀N(-d₁)

Where:

- C = Call option price
- P = Put option price
- S₀ = Current stock price
- K = Strike price
- r = Risk-free interest rate
- T = Time to expiration (in years)
- N() = Cumulative distribution function of the standard normal distribution
- e = Base of natural logarithm
- d₁ = [ln(S₀/K) + (r + σ²/2)T] / (σ√T)
- d₂ = d₁ - σ√T
- σ = Volatility of the stock

#### The Greeks:

The "Greeks" are sensitivity measures that describe how option prices change when the underlying factors change:

- **Delta (Δ)**: Measures how much the option price changes when the underlying stock price changes by $1. For call options, delta ranges from 0 to 1; for put options, from -1 to 0.

- **Gamma (Γ)**: Measures the rate of change of delta with respect to changes in the underlying price. High gamma means the delta can change rapidly with small moves in the stock.

- **Theta (Θ)**: Measures the rate at which an option loses value as time passes (time decay). Generally negative for both calls and puts.

- **Vega (V)**: Measures sensitivity to volatility. Higher vega means the option's value is more sensitive to changes in volatility.

- **Rho (ρ)**: Measures sensitivity to the risk-free interest rate. Generally, calls have positive rho, and puts have negative rho.

</details>
