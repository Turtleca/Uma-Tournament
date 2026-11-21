import json
from pathlib import Path
from typing import Any, Dict, List, Union


class UmaJsonLoader:
    """Loads and normalizes supported Uma JSON document shapes."""

    def load(self, filepath: Union[str, Path]) -> List[Dict[str, Any]]:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        if isinstance(data, dict):
            try:
                chara_info = data["single_mode_load_common"]["chara_info"]
            except (KeyError, TypeError):
                raise ValueError(
                    "Uma JSON must contain a JSON array or "
                    "single_mode_load_common.chara_info"
                ) from None
            if isinstance(chara_info, dict):
                return [chara_info]

        raise ValueError(
            "Uma JSON must contain a JSON array or "
            "single_mode_load_common.chara_info"
        )
