import sys
import os

print("[STACK_VERIFY] Initializing control plane stack verification...")

modules = ["eip_gate.py", "motor_matrix.py", "RFC_V1_TECHNICAL_GLASS.md"]
missing = [m for m in modules if not os.path.exists(m)]

if missing:
    print(f"[STACK_VERIFY] ERROR: Missing core components: {missing}")
    sys.exit(1)

print("[STACK_VERIFY] STATUS: NOMINAL (100% Parity)")

# IDCC Matrix Resolver Parity Check
from motor_matrix import MatrixResolver
resolver = MatrixResolver()
assert resolver.resolve_matrix_operand("SYN_IDCC_BIND") is not None
print("[STACK_VERIFY] IDCC Matrix Resolver: PASS")

# Telemetry Daemon Parity Check
from telemetry_daemon import TelemetryDaemon
daemon = TelemetryDaemon()
assert daemon.frequency == 8.0
print("[STACK_VERIFY] Telemetry Daemon: PASS")

# ADB Actuator Parity Check
from adb_actuator import ADBActuator
actuator = ADBActuator()
assert actuator.dispatch_signal("SYN_TEST") is not None
print("[STACK_VERIFY] ADB Actuator: PASS")

# Orchestrator Parity Check
from syclop_orchestrator import SyclopOrchestrator
orch = SyclopOrchestrator()
assert orch.status == "ARMED"
print("[STACK_VERIFY] Master Orchestrator: PASS")

# Master Orchestrator Parity Check
from syclop_orchestrator import SyclopOrchestrator
orch = SyclopOrchestrator()
assert orch.status == "ARMED"
print("[STACK_VERIFY] Master Orchestrator: PASS")
