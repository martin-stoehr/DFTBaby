# This file has been generated automatically by ./generate_slakotables.py
# from /local_1tb/home/humeniuka/DFTB-0.1.0/DFTB/SlaterKoster/confined_pseudo_atoms/h.py and /local_1tb/home/humeniuka/DFTB-0.1.0/DFTB/SlaterKoster/confined_pseudo_atoms/h.py.
from numpy import array
Z1 = 1
Z2 = 1
# overlaps S[(l1,l2,i)] and hamilton matrix elements H[(l1,l2,i)]
# l1 and l2 are the angular quantum numbers of valence orbitals
# on atom1 and atom2 respectively.
# i enumerates the Slater-Koster integrals:
index2symbol = \
{0: 'ss\\sigma'}
# grid for distance d between atomic centers
d = \
array([  0.        ,   0.04016064,   0.08032129,   0.12048193,
         0.16064257,   0.20080321,   0.24096386,   0.2811245 ,
         0.32128514,   0.36144578,   0.40160643,   0.44176707,
         0.48192771,   0.52208835,   0.562249  ,   0.60240964,
         0.64257028,   0.68273092,   0.72289157,   0.76305221,
         0.80321285,   0.84337349,   0.88353414,   0.92369478,
         0.96385542,   1.00401606,   1.04417671,   1.08433735,
         1.12449799,   1.16465863,   1.20481928,   1.24497992,
         1.28514056,   1.3253012 ,   1.36546185,   1.40562249,
         1.44578313,   1.48594378,   1.52610442,   1.56626506,
         1.6064257 ,   1.64658635,   1.68674699,   1.72690763,
         1.76706827,   1.80722892,   1.84738956,   1.8875502 ,
         1.92771084,   1.96787149,   2.00803213,   2.04819277,
         2.08835341,   2.12851406,   2.1686747 ,   2.20883534,
         2.24899598,   2.28915663,   2.32931727,   2.36947791,
         2.40963855,   2.4497992 ,   2.48995984,   2.53012048,
         2.57028112,   2.61044177,   2.65060241,   2.69076305,
         2.73092369,   2.77108434,   2.81124498,   2.85140562,
         2.89156627,   2.93172691,   2.97188755,   3.01204819,
         3.05220884,   3.09236948,   3.13253012,   3.17269076,
         3.21285141,   3.25301205,   3.29317269,   3.33333333,
         3.37349398,   3.41365462,   3.45381526,   3.4939759 ,
         3.53413655,   3.57429719,   3.61445783,   3.65461847,
         3.69477912,   3.73493976,   3.7751004 ,   3.81526104,
         3.85542169,   3.89558233,   3.93574297,   3.97590361,
         4.01606426,   4.0562249 ,   4.09638554,   4.13654618,
         4.17670683,   4.21686747,   4.25702811,   4.29718876,
         4.3373494 ,   4.37751004,   4.41767068,   4.45783133,
         4.49799197,   4.53815261,   4.57831325,   4.6184739 ,
         4.65863454,   4.69879518,   4.73895582,   4.77911647,
         4.81927711,   4.85943775,   4.89959839,   4.93975904,
         4.97991968,   5.02008032,   5.06024096,   5.10040161,
         5.14056225,   5.18072289,   5.22088353,   5.26104418,
         5.30120482,   5.34136546,   5.3815261 ,   5.42168675,
         5.46184739,   5.50200803,   5.54216867,   5.58232932,
         5.62248996,   5.6626506 ,   5.70281124,   5.74297189,
         5.78313253,   5.82329317,   5.86345382,   5.90361446,
         5.9437751 ,   5.98393574,   6.02409639,   6.06425703,
         6.10441767,   6.14457831,   6.18473896,   6.2248996 ,
         6.26506024,   6.30522088,   6.34538153,   6.38554217,
         6.42570281,   6.46586345,   6.5060241 ,   6.54618474,
         6.58634538,   6.62650602,   6.66666667,   6.70682731,
         6.74698795,   6.78714859,   6.82730924,   6.86746988,
         6.90763052,   6.94779116,   6.98795181,   7.02811245,
         7.06827309,   7.10843373,   7.14859438,   7.18875502,
         7.22891566,   7.26907631,   7.30923695,   7.34939759,
         7.38955823,   7.42971888,   7.46987952,   7.51004016,
         7.5502008 ,   7.59036145,   7.63052209,   7.67068273,
         7.71084337,   7.75100402,   7.79116466,   7.8313253 ,
         7.87148594,   7.91164659,   7.95180723,   7.99196787,
         8.03212851,   8.07228916,   8.1124498 ,   8.15261044,
         8.19277108,   8.23293173,   8.27309237,   8.31325301,
         8.35341365,   8.3935743 ,   8.43373494,   8.47389558,
         8.51405622,   8.55421687,   8.59437751,   8.63453815,
         8.6746988 ,   8.71485944,   8.75502008,   8.79518072,
         8.83534137,   8.87550201,   8.91566265,   8.95582329,
         8.99598394,   9.03614458,   9.07630522,   9.11646586,
         9.15662651,   9.19678715,   9.23694779,   9.27710843,
         9.31726908,   9.35742972,   9.39759036,   9.437751  ,
         9.47791165,   9.51807229,   9.55823293,   9.59839357,
         9.63855422,   9.67871486,   9.7188755 ,   9.75903614,
         9.79919679,   9.83935743,   9.87951807,   9.91967871,
         9.95983936,  10.        ])
