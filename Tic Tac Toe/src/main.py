import flet as ft


def main(page: ft.Page):
    page.title = "Tic Tac Toe"
    page.theme_mode = ft.ThemeMode.DARK

    main_col = ft.Column(
        controls=[
            ft.Text("Tic-Tac-Toe", size=20)
        ]
    )
    page.add(main_col)


if __name__ == "__main__":
    ft.run(main)
