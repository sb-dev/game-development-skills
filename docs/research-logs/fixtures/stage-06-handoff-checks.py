"""Synthetic Stage 6 contract checks; not an engine or asset-quality validator.

Run from the repository root:
    python docs/research-logs/fixtures/stage-06-handoff-checks.py

All dimensions, timing windows, names and deliveries below are invented fixtures.
"""

from copy import deepcopy
import json


def narrative(case):
    required, delivered, integration = (case[k] for k in ("required", "delivered", "integration"))
    failures = []
    if integration["event_binding"] != required["event"] or integration["event_binding"] not in delivered["events"]:
        failures.append("unknown_event_binding")
    if required["story_flag"] not in delivered["flags"]:
        failures.append("missing_story_flag")
    if integration["once"] != required["once"]:
        failures.append("wrong_repeat_policy")
    return failures


def environment(case):
    required, delivered, integration = (case[k] for k in ("required", "delivered", "integration"))
    failures = []
    if delivered["units"] != "m":
        failures.append("unresolved_units")
    opening = delivered["collision_opening_m"] * integration["uniform_scale"]
    if opening < required["actor_width_m"] + 2 * required["side_clearance_m"]:
        failures.append("insufficient_clearance")
    if required["tag"] not in delivered["tags"]:
        failures.append("missing_interaction_tag")
    return failures


def animation(case):
    required, delivered, integration = (case[k] for k in ("required", "delivered", "integration"))
    failures = []
    marker = delivered["markers_s"].get(required["event"])
    if marker is None:
        failures.append("missing_animation_event")
    elif not required["window_s"][0] <= marker / integration["playback_rate"] <= required["window_s"][1]:
        failures.append("event_outside_window")
    if integration["motion_owner"] != required["motion_owner"] or (delivered["root_motion"] and integration["motion_owner"] == "controller"):
        failures.append("movement_ownership_conflict")
    return failures


def audio(case):
    required, delivered, integration = (case[k] for k in ("required", "delivered", "integration"))
    failures = []
    if any(integration["mix_map"].get(state) not in delivered["mix_states"] for state in required["states"]):
        failures.append("unknown_mix_state")
    if required["cue"] not in delivered["cues"] or integration["trigger_map"].get("hazard") != required["cue"]:
        failures.append("missing_feedback_binding")
    return failures


CASES = {
    "narrative": {
        "required": {"event": "door_open", "story_flag": "met_guard", "once": True},
        "delivered": {"events": ["door_open"], "flags": ["met_guard"]},
        "integration": {"event_binding": "door_open", "once": True},
    },
    "environment": {
        "required": {"actor_width_m": 1.0, "side_clearance_m": 0.1, "tag": "traversable"},
        "delivered": {"collision_opening_m": 1.3, "units": "m", "tags": ["traversable"]},
        "integration": {"uniform_scale": 1.0},
    },
    "animation": {
        "required": {"event": "strike", "window_s": [0.25, 0.4], "motion_owner": "controller"},
        "delivered": {"markers_s": {"strike": 0.3}, "root_motion": False},
        "integration": {"playback_rate": 1.0, "motion_owner": "controller"},
    },
    "music_audio": {
        "required": {"states": ["explore", "alert"], "cue": "warning"},
        "delivered": {"mix_states": ["Explore", "Threat"], "cues": ["warning"]},
        "integration": {"mix_map": {"explore": "Explore", "alert": "Threat"}, "trigger_map": {"hazard": "warning"}},
    },
}

CHECKS = {"narrative": narrative, "environment": environment, "animation": animation, "music_audio": audio}
MUTATIONS = {
    "narrative": (("integration", "event_binding"), "GateOpen", "unknown_event_binding", "gameplay integration"),
    "environment": (("integration", "uniform_scale"), 0.5, "insufficient_clearance", "gameplay/import integration"),
    "animation": (("delivered", "markers_s", "strike"), 0.6, "event_outside_window", "animation producer"),
    "music_audio": (("integration", "mix_map", "alert"), "Danger", "unknown_mix_state", "gameplay/audio integration"),
}


def main():
    results = []
    for name, original in CASES.items():
        check = CHECKS[name]
        assert check(original) == [], name
        path, invalid, expected, owner = MUTATIONS[name]
        defective = deepcopy(original)
        destination, source = defective, original
        for part in path[:-1]:
            destination, source = destination[part], source[part]
        destination[path[-1]] = invalid
        failures = check(defective)
        assert failures == [expected], (name, failures)
        repaired = deepcopy(defective)
        destination = repaired
        for part in path[:-1]:
            destination = destination[part]
        destination[path[-1]] = deepcopy(source[path[-1]])
        assert check(repaired) == [], name
        assert original["required"] == defective["required"] == repaired["required"], name
        assert repaired == original, "Repair changed unrelated fixture data"
        results.append({"pattern": name, "baseline": "ACCEPT", "defect": "REJECT", "diagnostic": expected,
                        "repair": "ACCEPT", "repair_owner": owner, "requirements_preserved": True})
    print(json.dumps({"scope": "synthetic contract predicates only", "status": "PASS",
                      "patterns": len(results), "evaluations": len(results) * 3,
                      "runtime_or_perceptual_validation": False, "results": results}, indent=2))


if __name__ == "__main__":
    main()
