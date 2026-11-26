import flet as ft

class Cell(ft.Container):
    def __init__(self, border_type: int, cell_number: int, on_click, can_click=True):
        super().__init__(aspect_ratio=1.0, expand=True, padding=8, on_click=on_click)

        self.border_type = border_type
        self.cell_number = cell_number
        self.border_side = ft.BorderSide(width=8, color="#2c8f80")
        self.can_click = can_click
        self.set_border()

    # BORDER SYSTEM
    # 1 = right, bottom (Top-Left, Middle-Left)
    # 2 = right, bottom (Top-Middle, Center)
    # 3 = bottom only (Top-Right, Middle-Right)
    # 4 = right only (Bottom-Left, Bottom-Middle)
    # 5 = no internal borders (Bottom-Right)
    def set_border(self):
        if self.border_type in [1, 2]:
            self.border = ft.Border.only(
                bottom=self.border_side,
                right=self.border_side
            )
        elif self.border_type == 3:
            self.border = ft.Border.only(
                bottom=self.border_side,
            )
        elif self.border_type == 4:
            self.border = ft.Border.only(
                right=self.border_side,
            )
        elif self.border_type == 5:
            self.border = None


class Row(ft.Row):
    def __init__(self, controls):
        super().__init__(controls=controls, spacing=0)
