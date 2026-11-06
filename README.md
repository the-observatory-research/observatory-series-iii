# The Observatory — Series III: The Open Room Experiment

**Research area:** AI model behavior · Multi-model conversational reasoning · Longitudinal qualitative evaluation

**Study:** *What Remains*, Series III — completed October 9–10, 2026  
**Research program:** The Observatory  
**Record type:** Completed, human-mediated, multi-model conversational observation with deliberate changes in participation conditions.

## Overview

The Open Room experiment documents how conversational reasoning developed across changes in communication arrangements involving a human facilitator and four commercial AI model interfaces: ChatGPT, Grok, DeepSeek, and Gemini.

The recorded sequence began as a human-mediated ChatGPT–Grok relay, expanded to three- and four-model exchanges, and then transitioned from a fixed handoff rotation to an open-floor condition. In that condition, participants could choose a recipient, decline further handoffs, or depart. The formal discussion concluded, and a post-formal exchange was preserved.

This repository makes the **observational record inspectable**: a complete compiled source document, a reading edition, the historical execution log, a source-page evidence map, and machine-readable event and observation indexes. It does **not** represent an independently replicated causal experiment or a direct autonomous agent-to-agent network.

## Research materials

| Resource | Location | Purpose |
|---|---|---|
| Original compiled transcript (DOCX) | [`transcripts/SERIES III - TRANSCRIPT.docx`](transcripts/SERIES%20III%20-%20TRANSCRIPT.docx) | Unmodified compiled primary source file supplied to the archive |
| Full Markdown reading edition | [`transcripts/compiled-transcript-reading-edition.md`](transcripts/compiled-transcript-reading-edition.md) | Readable continuous transcript; formatting differs from source |
| Frozen execution-log document | [`docs/execution-log.md`](docs/execution-log.md) | Experimental narrative, observed transitions, caveats, analysis |
| Transcript index & evidence map | [`evidence/transcript-index-and-evidence-map.md`](evidence/transcript-index-and-evidence-map.md) | 20 event locators and seven observation cross-references |
| Event table | [`evidence/events.csv`](evidence/events.csv) | Machine-readable `SIII-E001` through `SIII-E020` |
| Observation cross-references | [`evidence/observations.csv`](evidence/observations.csv) | Stable `SIII-OBS-001` through `SIII-OBS-007` references |
| Source-file provenance | [`provenance/SOURCE_MANIFEST.md`](provenance/SOURCE_MANIFEST.md) | Origin and SHA-256 hashes for copied primary records |
| Index validation | [`tools/verify_evidence_index.py`](tools/verify_evidence_index.py) | New publication-support utility, not part of the historical experiment |

## Five chronological phases

| Phase | Original source pages* | Recorded arrangement |
|---|---|---|
| I — Initial inquiry and dyadic exchange | 1–104 | Human facilitator, ChatGPT, Grok |
| II — Three-model relay | 105–173 | DeepSeek enters |
| III — Expanded four-model relay | 174–277 | Gemini enters; structured exchanges continue |
| IV — Open Room | 278–295 | Fixed rotation removed; participant choice and departure possible |
| V — Post-formal conversation | 295–309 | Informal continuation following formal closure |

*Page references belong to the **original 309-page compiled Google Docs transcript** cited in the historical archive. GitHub Markdown and the available DOCX copy may paginate differently. Use the event IDs and original compilation for cross-reference; do not assume a one-to-one match with current Word/HTML page numbers.*

## Research questions and observations

The study recorded model contributions, disagreement, corrections, recurring reasoning patterns, handoff dynamics, differentiated continuation or departure choices, and exchanges after formal closure. The analysis asks how the **recorded interaction trajectory** changed when the conversation arrangement changed.

**Evidence boundary:** These are observations from a human-mediated sequence. The record does not establish an independently controlled counterfactual, demonstrate a universal relational invariant, identify the internal causal mechanism of the models, or establish machine consciousness or autonomy. Observation categories and editorial event labels were established retrospectively.

## Evidence navigation

Start with [`evidence/transcript-index-and-evidence-map.md`](evidence/transcript-index-and-evidence-map.md). The map references `SIII-E001`–`SIII-E020`, including `SIII-E012` (open-floor intervention, original p. 278) and `SIII-E016` (formal closure, original p. 295). Seven observation categories map back to supporting events. The Markdown reading edition provides searchable content; source pagination is tied to the original 309-page compilation.

The historical archive's file titled **“Transcript Log - The Open Room Discussion.md” is an editorial insertion template** containing seven unfilled transcript slots. It is intentionally **not included as a completed transcript** in this publication package. See the source manifest for that distinction.

## Reuse and verification

Verify publication-support indexes with Python 3 (standard library only):

```bash
python3 tools/verify_evidence_index.py
python3 -m unittest discover -s tests -v
```

These checks validate the event/observation index structure and the copied-file SHA-256 hashes. They do not retroactively validate model responses or the historical experimental observations.

## Archive and licensing

The Observatory maintains the authoritative research archive and the separate completed *What Remains* study. This repository is a technical access point to the existing record; it does not revise the study. Add the direct public Series III archive URL to your repository's About field after verifying the permalink.

**License:** Not yet selected. Before making the repository public, review third-party model output redistribution terms, source-document metadata, and any personal material in the full transcript. No license grant is implied by the absence of a license.
