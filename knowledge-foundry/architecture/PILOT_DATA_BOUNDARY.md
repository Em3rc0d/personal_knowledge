# Pilot Data Boundary

Status: **MK0 candidate / GENERATED**, informed by S-006.

This document defines a fail-closed engineering boundary for learner data. It is not legal advice.

## Core rule

`personal_knowledge` is a public knowledge repository.

**Do not store learner-identifiable raw pilot data in this repository.**

Only aggregate/de-identified evidence appropriate for publication belongs here.

## Before collecting pilot data

Declare:

```yaml
pilot_id:
purpose:
population:
data_fields:
why_each_field_is_needed:
consent_or_other_basis:
storage_location:
access_roles:
retention_period:
deletion_process:
de_identification_method:
cross_border_transfer:
sensitive_data:
jurisdictions:
privacy_notice:
incident_contact:
```

## Data minimization

Prefer:

- outcome score rather than full activity history when enough;
- pseudonymous pilot IDs rather than names/emails;
- aggregate friction metrics;
- qualitative feedback stripped of unnecessary identifiers;
- short retention for raw evidence;
- separate operational storage from the public knowledge repo.

Do not collect demographics merely because they may be "interesting".

## Peru jurisdiction note

For pilots operated in Peru, the current official framework includes Ley N.° 29733 and its Reglamento approved by Decreto Supremo N.° 016-2024-JUS, in force from 31 March 2025.

The ANPD states that holders of personal-data banks have registration obligations and the newer framework includes stronger preventive/security mechanisms. Applicability depends on the actual processing design and must be checked before real collection.

## Escalation triggers

Require explicit privacy/legal review before collecting:

- minors' data;
- health or other sensitive data;
- biometric data;
- high-volume behavioral telemetry;
- data used for consequential credential/employment decisions;
- cross-border transfers with unclear safeguards.

## Pilot evidence rule

The minimum useful pilot should be designed to answer the pedagogical question with the **least personal data necessary**.
