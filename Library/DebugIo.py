class DebugIO:
    """デバッグと本番用出力"""
    DEBUG = 0
    RELEASE = 1

    def __init__(self, mode=RELEASE) -> None:
        self.result = []
        self.mode = mode

    def print(self, data) -> None:
        if self.mode == self.DEBUG:
            self.result.append(data)
        elif self.mode == self.RELEASE:
            print(data)

    def debug_print(self) -> None:
        if self.mode == self.DEBUG:
            for r in self.result:
                print(r)
