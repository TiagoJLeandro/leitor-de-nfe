class Nfe:
    
    def __init__(self, path_filename="leitor-de-nfe/file.xml"):
        self.__path_filename_nfe: str = path_filename
        self.__ns: dict = {'key': 'http://www.portalfiscal.inf.br/nfe'}
        self.__carregar_nfe()
        self.__coletar_dados()
        self.__mesclar_listas()
        self.info_produtos: list = self.__gerar_namedtuples_itens_mesclados()
    
    def __carregar_nfe(self) -> None:
        import xml.etree.ElementTree as ET
        file: str = self.__path_filename_nfe
        tree = ET.parse(file)
        self.__root = tree.getroot()
    
    def __coletar_dados(self) -> None:
        pegar_texto_do_elemento: function = self.__pegar_texto_do_elemento
        pegar_lista_de_textos: function = self.__pegar_texto_dos_elemento
        self.xnome: str = pegar_texto_do_elemento('xNome')
        self.nnf: str = pegar_texto_do_elemento('nNF')
        self.modfrete: str = pegar_texto_do_elemento('modFrete')
        self.vfrete: float = float(pegar_texto_do_elemento('vFrete'))
        self.vicmsst: float = float(pegar_texto_do_elemento('vICMSST'))
        self.cprod: list = pegar_lista_de_textos('cProd')
        self.ncm: list = pegar_lista_de_textos('NCM')
        self.qcom: list[int] = [int(float(e)) for e in
            pegar_lista_de_textos('qCom')
        ]
        self.vuncom: list[float] = [float(e) for e in
            pegar_lista_de_textos('vUnCom')
        ]
        self.pipi: list[float] = self.__pegar_pipi()

    def __mesclar_listas(self) -> None:
        self.__itens_mesclados = list(
            zip(self.cprod, self.ncm, self.qcom, self.vuncom, self.pipi)
        )

    def __gerar_namedtuples_itens_mesclados(self) -> list:
        from collections import namedtuple
        info_produtos = namedtuple('produtos', 'cprod ncm qcom vuncom pipi')
        itens_mesclados = self.__itens_mesclados
        return [info_produtos(*dados) for dados in itens_mesclados]

    def __pegar_texto_do_elemento(self, elemento: str) -> str:
        ns = self.__ns
        root = self.__root
        element = root.find(f'.//key:{elemento}', ns)
        if element is None:
            msg = f'O {elemento=} é inexistente neste arquivo xml.' \
                '\n\nEste elemento costará com o valor \'0\'.'
            self.__mostrar_alerta(msg)
            return "0"

        if not 'text' in dir(element):
            msg = f'O {elemento=} não tem o atributo \'text\''
            self.__mostrar_erro(msg)
            raise Exception(msg)
        try:
            return element.text
        except:
            msg = f'Um erro inesperado aconteceu.'
            self.__mostrar_erro(msg)
            raise NameError(msg)

    def __pegar_texto_dos_elemento(self, elemento) -> list:
        ns = self.__ns
        root = self.__root
        element = root.findall(f'.//key:{elemento}', ns)
        return [e.text for e in element]

    def __pegar_pipi(self):
        ns = self.__ns
        root = self.__root
        element = root.findall(f'.//key:IPI', ns)
        pipi = []
        for e in element:
            busca = e.find('.//key:pIPI', ns)
            ipi = busca.text if busca != None else 0
            pipi.append(int(float(ipi)))
        return pipi

    def __mostrar_erro(self, msg):
        from tkinter.messagebox import showerror
        from tkinter import Tk
        window = Tk()
        window.withdraw()
        showerror(title="Erro", message=msg)

    def __mostrar_alerta(self, msg):
        from tkinter.messagebox import showwarning
        from tkinter import Tk
        window = Tk()
        window.withdraw()
        showwarning(title="Erro", message=msg)