# overlaps
S = \
{(0, 0, 0): array([  1.00012970e+00,   9.99573386e-01,   9.97937568e-01,
         9.95226778e-01,   9.91456702e-01,   9.86642472e-01,
         9.80813698e-01,   9.73992148e-01,   9.66206621e-01,
         9.57500158e-01,   9.47898043e-01,   9.37443676e-01,
         9.26180969e-01,   9.14149443e-01,   9.01384015e-01,
         8.87943512e-01,   8.73868806e-01,   8.59198534e-01,
         8.43989966e-01,   8.28278246e-01,   8.12114814e-01,
         7.95547569e-01,   7.78619396e-01,   7.61374810e-01,
         7.43854965e-01,   7.26109869e-01,   7.08176373e-01,
         6.90092241e-01,   6.71901972e-01,   6.53644004e-01,
         6.35350329e-01,   6.17059017e-01,   5.98806186e-01,
         5.80617092e-01,   5.62531480e-01,   5.44572688e-01,
         5.26764778e-01,   5.09139489e-01,   4.91718772e-01,
         4.74524865e-01,   4.57575624e-01,   4.40894905e-01,
         4.24498845e-01,   4.08401227e-01,   3.92616961e-01,
         3.77160093e-01,   3.62042060e-01,   3.47270593e-01,
         3.32857439e-01,   3.18808731e-01,   3.05130650e-01,
         2.91826216e-01,   2.78900477e-01,   2.66354916e-01,
         2.54191724e-01,   2.42410926e-01,   2.31013821e-01,
         2.19996603e-01,   2.09357854e-01,   1.99093540e-01,
         1.89200918e-01,   1.79675836e-01,   1.70512040e-01,
         1.61704306e-01,   1.53247173e-01,   1.45132511e-01,
         1.37354778e-01,   1.29905317e-01,   1.22777739e-01,
         1.15963184e-01,   1.09453217e-01,   1.03240036e-01,
         9.73148960e-02,   9.16690136e-02,   8.62942441e-02,
         8.11806127e-02,   7.63199881e-02,   7.17040106e-02,
         6.73228515e-02,   6.31685570e-02,   5.92319294e-02,
         5.55052666e-02,   5.19792412e-02,   4.86458392e-02,
         4.54969764e-02,   4.25250228e-02,   3.97217602e-02,
         3.70796497e-02,   3.45912737e-02,   3.22494810e-02,
         3.00471299e-02,   2.79776068e-02,   2.60341783e-02,
         2.42105046e-02,   2.25004724e-02,   2.08981531e-02,
         1.93977915e-02,   1.79938671e-02,   1.66812496e-02,
         1.54547963e-02,   1.43096564e-02,   1.32410007e-02,
         1.22446295e-02,   1.13161961e-02,   1.04516508e-02,
         9.64722990e-03,   8.89922307e-03,   8.20415871e-03,
         7.55871305e-03,   6.95976124e-03,   6.40434424e-03,
         5.88962902e-03,   5.41296131e-03,   4.97181442e-03,
         4.56380928e-03,   4.18674084e-03,   3.83847424e-03,
         3.51701551e-03,   3.22050930e-03,   2.94720530e-03,
         2.69544419e-03,   2.46368862e-03,   2.25051194e-03,
         2.05450034e-03,   1.87442073e-03,   1.70908063e-03,
         1.55737775e-03,   1.41827363e-03,   1.29080969e-03,
         1.17408040e-03,   1.06726082e-03,   9.69571267e-04,
         8.80299640e-04,   7.98747841e-04,   7.24311768e-04,
         6.56413656e-04,   5.94520780e-04,   5.38134412e-04,
         4.86800142e-04,   4.40094410e-04,   3.97627855e-04,
         3.59041838e-04,   3.24002979e-04,   2.92205345e-04,
         2.63368745e-04,   2.37233477e-04,   2.13561335e-04,
         1.92134706e-04,   1.72753087e-04,   1.55232066e-04,
         1.39403196e-04,   1.25112347e-04,   1.12218192e-04,
         1.00591476e-04,   9.01156402e-05,   8.06809963e-05,
         7.21902671e-05,   6.45537757e-05,   5.76898302e-05,
         5.15243365e-05,   4.59898247e-05,   4.10249099e-05,
         3.65736856e-05,   3.25855895e-05,   2.90147204e-05,
         2.58194585e-05,   2.29619379e-05,   2.04082863e-05,
         1.81276040e-05,   1.60920086e-05,   1.42762511e-05,
         1.26576707e-05,   1.12156991e-05,   9.93199980e-06,
         8.78985344e-06,   7.77430090e-06,   6.87189065e-06,
         6.07052734e-06,   5.35932669e-06,   4.72857348e-06,
         4.16960985e-06,   3.67439151e-06,   3.23600908e-06,
         2.84820655e-06,   2.50532863e-06,   2.20237440e-06,
         1.93487307e-06,   1.69882631e-06,   1.49066584e-06,
         1.30721221e-06,   1.14563533e-06,   1.00341026e-06,
         8.78307249e-07,   7.68330616e-07,   6.71711092e-07,
         5.86883172e-07,   5.12452000e-07,   4.47188138e-07,
         3.89996682e-07,   3.39916171e-07,   2.96080223e-07,
         2.57738394e-07,   2.24224904e-07,   1.94947714e-07,
         1.69390001e-07,   1.47092460e-07,   1.27651750e-07,
         1.10712411e-07,   9.59618966e-08,   8.31255276e-08,
         7.19619934e-08,   6.22592272e-08,   5.38314159e-08,
         4.65159706e-08,   4.01699026e-08,   3.46681799e-08,
         2.99015344e-08,   2.57743936e-08,   2.22032192e-08,
         1.91150673e-08,   1.64462881e-08,   1.41413146e-08,
         1.21518907e-08,   1.04359306e-08,   8.95675179e-09,
         7.68247698e-09,   6.58542795e-09,   5.64153068e-09,
         4.82994414e-09,   4.13252481e-09,   3.53364080e-09,
         3.01969554e-09,   2.57889003e-09,   2.20106078e-09,
         1.87742892e-09,   1.60038952e-09,   1.36338663e-09,
         1.16075603e-09,   9.87633578e-10,   8.39809993e-10,
         7.13667115e-10,   6.06096573e-10,   5.14419975e-10,
         4.36335541e-10,   3.69875903e-10,   3.13343048e-10,
         2.65286873e-10,   2.24460173e-10,   1.89799430e-10,
         1.60391166e-10])}
