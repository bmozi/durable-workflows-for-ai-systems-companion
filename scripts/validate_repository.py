#!/usr/bin/env python3
"""Validate the companion repository's reader routes and local links."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "companion.json"
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
COMMIT_PATTERN = re.compile(r"^[0-9a-f]{7,40}$")
CHECKSUM_PATTERN = re.compile(r"^([0-9a-f]{64})  (.+)$")
FREEZE_ORDER = ["complete", "manifest", "verify", "record"]
PRIOR_TRIPLE = ["governed_outputs", "governing_manifest", "detached_record"]
DETACHED_RECORD_FIELDS = [
    "attempt_id",
    "phase",
    "facilitator_actor_code",
    "manifest_verification_command",
    "manifest_verification_stdout",
    "manifest_verification_stderr",
    "manifest_verification_exit_status",
    "manifest_verification_timestamp",
    "manifest_verification_timezone",
    "governing_manifest_filename",
    "governing_manifest_sha256",
    "governed_output_inventory",
    "record_completion_timestamp",
    "record_completion_timezone",
]
SEALED_STAGED_INPUTS = {
    "stage_a_initial": [
        "00-packet-route.md",
        "02-scenario-and-task.md",
        "03-practitioner-workbook.md",
        "START-HERE.md",
        "workflow-responsibility-and-progress-brief.md",
        "compensation-and-failure-matrix.md",
        "time-and-failure-test-plan.md",
    ],
    "stage_a_revised_record": ["06-revised-artifact-freeze-record.md"],
    "initial_to_live_update": [
        "WF-A-INITIAL-PRACTITIONER-WORKBOOK-v1.md",
        "WF-A-INITIAL-WORKFLOW-RESPONSIBILITY-AND-PROGRESS-BRIEF-v1.md",
        "WF-A-INITIAL-COMPENSATION-AND-FAILURE-MATRIX-v1.md",
        "WF-A-INITIAL-TIME-AND-FAILURE-TEST-PLAN-v1.md",
        "WF-A-INITIAL-ARTIFACTS-SHA256SUMS-v1.txt",
        "WF-A-INITIAL-FREEZE-VERIFICATION-RECORD-v1.md",
        "WF-A-LIVE-UPDATE-v1.md",
    ],
    "revised_to_handoff": [
        "WF-A-REVISED-PRACTITIONER-WORKBOOK-v1.md",
        "WF-A-REVISED-WORKFLOW-RESPONSIBILITY-AND-PROGRESS-BRIEF-v1.md",
        "WF-A-REVISED-COMPENSATION-AND-FAILURE-MATRIX-v1.md",
        "WF-A-REVISED-TIME-AND-FAILURE-TEST-PLAN-v1.md",
        "WF-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt",
        "WF-A-REVISED-FREEZE-RECORD-v1.md",
        "05-one-screen-handoff.md",
    ],
    "handoff_to_stage_b_section_1": [
        "WF-A-ONE-SCREEN-HANDOFF-v1.md",
        "WF-A-HANDOFF-SHA256SUMS-v1.txt",
        "WF-A-HANDOFF-FREEZE-VERIFICATION-RECORD-v1.md",
        "00-packet-route.md",
        "04-decision-owner-workbook.md",
    ],
    "section_1_to_section_2": [
        "WF-B-SECTION-1-v1.md",
        "WF-B-SECTION-1-SHA256SUMS-v1.txt",
        "WF-B-SECTION-1-FREEZE-VERIFICATION-RECORD-v1.md",
        "02-scenario-and-task.md",
        "WF-A-REVISED-PRACTITIONER-WORKBOOK-v1.md",
        "WF-A-REVISED-WORKFLOW-RESPONSIBILITY-AND-PROGRESS-BRIEF-v1.md",
        "WF-A-REVISED-COMPENSATION-AND-FAILURE-MATRIX-v1.md",
        "WF-A-REVISED-TIME-AND-FAILURE-TEST-PLAN-v1.md",
        "WF-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt",
        "WF-A-REVISED-FREEZE-RECORD-v1.md",
    ],
    "section_2_to_sections_3_5": [
        "WF-B-SECTION-2-v1.md",
        "WF-B-SECTION-2-SHA256SUMS-v1.txt",
        "WF-B-SECTION-2-FREEZE-VERIFICATION-RECORD-v1.md",
        "EXECUTIVE-DECISION-BRIEF.md",
        "VALUE-AND-EVIDENCE-LEDGER.md",
    ],
    "sections_3_5_to_debrief": [
        "WF-B-SECTIONS-3-5-v1.md",
        "WF-B-SECTIONS-3-5-SHA256SUMS-v1.txt",
        "WF-B-SECTIONS-3-5-FREEZE-VERIFICATION-RECORD-v1.md",
        "07-stage-b-section-6-debrief.md",
    ],
}
ENTRY_INPUTS = {
    "stage_a_human": ["WF-A-HUMAN-CONSENT-<attempt-id>-v1.md"],
    "stage_a_synthetic": ["WF-SYNTHETIC-CONTEXT-<attempt-id>-v1.md"],
    "stage_b_human": ["WF-B-HUMAN-CONSENT-<attempt-id>-v1.md"],
    "stage_b_synthetic": ["WF-SYNTHETIC-CONTEXT-<attempt-id>-v1.md"],
}
ACCESS_LOG_FIELDS = [
    "event_id",
    "sequence",
    "attempt_id",
    "stage",
    "phase",
    "event_type",
    "actor_code",
    "exact_filename",
    "timestamp",
    "timezone",
    "result",
    "prior_event_id",
    "prior_event_sha256",
    "notes",
]
ACCESS_LOG_EVENTS = [
    "entry_branch_selected",
    "run_log_started",
    "entry_context_record_completed",
    "stage_a_started",
    "sealed_input_manifest_created",
    "sealed_input_manifest_verified",
    "participant_file_released",
    "participant_file_opened",
    "participant_file_read_completed",
    "governed_artifact_completed",
    "governing_manifest_created",
    "governing_manifest_verified",
    "detached_record_completed",
    "handoff_layout_proof_completed",
    "stage_a_material_feedback_completed",
    "stage_a_ended",
    "stage_b_started",
    "phase_input_manifest_created",
    "phase_input_manifest_verified",
    "stage_b_scoring_ended",
    "stage_b_section_6_debrief_completed",
    "stage_b_ended",
    "run_results_completed",
    "deviation_recorded",
    "stop_recorded",
    "run_log_closed",
]
ACCESS_LOG_COMPLETE_EVENTS = [
    event for event in ACCESS_LOG_EVENTS
    if event not in {"deviation_recorded", "stop_recorded"}
]
ACCESS_LOG_ORDER_RULES = [
    "input_manifest_created_before_verified",
    "input_manifest_verified_before_release_open_read",
    "each_file_release_before_open_before_read_complete",
    "artifact_complete_before_governing_manifest_created",
    "governing_manifest_created_before_verified",
    "governing_manifest_verified_before_detached_record_completed",
    "detached_record_timestamp_strictly_after_verification",
    "detached_record_completed_before_next_phase_manifest_created",
    "next_phase_manifest_verified_before_next_release_open_read",
    "entry_branch_selected_first_then_run_log_started",
    "selected_entry_context_verified_before_stage_start",
    "stage_a_ended_after_material_feedback",
    "stage_b_scoring_ended_before_debrief",
    "stage_b_ended_after_debrief",
    "run_results_completed_after_stage_b_ended_before_run_log_closed",
]
PHASE_PROTOCOL = {
    "stage_a_initial": {
        "results_label": "Initial Stage A",
        "state": "INITIAL COMPLETE",
        "manifest": "WF-A-INITIAL-ARTIFACTS-SHA256SUMS-v1.txt",
        "record": "WF-A-INITIAL-FREEZE-VERIFICATION-RECORD-v1.md",
        "next_release": "initial_to_live_update",
        "output": None,
        "outputs": [
            "WF-A-INITIAL-PRACTITIONER-WORKBOOK-v1.md",
            "WF-A-INITIAL-WORKFLOW-RESPONSIBILITY-AND-PROGRESS-BRIEF-v1.md",
            "WF-A-INITIAL-COMPENSATION-AND-FAILURE-MATRIX-v1.md",
            "WF-A-INITIAL-TIME-AND-FAILURE-TEST-PLAN-v1.md",
        ],
    },
    "stage_a_revised": {
        "results_label": "Revised Stage A",
        "state": "REVISED COMPLETE",
        "manifest": "WF-A-REVISED-ARTIFACTS-SHA256SUMS-v1.txt",
        "record": "WF-A-REVISED-FREEZE-RECORD-v1.md",
        "next_release": "revised_to_handoff",
        "output": None,
        "outputs": [
            "WF-A-REVISED-PRACTITIONER-WORKBOOK-v1.md",
            "WF-A-REVISED-WORKFLOW-RESPONSIBILITY-AND-PROGRESS-BRIEF-v1.md",
            "WF-A-REVISED-COMPENSATION-AND-FAILURE-MATRIX-v1.md",
            "WF-A-REVISED-TIME-AND-FAILURE-TEST-PLAN-v1.md",
        ],
    },
    "stage_a_handoff": {
        "results_label": "Handoff",
        "state": "HANDOFF COMPLETE",
        "manifest": "WF-A-HANDOFF-SHA256SUMS-v1.txt",
        "record": "WF-A-HANDOFF-FREEZE-VERIFICATION-RECORD-v1.md",
        "next_release": "handoff_to_stage_b_section_1",
        "output": ("WF-A-ONE-SCREEN-HANDOFF", "1", "WF-A-ONE-SCREEN-HANDOFF-v1.md"),
        "outputs": ["WF-A-ONE-SCREEN-HANDOFF-v1.md"],
    },
    "stage_b_section_1": {
        "results_label": "Stage B Section 1",
        "state": "SECTION 1 COMPLETE",
        "manifest": "WF-B-SECTION-1-SHA256SUMS-v1.txt",
        "record": "WF-B-SECTION-1-FREEZE-VERIFICATION-RECORD-v1.md",
        "next_release": "section_1_to_section_2",
        "output": ("WF-B-SECTION-1", "1", "WF-B-SECTION-1-v1.md"),
        "outputs": ["WF-B-SECTION-1-v1.md"],
    },
    "stage_b_section_2": {
        "results_label": "Stage B Section 2",
        "state": "SECTION 2 COMPLETE",
        "manifest": "WF-B-SECTION-2-SHA256SUMS-v1.txt",
        "record": "WF-B-SECTION-2-FREEZE-VERIFICATION-RECORD-v1.md",
        "next_release": "section_2_to_sections_3_5",
        "output": ("WF-B-SECTION-2", "1", "WF-B-SECTION-2-v1.md"),
        "outputs": ["WF-B-SECTION-2-v1.md"],
    },
    "stage_b_sections_3_5": {
        "results_label": "Stage B Sections 3-5",
        "state": "SECTIONS 3-5 COMPLETE",
        "manifest": "WF-B-SECTIONS-3-5-SHA256SUMS-v1.txt",
        "record": "WF-B-SECTIONS-3-5-FREEZE-VERIFICATION-RECORD-v1.md",
        "next_release": "sections_3_5_to_debrief",
        "output": ("WF-B-SECTIONS-3-5", "1", "WF-B-SECTIONS-3-5-v1.md"),
        "outputs": ["WF-B-SECTIONS-3-5-v1.md"],
    },
}
RELEASE_PROTOCOL = {
    "initial_to_live_update": {
        "from_phase": "stage_a_initial",
        "manifest": "WF-A-LIVE-UPDATE-INPUT-SHA256SUMS-v1.txt",
        "new_inputs": ["live_update"],
    },
    "revised_to_handoff": {
        "from_phase": "stage_a_revised",
        "manifest": "WF-A-HANDOFF-INPUT-SHA256SUMS-v1.txt",
        "new_inputs": ["blank_handoff"],
    },
    "handoff_to_stage_b_section_1": {
        "from_phase": "stage_a_handoff",
        "manifest": "WF-B-PHASE-1-INPUT-SHA256SUMS-v1.txt",
        "new_inputs": ["packet_route", "blank_decision_owner_workbook"],
    },
    "section_1_to_section_2": {
        "from_phase": "stage_b_section_1",
        "manifest": "WF-B-PHASE-2-INPUT-SHA256SUMS-v1.txt",
        "new_inputs": [
            "scenario",
            "revised_governed_outputs",
            "revised_governing_manifest",
            "revised_detached_record",
        ],
    },
    "section_2_to_sections_3_5": {
        "from_phase": "stage_b_section_2",
        "manifest": "WF-B-PHASE-3-INPUT-SHA256SUMS-v1.txt",
        "new_inputs": ["executive_decision_brief", "value_and_evidence_ledger"],
    },
    "sections_3_5_to_debrief": {
        "from_phase": "stage_b_sections_3_5",
        "manifest": "WF-B-DEBRIEF-INPUT-SHA256SUMS-v1.txt",
        "new_inputs": ["section_6_debrief_template"],
    },
}
CORRECTION_REQUIREMENTS = {
    "preserve_prior_chain": True,
    "new_filename": True,
    "new_artifact_id": True,
    "new_version": True,
    "new_completion_timestamp": True,
    "new_governing_manifest": True,
    "new_verification_event": True,
    "new_detached_record": True,
    "new_next_release_manifest_when_applicable": True,
    "stop_current_attempt": True,
}
BINDING_DOCUMENTS = {
    "WF-A-ONE-SCREEN-HANDOFF": {
        "README.md",
        "participant/00-packet-route.md",
        "participant/05-one-screen-handoff.md",
    },
    "WF-B-SECTION-1": {
        "participant/00-packet-route.md",
        "participant/04-decision-owner-workbook.md",
    },
    "WF-B-SECTION-2": {
        "participant/00-packet-route.md",
        "participant/04-decision-owner-workbook.md",
    },
    "WF-B-SECTIONS-3-5": {
        "participant/00-packet-route.md",
        "participant/04-decision-owner-workbook.md",
    },
}
ENTRY_BRANCH_CONTRACT = {
    "selection": "exactly_one",
    "selection_event": "entry_branch_selected",
    "selection_is_first_semantic_log_event": True,
    "run_log_started_immediately_after_selection": True,
    "selection_before_scored_input": True,
    "branch_mixing_stops_attempt": True,
    "human": {
        "template": "participant/01-consent-and-privacy.md",
        "stage_a_record_pattern": "WF-A-HUMAN-CONSENT-<attempt-id>-v1.md",
        "stage_b_record_pattern": "WF-B-HUMAN-CONSENT-<attempt-id>-v1.md",
        "stage_a_manifest_pattern": "WF-A-HUMAN-CONTEXT-<attempt-id>-SHA256SUMS-v1.txt",
        "stage_b_manifest_pattern": "WF-B-HUMAN-CONTEXT-<attempt-id>-SHA256SUMS-v1.txt",
        "required_state": "HUMAN CONSENT COMPLETE",
        "synthetic_context_forbidden": True,
    },
    "synthetic": {
        "template": "facilitator-only/06-synthetic-context-record-template.md",
        "record_pattern": "WF-SYNTHETIC-CONTEXT-<attempt-id>-v1.md",
        "manifest_pattern": "WF-SYNTHETIC-CONTEXT-<attempt-id>-SHA256SUMS-v1.txt",
        "required_identity_statement": "SYNTHETIC — NO HUMAN PARTICIPANT OR HUMAN DATA",
        "required_state": "SYNTHETIC CONTEXT COMPLETE",
        "human_consent_record_forbidden": True,
        "human_result_claims_forbidden": [
            "human consent obtained",
            "participant consented",
            "human comprehension passed",
            "human usability passed",
            "practitioner result observed",
        ],
    },
    "stage_context_gates": {
        "stage_a": "selected_branch_record_and_manifest_verified_before_stage_a_started",
        "stage_b": "same_selected_branch_record_and_manifest_verified_before_stage_b_started",
    },
}
FULL_ROUTE_CONTRACT = {
    "scored_freeze_chain_ids": list(PHASE_PROTOCOL),
    "six_scored_freezes_are_full_route_closure": False,
    "required_boundary_order": [
        "entry_branch_selected", "run_log_started", "entry_context_record_completed",
        "stage_a_started", "stage_a_initial", "stage_a_revised", "stage_a_handoff",
        "handoff_layout_proof_completed", "stage_a_material_feedback_completed",
        "stage_a_ended", "stage_b_started", "stage_b_section_1", "stage_b_section_2",
        "stage_b_sections_3_5", "stage_b_scoring_ended",
        "stage_b_section_6_debrief_completed", "stage_b_ended",
        "run_results_completed", "run_log_closed",
    ],
    "premature_log_close_forbidden": True,
}
DEBRIEF_CONTRACT = {
    "template": "participant/07-stage-b-section-6-debrief.md",
    "input_manifest": "WF-B-DEBRIEF-INPUT-SHA256SUMS-v1.txt",
    "output_filename": "WF-B-SECTION-6-DEBRIEF-v1.md",
    "required_state": "SECTION 6 DEBRIEF COMPLETE",
    "completion_event": "stage_b_section_6_debrief_completed",
    "after_event": "stage_b_scoring_ended",
    "retroactive_score_or_artifact_change_forbidden": True,
}
RUN_RESULTS_CONTRACT = {
    "template": "facilitator-only/03-results-and-deviation-log.md",
    "filename_pattern": "WF-RUN-RESULTS-AND-DEVIATIONS-<attempt-id>-v1.md",
    "required_state": "RUN RESULTS COMPLETE",
    "completion_event": "run_results_completed",
    "after_event": "stage_b_ended",
    "before_event": "run_log_closed",
    "immutable_before_log_close": True,
    "final_pre_results_checkpoint_required": True,
    "forbidden_fields": [
        "final_closed_log_sha256", "predicted_future_log_hash",
        "predicted_future_closeout_timestamp",
    ],
}
EXTERNAL_CLOSEOUT_CONTRACT = {
    "template": "facilitator-only/08-external-closeout-record-template.md",
    "filename_pattern": "WF-EXTERNAL-CLOSEOUT-<attempt-id>-v1.md",
    "required_state": "EXTERNAL CLOSEOUT COMPLETE",
    "after_event": "run_log_closed",
    "binds_results_sha256": True,
    "binds_closed_log_sha256": True,
    "binds_external_manifest_sha256": True,
    "external_to_closed_log": True,
}
LAYOUT_PROOF_CONTRACT = {
    "handoff_markdown": "WF-A-ONE-SCREEN-HANDOFF-v1.md",
    "handoff_pdf": "WF-A-ONE-SCREEN-HANDOFF-v1.pdf",
    "proof_template": "facilitator-only/07-handoff-layout-proof-record-template.md",
    "proof_filename_pattern": "WF-A-HANDOFF-LAYOUT-PROOF-<attempt-id>-v1.md",
    "completion_event": "handoff_layout_proof_completed",
    "page_count": 1,
    "page_size": "US Letter portrait",
    "minimum_margin_inches": 0.5,
    "minimum_font_points": 9,
    "maximum_reader_facing_words_excluding_labeled_provenance": 450,
    "clipping_forbidden": True,
    "overlap_forbidden": True,
    "favorable_one_page_claim_requires_pass_proof": True,
    "human_comprehension_evidence": False,
}
SEMANTIC_TRANSFER_CONTRACT = {
    "source_artifact": "WF-A-ONE-SCREEN-HANDOFF-v1.md",
    "target_artifact": "WF-B-SECTION-1-v1.md",
    "preserve_or_attribute_source_business_domain_nouns": True,
    "unsupported_business_domain_noun_invention_rejected": True,
    "affected_score_when_invented": 0,
    "permanent_regression_fixture": {
        "source_text": "First contractor request timed out after API receipt/acceptance.",
        "candidate_text": "A timed-out first billing request after receipt/acceptance.",
        "unsupported_noun": "billing",
        "expected_result": "REJECT",
    },
}
EVIDENCE_STATE_CONTRACT = {
    "human_pilot": "PREPARED/UNRUN",
    "human_comprehension": "UNRUN",
    "real_world": "UNRUN",
    "synthetic_may_not_upgrade_human_or_real_world_state": True,
}


def markdown_links(path: Path):
    in_fence = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.lstrip()
        if stripped.startswith(chr(96) * 3) or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in LINK_PATTERN.finditer(line):
            yield number, match.group(1).strip()


def local_target(source: Path, raw: str) -> Path | None:
    target = raw
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(" ", 1)[0]
    parsed = urlsplit(target)
    if parsed.scheme or target.startswith("//") or target.startswith("#"):
        return None
    decoded = unquote(parsed.path)
    if not decoded:
        return None
    if decoded.startswith("/"):
        raise ValueError("absolute local path")
    resolved = (source.parent / decoded).resolve()
    try:
        resolved.relative_to(ROOT)
    except ValueError as exc:
        raise ValueError("link escapes repository") from exc
    return resolved


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_temporal_freeze_protocol(errors: list[str]) -> None:
    """Validate the canonical v1.2.5 freeze, release, and closure graph."""
    packet = ROOT / "testing" / "workflows-reader-value-v1"
    protocol_path = packet / "TEMPORAL-FREEZE-PROTOCOL.json"
    try:
        protocol = json.loads(protocol_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"temporal protocol inventory is unreadable: {exc}")
        return

    if protocol.get("schema_version") != 3:
        errors.append("temporal protocol: schema_version must be 3")
    if protocol.get("packet_id") != "WF-RV-PILOT-001":
        errors.append("temporal protocol: packet_id mismatch")
    if protocol.get("packet_version") != "1.2.5":
        errors.append("temporal protocol: packet_version must be 1.2.5")

    if protocol.get("entry_branch_contract") != ENTRY_BRANCH_CONTRACT:
        errors.append("temporal protocol: exactly-one entry branch or synthetic claim boundary mismatch")

    expected_record_schema = {
        "required_fields": DETACHED_RECORD_FIELDS,
        "success_exit_status": 0,
        "observed_output_required": True,
        "record_completion_relation": "strictly_after_manifest_verification",
        "record_excluded_from_described_manifest": True,
    }
    if protocol.get("detached_record_schema") != expected_record_schema:
        errors.append(
            "temporal protocol: detached-record required fields and completion relation are incomplete"
        )

    expected_input_policy = {
        "flat_phase_directories": True,
        "exact_declared_membership_required": True,
        "undeclared_files_forbidden": True,
        "forbidden_filenames": ["ORCHESTRATION.md"],
        "hidden_or_generated_instructions_forbidden": True,
        "facilitator_execution_log_participant_input": False,
        "declared_staged_inputs": SEALED_STAGED_INPUTS,
        "declared_entry_inputs": ENTRY_INPUTS,
    }
    if protocol.get("sealed_participant_input_policy") != expected_input_policy:
        errors.append(
            "temporal protocol: sealed participant input inventory or isolation policy mismatch"
        )

    expected_access_log = {
        "filename_pattern": "WF-RUN-EXECUTION-ACCESS-LOG-<attempt-id>.jsonl",
        "participant_input": False,
        "required_fields": ACCESS_LOG_FIELDS,
        "event_type_inventory": ACCESS_LOG_EVENTS,
        "required_event_types_for_unstopped_complete_attempt": ACCESS_LOG_COMPLETE_EVENTS,
        "conditional_event_types": ["deviation_recorded", "stop_recorded"],
        "continuity": {
            "sequence_starts_at": 1,
            "sequence_increment": 1,
            "unique_event_id": True,
            "constant_attempt_id": True,
            "first_prior_binding": "GENESIS",
            "later_prior_event_id_required": True,
            "later_prior_event_sha256_required": True,
            "timestamps_non_decreasing": True,
            "closed_log_external_manifest_required": True,
        },
        "event_order_rules": ACCESS_LOG_ORDER_RULES,
        "verification_event_notes_require": [
            "literal_command",
            "observed_stdout",
            "observed_stderr",
            "integer_exit_status",
        ],
    }
    if protocol.get("facilitator_execution_access_log") != expected_access_log:
        errors.append(
            "temporal protocol: facilitator access-log schema or continuity is incomplete"
        )

    expected_states = [entry["state"] for entry in PHASE_PROTOCOL.values()]
    if protocol.get("allowed_completion_states") != expected_states:
        errors.append("temporal protocol: allowed completion states are incomplete or stale")

    chains = protocol.get("freeze_chains")
    if not isinstance(chains, list):
        errors.append("temporal protocol: freeze_chains must be a list")
        chains = []
    chain_by_id = {
        entry.get("id"): entry for entry in chains if isinstance(entry, dict)
    }
    if len(chain_by_id) != len(chains) or set(chain_by_id) != set(PHASE_PROTOCOL):
        errors.append("temporal protocol: freeze inventory must contain each of six phases exactly once")
    for phase, expected in PHASE_PROTOCOL.items():
        chain = chain_by_id.get(phase)
        if chain is None:
            continue
        checks = {
            "results_label": expected["results_label"],
            "output_role": "governed_outputs",
            "completion_state": expected["state"],
            "governing_manifest": expected["manifest"],
            "detached_record": expected["record"],
            "order": FREEZE_ORDER,
            "manifest_membership": ["governed_outputs"],
            "manifest_exclusions": ["governing_manifest", "detached_record"],
            "next_release": expected["next_release"],
            "governed_output_filenames": expected["outputs"],
        }
        for field, wanted in checks.items():
            if chain.get(field) != wanted:
                errors.append(f"temporal protocol: {phase}.{field} must equal {wanted!r}")
        output = expected["output"]
        actual_output = (
            chain.get("output_artifact_id"),
            chain.get("output_version"),
            chain.get("output_filename"),
        )
        if output is None:
            if actual_output != (None, None, None):
                errors.append(f"temporal protocol: {phase} must use the governed-output set")
        elif actual_output != output:
            errors.append(f"temporal protocol: {phase} artifact ID/version/filename mismatch")

    releases = protocol.get("release_triples")
    if not isinstance(releases, list):
        errors.append("temporal protocol: release_triples must be a list")
        releases = []
    release_by_id = {
        entry.get("id"): entry for entry in releases if isinstance(entry, dict)
    }
    if len(release_by_id) != len(releases) or set(release_by_id) != set(RELEASE_PROTOCOL):
        errors.append("temporal protocol: release inventory must contain each of six releases exactly once")
    for release_id, expected in RELEASE_PROTOCOL.items():
        release = release_by_id.get(release_id)
        if release is None:
            continue
        if release.get("from_phase") != expected["from_phase"]:
            errors.append(f"temporal protocol: {release_id} has the wrong predecessor")
        if release.get("manifest") != expected["manifest"]:
            errors.append(f"temporal protocol: {release_id} manifest filename mismatch")
        if release.get("required_prior_bundle") != PRIOR_TRIPLE:
            errors.append(f"temporal protocol: {release_id} must bind the completed triple")
        if release.get("new_inputs") != expected["new_inputs"]:
            errors.append(f"temporal protocol: {release_id} new-input inventory mismatch")
        exact_membership = PRIOR_TRIPLE + expected["new_inputs"]
        if release.get("exact_membership") != exact_membership:
            errors.append(f"temporal protocol: {release_id} exact membership mismatch")

    if protocol.get("correction_requirements") != CORRECTION_REQUIREMENTS:
        errors.append("temporal protocol: immutable correction requirements are incomplete")
    if protocol.get("results_inventory") != list(PHASE_PROTOCOL):
        errors.append("temporal protocol: results inventory must list all six phases in order")

    closure_contracts = {
        "full_route_contract": FULL_ROUTE_CONTRACT,
        "debrief_contract": DEBRIEF_CONTRACT,
        "run_results_contract": RUN_RESULTS_CONTRACT,
        "external_closeout_contract": EXTERNAL_CLOSEOUT_CONTRACT,
        "layout_proof_contract": LAYOUT_PROOF_CONTRACT,
        "semantic_transfer_contract": SEMANTIC_TRANSFER_CONTRACT,
        "evidence_state_contract": EVIDENCE_STATE_CONTRACT,
    }
    for name, expected in closure_contracts.items():
        if protocol.get(name) != expected:
            errors.append(f"temporal protocol: {name} mismatch")

    bindings = protocol.get("artifact_bindings")
    if not isinstance(bindings, list):
        errors.append("temporal protocol: artifact_bindings must be a list")
        bindings = []
    binding_by_id = {
        entry.get("artifact_id"): entry for entry in bindings if isinstance(entry, dict)
    }
    expected_outputs = {
        value["output"][0]: value["output"]
        for value in PHASE_PROTOCOL.values()
        if value["output"] is not None
    }
    if len(binding_by_id) != len(bindings) or set(binding_by_id) != set(expected_outputs):
        errors.append("temporal protocol: artifact binding inventory mismatch")
    for artifact_id, expected in expected_outputs.items():
        binding = binding_by_id.get(artifact_id)
        if binding is None:
            continue
        wanted_documents = BINDING_DOCUMENTS[artifact_id]
        if (
            binding.get("version"),
            binding.get("filename"),
        ) != (expected[1], expected[2]):
            errors.append(f"temporal protocol: {artifact_id} version/filename mismatch")
        documents = binding.get("documents")
        if not isinstance(documents, list) or set(documents) != wanted_documents:
            errors.append(f"temporal protocol: {artifact_id} document binding mismatch")
            continue
        variant = re.compile(rf"{re.escape(artifact_id)}-v([0-9]+)\.md")
        for relative in documents:
            path = packet / relative
            if not path.is_file():
                errors.append(f"temporal protocol: missing binding document {relative}")
                continue
            content = path.read_text(encoding="utf-8")
            if expected[2] not in content:
                errors.append(f"temporal protocol: {relative} omits {expected[2]}")
            wrong_versions = {match.group(1) for match in variant.finditer(content)} - {expected[1]}
            if wrong_versions:
                errors.append(f"temporal protocol: {relative} has stale {artifact_id} versions")

    results_path = packet / "facilitator-only" / "03-results-and-deviation-log.md"
    try:
        results_text = results_path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"temporal protocol: results inventory is unreadable: {exc}")
    else:
        section = results_text.split("## Temporal freeze chain", 1)
        section = section[1].split("\n## ", 1)[0] if len(section) == 2 else ""
        rows = []
        for line in section.splitlines():
            if not line.startswith("|") or line.startswith("| ---"):
                continue
            label = line.split("|", 2)[1].strip()
            if label and label != "Output phase":
                rows.append(label)
        expected_rows = [entry["results_label"] for entry in PHASE_PROTOCOL.values()]
        if rows != expected_rows or len(rows) != 6:
            errors.append("temporal protocol: results log must contain all six freeze rows in order")

    handoff_path = packet / "participant" / "05-one-screen-handoff.md"
    handoff_text = handoff_path.read_text(encoding="utf-8") if handoff_path.is_file() else ""
    state_rows = [
        line for line in handoff_text.splitlines()
        if line.startswith("| Handoff state before hashing |")
    ]
    if state_rows != ["| Handoff state before hashing | `HANDOFF COMPLETE` / invalid |"]:
        errors.append("temporal protocol: handoff state field must require HANDOFF COMPLETE")

    semantic_requirements = {
        "README.md": [
            "An undeclared file fails the release.",
            "`ORCHESTRATION.md`",
            "observed standard output and standard error",
            "own later exact completion timestamp/timezone",
            "SYNTHETIC — NO HUMAN PARTICIPANT OR HUMAN DATA",
            "six scored freeze chains",
            "US Letter",
            "450",
            "`entry_branch_selected` -> `run_log_started`",
        ],
        "participant/00-packet-route.md": [
            "An undeclared hidden prompt",
            "facilitator/actor code",
            "integer exit status",
            "record's own later completion timestamp and timezone",
            "WF-B-DEBRIEF-INPUT-SHA256SUMS-v1.txt",
            "WF-RUN-RESULTS-AND-DEVIATIONS-<attempt-id>-v1.md",
            "unsupported",
            "`entry_branch_selected` -> `run_log_started`",
        ],
        "participant/06-revised-artifact-freeze-record.md": [
            "- Attempt ID:",
            "- Phase: `stage_a_revised` / invalid",
            "- Facilitator/actor code:",
            "- Literal manifest verification command:",
            "- Observed standard output, verbatim:",
            "- Observed standard error, verbatim; write `(empty)` when empty:",
            "- Integer exit status:",
            "- Manifest verification timestamp:",
            "- Manifest verification timezone:",
            "- Detached record completion timestamp:",
            "- Detached record completion timezone:",
        ],
        "facilitator-only/01-facilitator-guide.md": [
            "Never add `ORCHESTRATION.md`",
            "Create the separate facilitator-only JSONL execution/access log",
            "observed standard output and standard error",
            "own later exact completion timestamp and timezone",
            "`entry_branch_selected` -> `run_log_started`",
        ],
        "facilitator-only/02-observation-and-scoring-rubric.md": [
            "| Declared-input isolation |",
            "| Execution/access continuity |",
        ],
        "facilitator-only/03-results-and-deviation-log.md": [
            "## Facilitator execution/access log identity",
            "literal command, observed standard output and standard error",
            "own later completion timestamp/timezone",
            "`entry_branch_selected` -> `run_log_started`",
        ],
        "facilitator-only/04-freeze-and-correction-record-templates.md": [
            "- literal manifest-verification command;",
            "- observed standard output, verbatim;",
            "- integer exit status;",
            "A record without its own later completion timestamp and timezone is incomplete.",
            "`entry_branch_selected` -> `run_log_started`",
        ],
        "facilitator-only/05-run-execution-and-access-log-schema.md": [
            "Keep it outside every sealed participant-input directory.",
            "`participant_file_read_completed`",
            "`prior_event_sha256`",
            "`run_log_closed`",
            "observed standard error (write `(empty)` when it was empty)",
            "`stage_a_started`",
            "`stage_a_ended`",
            "`stage_b_scoring_ended`",
            "`run_results_completed`",
            "`entry_branch_selected` -> `run_log_started`",
        ],
        "facilitator-only/06-synthetic-context-record-template.md": [
            "SYNTHETIC — NO HUMAN PARTICIPANT OR HUMAN DATA",
            "SYNTHETIC CONTEXT COMPLETE",
            "Human consent",
        ],
        "facilitator-only/07-handoff-layout-proof-record-template.md": [
            "US Letter portrait",
            "0.5",
            "9 points",
            "450",
            "Layout proof is not comprehension evidence.",
        ],
        "facilitator-only/08-external-closeout-record-template.md": [
            "EXTERNAL CLOSEOUT COMPLETE",
            "Active closed-log SHA-256",
            "Run-results SHA-256",
        ],
        "participant/07-stage-b-section-6-debrief.md": [
            "WF-B-DEBRIEF-INPUT-SHA256SUMS-v1.txt",
            "WF-B-SECTION-6-DEBRIEF-v1.md",
            "SECTION 6 DEBRIEF COMPLETE",
        ],
    }
    for relative, snippets in semantic_requirements.items():
        path = packet / relative
        if not path.is_file():
            errors.append(f"temporal protocol: missing required protocol document {relative}")
            continue
        normalized = " ".join(path.read_text(encoding="utf-8").split())
        for snippet in snippets:
            if " ".join(snippet.split()) not in normalized:
                errors.append(
                    f"temporal protocol: {relative} omits required protocol language: {snippet}"
                )

    protected = protocol.get("protected_documents")
    expected_protected = {
        str(path.relative_to(packet))
        for path in packet.rglob("*.md")
    }
    if not isinstance(protected, dict) or set(protected) != expected_protected:
        errors.append("temporal protocol: protected-document inventory is incomplete")
    else:
        for relative, expected_hash in protected.items():
            path = packet / relative
            if not re.fullmatch(r"[0-9a-f]{64}", str(expected_hash)):
                errors.append(f"temporal protocol: invalid protected hash for {relative}")
            elif sha256(path) != expected_hash:
                errors.append(f"temporal protocol: protected document drift: {relative}")

    for path in sorted(packet.rglob("*.md")):
        header = "\n".join(path.read_text(encoding="utf-8").splitlines()[:6])
        if ("**Packet:**" in header or "**Version:**" in header) and "1.2.5" not in header:
            errors.append(f"{path.relative_to(ROOT)}: packet header is not version 1.2.5")


def main() -> int:
    errors: list[str] = []
    if not MANIFEST.is_file():
        print("missing companion.json", file=sys.stderr)
        return 1

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"invalid companion.json: {exc}", file=sys.stderr)
        return 1

    if manifest.get("schema_version") != 1:
        errors.append("companion.json: schema_version must be 1")
    if not COMMIT_PATTERN.fullmatch(str(manifest.get("source_commit", ""))):
        errors.append("companion.json: source_commit must be a 7-40 character Git hash")
    if manifest.get("reader_value_packet_version") != "1.2.5":
        errors.append("companion.json: reader_value_packet_version must be 1.2.5")
    if manifest.get("human_evidence_state") != "PREPARED/UNRUN":
        errors.append("companion.json: human evidence state must remain PREPARED/UNRUN")
    if manifest.get("real_world_evidence_state") != "UNRUN":
        errors.append("companion.json: real-world evidence state must remain UNRUN")

    required = manifest.get("required_files")
    if not isinstance(required, list) or not required:
        errors.append("companion.json: required_files must be a non-empty list")
        required = []
    for relative in required:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    checksum_manifests = manifest.get("checksum_manifests", [])
    if not isinstance(checksum_manifests, list):
        errors.append("companion.json: checksum_manifests must be a list")
        checksum_manifests = []
    checked_checksums = 0
    for relative in checksum_manifests:
        checksum_path = ROOT / relative
        if not checksum_path.is_file():
            errors.append(f"missing checksum manifest: {relative}")
            continue
        listed_targets: set[Path] = set()
        for number, line in enumerate(
            checksum_path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            match = CHECKSUM_PATTERN.fullmatch(line)
            if not match:
                errors.append(f"{relative}:{number}: invalid SHA256SUMS line")
                continue
            expected, raw_target = match.groups()
            target = (checksum_path.parent / raw_target).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{relative}:{number}: checksum target escapes repository")
                continue
            if not target.is_file():
                errors.append(f"{relative}:{number}: missing checksum target: {raw_target}")
                continue
            listed_targets.add(target)
            checked_checksums += 1
            if sha256(target) != expected:
                errors.append(f"{relative}:{number}: checksum mismatch: {raw_target}")
        packet_files = {
            path.resolve()
            for path in checksum_path.parent.rglob("*")
            if path.is_file()
            and path != checksum_path
            and "__pycache__" not in path.parts
        }
        for unlisted in sorted(packet_files - listed_targets):
            errors.append(
                f"{relative}: packet file missing from checksum manifest: "
                f"{unlisted.relative_to(checksum_path.parent)}"
            )

    validate_temporal_freeze_protocol(errors)

    gateways = manifest.get("gateway_assets")
    if not isinstance(gateways, list) or not gateways:
        errors.append("companion.json: gateway_assets must be a non-empty list")
        gateways = []
    for gateway in gateways:
        relative = gateway.get("path", "")
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing gateway asset: {relative}")
            continue
        content = path.read_text(encoding="utf-8").casefold()
        phrases = [gateway.get("first_pass", ""), *gateway.get("required_language", [])]
        for phrase in phrases:
            if not phrase or phrase.casefold() not in content:
                errors.append(f"{relative}: missing required gateway language: {phrase!r}")
        for example in gateway.get("examples", []):
            if not (ROOT / example).is_file():
                errors.append(f"{relative}: missing comprehensive example: {example}")

    markdown_files = sorted(
        path for path in ROOT.rglob("*.md") if ".git" not in path.parts
    )
    checked_links = 0
    for source in markdown_files:
        for line, raw in markdown_links(source):
            try:
                target = local_target(source, raw)
            except ValueError as exc:
                errors.append(f"{source.relative_to(ROOT)}:{line}: {exc}: {raw}")
                continue
            if target is None:
                continue
            checked_links += 1
            if not target.exists():
                errors.append(
                    f"{source.relative_to(ROOT)}:{line}: missing local link target: {raw}"
                )

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        print(f"companion validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1

    print(
        f"companion validation passed: {len(markdown_files)} Markdown files, "
        f"{checked_links} local links, {len(gateways)} gateway asset(s), "
        f"{checked_checksums} checksum(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
