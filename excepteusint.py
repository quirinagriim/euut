from rich.console import Console

console = Console()

def cprint(text, color="white"):
    """
    Prints text in a specific color.

    Args:
        text (str): The text to print.
        color (str, optional): The color of the text. Defaults to "white".
    """
    console.print(text, style=f"bold {color}")

cprint(f'\n>>> {address_wallet} | {to_symbol} | {error}', 'red')