# hamiltonian matrix elements
H = \
{(0, 0, 0): array([ -8.27656654e-01,  -8.26369010e-01,  -8.23115782e-01,
        -8.17968673e-01,  -8.11162061e-01,  -8.02880360e-01,
        -7.93326607e-01,  -7.82654134e-01,  -7.71029199e-01,
        -7.58591873e-01,  -7.45464020e-01,  -7.31768769e-01,
        -7.17608071e-01,  -7.03078777e-01,  -6.88258907e-01,
        -6.73232708e-01,  -6.58067248e-01,  -6.42817490e-01,
        -6.27542033e-01,  -6.12284453e-01,  -5.97086508e-01,
        -5.81986582e-01,  -5.67012441e-01,  -5.52193204e-01,
        -5.37548904e-01,  -5.23102359e-01,  -5.08866933e-01,
        -4.94854134e-01,  -4.81077412e-01,  -4.67544421e-01,
        -4.54258948e-01,  -4.41226620e-01,  -4.28450197e-01,
        -4.15929749e-01,  -4.03668266e-01,  -3.91662157e-01,
        -3.79909873e-01,  -3.68410395e-01,  -3.57160397e-01,
        -3.46156745e-01,  -3.35395573e-01,  -3.24874249e-01,
        -3.14588871e-01,  -3.04535099e-01,  -2.94709336e-01,
        -2.85108044e-01,  -2.75728373e-01,  -2.66565328e-01,
        -2.57616859e-01,  -2.48879576e-01,  -2.40349864e-01,
        -2.32024605e-01,  -2.23901381e-01,  -2.15976545e-01,
        -2.08248216e-01,  -2.00713163e-01,  -1.93370180e-01,
        -1.86215444e-01,  -1.79246706e-01,  -1.72461704e-01,
        -1.65858243e-01,  -1.59434042e-01,  -1.53186596e-01,
        -1.47113705e-01,  -1.41213405e-01,  -1.35482459e-01,
        -1.29919602e-01,  -1.24521712e-01,  -1.19287210e-01,
        -1.14213446e-01,  -1.09297565e-01,  -1.04537569e-01,
        -9.99311446e-02,  -9.54754249e-02,  -9.11686316e-02,
        -8.70071472e-02,  -8.29890309e-02,  -7.91118754e-02,
        -7.53722842e-02,  -7.17681620e-02,  -6.82962905e-02,
        -6.49546568e-02,  -6.17396541e-02,  -5.86487617e-02,
        -5.56790427e-02,  -5.28280680e-02,  -5.00924196e-02,
        -4.74693700e-02,  -4.49559121e-02,  -4.25492476e-02,
        -4.02462386e-02,  -3.80442343e-02,  -3.59400780e-02,
        -3.39308341e-02,  -3.20136211e-02,  -3.01855672e-02,
        -2.84437172e-02,  -2.67851518e-02,  -2.52072256e-02,
        -2.37069759e-02,  -2.22816574e-02,  -2.09282732e-02,
        -1.96444317e-02,  -1.84272967e-02,  -1.72742033e-02,
        -1.61827288e-02,  -1.51502658e-02,  -1.41743622e-02,
        -1.32525787e-02,  -1.23825642e-02,  -1.15620514e-02,
        -1.07887785e-02,  -1.00605535e-02,  -9.37526302e-03,
        -8.73084073e-03,  -8.12535795e-03,  -7.55682440e-03,
        -7.02338089e-03,  -6.52324961e-03,  -6.05471041e-03,
        -5.61607254e-03,  -5.20574702e-03,  -4.82222899e-03,
        -4.46393882e-03,  -4.12951411e-03,  -3.81759005e-03,
        -3.52687157e-03,  -3.25611431e-03,  -3.00413458e-03,
        -2.76979390e-03,  -2.55203379e-03,  -2.34982403e-03,
        -2.16221244e-03,  -1.98822310e-03,  -1.82701523e-03,
        -1.67775699e-03,  -1.53966827e-03,  -1.41199581e-03,
        -1.29404544e-03,  -1.18515316e-03,  -1.08469888e-03,
        -9.92098560e-04,  -9.06796841e-04,  -8.28275035e-04,
        -7.56049425e-04,  -6.89660255e-04,  -6.28679621e-04,
        -5.72709559e-04,  -5.21376152e-04,  -4.74326173e-04,
        -4.31234079e-04,  -3.91795771e-04,  -3.55726924e-04,
        -3.22762842e-04,  -2.92661421e-04,  -2.65188656e-04,
        -2.40135171e-04,  -2.17303875e-04,  -1.96512078e-04,
        -1.77591386e-04,  -1.60385889e-04,  -1.44751375e-04,
        -1.30554118e-04,  -1.17671093e-04,  -1.05989051e-04,
        -9.54034980e-05,  -8.58177455e-05,  -7.71440645e-05,
        -6.93011337e-05,  -6.22143908e-05,  -5.58152828e-05,
        -5.00411606e-05,  -4.48345416e-05,  -4.01432219e-05,
        -3.59189636e-05,  -3.21179392e-05,  -2.87001613e-05,
        -2.56291438e-05,  -2.28715585e-05,  -2.03972419e-05,
        -1.81789795e-05,  -1.61909315e-05,  -1.44107666e-05,
        -1.28179472e-05,  -1.13935782e-05,  -1.01207835e-05,
        -8.98425332e-06,  -7.97010682e-06,  -7.06578608e-06,
        -6.25994898e-06,  -5.54236648e-06,  -4.90378710e-06,
        -4.33594122e-06,  -3.83132510e-06,  -3.38319956e-06,
        -2.98552829e-06,  -2.63286082e-06,  -2.32033564e-06,
        -2.04356129e-06,  -1.79864472e-06,  -1.58201686e-06,
        -1.39056226e-06,  -1.22147804e-06,  -1.07224216e-06,
        -9.40624035e-07,  -8.24620034e-07,  -7.22448984e-07,
        -6.32521873e-07,  -5.53425155e-07,  -4.83902058e-07,
        -4.22835568e-07,  -3.69232451e-07,  -3.22212506e-07,
        -2.80996962e-07,  -2.44892805e-07,  -2.13287272e-07,
        -1.85638930e-07,  -1.61468873e-07,  -1.40353860e-07,
        -1.21920209e-07,  -1.05838263e-07,  -9.18170600e-08,
        -7.96012542e-08,  -6.89657496e-08,  -5.97121940e-08,
        -5.16663811e-08,  -4.46754841e-08,  -3.86051363e-08,
        -3.33378404e-08,  -2.87702014e-08,  -2.48122587e-08,
        -2.13849637e-08,  -1.84189264e-08,  -1.58538510e-08,
        -1.36371137e-08,  -1.17226569e-08,  -1.00703854e-08,
        -8.64530791e-09,  -7.41708160e-09,  -6.35918640e-09,
        -5.44860459e-09,  -4.66537227e-09,  -3.99211529e-09,
        -3.41376062e-09,  -2.91730534e-09,  -2.49141046e-09,
        -2.12630986e-09,  -1.81352101e-09,  -1.54574115e-09,
        -1.31664132e-09])}
