from fasthtml.common import *
import numpy as np
from math import log, sqrt, exp
from scipy.stats import norm


# Black-Scholes Option Pricing Model Implementation
def black_scholes(S, K, T, r, sigma, option_type="call"):
    """
    Calculate the Black-Scholes price of a European option.

    Parameters:
    S : float
        Current stock price
    K : float
        Option strike price
    T : float
        Time to expiration in years
    r : float
        Risk-free interest rate (annual)
    sigma : float
        Volatility of the stock (annual)
    option_type : str
        Type of option - "call" or "put"

    Returns:
    float : Option price
    """
    # Convert decimal percentages to their proper form
    sigma = max(0.001, sigma)  # Prevent division by zero

    d1 = (log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)

    if option_type.lower() == "call":
        price = S * float(norm.cdf(d1)) - K * exp(-r * T) * float(norm.cdf(d2))
    else:  # put option
        price = K * exp(-r * T) * float(norm.cdf(-d2)) - S * float(norm.cdf(-d1))

    return round(price, 2)


def calculate_greeks(S, K, T, r, sigma, option_type="call"):
    """Calculate option Greeks."""
    # Prevent division by zero
    sigma = max(0.001, sigma)
    T = max(0.001, T)

    d1 = (log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)

    # Delta - rate of change of option price with respect to underlying price
    if option_type.lower() == "call":
        delta = float(norm.cdf(d1))
    else:
        delta = float(norm.cdf(d1)) - 1

    # Gamma - rate of change of delta with respect to underlying price
    gamma = float(norm.pdf(d1)) / (S * sigma * sqrt(T))

    # Theta - rate of change of option price with respect to time
    if option_type.lower() == "call":
        theta = -S * float(norm.pdf(d1)) * sigma / (2 * sqrt(T)) - r * K * exp(-r * T) * float(norm.cdf(d2))
    else:
        theta = -S * float(norm.pdf(d1)) * sigma / (2 * sqrt(T)) + r * K * exp(-r * T) * float(norm.cdf(-d2))
    theta = theta / 365  # Daily theta

    # Vega - rate of change of option price with respect to volatility
    vega = S * sqrt(T) * float(norm.pdf(d1)) * 0.01  # 1% change in volatility

    # Rho - rate of change of option price with respect to interest rate
    if option_type.lower() == "call":
        rho = K * T * exp(-r * T) * float(norm.cdf(d2)) * 0.01  # 1% change in interest rate
    else:
        rho = -K * T * exp(-r * T) * float(norm.cdf(-d2)) * 0.01

    return {
        "delta": round(delta, 4),
        "gamma": round(gamma, 4),
        "theta": round(theta, 4),
        "vega": round(vega, 4),
        "rho": round(rho, 4),
    }

    # Create the FastHTML app


