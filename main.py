from fasthtml.common import *


app, rt = fast_app()


@rt("/")
def get():
    inp = Label("Enter Current Stock Price:", Input(id="current-stock-price", name="current-stock-price", placeholder="Current Stock Price"))
    return (Title("Options Pricer"), 
            Div(
                H1("Finance Made Easy"),
                inp
            ))


serve()
