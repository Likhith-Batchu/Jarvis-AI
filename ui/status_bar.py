from core.runtime import Runtime


class StatusBar:

    @staticmethod
    def draw(runtime):

        print()

        print("=" * 60)

        print(
            f"State : {runtime.get_state()} | "
            f"Mode : {runtime.get_mode()} | "
            f"Wake : {runtime.wake_word.capitalize()}"
        )

        print("=" * 60)