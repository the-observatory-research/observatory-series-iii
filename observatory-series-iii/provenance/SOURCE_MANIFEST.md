# Source manifest and archival boundaries

This manifest was generated when building the GitHub package. The four copies below are included unchanged; compare their SHA-256 hashes to verify package integrity. This does not independently authenticate platform messages.

| Copied file | SHA-256 | Bytes | Provenance |
|---|---|---:|---|
| `transcripts/SERIES III - TRANSCRIPT.docx` | `3a7bd8a02721f260830773679c59a89ee20c5b8427588040bbf35f3b57663484` | 801,025 | User-library compiled original DOCX; preserved byte-for-byte in this package; not independently authenticated as platform exports |
| `transcripts/compiled-transcript-reading-edition.md` | `d98199d06100567241b0e2cc4db7e367c18341147921cd13b3daaae2d237ff82` | 556,482 | User-library formatted Markdown continuous reading edition, distinct from source DOCX |
| `docs/execution-log.md` | `12316effa8a0c2b12c35ea99a42c687f91095a177b964fd8e457393cc71418af` | 176,644 | The Observatory archival experiments-probes.zip, Series III historical execution log; bytes preserved |
| `evidence/transcript-index-and-evidence-map.md` | `4cdcc311ffd37907380575e546215be890b3954d62fa004a3ac1308e2441cd38` | 6,208 | The Observatory archival experiments-probes.zip, Series III event/evidence map; bytes preserved |

## Deliberately excluded editorial template

The source archive also contains `Transcript Log - The Open Room Discussion.md` (SHA-256 `92271ec898c4705463dcb3c1751bd7a784016f6c4cfbd567c877588c3757619e`). It contains seven literal `[Insert the complete original transcript here...]` placeholders. **It is not an unabridged transcript** and has not been copied into the public-ready evidence directory. The complete compiled DOCX and Markdown reading edition are included instead.

## Archival and epistemic distinctions

1. **Compiled original DOCX**: available user-library document of the continuous interaction; unmodified here. The archival record refers to the original Google Docs compilation for 309-page pagination.
2. **Formatted Markdown**: continuous reading edition prepared from the compiled record; editorial formatting is not original platform output formatting.
3. **Execution log**: post-execution observational analysis, preserved separately from the transcript.
4. **Evidence map and CSVs**: retrospective cross-references, not a contemporary pre-registered measure.
5. **Source authenticity**: source-file hashes prove identity of these copies, not authenticity of every historic platform message or exact session configuration.
6. **Publication review**: review personal data, third-party outputs, licensing and confidential information prior to making the repository public.

## Local verification

Run `python3 tools/verify_evidence_index.py`.
