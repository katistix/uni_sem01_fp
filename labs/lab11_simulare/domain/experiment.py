

class Experiment:
    def __init__(self, id: str, titlu: str, tip: str, experimenter_name: str, nr_repetari: int, nr_succese: int):
        self.__id = id
        self.__titlu = titlu
        self.__tip = tip
        self.__experimenter_name = experimenter_name
        self.__nr_repetari = nr_repetari
        self.__nr_succese = nr_succese


    # Getters
    def get_id(self)-> str:
        return self.__id
    
    def get_titlu(self)-> str:
        return self.__titlu
    
    def get_tip(self)->str:
        return self.__tip
    
    def get_experimenter_name(self)->str:
        return self.__experimenter_name
    
    def get_nr_repetari(self)->int:
        return self.__nr_repetari
    
    def get_nr_succese(self)->int:
        return self.__nr_succese
    

    # Setters
    def set_titlu(self, titlu: str):
        self.__titlu = titlu
    
    def set_tip(self, tip: str):
        self.__tip = tip

    def set_experimenter_name(self, experimenter_name: str):
        self.__experimenter_name = experimenter_name

    def set_nr_repetari(self, nr_repetari: int):
        self.__nr_repetari = nr_repetari
    
    def set_nr_succese(self, nr_succese: int):
        self.__nr_succese = nr_succese