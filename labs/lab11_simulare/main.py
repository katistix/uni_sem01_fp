from repos.experimente import ExperimenteRepo
from services.experimente_service import ExperimenteService
from ui.cli import CLI

def main():
    experimente_repo = ExperimenteRepo("data/experimente.csv")
    experimente_service = ExperimenteService(experimente_repo)
    cli = CLI(experimente_service)

    cli.run()
    

main()