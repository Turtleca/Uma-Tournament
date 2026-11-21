import json
from pathlib import Path
from typing import Any, Dict, List, Union


class UmaJsonLoader:
    """Loads a horseACT veterans.json array."""

    def load(self, filepath: Union[str, Path]) -> List[Dict[str, Any]]:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("veterans.json must contain a JSON array")
        if not all(isinstance(item, dict) for item in data):
            raise ValueError("veterans.json must contain an array of Uma objects")
        return data
