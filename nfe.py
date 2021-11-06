class Nfe:
    def __init__(self):
        self.__path_filename_nfe: str = ""
        self.__path_filename_schema: str = ""
    
    def __carregar_nfe(self) -> None:
        ...
    
    def __mesclar_dados(self) -> None:
        ...

    def __validar_xml(self) -> None:
        ...
    
    def __coletar_dados(self) -> None:
        ...
    
    def __gerar_json(self) -> None:
        ...

    def __pegar_xnome(self) -> None:
        self.xnome: str = ""
    
    def __pegar_cnfe(self) -> None:
        self.cnfe: str = ""
    
    def __pegar_modfrete(self) -> None:
        self.modfrete: str = ""

    def __pegar_vfrete(self) -> None:
        self.vfrete: float = ""
    
    def __pegar_vicmsst(self) -> None:
        self.vicmsst: float = ""
    
    def __pegar_cprod(self) -> None:
        self.__cprod: list = []

    def __pegar_ncm(self) -> None:
        self.__ncm: list = []

    def _pegar_qcom(self) -> None:
        self.__qcom: list = []
    
    def _pegar_vuncom(self) -> None:
        self.__vuncom: list = []

    def _pegar_pipi(self) -> None:
        self.__pipi: list = []
