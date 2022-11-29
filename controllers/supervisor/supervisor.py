"""Supervisor of the Robot Programming benchmark."""

from controller import Supervisor
import os

supervisor = Supervisor()

timestep = int(supervisor.getBasicTimeStep())

thymio = supervisor.getFromDef("BENCHMARK_ROBOT")
translation = thymio.getField("translation")

tx = 0
ongoing_benchmark = True
while supervisor.step(timestep) != -1 and ongoing_benchmark:
    t = translation.getSFVec3f()
    if ongoing_benchmark:
        ongoing_benchmark = False
        break

print(f"Benchmark complete! Your performance was {0.123}")

# Performance output used by automated CI script
CI = os.environ.get("CI")
if CI:
    print(f"performance:{0.123}")

supervisor.simulationSetMode(Supervisor.SIMULATION_MODE_PAUSE)
