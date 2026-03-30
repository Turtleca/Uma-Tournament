"""Uma Class file"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional

from uma_enums.aptitudes import UmaDistance, UmaStats, UmaStyle, UmaTrack
from uma_enums.letter_grade import LetterGrade


class Uma:
    """
    Data for an Umamusume
    Attributes
    ----------
    name :
    outfit_id :
    score :
    stats :
    aptitudes :
    skills :
    name :
    outfit_id :
    score :
    skills :

    """

    def __init__(
        self,
        name: str = "",
        outfit_id: str = "",
        score: int = 0,
        stats: Optional[Dict[str, int]] = None,
        aptitudes: Optional[Dict[str, Any]] = None,
        skills: Optional[List[int]] = None,
        strategy: Optional[Any] = None,
    ) -> None:
        # Identifiers
        self.name = name
        self.outfit_id = outfit_id
        self.score = int(score)

        default_stats = {"speed": 1, "stamina": 1, "power": 1, "guts": 1, "wisdom": 1}

        # Stats
        self.stats: Dict[str, int] = default_stats.copy()
        if stats:
            for str_s, value in stats.items():
                str_stat = str(str_s).strip().lower()
                if str_stat in self.stats:
                    try:
                        self.stats[str_stat] = int(value)
                    except Exception:  # TODO: limit to known Exceptions
                        print("Unknown Error, defaulting to 1 for", str_stat)
                        self.stats[str_stat] = 1

        # aptitudes stored as LetterGrade
        # TODO: Allow for smart defaulting
        default_apts = {
            "surfaceAptitude": LetterGrade.G,
            "distanceAptitude": LetterGrade.G,
            "strategyAptitude": LetterGrade.G,
        }

        self.aptitudes: Dict[str, LetterGrade] = default_apts.copy()
        if aptitudes:
            # aptitudes might be passed in as strings or LetterGrade values
            for k, v in aptitudes.items():
                key = str(k)
                if key in self.aptitudes:
                    self.aptitudes[key] = LetterGrade.from_str(v)
                else:
                    lk = key.strip().lower()
                    if lk.startswith("surf"):
                        self.aptitudes["surfaceAptitude"] = LetterGrade.from_str(v)
                    elif lk.startswith("dist"):
                        self.aptitudes["distanceAptitude"] = LetterGrade.from_str(v)
                    elif lk.startswith("strat"):
                        self.aptitudes["strategyAptitude"] = LetterGrade.from_str(v)

        # Skills
        self.skills: List[int] = list(self._resolve_skills(skills) or [])

        # Normalize and store strategy internally as UmaStyle or None
        if isinstance(strategy, UmaStyle):
            self.strategy: Optional[UmaStyle] = strategy
        else:
            self.strategy = UmaStyle.from_name(strategy)

        print(f'Created Uma:"{self.name}"')
        print(self)

    # ---------------------
    # Setters (chaining)
    # ---------------------
    def set_name_outfit(self, name: str, outfit: str) -> "Uma":
        self.name = name
        self.outfit_id = outfit
        print(f"Named Uma {self.outfit_id} {self.name}")
        return self

    # TODO: Calculate the score on call rather than set it default
    def set_score(self, score: int) -> "Uma":
        self.score = int(score)
        print(f"Set score to {score}")
        return self

    def set_stats(self, stats: Dict[str, int]) -> "Uma":
        for k, v in stats.items():
            kk = str(k).strip().lower()
            if kk in self.stats:
                try:
                    self.stats[kk] = int(v)
                except Exception:
                    pass
        return self

    def set_stat(self, key: str, value: int) -> "Uma":
        kk = str(key).strip().lower()
        if kk in self.stats:
            try:
                self.stats[kk] = int(value)
            except Exception:
                pass
        return self

    def set_aptitudes(self, aptitudes_dict: Dict[str, Any]) -> "Uma":
        for k, v in aptitudes_dict.items():
            key = str(k)
            if key in self.aptitudes:
                self.aptitudes[key] = LetterGrade.from_str(v)
            else:
                lk = key.strip().lower()
                if lk.startswith("surf"):
                    self.aptitudes["surfaceAptitude"] = LetterGrade.from_str(v)
                elif lk.startswith("dist"):
                    self.aptitudes["distanceAptitude"] = LetterGrade.from_str(v)
                elif lk.startswith("strat"):
                    self.aptitudes["strategyAptitude"] = LetterGrade.from_str(v)
        return self

    def add_skills(self, skills: List[Any]) -> "Uma":
        skills = list(skills)

        new_ids = self._resolve_skills(skills)
        for skill_id in new_ids:
            if skill_id not in self.skills:
                self.skills.append(skill_id)
        print(f"{self.name} added skills: {new_ids}")
        return self

    def rem_skills(self, skills: List[Any]) -> "Uma":
        skills = list(skills)
        remove_ids = self._resolve_skills(skills)
        before = len(self.skills)
        self.skills = [s for s in self.skills if s not in remove_ids]
        removed_count = before - len(self.skills)
        print(f"{self.name} removed {removed_count} skills: {remove_ids}")
        return self

    def set_skills(self, skills: List[Any]) -> "Uma":
        skills = list(skills)
        new_ids = self._resolve_skills(skills)
        self.skills = new_ids
        print(f"{self.name} skills set to: {new_ids}")
        return self

    def set_strategy(self, strategy: Optional[Any]) -> "Uma":
        """Set strategy; accepts UmaStyle or string synonyms, normalizes to UmaStyle."""
        if isinstance(strategy, UmaStyle):
            self.strategy = strategy
        else:
            self.strategy = UmaStyle.from_name(strategy)
        return self

    # ---------------------
    # Export / Import
    # ---------------------
    def to_template_flat(self) -> Dict[str, Any]:
        """Return the flat template keys used by other programs (template.json style)."""
        strategy_out = self.strategy.value if self.strategy else ""
        return {
            "speed": int(self.stats.get("speed", 1)),
            "stamina": int(self.stats.get("stamina", 1)),
            "power": int(self.stats.get("power", 1)),
            "guts": int(self.stats.get("guts", 1)),
            "wisdom": int(self.stats.get("wisdom", 1)),
            "strategy": strategy_out,
            "distanceAptitude": self.aptitudes["distanceAptitude"].value,
            "surfaceAptitude": self.aptitudes["surfaceAptitude"].value,
            "strategyAptitude": self.aptitudes["strategyAptitude"].value,
            "skills": list(self.skills),
        }

    def to_dict(self) -> Dict[str, Any]:
        """
        Full representation of the Uma. This is the canonical in-memory->JSON shape
        for this class. It also includes the flat template keys for external compatibility.
        """
        full = {
            "meta": {
                "name": self.name,
                "outfit_id": self.outfit_id,
                "score": self.score,
            },
            "stats": dict(self.stats),
            "aptitudes": {k: v.value for k, v in self.aptitudes.items()},
            "skills": list(self.skills),
            # Exported strategy in full object is also the Japanese romanized name or None
            "strategy": (self.strategy.value if self.strategy else None),
        }
        flat = self.to_template_flat()
        merged = {}
        merged.update(flat)
        merged.update({"uma": full})
        return merged

    def to_json(self, path: Optional[str] = None, indent: int = 2) -> str:
        """
        Serialize the Uma to JSON (same content as to_dict()).
        If path is provided, write to that file.
        """
        obj = self.to_dict()
        dump = json.dumps(obj, ensure_ascii=False, indent=indent)
        if path:
            Path(path).write_text(dump, encoding="utf-8")
        return dump

    @classmethod
    def from_template_flat(cls, data: Dict[str, Any]) -> "Uma":
        """
        Create an Uma from flat template keys only (template.json shape).
        This will create an Uma with default meta (empty name/outfit/score=0).
        """
        stats: Dict[str, int] = {}
        for k in ("speed", "stamina", "power", "guts", "wisdom"):
            if k in data:
                try:
                    stats[k] = int(data[k])
                except Exception:
                    stats[k] = 1
        aptitudes: Dict[str, str] = {}
        if "distanceAptitude" in data:
            aptitudes["distanceAptitude"] = LetterGrade.from_str(
                data["distanceAptitude"]
            ).value
        if "surfaceAptitude" in data:
            aptitudes["surfaceAptitude"] = LetterGrade.from_str(
                data["surfaceAptitude"]
            ).value
        if "strategyAptitude" in data:
            aptitudes["strategyAptitude"] = LetterGrade.from_str(
                data["strategyAptitude"]
            ).value
        skills = list(data.get("skills", []))
        strategy_raw = data.get("strategy", None)
        strategy_enum = UmaStyle.from_name(strategy_raw)
        return cls(
            stats=stats, aptitudes=aptitudes, skills=skills, strategy=strategy_enum
        )

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Uma":
        """
        Create Uma from a dictionary produced by to_dict()/to_json()
        Accepts:
          - merged format (flat template keys at root + 'uma' nested full object)
          - legacy/plain full dict (meta/stats/aptitudes at root)
          - template-flat only (fallback)
        """
        # Case 1: merged format -> 'uma' key exists
        if "uma" in data and isinstance(data["uma"], dict):
            uma_block = data["uma"]
            meta = uma_block.get("meta", {})
            name = meta.get("name", "")
            outfit = meta.get("outfit_id", "")
            score = int(meta.get("score", 0))
            stats = uma_block.get("stats", {})
            aptitudes_raw = uma_block.get("aptitudes", {})
            aptitudes = {
                k: LetterGrade.from_str(v).value for k, v in aptitudes_raw.items()
            }
            skills = uma_block.get("skills", [])
            strategy_raw = uma_block.get("strategy", None)
            strategy_enum = UmaStyle.from_name(strategy_raw)
            return cls(
                name=name,
                outfit_id=outfit,
                score=score,
                stats=stats,
                aptitudes=aptitudes,
                skills=skills,
                strategy=strategy_enum,
            )

        # Case 2: full object at root (meta/stats/aptitudes at root)
        if "meta" in data and isinstance(data["meta"], dict):
            meta = data["meta"]
            name = meta.get("name", "")
            outfit = meta.get("outfit_id", "")
            score = int(meta.get("score", 0))
            stats = data.get("stats", {})
            aptitudes_raw = data.get("aptitudes", {})
            aptitudes = {
                k: LetterGrade.from_str(v).value for k, v in aptitudes_raw.items()
            }
            skills = data.get("skills", [])
            strategy_raw = data.get("strategy", None)
            strategy_enum = UmaStyle.from_name(strategy_raw)
            return cls(
                name=name,
                outfit_id=outfit,
                score=score,
                stats=stats,
                aptitudes=aptitudes,
                skills=skills,
                strategy=strategy_enum,
            )

        # Case 3: template-flat only
        return cls.from_template_flat(data)

    @classmethod
    def from_json(cls, src: str, from_string: bool = False) -> "Uma":
        """
        Load an Uma from a JSON file path or JSON string.
        If from_string is False (default), src is treated as a file path.
        """
        if from_string:
            data = json.loads(src)
        else:
            p = Path(src)
            data = json.loads(p.read_text(encoding="utf-8"))
        return cls.from_dict(data)

    # ---------------------
    # Convenience
    # ---------------------
    def _resolve_skills(self, skills: List[Any]) -> List[int]:
        """
        Convert each item in `skills` to a valid integer skill ID,
        calling get_skill_id() when needed.
        """
        resolved = []
        skills = list(skills)
        for s in skills:
            if isinstance(s, int):
                resolved.append(s)
            else:
                skill_id = Uma.get_skill_id(str(s))
                if skill_id is not None:
                    resolved.append(skill_id)
        return resolved

    @classmethod
    def get_skill_id(cls, name: str, lang: str = "en") -> int | None:
        """
        Calls the TypeScript script via ts-node to get a skill ID from its name.
        Returns an integer skill ID, or None if the lookup fails.
        """
        try:
            print("Calling subprocess")
            result = subprocess.run(
                [
                    "npx",
                    "ts-node",
                    "../uma-skill-tools/tools/skillgrep.ts",
                    "-N",
                    name,
                    "--lang",
                    lang,
                    "-l",
                    "-d",
                ],
                capture_output=True,
                # shell=True,
                text=True,
                check=True,  # Raises CalledProcessError if exit code != 0
                timeout=5,
                cwd="uma-skill-tools",
            )
            print("subprocess done")
            # print(result.stdout)
            output = result.stdout.strip().splitlines()
            return int(output[0])  # Always take first option
        except subprocess.CalledProcessError as e:
            print(
                f"Error running skillgrep for '{name}': {e.stderr.strip() or e.stdout.strip()}"
            )
        except ValueError:
            print(
                f"Could not parse skill ID output for '{name}' — got: {result.stdout.strip()}"
            )
        except Exception as e:
            print(f"Unexpected error while fetching skill ID for '{name}': {e}")
        return None

    def as_simple_template(self) -> Dict[str, Any]:
        """Return the simple template dict (same shape as umas/template.json)."""
        return self.to_template_flat()

    def __repr__(self) -> str:
        apt = {k: v.value for k, v in self.aptitudes.items()}
        strat = self.strategy.value if self.strategy else None
        return f"<Uma name={self.name!r} outfit={self.outfit_id!r} score={self.score} stats={self.stats} aptitudes={apt} strategy={strat} skills={self.skills}>"


def main():
    Test = Uma.from_json("umas/template.json")

    Test.set_name_outfit("Mejiro Mcqueen", "[Temp]")
    Test.set_score(12000)
    Test.set_stats(
        {"speed": 1200, "stamina": 800, "power": 800, "guts": 400, "wisdom": 2}
    )

    Test.add_skills(["Corner"])


if __name__ == "__main__":
    main()
