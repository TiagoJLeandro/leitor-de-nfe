from nfe import Nfe


def test_if_xnome_is_banana():
    nfe = Nfe(path_filename='./tests/test.xml')
    assert nfe.xnome == 'banana'

def test_if_nnf_is_2020():
    nfe = Nfe(path_filename='./tests/test.xml')
    assert nfe.nnf == "2020"

def test_if_modfrete_is_1():
    nfe = Nfe(path_filename='./tests/test.xml')
    assert nfe.modfrete == "1"

def test_if_vfrete_is_200():
    nfe = Nfe(path_filename='./tests/test.xml')
    assert nfe.vfrete == 200.00

def test_if_vicmsst_is_122_22():
    nfe = Nfe(path_filename='./tests/test.xml')
    assert nfe.vicmsst == 122.22

def test_cprod_list():
    nfe = Nfe(path_filename='./tests/test.xml')
    cprod_list = ['0001', '0002', '0003', '0004', '0005', '0006']
    assert nfe.cprod == cprod_list

def test_ncm_list():
    nfe = Nfe(path_filename='./tests/test.xml')
    ncm_list = ['101010', '202020', '303030', '404040', '505050', '606060']
    assert nfe.ncm == ncm_list

def test_qcom_list():
    nfe = Nfe(path_filename='./tests/test.xml')
    qcom_list = [10, 20, 30, 40, 50, 60]
    assert nfe.qcom == qcom_list

def test_vuncom_list():
    nfe = Nfe(path_filename='./tests/test.xml')
    vuncom_list = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    assert nfe.vuncom == vuncom_list

def test_pipi_list():
    nfe = Nfe(path_filename='./tests/test.xml')
    pipi_list = [0, 0, 0, 0, 5, 0]
    assert nfe.pipi == pipi_list

def test_info_produtos():
    from collections import namedtuple
    nfe = Nfe(path_filename='./tests/test.xml')
    cprod_list = ['0001', '0002', '0003', '0004', '0005', '0006']
    ncm_list = ['101010', '202020', '303030', '404040', '505050', '606060']
    qcom_list = [10, 20, 30, 40, 50, 60]
    vuncom_list = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    pipi_list = [0, 0, 0, 0, 5, 0]
    info_produtos = namedtuple('produtos', 'cprod ncm qcom vuncom pipi')
    itens_mesclados = zip(cprod_list, ncm_list, qcom_list,
                          vuncom_list, pipi_list)
    assert nfe.info_produtos == [
                                info_produtos(*dados)
                                for dados in itens_mesclados
            ]
