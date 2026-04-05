class Config:
    """Maneja las variables configurables del temporizador."""
    def __init__(self):
        self.work_min = 25
        self.short_break_min = 5
        self.long_break_min = 15
        self.total_cycles = 4

    def validate_positive(self, val):
        """Valida que los valores sean positivos (Commit 4)."""
        return val > 0
