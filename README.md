# ChainPulse AI

Predicting maritime logistics ETA under geopolitical disruptions.

## Project Overview

ChainPulse AI is an experimentation project for predicting maritime logistics delays under geopolitical risk scenarios. The current focus of the repository is organized around three areas:

- synthetic maritime shipment dataset generation;
- machine learning pipeline training for regression and classification;
- preparation of a consistent foundation for a future Streamlit interface.

The product goal remains to answer questions such as:

- "If geopolitical risk escalates on a route, what is the new expected ETA?"
- "Which shipments are most likely to experience critical delays?"
- "What is the expected impact on freight cost across different scenarios?"

## Current Repository State

The project currently includes:

- a notebook for generating a synthetic maritime shipment dataset;
- a processed dataset saved at `data/processed/synthetic_shipments.csv`;
- a baseline training notebook with features closer to the targets;
- an app-ready training notebook with a simplified schema for future app usage;
- trained pipelines saved under `models/baseline/` and `models/app_ready/`;
- a root `requirements.txt` for the current Python dependencies;
- a `CHANGELOG.md` file documenting notable project changes.

## Getting Started

### Prerequisites

- Python 3.13 or a compatible local environment
- `pip`
- Jupyter support for running the notebooks

### Installation

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Recommended Workflow

Run the notebooks in this order:

1. `notebooks/synthetic_shipping_scenarios.ipynb`
2. `notebooks/train_baseline_models.ipynb`
3. `notebooks/train_app_ready_models.ipynb`

This sequence regenerates the dataset first and then retrains both modeling approaches on the latest processed data.

## Synthetic Dataset

The synthetic dataset models routes between global ports, geopolitical events, operational delays, and freight cost behavior.

Examples of available columns:

- `origin_port`
- `destination_port`
- `route_corridor`
- `ocean_side`
- `vessel_type`
- `cargo_type`
- `distance_nm`
- `avg_speed_knots`
- `baseline_eta_days`
- `weather_delay_days`
- `port_handling_days`
- `geopolitical_event`
- `geopolitical_delay_days`
- `expected_delay_days`
- `adjusted_eta_days`
- `freight_cost_index`
- `delay_class`

### Currently Used Targets

Regression:

- `expected_delay_days`
- `adjusted_eta_days`
- `freight_cost_index`

Classification:

- `delay_class`

## Notebooks

### 1. Data generation

File: `notebooks/synthetic_shipping_scenarios.ipynb`

Responsibilities:

- define ports, events, and route rules;
- generate synthetic shipments with baseline ETA and adjusted ETA;
- save the dataset to `data/processed/synthetic_shipments.csv`.

### 2. Baseline training

File: `notebooks/train_baseline_models.ipynb`

Responsibilities:

- train 3 regression models and 1 classification model;
- use a single shared set of columns across all models;
- save pipelines to `models/baseline/`.

Note:

- this notebook uses highly informative features, such as direct delay fields, so it serves as a technical baseline reference.

### 3. App-ready training

File: `notebooks/train_app_ready_models.ipynb`

Responsibilities:

- train 3 regression models and 1 classification model with a more product-friendly schema;
- replace direct delay fields with simplified risk levels;
- save pipelines to `models/app_ready/`.

Note:

- this notebook was designed to reduce the number of manual inputs a final user would need to provide in Streamlit.

## How to Use the Project

### 1. Generate the dataset

Open `notebooks/synthetic_shipping_scenarios.ipynb` and run the notebook from top to bottom. This produces or refreshes `data/processed/synthetic_shipments.csv`.

### 2. Train the baseline models

Open `notebooks/train_baseline_models.ipynb` and run all cells. This creates a technical-reference set of pipelines under `models/baseline/`.

### 3. Train the app-ready models

Open `notebooks/train_app_ready_models.ipynb` and run all cells. This creates a product-oriented set of pipelines under `models/app_ready/`.

### 4. Read the metadata

Each training flow writes a `training_metadata.json` file containing:

- shared input features;
- trained targets;
- validation metrics;
- saved artifact paths.

## Current Structure

```text
Chain-Pulse-AI/
  data/
    processed/
      synthetic_shipments.csv
  models/
    training_metadata.json
    baseline/
      *.joblib
      training_metadata.json
    app_ready/
      *.joblib
      training_metadata.json
  notebooks/
    synthetic_shipping_scenarios.ipynb
    train_baseline_models.ipynb
    train_app_ready_models.ipynb
  CHANGELOG.md
  LICENSE
  README.md
  requirements.txt
```

## Model Artifacts

Each model folder contains:

- one saved pipeline per target in `.joblib` format;
- one `training_metadata.json` file containing:
- the features used;
- the trained targets;
- validation metrics;
- saved artifact paths.

Available folders:

- `models/baseline/`
- `models/app_ready/`

Note:

- `models/training_metadata.json` may still exist from an earlier save layout, but the organized outputs now live under `models/baseline/` and `models/app_ready/`.

## Difference Between Baseline and App-Ready

### Baseline

Stronger in offline metrics because it uses variables close to the targets, such as:

- `weather_delay_days`
- `port_handling_days`
- `geopolitical_delay_days`

Recommended use:

- technical validation;
- an upper-bound performance reference on the synthetic dataset.

### App-ready

More suitable for a future interface because it uses more compact and product-plausible inputs, such as:

- `origin_port`
- `destination_port`
- `vessel_type`
- `cargo_type`
- `distance_nm`
- `baseline_eta_days`
- `weather_risk_level`
- `port_congestion_level`
- `geopolitical_risk_level`

Recommended use:

- Streamlit integration;
- what-if simulations with less friction for the final user.

## Current Stack

- Python
- Pandas
- NumPy
- scikit-learn
- Jupyter Notebook
- joblib

Pinned package versions are listed in `requirements.txt`.

## Documentation

- `README.md`: current project overview, workflow, and artifact layout
- `CHANGELOG.md`: notable repository changes using the Keep a Changelog format

## Natural Next Steps

- build an inference layer to load pipelines and predict from a single payload;
- create the Streamlit interface with route controls and risk sliders;
- replace part of the synthetic features with operational signals that are closer to a real-world scenario.

## License

This project is licensed under Apache 2.0. See `LICENSE` for details.