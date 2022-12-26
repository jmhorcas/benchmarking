"""Information about the real feature models zoo used for testing.

Most of the metrics and values of the analysis operations have been manually extracted 
from FeatureIDE, others have been calculated using a bruce-force algorithm 
(e.g., product distribution).
"""

INPUT_FIDE_MODELS_FOLDER = 'models/featureide/'
INPUT_UVL_MODELS_FOLDER = 'models/uvl/'
INPUT_FAMA_MODELS_FOLDER = 'models/fama/'
INPUT_GLENCOE_MODELS_FOLDER = 'models/glencoe/'
INPUT_TXTCNF_MODELS_FOLDER = 'models/textual_cnf/'

FIDE_EXTENSION = '.xml'
UVL_EXTENSION = '.uvl'
FAMA_EXTENSION = '.fama'
GLENCOE_EXTENSION = '.gfm.json'
TXTCNF_EXTENSION = '.txt'

# FM properties and metrics (the value assigned to the constant is irrelevant)
NAME = 0
NOF_FEATURES = 1
NOF_CONSTRAINTS = 2
NOF_ORS = 3
NOF_ALTERNATIVES = 4
NOF_ABSTRACT_FEATURES = 5
NOF_LEAF_FEATURES = 6
ROOT_NAME = 7
NOF_CORE_FEATURES = 8
NOF_DEAD_FEATURES = 9
NOF_FALSE_OPTIONAL_FEATURES = 10
NOF_PRODUCTS = 11
PRODUCT_DISTRIBUTION = 12
NOF_MANDATORY_FEATURES = 13
NOF_VARIANT_FEATURES = 14
NOF_OPTIONAL_FEATURES = 15

