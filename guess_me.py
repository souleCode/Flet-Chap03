import flet as ft
from random import randint


def main(page: ft.Page):
    page.title = "Guess me App..."

    # Players
    player1 = ft.TextField(hint_text="Guess a number (1-200)", label="Player1")
    player2 = ft.TextField(hint_text="Guess a number (1-200)", label="Player2")
    #  Generer un nombre aleatoire
    answer = randint(1, 200)
    print("=>", answer)
    # Result
    result = ft.Text()

    def check_guess_of_palyer1(e):
        if int(player1.value) < answer:
            result.value = "Guess a higher value"
        elif int(player1.value) > answer:
            result.value = "Guess a lower value"
        elif int(player1.value) == answer:
            result.value = "Congrats player1, the number was " + \
                str(answer)

        else:
            result.value = "Something went really wrong"
        page.update()

    def check_guess_of_palyer2(e):
        if int(player2.value) < answer:
            result.value = "Guess a higher value"
        elif int(player2.value) > answer:
            result.value = "Guess a lower value"
        elif int(player2.value) == answer:
            result.value = "Congrats player2 , the number was " + \
                str(answer)

        else:
            result.value = "Something went really wrong"
        page.update()
    # Buttons to check the players
    check_player1 = ft.ElevatedButton(
        "Check your guess", on_click=check_guess_of_palyer1)
    check_player2 = ft.ElevatedButton(
        "Check your guess", on_click=check_guess_of_palyer2)

    # Add controls to the page
    page.add(
        ft.Card(
            ft.Container(
                content=ft.Row(
                    controls=[ft.Text(value="Guess me")],
                    alignment='center',
                ),
                padding=20
            ),
        ),

        ft.Column(
            [
                ft.Row([player1, check_player1]),
                ft.Row([player2, check_player2]),
                result
            ]
        ),
    )


# Correct way to start the app
ft.app(target=main)
