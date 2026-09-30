"""Patent Council on OpenClaw: a deterministic runner that drives the council's agents through the fast flow.

The runner is the Orchestrator. It owns the task graph, the gates, the deterministic checks, the loop-back
routing and the two deliverables; the OpenClaw agents only do judgement work. Every agent turn gets its
inputs embedded in the prompt and writes its outputs to the exact paths it is given.
"""
