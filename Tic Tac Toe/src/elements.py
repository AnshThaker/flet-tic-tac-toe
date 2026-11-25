import flet as ft

class Cell(ft.Container):
    def __init__(self, border_type: int):
        super().__init__(aspect_ratio=1.0, expand=True)

        self.border_type = border_type
        self.border_side = ft.BorderSide(width=8, color="#2c8f80")
        self.set_border()

    # # 1 = bottom, right
    # # 2 = left, bottom, right
    # # 3 = left, bottom
    # # 4 = top, right, bottom
    # # 5 = all
    # # 6 = top, left, bottom
    # # 7 = top, right
    # # 8 = top, right, left
    # # 9 = top, left
    # def set_border(self):
    #     if self.border_type == 1:
    #         self.border = ft.Border.only(
    #             bottom=self.border_side,
    #             right=self.border_side
    #         )
    #     elif self.border_type == 2:
    #         self.border = ft.Border.only(
    #             left=self.border_side,
    #             bottom=self.border_side,
    #             right=self.border_side
    #         )
    #     elif self.border_type == 3:
    #         self.border = ft.Border.only(
    #             left=self.border_side,
    #             bottom=self.border_side
    #         )
    #     elif self.border_type == 4:
    #         self.border = ft.Border.only(
    #             top=self.border_side,
    #             right=self.border_side,
    #             bottom=self.border_side
    #         )
    #     elif self.border_type == 5:
    #         self.border = ft.Border.all(width=8, color="#499F92")
    #     elif self.border_type == 6:
    #         self.border = ft.Border.only(
    #             top=self.border_side,
    #             left=self.border_side,
    #             bottom=self.border_side
    #         )
    #     elif self.border_type == 7:
    #         self.border = ft.Border.only(
    #             top=self.border_side,
    #             right=self.border_side
    #         )
    #     elif self.border_type == 8:
    #         self.border = ft.Border.only(
    #             top=self.border_side,
    #             right=self.border_side,
    #             left=self.border_side
    #         )
    #     elif self.border_type == 9:
    #         self.border = ft.Border.only(
    #             top=self.border_side,
    #             left=self.border_side
    #         )

    # NEW BORDER SYSTEM
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
