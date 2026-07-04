import mss


def capture():

    with mss.mss() as sct:

        monitor = sct.monitors[1]

        filename = "vision/screenshot.png"

        sct.shot(
            output=filename
        )

    return filename