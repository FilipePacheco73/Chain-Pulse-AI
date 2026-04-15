# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.2.0] - 2026-04-14

### Added

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

**Repository Documentation**
- Updated `README.md` to reflect the current project state instead of the earlier high-level roadmap
- Documented the current notebooks, generated dataset, baseline training flow, and app-ready training flow
- Clarified the distinction between the baseline approach and the app-ready approach for future product integration

**Model Output Organization**
- Moved baseline training outputs to `models/baseline/` to match the structured output layout already used by `models/app_ready/`
- Standardized model artifact storage so each training flow owns its own directory and metadata file

**Training Schema Strategy**
- Kept the baseline notebook as a higher-information technical reference using direct delay-related features
- Introduced an app-ready schema that replaces direct delay inputs with simplified risk levels such as `weather_risk_level`, `port_congestion_level`, and `geopolitical_risk_level`

### Validated

**Baseline Training Outputs**
- Baseline regression and classification pipelines were executed and saved successfully under `models/baseline/`
- Baseline metadata was written successfully to `models/baseline/training_metadata.json`
- Baseline metrics recorded in metadata include `expected_delay_days` MAE `0.0025`, `adjusted_eta_days` MAE `0.0055`, `freight_cost_index` MAE `0.0006`, and `delay_class` accuracy `0.9929`

**App-Ready Training Outputs**
- App-ready regression and classification pipelines were executed and saved successfully under `models/app_ready/`
- App-ready metadata was written successfully to `models/app_ready/training_metadata.json`
- App-ready metrics recorded in metadata include `expected_delay_days` MAE `0.1801`, `adjusted_eta_days` MAE `0.1802`, `freight_cost_index` MAE `0.0064`, and `delay_class` accuracy `0.9025`

---

## [0.1.0] - 2026-04-14

### Added

**Project Foundation**
- Initial repository setup for ChainPulse AI
- Core project documentation in `README.md`
- Apache 2.0 licensing via `LICENSE`

**Workspace Setup**
- Added local editor configuration in `.vscode/settings.json`
- Added `.gitignore` entries for `*.joblib`, `.venv/`, and `__pycache__/`