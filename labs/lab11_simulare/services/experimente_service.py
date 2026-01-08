from repos.experimente import ExperimenteRepo


class TipValues:
    def __init__(self, nr_repetari:int, nr_succese:int):
        self._nr_repetari = nr_repetari
        self._nr_succese = nr_succese

    def get_nr_repetari(self)->int:
        return self._nr_repetari
    def get_nr_succese(self)->int:
        return self._nr_succese


    def add_repetari(self, reps: int) -> int:
        self._nr_repetari += reps
        return self._nr_repetari
    
    def add_succese(self, succese: int) -> int:
        self._nr_succese += succese
        return self._nr_succese

class ConducatorSuccessRate:
    def __init__(self, nume:str,nr_repetari:int, nr_succese:int):
        self._nume = nume
        self._nr_repetari = nr_repetari
        self._nr_succese = nr_succese
        self._success_rate = 0

    def get_success_rate(self)->float:
        return self._success_rate

    def get_nume(self)->str:
        return self._nume
    
    def get_nr_repetari(self)->int:
        return self._nr_repetari
    
    def get_nr_succese(self)->int:
        return self._nr_succese


    def add_repetari(self, reps: int) -> int:
        self._nr_repetari += reps
        return self._nr_repetari
    
    def add_succese(self, succese: int) -> int:
        self._nr_succese += succese
        return self._nr_succese
    
    def compute_success_rate(self):
        self._success_rate = self._nr_succese/self._nr_repetari


class ExperimenteService:

    def __init__(self, experimente_repo: ExperimenteRepo) -> None:
        self._experimente_repo = experimente_repo

    def get_media_globala(self) -> float:
        repetari_totale = 0
        succese_totale = 0
        for experiment in self._experimente_repo.get_all():
            repetari = experiment.get_nr_repetari()
            succese = experiment.get_nr_succese()
            repetari_totale += repetari
            succese_totale += succese

        return succese_totale / repetari_totale


    def get_medii_tipuri(self) -> dict[str, float]:
        # pentru fiecare tip de experimente
        tipuri: dict[str,TipValues] = dict()

        for experiment in self._experimente_repo.get_all():
            tip = experiment.get_tip()
            repetari = experiment.get_nr_repetari()
            succese = experiment.get_nr_succese()

            if tip not in tipuri:
                # Daca nu este deja luat in calcul tipul curent, il adaugam
                tipuri[tip] = TipValues(0,0)

            # Adaugam la tipul curent datele experimentului curent
            tipuri[tip].add_repetari(repetari)
            tipuri[tip].add_succese(succese)

        medii: dict[str, float] = dict()

        # Dupa ce avem numarul de repetari, calculam media la fiecare
        for tip in tipuri:
            medii[tip] = tipuri[tip].get_nr_succese() / tipuri[tip].get_nr_repetari()

        return medii


    def get_conducator_ranking_for_experiment_type(self, tip: str) -> list[ConducatorSuccessRate]:
        conducatori:dict[str, ConducatorSuccessRate] = dict()

        experimente = self._experimente_repo.get_all()
        for experiment in experimente:
            tip_exp = experiment.get_tip()

            if tip != tip_exp:
                continue

            conducator = experiment.get_experimenter_name()
            repetari = experiment.get_nr_repetari()
            succese = experiment.get_nr_succese()

            if conducator not in conducatori:
                conducatori[conducator] = ConducatorSuccessRate(conducator,0,0)

            conducatori[conducator].add_repetari(repetari)
            conducatori[conducator].add_succese(succese)


        # Pentru fiecare conducator, calculeaza success_rate-ul
        for conducator in conducatori:
            conducatori[conducator].compute_success_rate()

        lista_sortata = []
        for conducator in conducatori:
            lista_sortata.append(conducatori[conducator])


        # TODO: Sorteaza lista in functie de success rate
        # lista_sortata.sort(reverse=True) # trebuie o cheie de sortare

        return lista_sortata
        






