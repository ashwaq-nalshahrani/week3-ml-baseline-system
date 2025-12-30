import typer
from .sample_data import make_sample_feature_table
from .train import run_training_pipeline

app = typer.Typer(
    help="Week 3 ML Baseline System",
    add_completion=False,
)


@app.command()
def make_sample_data():
    """Generate sample feature table for testing (Day 1)"""
    path = make_sample_feature_table()
    typer.echo(f"Sample data written to: {path}")


@app.command()
def train(
    target: str = typer.Option(
        ..., "--target", "-t", help="The name of the target column"
    ),
    seed: int = typer.Option(42, "--seed", help="Random seed for reproducibility"),
):
    """Train baseline model and save versioned artifacts (Day 2)"""
    try:
        run_id = run_training_pipeline(target_column=target, seed=seed)
        typer.echo(f"Training completed successfully.")
        typer.echo(f"Run ID: {run_id}")
        typer.echo(f"Artifacts saved in: models/runs/{run_id}")
    except Exception as e:
        typer.secho(f"Error during training: {e}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)


@app.command()
def predict():
    """Run batch prediction (Planned for Day 3/4)"""
    typer.echo("Predict command is not yet implemented.")


if __name__ == "__main__":
    app()
