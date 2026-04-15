# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.2.0] - 2026-04-14

### Added

**Interactive Streamlit Interface**
- Added guided Streamlit app organized under `app/` with modules for constants, data utilities, modeling, visuals, and layout
- Added scenario presets for fast simulation (`Normal Flow`, `Port Congestion`, `Geopolitical Escalation`, `Severe Storm`)
- Added predefined option selectors for weather conditions, port status, and geopolitical events by location
- Added route-relevance check that highlights geopolitical events matching the selected corridor and regions
- Added integrated model inference for `expected_delay_days`, `adjusted_eta_days`, `freight_cost_index`, and `delay_class` from `models/app_ready/`
- Added dynamic world map that updates route color and line width based on predicted delay profile
- Added delay intensity gauge and KPI metrics for decision support
- Added `app.py` as a compatibility wrapper entrypoint

### Changed

**English Standardization**
- Translated all Streamlit UI copy to English across `app/main.py`, `app/layout.py`, `app/modeling.py`, and `app/visuals.py`
- Replaced Portuguese risk labels and scenario names with English equivalents in `app/constants.py`

**Dependencies and Stack**
- Updated `requirements.txt` to include Streamlit and Plotly
- Added `pandas==2.2.3` pin to resolve compatibility conflict with Streamlit `1.44.1`

**Repository Documentation**
- Updated `README.md` to reflect the modular app structure, English labels, English run instructions, and current stack
- Clarified the distinction between baseline and app-ready training approaches
- Updated `.gitignore` to include `.vscode/` and `.ipynb_checkpoints/`

---

## [0.1.0] - 2026-04-14

### Added

**Project Foundation**
- Initial repository setup for ChainPulse AI
- Core project documentation in `README.md`
- Apache 2.0 licensing via `LICENSE`
- Added local editor configuration in `.vscode/settings.json`
- Added `.gitignore` entries for `.venv/` and `__pycache__/`

**Synthetic Maritime Dataset Workflow**
- Added `notebooks/synthetic_shipping_scenarios.ipynb` to generate a synthetic maritime shipment dataset for ETA, delay, risk, and freight-cost experiments
- Added export of processed synthetic data to `data/processed/synthetic_shipments.csv`
- Added notebook documentation covering dataset columns, prediction targets, and scenario simulation use cases

**Baseline Model Training**
- Added `notebooks/train_baseline_models.ipynb` for shared-schema training of three regression pipelines and one delay-class classifier
- Added baseline model artifact folder at `models/baseline/`
- Added baseline metadata export to `models/baseline/training_metadata.json`

**App-Ready Model Training**
- Added `notebooks/train_app_ready_models.ipynb` for a simplified training schema aimed at future end-user Streamlit inputs
- Added app-ready model artifact folder at `models/app_ready/`
- Added app-ready metadata export to `models/app_ready/training_metadata.json`

**Model Artifacts and Metadata**
- Added saved scikit-learn pipeline artifacts for `expected_delay_days`, `adjusted_eta_days`, `freight_cost_index`, and `delay_class`
- Added metadata files capturing shared features, targets, evaluation metrics, and artifact paths for each training flow

### Changed

**Model Output Organization**
- Standardized model artifact storage so each training flow owns its own directory and metadata file
- Introduced an app-ready schema that replaces direct delay inputs with simplified risk levels such as `weather_risk_level`, `port_congestion_level`, and `geopolitical_risk_level`

### Validated

**Baseline Training Outputs**
- Baseline metrics: `expected_delay_days` MAE `0.0025`, `adjusted_eta_days` MAE `0.0055`, `freight_cost_index` MAE `0.0006`, `delay_class` accuracy `0.9929`

**App-Ready Training Outputs**
- App-ready metrics: `expected_delay_days` MAE `0.1801`, `adjusted_eta_days` MAE `0.1802`, `freight_cost_index` MAE `0.0064`, `delay_class` accuracy `0.9025`