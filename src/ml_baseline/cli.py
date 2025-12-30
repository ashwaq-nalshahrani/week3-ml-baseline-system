import typer
from .sample_data import make_sample_feature_table

app = typer.Typer(
    help="Week 3 ML Baseline System",
    add_completion=False,
)

@app.command()
def make_sample_data():
    """Generate sample feature table"""
    path = make_sample_feature_table()
    typer.echo(f"Sample data written to: {path}")

@app.command()
def train():
    """Train baseline model (coming soon)"""
    raise NotImplementedError("Training will be implemented later.")

@app.command()
def predict():
    """Run batch prediction (coming soon)"""
    raise NotImplementedError("Prediction will be implemented later.")