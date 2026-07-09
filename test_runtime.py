from core.runtime import Runtime

runtime = Runtime()

print(runtime.get_state())

runtime.wake()

print(runtime.get_state())

runtime.sleep()

print(runtime.get_state())