MODELS = [
    {NAME: 'pizzas',
     NOF_FEATURES: 12,
     NOF_CONSTRAINTS: 1,
     NOF_ORS: 1,
     NOF_ALTERNATIVES: 2,
     NOF_ABSTRACT_FEATURES: 1,
     NOF_LEAF_FEATURES: 8,
     ROOT_NAME: 'Pizza',
     NOF_CORE_FEATURES: 4,
     NOF_DEAD_FEATURES: 0,
     NOF_FALSE_OPTIONAL_FEATURES: 0,
     NOF_MANDATORY_FEATURES: 3,
     NOF_VARIANT_FEATURES: 8,
     NOF_OPTIONAL_FEATURES: 1,
     NOF_PRODUCTS: 42,
     PRODUCT_DISTRIBUTION: [0, 0, 0, 0, 0, 0, 0, 12, 18, 10, 2, 0, 0]
    },
    {NAME: 'wget',
     NOF_FEATURES: 17,
     NOF_CONSTRAINTS: 0,
     NOF_ORS: 0,
     NOF_ALTERNATIVES: 1,
     NOF_ABSTRACT_FEATURES: 0,
     NOF_LEAF_FEATURES: 15,
     ROOT_NAME: 'wget',
     NOF_CORE_FEATURES: 2,
     NOF_DEAD_FEATURES: 0,
     NOF_FALSE_OPTIONAL_FEATURES: 0,
     NOF_MANDATORY_FEATURES: 1,
     NOF_VARIANT_FEATURES: 15,
     NOF_OPTIONAL_FEATURES: 12,
     NOF_PRODUCTS: 8192,
     PRODUCT_DISTRIBUTION: [0, 0, 1, 11, 58, 198, 495, 957, 1452, 1716, 1551, 1045, 506, 166, 33, 3, 0, 0]
    },
    {NAME: 'GPL',
     NOF_FEATURES: 18,
     NOF_CONSTRAINTS: 13,
     NOF_ORS: 1,
     NOF_ALTERNATIVES: 0,
     NOF_ABSTRACT_FEATURES: 1,
     NOF_LEAF_FEATURES: 13,
     ROOT_NAME: 'GPL',
     NOF_CORE_FEATURES: 5,
     NOF_DEAD_FEATURES: 0,
     NOF_FALSE_OPTIONAL_FEATURES: 0,
     NOF_MANDATORY_FEATURES: 4,
     NOF_VARIANT_FEATURES: 13,
     NOF_OPTIONAL_FEATURES: 6,
     NOF_PRODUCTS: 436,
     PRODUCT_DISTRIBUTION: [0, 0, 0, 0, 0, 0, 0, 1, 10, 27, 52, 73, 83, 78, 61, 36, 13, 2, 0]
    },
    {NAME: 'Truck',
     NOF_FEATURES: 33,
     NOF_CONSTRAINTS: 10,
     NOF_ORS: 0,
     NOF_ALTERNATIVES: 9,
     NOF_ABSTRACT_FEATURES: 0,
     NOF_LEAF_FEATURES: 20,
     ROOT_NAME: 'Truck',
     NOF_CORE_FEATURES: 8,
     NOF_DEAD_FEATURES: 1,
     NOF_FALSE_OPTIONAL_FEATURES: 1,
     NOF_MANDATORY_FEATURES: 8,
     NOF_VARIANT_FEATURES: 24,
     NOF_OPTIONAL_FEATURES: 3,
     NOF_PRODUCTS: 234,
     PRODUCT_DISTRIBUTION: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 47, 88, 71, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    },
    {NAME: 'jHipster',
     NOF_FEATURES: 45,
     NOF_CONSTRAINTS: 13,
     NOF_ORS: 0,
     NOF_ALTERNATIVES: 10,
     NOF_ABSTRACT_FEATURES: 13,
     NOF_LEAF_FEATURES: 32,
     ROOT_NAME: 'JHipster',
     NOF_CORE_FEATURES: 7,
     NOF_DEAD_FEATURES: 0,
     NOF_FALSE_OPTIONAL_FEATURES: 0,
     NOF_MANDATORY_FEATURES: 8,
     NOF_VARIANT_FEATURES: 36,
     NOF_OPTIONAL_FEATURES: 10,
     NOF_PRODUCTS: 26256,
     PRODUCT_DISTRIBUTION: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 8, 16, 42, 106, 200, 238, 250, 488, 1276, 2688, 4314, 5460, 5322, 3696, 1668, 432, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    },
    {NAME: 'tankwar',
     NOF_FEATURES: 37,
     NOF_CONSTRAINTS: 0,
     NOF_ORS: 2,
     NOF_ALTERNATIVES: 6,
     NOF_ABSTRACT_FEATURES: 0,
     NOF_LEAF_FEATURES: 26,
     ROOT_NAME: 'TankWar',
     NOF_CORE_FEATURES: 7,
     NOF_DEAD_FEATURES: 0,
     NOF_FALSE_OPTIONAL_FEATURES: 0,
     NOF_MANDATORY_FEATURES: 6,
     NOF_VARIANT_FEATURES: 30,
     NOF_OPTIONAL_FEATURES: 8,
     NOF_PRODUCTS: 1741824,
     PRODUCT_DISTRIBUTION: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 72, 216, 1176, 4008, 12072, 30792, 65856, 120840, 189792, 254880, 291888, 282456, 227088, 147864, 75288, 28608, 7584, 1248, 96, 0, 0, 0, 0, 0, 0, 0]
    },
    {NAME: 'mobilemedia2',
     NOF_FEATURES: 43,
     NOF_CONSTRAINTS: 3,
     NOF_ORS: 4,
     NOF_ALTERNATIVES: 3,
     NOF_ABSTRACT_FEATURES: 0,
     NOF_LEAF_FEATURES: 31,
     ROOT_NAME: 'MobileMedia2',
     NOF_CORE_FEATURES: 10,
     NOF_DEAD_FEATURES: 0,
     NOF_FALSE_OPTIONAL_FEATURES: 0,
     NOF_MANDATORY_FEATURES: 12,
     NOF_VARIANT_FEATURES: 30,
     NOF_OPTIONAL_FEATURES: 10,
     NOF_PRODUCTS: 2128896,
     PRODUCT_DISTRIBUTION: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 72, 432, 1464, 4044, 9756, 20964, 41208, 73932, 119004, 170652, 219300, 255060, 270036, 260196, 227064, 178236, 125376, 78816, 43524, 20184, 7332, 1908, 312, 24, 0, 0, 0, 0, 0, 0]
    },
    {NAME: 'aafms_framework-namesAdapted',
     NOF_FEATURES: 59,
     NOF_CONSTRAINTS: 14,
     NOF_ORS: 6,
     NOF_ALTERNATIVES: 1,
     NOF_ABSTRACT_FEATURES: 1,
     NOF_LEAF_FEATURES: 45,
     ROOT_NAME: 'AAFMFramework',
     NOF_CORE_FEATURES: 3,
     NOF_DEAD_FEATURES: 0,
     NOF_FALSE_OPTIONAL_FEATURES: 0,
     NOF_MANDATORY_FEATURES: 6,
     NOF_VARIANT_FEATURES: 52,
     NOF_OPTIONAL_FEATURES: 14,
     NOF_PRODUCTS: 132224790560,
     PRODUCT_DISTRIBUTION: None
    },
    {NAME: 'WeaFQAs',
     NOF_FEATURES: 179,
     NOF_CONSTRAINTS: 7,
     NOF_ORS: 13,
     NOF_ALTERNATIVES: 23,
     NOF_ABSTRACT_FEATURES: 0,
     NOF_LEAF_FEATURES: 124,
     ROOT_NAME: 'FQAs',
     NOF_CORE_FEATURES: 1,
     NOF_DEAD_FEATURES: 0,
     NOF_FALSE_OPTIONAL_FEATURES: 0,
     NOF_MANDATORY_FEATURES: 40,
     NOF_VARIANT_FEATURES: 138,
     NOF_OPTIONAL_FEATURES: 17,
     NOF_PRODUCTS: 2934973779180551210188799,
     PRODUCT_DISTRIBUTION: None
    },
    {NAME: 'busybox-1.18.0',
     NOF_FEATURES: 854,
     NOF_CONSTRAINTS: 67,
     NOF_ORS: 0,
     NOF_ALTERNATIVES: 8,
     NOF_ABSTRACT_FEATURES: 0,
     NOF_LEAF_FEATURES: 683,
     ROOT_NAME: 'root',
     NOF_CORE_FEATURES: 20,
     NOF_DEAD_FEATURES: 15,
     NOF_FALSE_OPTIONAL_FEATURES: 3,
     NOF_MANDATORY_FEATURES: 42,
     NOF_VARIANT_FEATURES: 811,
     NOF_OPTIONAL_FEATURES: 788,
     NOF_PRODUCTS: None,
     PRODUCT_DISTRIBUTION: None
    },
    {NAME: 'embtoolkit',
     NOF_FEATURES: 1179,
     NOF_CONSTRAINTS: 167,
     NOF_ORS: 0,
     NOF_ALTERNATIVES: 70,
     NOF_ABSTRACT_FEATURES: 0,
     NOF_LEAF_FEATURES: 966,
     ROOT_NAME: 'root',
     NOF_CORE_FEATURES: 78,
     NOF_DEAD_FEATURES: 42,
     NOF_FALSE_OPTIONAL_FEATURES: 0,
     NOF_MANDATORY_FEATURES: 271,
     NOF_VARIANT_FEATURES: 907,
     NOF_OPTIONAL_FEATURES: 521,
     NOF_PRODUCTS: None,
     PRODUCT_DISTRIBUTION: None
    },
    {NAME: 'ea2468',
     NOF_FEATURES: 1408,
     NOF_CONSTRAINTS: 1281,
     NOF_ORS: 0,
     NOF_ALTERNATIVES: 12,
     NOF_ABSTRACT_FEATURES: 0,
     NOF_LEAF_FEATURES: 1069,
     ROOT_NAME: 'root',
     NOF_CORE_FEATURES: 4,
     NOF_DEAD_FEATURES: 124,
     NOF_FALSE_OPTIONAL_FEATURES: 222,
     NOF_MANDATORY_FEATURES: 496,
     NOF_VARIANT_FEATURES: 911,
     NOF_OPTIONAL_FEATURES: 881,
     NOF_PRODUCTS: None,
     PRODUCT_DISTRIBUTION: None
    },
    {NAME: 'uClinux-distribution',
     NOF_FEATURES: 1580,
     NOF_CONSTRAINTS: 247,
     NOF_ORS: 0,
     NOF_ALTERNATIVES: 10,
     NOF_ABSTRACT_FEATURES: 0,
     NOF_LEAF_FEATURES: 1368,
     ROOT_NAME: 'root',
     NOF_CORE_FEATURES: 6,
     NOF_DEAD_FEATURES: 0,
     NOF_FALSE_OPTIONAL_FEATURES: 0,
     NOF_MANDATORY_FEATURES: 40,
     NOF_VARIANT_FEATURES: 1539,
     NOF_OPTIONAL_FEATURES: 1496,
     NOF_PRODUCTS: None,
     PRODUCT_DISTRIBUTION: None
    },
    {NAME: 'automotive2_1',
     NOF_FEATURES: 14010,
     NOF_CONSTRAINTS: 624,
     NOF_ORS: 106,
     NOF_ALTERNATIVES: 1010,
     NOF_ABSTRACT_FEATURES: 0,
     NOF_LEAF_FEATURES: 12615,
     ROOT_NAME: 'N_379925076__F_91527E35945B',
     NOF_CORE_FEATURES: 1394,
     NOF_DEAD_FEATURES: 1,
     NOF_FALSE_OPTIONAL_FEATURES: 2,
     NOF_MANDATORY_FEATURES: 1496,
     NOF_VARIANT_FEATURES: 12513,
     NOF_OPTIONAL_FEATURES: 1369,
     NOF_PRODUCTS: None,
     PRODUCT_DISTRIBUTION: None
    },
    {NAME: 'linux-2.6.33.3',
     NOF_FEATURES: 6467,
     NOF_CONSTRAINTS: 7650,
     NOF_ORS: 2,
     NOF_ALTERNATIVES: 39,
     NOF_ABSTRACT_FEATURES: 0,
     NOF_LEAF_FEATURES: 5523,
     ROOT_NAME: 'root',
     NOF_CORE_FEATURES: 53,
     NOF_DEAD_FEATURES: 211,
     NOF_FALSE_OPTIONAL_FEATURES: 39,
     NOF_MANDATORY_FEATURES: 244,
     NOF_VARIANT_FEATURES: 6222,
     NOF_OPTIONAL_FEATURES: 6037,
     NOF_PRODUCTS: None,
     PRODUCT_DISTRIBUTION: None
    }
]
