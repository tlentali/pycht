"""
Main project settings and execution logic.
"""

import typer

from .pycht import Pycht


app = typer.Typer()


@app.command()
def stencil(input_img: str, nb_colors: int = 4, output_path: str = "./"):
    typer.echo(f"Processing {input_img} into {output_path} with {nb_colors} levels.")
    Pycht().stencil(input_img, nb_colors, output_path)


if __name__ == "__main__":
    app()