app, rt = fast_app(
    title="Black-Scholes Options Pricer",
    # Set dark theme for PicoCSS
    htmlkw={"data-theme": "dark"},
    hdrs=(
        # Add custom styles for the dashboard
        Style("""
            :root {
                /* Gruvbox Material Dark Palette */
                --bg0: #282828;
                --bg1: #32302f;
                --bg2: #45403d;
                --bg3: #5a524c;
                
                --fg0: #e2cca9;
                --fg1: #c5b18d;
                --fg2: #a89984;
                
                --red: #ea6962;
                --orange: #e78a4e;
                --yellow: #d8a657;
                --green: #a9b665;
                --aqua: #89b482;
                --blue: #7daea3;
                --purple: #d3869b;
                
                /* Application-specific colors */
                --primary-color: var(--fg0);
                --secondary-color: var(--aqua);
                --accent-color: var(--orange);
                --background-color: var(--bg0);
                --card-bg: var(--bg1);
                --border-color: var(--bg3);
                --hover-color: var(--bg2);
                --call-color: var(--green);
                --put-color: var(--red);
                --button-color: var(--blue);
                --button-hover: var(--aqua);
            }
            
            body {
                font-family: 'Inter', system-ui, sans-serif;
                color: var(--fg0);
                background-color: var(--background-color);
                line-height: 1.6;
            }
            
            h1, h2, h3 {
                color: var(--fg0);
                margin-top: 1.5rem;
                margin-bottom: 1rem;
            }
            
            h1 {
                color: var(--secondary-color);
            }
            
            p {
                color: var(--fg1);
            }
            
            label {
                font-weight: 600;
                color: var(--fg0);
                display: block;
                margin-bottom: 0.5rem;
            }
            
            input, select {
                background-color: var(--bg2);
                color: var(--fg0);
                border: 1px solid var(--border-color);
                border-radius: 4px;
                padding: 0.5rem;
                width: 100%;
                transition: all 0.2s;
            }
            
            input:focus, select:focus {
                outline: none;
                border-color: var(--secondary-color);
                box-shadow: 0 0 0 2px rgba(137, 180, 130, 0.3);
            }
            
            .result-card {
                background-color: var(--card-bg);
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                border: 1px solid var(--border-color);
            }
            
            .result-value {
                font-size: 2rem;
                font-weight: 700;
            }
            
            #call_price {
                color: var(--call-color);
            }
            
            #put_price {
                color: var(--put-color);
            }
            
            .result-label {
                font-size: 0.9rem;
                color: var(--fg2);
                margin-bottom: 0.5rem;
            }
            
            .greeks-grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
                gap: 1rem;
                margin-top: 1rem;
            }
            
            .greek-card {
                background-color: var(--bg2);
                border-radius: 6px;
                padding: 0.75rem;
                text-align: center;
                border: 1px solid var(--border-color);
                transition: transform 0.2s, box-shadow 0.2s;
            }
            
            .greek-card:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }
            
            .greek-value {
                font-size: 1.2rem;
                font-weight: 600;
                color: var(--secondary-color);
            }
            
            .greek-label {
                font-size: 0.8rem;
                color: var(--fg2);
                margin-bottom: 0.2rem;
            }
            
            .input-group {
                margin-bottom: 1.5rem;
            }
            
            button {
                background-color: var(--button-color);
                color: var(--fg0);
                border: none;
                padding: 0.6rem 1.5rem;
                border-radius: 4px;
                cursor: pointer;
                font-weight: 600;
                transition: all 0.2s;
                width: 100%;
                margin-top: 1rem;
            }
            
            button:hover {
                background-color: var(--button-hover);
                transform: translateY(-2px);
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }
            
            .info-text {
                font-size: 0.85rem;
                color: var(--fg2);
                margin-top: 0.3rem;
            }
            
            .grid {
                grid-gap: 2rem;
            }
            
            .column {
                padding: 1rem;
                background-color: var(--bg1);
                border-radius: 8px;
                border: 1px solid var(--border-color);
            }
            
            ul {
                color: var(--fg1);
                padding-left: 1.5rem;
            }
            
            li {
                margin-bottom: 0.5rem;
            }
            
            strong {
                color: var(--yellow);
                font-weight: 600;
            }
            
            @media (max-width: 768px) {
                .greeks-grid {
                    grid-template-columns: repeat(2, 1fr);
                }
                
                .column {
                    margin-bottom: 1rem;
                }
            }
        """),
    ),
)


@rt("/")
def get(request):
    """Render the options pricing dashboard."""
    form = Form(
        Grid(
            Div(
                H2("Input Parameters"),
                Div(
                    Label(
                        "Stock Price ($)",
                        Input(
                            type="number",
                            id="stock_price",
                            name="stock_price",
                            value="100",
                            step="0.01",
                            min="0.01",
                            required=True,
                        ),
                    ),
                    cls="input-group",
                ),
                Div(
                    Label(
                        "Strike Price ($)",
                        Input(
                            type="number",
                            id="strike_price",
                            name="strike_price",
                            value="100",
                            step="0.01",
                            min="0.01",
                            required=True,
                        ),
                    ),
                    cls="input-group",
                ),
                Div(
                    Label(
                        "Time to Expiration (years)",
                        Input(
                            type="number",
                            id="time_to_expiry",
                            name="time_to_expiry",
                            value="1",
                            step="0.01",
                            min="0.01",
                            max="30",
                            required=True,
                        ),
                    ),
                    P("E.g. 0.5 for 6 months, 0.25 for 3 months", cls="info-text"),
                    cls="input-group",
                ),
                Div(
                    Label(
                        "Risk-Free Interest Rate (%)",
                        Input(
                            type="number",
                            id="risk_free_rate",
                            name="risk_free_rate",
                            value="5",
                            step="0.1",
                            min="0",
                            max="100",
                            required=True,
                        ),
                    ),
                    cls="input-group",
                ),
                Div(
                    Label(
                        "Volatility (%)",
                        Input(
                            type="number",
                            id="volatility",
                            name="volatility",
                            value="20",
                            step="0.1",
                            min="0.1",
                            max="200",
                            required=True,
                        ),
                    ),
                    P("Annual volatility, e.g. 20 for 20%", cls="info-text"),
                    cls="input-group",
                ),
                Div(
                    Label(
                        "Option Type",
                        Select(
                            Option("Call", value="call", selected=True),
                            Option("Put", value="put"),
                            id="option_type",
                            name="option_type",
                        ),
                    ),
                    cls="input-group",
                ),
                Button("Calculate Option Price", type="submit"),
                cls="column",
            ),
            Div(
                H2("Option Price", id="results-heading"),
                Div(
                    Div(
                        P("Call Option Price", cls="result-label"),
                        P("$0.00", id="call_price", cls="result-value"),
                    ),
                    cls="result-card",
                ),
                Div(
                    P("Put Option Price", cls="result-label"),
                    P("$0.00", id="put_price", cls="result-value"),
                    cls="result-card",
                ),
                H3("Option Greeks"),
                Div(id="greeks_container"),
                P("Greeks show option price sensitivity to different factors.", cls="info-text"),
                Div(id="explanation", style="margin-top: 1.5rem;"),
                cls="column",
            ),
        ),
        hx_post="/calculate",
        hx_trigger="submit",
        hx_target="#explanation",
        hx_swap="beforeend",
    )

    # Add explanation text
    explanation = Div(
        H3("Understanding the Results"),
        P("""The Black-Scholes model provides theoretical prices for European-style options based on the inputs you provide. 
           The model assumes that stock prices follow a log-normal distribution and that markets are efficient."""),
        P("""The Greeks help traders understand how option prices might change when market conditions change:"""),
        Ul(
            Li(B("Delta:"), " How much the option price changes when the stock price changes by $1."),
            Li(B("Gamma:"), " How much Delta changes when the stock price changes by $1."),
            Li(B("Theta:"), " How much the option price changes with one day passing (time decay)."),
            Li(B("Vega:"), " How much the option price changes when volatility changes by 1%."),
            Li(B("Rho:"), " How much the option price changes when interest rates change by 1%."),
        ),
        cls="result-card",
        id="initial_explanation",
    )

    return Titled("Black-Scholes Options Pricer", Container(form, explanation))