# dipoles
Dipole = \
{(0, 0, 3): array([ -3.07954681e-18,  -2.00717535e-02,  -4.00778164e-02,
        -5.99534215e-02,  -7.96350764e-02,  -9.90604877e-02,
        -1.18170327e-01,  -1.36906528e-01,  -1.55213915e-01,
        -1.73042196e-01,  -1.90340974e-01,  -2.07065873e-01,
        -2.23176137e-01,  -2.38633387e-01,  -2.53401131e-01,
        -2.67452866e-01,  -2.80761062e-01,  -2.93300703e-01,
        -3.05056616e-01,  -3.16009773e-01,  -3.26150527e-01,
        -3.35471865e-01,  -3.43968409e-01,  -3.51638969e-01,
        -3.58484320e-01,  -3.64512985e-01,  -3.69730638e-01,
        -3.74146396e-01,  -3.77776209e-01,  -3.80636065e-01,
        -3.82741163e-01,  -3.84113043e-01,  -3.84775059e-01,
        -3.84746265e-01,  -3.84057638e-01,  -3.82731809e-01,
        -3.80793814e-01,  -3.78276329e-01,  -3.75207096e-01,
        -3.71615858e-01,  -3.67530621e-01,  -3.62985767e-01,
        -3.58011074e-01,  -3.52635598e-01,  -3.46890487e-01,
        -3.40807313e-01,  -3.34416361e-01,  -3.27745339e-01,
        -3.20826447e-01,  -3.13687306e-01,  -3.06356074e-01,
        -2.98858173e-01,  -2.91221381e-01,  -2.83470092e-01,
        -2.75629581e-01,  -2.67722910e-01,  -2.59774578e-01,
        -2.51803341e-01,  -2.43830432e-01,  -2.35873872e-01,
        -2.27952913e-01,  -2.20084860e-01,  -2.12284066e-01,
        -2.04565688e-01,  -1.96944157e-01,  -1.89429985e-01,
        -1.82036453e-01,  -1.74772214e-01,  -1.67648318e-01,
        -1.60671882e-01,  -1.53849904e-01,  -1.47189609e-01,
        -1.40696235e-01,  -1.34374257e-01,  -1.28228395e-01,
        -1.22259959e-01,  -1.16472271e-01,  -1.10867647e-01,
        -1.05445430e-01,  -1.00207149e-01,  -9.51516939e-02,
        -9.02796505e-02,  -8.55883088e-02,  -8.10763985e-02,
        -7.67418881e-02,  -7.25828703e-02,  -6.85958108e-02,
        -6.47777013e-02,  -6.11251423e-02,  -5.76346146e-02,
        -5.43020420e-02,  -5.11237394e-02,  -4.80952693e-02,
        -4.52123881e-02,  -4.24707711e-02,  -3.98659547e-02,
        -3.73933330e-02,  -3.50482955e-02,  -3.28265553e-02,
        -3.07233902e-02,  -2.87342498e-02,  -2.68542384e-02,
        -2.50793617e-02,  -2.34049839e-02,  -2.18267407e-02,
        -2.03405450e-02,  -1.89421214e-02,  -1.76274093e-02,
        -1.63923897e-02,  -1.52332124e-02,  -1.41461419e-02,
        -1.31274864e-02,  -1.21737282e-02,  -1.12814263e-02,
        -1.04472743e-02,  -9.66817665e-03,  -8.94102433e-03,
        -8.26286776e-03,  -7.63092565e-03,  -7.04251869e-03,
        -6.49504625e-03,  -5.98607074e-03,  -5.51330234e-03,
        -5.07436831e-03,  -4.66723233e-03,  -4.28986101e-03,
        -3.94035334e-03,  -3.61688255e-03,  -3.31774379e-03,
        -3.04129260e-03,  -2.78602222e-03,  -2.55047863e-03,
        -2.33332435e-03,  -2.13320206e-03,  -1.94895134e-03,
        -1.77943461e-03,  -1.62359088e-03,  -1.48040993e-03,
        -1.34896425e-03,  -1.22837596e-03,  -1.11782931e-03,
        -1.01656424e-03,  -9.23863915e-04,  -8.39063542e-04,
        -7.61548180e-04,  -6.90740044e-04,  -6.26103512e-04,
        -5.67144615e-04,  -5.13402749e-04,  -4.64449353e-04,
        -4.19889146e-04,  -3.79356715e-04,  -3.42513357e-04,
        -3.09046099e-04,  -2.78670856e-04,  -2.51115551e-04,
        -2.26138186e-04,  -2.03512907e-04,  -1.83031992e-04,
        -1.64505412e-04,  -1.47758473e-04,  -1.32630733e-04,
        -1.18974640e-04,  -1.06655644e-04,  -9.55504849e-05,
        -8.55463987e-05,  -7.65397931e-05,  -6.84374259e-05,
        -6.11533630e-05,  -5.46094266e-05,  -4.87341907e-05,
        -4.34630863e-05,  -3.87369528e-05,  -3.45027302e-05,
        -3.07115361e-05,  -2.73193305e-05,  -2.42861999e-05,
        -2.15759706e-05,  -1.91558263e-05,  -1.69962782e-05,
        -1.50708790e-05,  -1.33547161e-05,  -1.18263786e-05,
        -1.04663012e-05,  -9.25663591e-06,  -8.18151131e-06,
        -7.22663437e-06,  -6.37912691e-06,  -5.62741322e-06,
        -4.96110657e-06,  -4.37089785e-06,  -3.84842087e-06,
        -3.38624481e-06,  -2.97766685e-06,  -2.61670586e-06,
        -2.29803652e-06,  -2.01687936e-06,  -1.76899725e-06,
        -1.55058922e-06,  -1.35829956e-06,  -1.18907720e-06,
        -1.04026942e-06,  -9.09506639e-07,  -7.94666385e-07,
        -6.93886751e-07,  -6.05501093e-07,  -5.28037360e-07,
        -4.60190141e-07,  -4.00804709e-07,  -3.48860146e-07,
        -3.03454189e-07,  -2.63789095e-07,  -2.29161851e-07,
        -1.98953850e-07,  -1.72617654e-07,  -1.49671861e-07,
        -1.29693402e-07,  -1.12310109e-07,  -9.71948152e-08,
        -8.40602357e-08,  -7.26542850e-08,  -6.27556329e-08,
        -5.41710791e-08,  -4.67311752e-08,  -4.02873976e-08,
        -3.47099864e-08,  -2.98856770e-08,  -2.57154109e-08,
        -2.21129973e-08,  -1.90029755e-08,  -1.63200278e-08,
        -1.40070215e-08,  -1.20141061e-08,  -1.02981358e-08,
        -8.82165397e-09,  -7.55203891e-09,  -6.46102899e-09,
        -5.52407989e-09,  -4.72001590e-09,  -4.03041342e-09,
        -3.43935959e-09,  -2.93311795e-09,  -2.49979184e-09,
        -2.12910716e-09,  -1.81224338e-09,  -1.54154713e-09,
        -1.31045323e-09,  -1.11328640e-09,  -9.45185917e-10,
        -8.01955830e-10])}
