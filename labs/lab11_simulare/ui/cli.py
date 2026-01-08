from services.experimente_service import ExperimenteService
from services.experimente_service import ConducatorSuccessRate
import os

class CLI:

    def __init__(self, experimente_service: ExperimenteService):
        self._experimente_service = experimente_service
        self._commands = {
            "medii": self._medii_command,
            "ranking": self._ranking_command,
        }


    def _medii_command(self):
        media_globala = self._experimente_service.get_media_globala()
        medii_tipuri = self._experimente_service.get_medii_tipuri()

        # afisare
        for tip in medii_tipuri:
            succes_text = ""

            if medii_tipuri[tip] >= media_globala:
                succes_text = f", succes"

            print(f"{tip}: {medii_tipuri[tip]}{succes_text}")

    def _ranking_command(self):
        tip = input("Introduceti un tip: ")
        # TODO: valideaza inputul

        medii_tipuri = self._experimente_service.get_medii_tipuri()

        if tip not in medii_tipuri:
            print(f"Nu exista tipul: {tip}")

        ranking: list[ConducatorSuccessRate] = self._experimente_service.get_conducator_ranking_for_experiment_type(tip)

        for rank_item in ranking:
            a = rank_item
            print(f"{rank_item.get_nume()}: {rank_item.get_success_rate()}")


    def run(self):
        print("Comenzi disponibile: medii, ranking")
        while True:
            user_input = input(">>> ")
            # Validate user input

            if user_input == "exit":
                os._exit(0)
                

            if user_input in self._commands:
                self._commands[user_input]()
            else:
                print("unknown command")