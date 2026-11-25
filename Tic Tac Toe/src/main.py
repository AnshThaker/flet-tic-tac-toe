import flet as ft
from elements import Cell, Row


def main(page: ft.Page):
    page.title = "Tic Tac Toe"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    turn_row = ft.Row(
        controls=[
            ft.Image(src="cross_pale.png", width=24),
            ft.Text("Turn", size=24)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # starts from 1 (top left) to 9 (bottom right)
    # 2 is top middle
    cells = [
        Cell(1), Cell(2), Cell(3),
        Cell(1), Cell(2), Cell(3),
        Cell(4), Cell(4), Cell(5),
    ]

    game_row_1 = Row(
        controls=[
            cells[0],
            cells[1],
            cells[2],
        ]
    )
    game_row_2 = Row(
        controls=[
            cells[3],
            cells[4],
            cells[5],
        ]
    )
    game_row_3 = Row(
        controls=[
            cells[6],
            cells[7],
            cells[8],
        ]
    )
    game_container_col = ft.Column(
        controls=[
            game_row_1,
            game_row_2,
            game_row_3,
        ],
        spacing=0
    )
    game_container = ft.Container(
        content=game_container_col,
        bgcolor="#33b5a4",
        aspect_ratio=1.0,
        padding=8,
        border_radius=10,
    )

    main_col = ft.Column(
        controls=[
            ft.Text("Tic-Tac-Toe", size=30),
            turn_row,
            ft.Container(
                content=game_container,
                expand=True,
                alignment=ft.Alignment.CENTER,
                padding=10
            ),
        ],
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER
    )
    page.add(main_col)


if __name__ == "__main__":
    ft.run(main)
