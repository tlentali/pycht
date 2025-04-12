"""
Main project settings and execution logic.
"""

import typer
from typing_extensions import Annotated

from .pycht import Pycht

app = typer.Typer(help="Main CLI for Pycht.")


@app.command()
def compute(
    input_img: Annotated[str, typer.Argument(help="The input image")],
    nb_colors: Annotated[int, typer.Option("--nb-colors", "-n", help="Number of color clusters")] = 3,
    output_path: Annotated[str, typer.Option("--output-path", "-o", help="The output folder")] = "./",
):
    """Stencil your picture with an input image 🎨 !"""
    typer.echo(f"Processing {input_img} into {output_path} with {nb_colors} levels.")
    Pycht().stencil(input_img, nb_colors, output_path)


# @app.command()
# def compute(
#     input_img: Annotated[str, typer.Argument(help="The input image")],
#     nb_colors: Annotated[int, typer.Option("--nb-colors", "-n", help="Number of color clusters")] = 3,
#     output_path: Annotated[str, typer.Option("--output-path", "-o", help="The output folder")] = "./",
# ):
#     """Stencil your picture with an input image 🎨 !"""
#     typer.echo(f"Processing {input_img} into {output_path} with {nb_colors} levels.")
#     Pycht().stencil(input_img, nb_colors, output_path)


if __name__ == "__main__":
    app()
