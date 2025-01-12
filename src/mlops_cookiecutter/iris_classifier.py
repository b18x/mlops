import pickle
from typing import Annotated

import typer
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

app = typer.Typer()
train_app = typer.Typer()
app.add_typer(train_app, name="train")

# Load the dataset
data = load_breast_cancer()
x = data.data
y = data.target

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_text = scaler.fit_transform(x_test)


@train_app.command()
def svm(
    output: Annotated[str, typer.Option("--output", "-o")] = "model.ckpt",
    kernel: Annotated[str, typer.Option("--kernel")] = "linear",
):
    """Train and evaluate an SVM model."""
    model = SVC(kernel=kernel, random_state=42)
    model.fit(x_train, y_train)

    with open(output, "wb") as f:
        pickle.dump((model), f)

    print(f"Trained SVM model and saved as {output}")


@train_app.command()
def knn(
    output: Annotated[str, typer.Option("--output", "-o")] = "model.ckpt", k: Annotated[int, typer.Option("-k")] = 5
):
    """Train and evaluate a KNN model."""
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(x_train, y_train)

    with open(output, "wb") as f:
        pickle.dump((model), f)

    print(f"Trained KNN model and saved as {output}")


@app.command()
def evaluate(model_path: Annotated[str, typer.Argument()]):
    """Evaluate the model"""

    # Load the model
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    # Make predictions on the test set
    y_pred = model.predict(x_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(report)
    return accuracy, report


if __name__ == "__main__":
    app()
