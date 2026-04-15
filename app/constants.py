from __future__ import annotations

MODEL_DIR = "models/app_ready"
DATA_PATH = "data/processed/synthetic_shipments.csv"

PORT_REGION = {
    "Dubai": "Middle East",
    "Durban": "Africa",
    "Houston": "North America",
    "Los Angeles": "North America",
    "Mumbai": "South Asia",
    "Rotterdam": "Europe",
    "Santos": "South America",
    "Shanghai": "East Asia",
    "Singapore": "Southeast Asia",
    "Sydney": "Oceania",
}

PORT_COORDS = {
    "Dubai": (25.2048, 55.2708),
    "Durban": (-29.8587, 31.0218),
    "Houston": (29.7604, -95.3698),
    "Los Angeles": (34.0522, -118.2437),
    "Mumbai": (19.076, 72.8777),
    "Rotterdam": (51.9244, 4.4777),
    "Santos": (-23.9608, -46.3336),
    "Shanghai": (31.2304, 121.4737),
    "Singapore": (1.3521, 103.8198),
    "Sydney": (-33.8688, 151.2093),
}

CORRIDOR_OCEAN = {
    "Atlantic Crossing": "Atlantic Side",
    "Cape Diversion": "Indian-Atlantic Side",
    "Pacific Crossing": "Pacific Side",
    "Panama Corridor": "Atlantic-Pacific Side",
    "Suez Corridor": "Indian-Atlantic Side",
}

VESSEL_TYPES = ["Bulk Carrier", "Container", "Tanker"]
CARGO_TYPES = ["Auto Parts", "Chemicals", "Electronics", "Food", "Machinery", "Textiles"]

RISK_LABEL_TO_LEVEL = {
    "Low": 0,
    "Minor": 1,
    "Moderate": 2,
    "High": 3,
}

SCENARIOS = {
    "Normal Flow": {
        "weather": "Low",
        "port": "Low",
        "geo": "Low",
    },
    "Port Congestion": {
        "weather": "Minor",
        "port": "High",
        "geo": "Low",
    },
    "Geopolitical Escalation": {
        "weather": "Minor",
        "port": "Moderate",
        "geo": "High",
    },
    "Severe Storm": {
        "weather": "High",
        "port": "Moderate",
        "geo": "Minor",
    },
}

WEATHER_RISK_OPTIONS = {
    "Calm sea and good visibility": {
        "risk": "Low",
        "description": "Stable conditions with minimal operational impact.",
    },
    "Rain and moderate winds": {
        "risk": "Minor",
        "description": "May require minor speed adjustments.",
    },
    "Cold front with high waves": {
        "risk": "Moderate",
        "description": "Increases the chance of relevant transit delays.",
    },
    "Severe storm": {
        "risk": "High",
        "description": "High probability of rerouting and major delays.",
    },
}

PORT_RISK_OPTIONS = {
    "Free berth and normal queue": {
        "risk": "Low",
        "description": "Port operation without major bottlenecks.",
    },
    "Light berth waiting line": {
        "risk": "Minor",
        "description": "Short waiting time before operations start.",
    },
    "Yard saturation and long queue": {
        "risk": "Moderate",
        "description": "Noticeable handling delays at the terminal.",
    },
    "Critical terminal congestion": {
        "risk": "High",
        "description": "Strong impact on turnaround and release times.",
    },
}

GEOPOLITICAL_RISK_OPTIONS = {
    "No relevant incident": {
        "risk": "Low",
        "description": "No significant geopolitical disruption signs on the corridor.",
        "corridors": list(CORRIDOR_OCEAN.keys()),
        "regions": sorted(set(PORT_REGION.values())),
    },
    "Stricter inspections and sanctions": {
        "risk": "Moderate",
        "description": "Increases bureaucracy, inspections, and temporary retention risk.",
        "corridors": ["Atlantic Crossing", "Suez Corridor", "Panama Corridor"],
        "regions": ["Europe", "Middle East", "North America"],
    },
    "Red Sea and Suez Canal disruption risk": {
        "risk": "High",
        "description": "Possible rerouting with major increase in transit time.",
        "corridors": ["Suez Corridor", "Cape Diversion"],
        "regions": ["Middle East", "Europe", "South Asia"],
    },
    "Tension in the Strait of Hormuz": {
        "risk": "High",
        "description": "Elevated risk for routes connected to the Gulf region.",
        "corridors": ["Suez Corridor", "Cape Diversion"],
        "regions": ["Middle East", "South Asia"],
    },
    "Piracy risk in the Gulf of Guinea": {
        "risk": "Moderate",
        "description": "Higher chance of convoying, speed reduction, and security adjustments.",
        "corridors": ["Cape Diversion", "Atlantic Crossing"],
        "regions": ["Africa", "Europe", "South America"],
    },
    "Panama Canal restrictions": {
        "risk": "High",
        "description": "Queues and reduced crossing windows for interoceanic traffic.",
        "corridors": ["Panama Corridor", "Pacific Crossing"],
        "regions": ["North America", "South America"],
    },
}

DELAY_COLORS = {
    "on_time": "#1f9d55",
    "minor_delay": "#f39c12",
    "critical_delay": "#c0392b",
}
