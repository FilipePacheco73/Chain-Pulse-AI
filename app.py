from __future__ import annotations

from app.main import run_app
from app.modeling import add_time_features


# Keep symbol in __main__ so joblib can resolve older FunctionTransformer pickle references.
_ = add_time_features


if __name__ == "__main__":
    run_app()