@rt("/calculate")
def post(
    stock_price: float,
    strike_price: float,
    time_to_expiry: float,
    risk_free_rate: float,
    volatility: float,
    option_type: str,
):
    """Calculate option prices and Greeks based on input parameters."""

    # Convert percentage inputs to decimal
    risk_free_rate = risk_free_rate / 100
    volatility = volatility / 100

    # Calculate option prices
    call_price = black_scholes(stock_price, strike_price, time_to_expiry, risk_free_rate, volatility, "call")
    put_price = black_scholes(stock_price, strike_price, time_to_expiry, risk_free_rate, volatility, "put")

    # Calculate Greeks for the selected option type
    greeks = calculate_greeks(stock_price, strike_price, time_to_expiry, risk_free_rate, volatility, option_type)

    # Create the Greeks display
    greeks_display = Div(
        Div(
            Div(P("Delta", cls="greek-label"), P(greeks["delta"], cls="greek-value"), cls="greek-card"),
            Div(P("Gamma", cls="greek-label"), P(greeks["gamma"], cls="greek-value"), cls="greek-card"),
            Div(P("Theta", cls="greek-label"), P(greeks["theta"], cls="greek-value"), cls="greek-card"),
            Div(P("Vega", cls="greek-label"), P(greeks["vega"], cls="greek-value"), cls="greek-card"),
            Div(P("Rho", cls="greek-label"), P(greeks["rho"], cls="greek-value"), cls="greek-card"),
            cls="greeks-grid",
        ),
        hx_swap_oob="innerHTML",
        id="greeks_container",
    )

    # Update the prices with hx-swap-oob
    call_display = P(f"${call_price}", hx_swap_oob="innerHTML", id="call_price", cls="result-value")
    put_display = P(f"${put_price}", hx_swap_oob="innerHTML", id="put_price", cls="result-value")

    # Analysis of the results
    itm_otm = ""
    if option_type == "call":
        if stock_price > strike_price:
            itm_otm = "in-the-money"
        elif stock_price < strike_price:
            itm_otm = "out-of-the-money"
        else:
            itm_otm = "at-the-money"
    else:  # put option
        if stock_price < strike_price:
            itm_otm = "in-the-money"
        elif stock_price > strike_price:
            itm_otm = "out-of-the-money"
        else:
            itm_otm = "at-the-money"

    explanation = Div(
        H3("Analysis of Your Option"),
        P(f"This {option_type} option is currently {itm_otm}."),
        P(
            f"With a Delta of {greeks['delta']}, a $1 change in the stock price would change the option value by approximately ${abs(greeks['delta'])}."
        ),
        P(f"The option is losing ${abs(greeks['theta'])} in value each day due to time decay (Theta)."),
        P(f"If volatility increases by 1%, the option value would change by approximately ${greeks['vega']} (Vega)."),
        cls="result-card",
        style="margin-top: 2rem;",
    )

    return (call_display, put_display, greeks_display, explanation)


serve()
