from domain.experiment import Experiment
import os

class ExperimenteRepo:

    def __init__(self, database_file_path: str) -> None:
        self.__database_path = database_file_path
        self._experimente: list[Experiment] = []
        self._load_data()


    def _load_data(self):
        """
        Load data into memory from the database csv file.
        """
        if not os.path.exists(self.__database_path):
            return
            
        with open(self.__database_path, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                    
                parts = line.split(',')
                if len(parts) == 6:
                    experiment = Experiment(
                        id=parts[0],
                        titlu=parts[1],
                        tip=parts[2],
                        experimenter_name=parts[3],
                        nr_repetari=int(parts[4]),
                        nr_succese=int(parts[5])
                    )
                    self._experimente.append(experiment)
            

    def get_all(self) -> list[Experiment]:
        """
        Get all experiments from the database
        :return: Returneaza toate experimentele din baza de date
        :rtype: list[Experiment]
        """
        return self._experimente

    def get_experiment_by_id(self, id: str) -> Experiment | None:
        """
        Get an experiment from the database by id
        :param id: id-ul experimentului cautat
        :type id: str
        :return: Returneaza un experiment din baza de data in functie de ID
        :rtype: Experiment
        """
        for experiment in self._experimente:
            if experiment.get_id() == id:
                return experiment
        
        return None