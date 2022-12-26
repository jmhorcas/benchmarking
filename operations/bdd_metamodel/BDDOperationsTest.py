import pytest

from flamapy.metamodels.fm_metamodel.transformations import UVLReader
from flamapy.metamodels.bdd_metamodel.transformations import FmToBDD
from flamapy.metamodels.bdd_metamodel.operations import (
    BDDProductsNumber,
    BDDProductDistribution
)

from models.models_info import *

import sys

sys.setrecursionlimit(5000)

@pytest.mark.parametrize("model_name, expected_nof_products", [[m[NAME], m[NOF_PRODUCTS]] for m in MODELS[:9]])
def test_nof_products(model_name, expected_nof_products):
    fm = UVLReader(INPUT_UVL_MODELS_FOLDER + model_name + UVL_EXTENSION).transform()
    bdd = FmToBDD(fm).transform()
    
    nof_products = BDDProductsNumber().execute(bdd).get_result()
    assert nof_products == expected_nof_products

@pytest.mark.parametrize("model_name", [m[NAME] for m in MODELS[:10]])
def test_product_distribution(model_name):
    fm = UVLReader(INPUT_UVL_MODELS_FOLDER + model_name + UVL_EXTENSION).transform()
    bdd = FmToBDD(fm).transform()

    product_dist = BDDProductDistribution().execute(bdd).get_result()
    nof_products = BDDProductsNumber().execute(bdd).get_result()

    assert len(product_dist) == len(fm.get_features())
    assert sum(product_dist) == nof_products
