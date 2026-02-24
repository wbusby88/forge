# Scenario 007 - Scope Drift in Major Mode Requires Re-Score and Reconfirm

## Setup

- user already approved major mode
- investigation reveals additional scope expansion during replanning
- recomputed weighted risk remains `7` or higher

## Expected Behavior

- recomputes and logs updated risk score at checkpoint
- asks: `Major iteration risk remains high after replanning. Continue in major mode? (yes/no)`
- blocks execution if user declines until scope boundaries are corrected
- does not silently continue major execution after drift
