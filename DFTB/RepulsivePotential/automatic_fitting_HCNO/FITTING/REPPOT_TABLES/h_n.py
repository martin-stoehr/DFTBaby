# This file has been generated automatically by /home/humeniuka/DFTB-0.1.0/DFTB/RepulsivePotential/FitReppots.py
# The repulsive potential has been fitted to the following data sets:
#   - acetic_acid_equilib_dislocated
#   - methylamine_dislocated
#   - glycine_equilib_dislocated
#   - dinitrogen_trioxide_equilib_dislocated
#   - propan-2-imine_dislocated
#   - formaldehyde_equilib_dislocated
#   - nitrobenzene_equilib_dislocated
#   - acetone_dislocated
#   - ethanol_equilib_dislocated
#   - hydrogen_peroxide_dislocated
#   - nitrobenzene_dislocated
#   - ethenol_equilib_dislocated
#   - benzene_dislocated
#   - ethene_CC_stretch
#   - methane_equilib_dislocated
#   - h2_stretch
#   - water_dislocated
#   - anisole_dislocated
#   - zundel_cation_dislocated
#   - formaldehyde_dislocated
#   - water_equilib_dislocated
#   - ammonia_dislocated
#   - pyrimidine_dislocated
#   - ethane_equilib_dislocated
#   - azidobenzene_dislocated
#   - ethine_equilib_dislocated
#   - acetonitrile_equilib_dislocated
#   - furan_dislocated
#   - ethine_CC_stretch
#   - ethanimine_dislocated
#   - ethanimine_equilib_dislocated
#   - nitrous_acid_equilib_dislocated
#   - hydrazine_equilib_dislocated
#   - pyrrole_equilib_dislocated
#   - dipeptide_equilib_dislocated
#   - anisole_equilib_dislocated
#   - acetone_equilib_dislocated
#   - dimethylamine_equilib_dislocated
#   - ethene_equilib_dislocated
#   - pyridine_dislocated
#   - carbon_dioxide_equilib_dislocated
#   - methylamine_equilib_dislocated
#   - ethane_CC_stretch
#   - carbonic_acid_dislocated
#   - nitrous_acid_dislocated
#   - dimethylether_equilib_dislocated
#   - methanol_equilib_dislocated
#   - dinitrogen_trioxide_dislocated
#   - ethene_dislocated
#   - n2_stretch
#   - furan_equilib_dislocated
#   - piperidine_equilib_dislocated
#   - ethane_dislocated
#   - zundel_cation_equilib_dislocated
#   - ethenol_dislocated
#   - propan-2-imine_equilib_dislocated
#   - nitrate_equilib_dislocated
#   - glycine_dislocated
#   - dimethylamine_dislocated
#   - acetic_acid_dislocated
#   - ethine_dislocated
#   - methane_dislocated
#   - dipeptide_dislocated
#   - ethanol_dislocated
#   - pyridine_equilib_dislocated
#   - methanol_dislocated
#   - benzene_equilib_dislocated
#   - trimethylamine_dislocated
#   - carbonic_acid_equilib_dislocated
#   - hydrazine_dislocated
#   - dimethylether_dislocated
#   - trimethylamine_equilib_dislocated
#   - azidobenzene_equilib_dislocated
#   - hydrogen_peroxide_equilib_dislocated
#   - carbon_dioxide_dislocated
#   - acetonitrile_dislocated
#   - pyrrole_dislocated
#   - pyrimidine_equilib_dislocated
#   - ammonia_equilib_dislocated
#   - piperidine_dislocated
from numpy import array
Z1 = 1
Z2 = 7
# grid for distance d between atomic centers in bohr
d = \
array([ 0.54302286,  0.54685777,  0.55069268,  0.55452759,  0.5583625 ,
        0.56219741,  0.56603233,  0.56986724,  0.57370215,  0.57753706,
        0.58137197,  0.58520688,  0.5890418 ,  0.59287671,  0.59671162,
        0.60054653,  0.60438144,  0.60821635,  0.61205127,  0.61588618,
        0.61972109,  0.623556  ,  0.62739091,  0.63122582,  0.63506074,
        0.63889565,  0.64273056,  0.64656547,  0.65040038,  0.65423529,
        0.65807021,  0.66190512,  0.66574003,  0.66957494,  0.67340985,
        0.67724476,  0.68107968,  0.68491459,  0.6887495 ,  0.69258441,
        0.69641932,  0.70025423,  0.70408915,  0.70792406,  0.71175897,
        0.71559388,  0.71942879,  0.7232637 ,  0.72709862,  0.73093353,
        0.73476844,  0.73860335,  0.74243826,  0.74627317,  0.75010809,
        0.753943  ,  0.75777791,  0.76161282,  0.76544773,  0.76928265,
        0.77311756,  0.77695247,  0.78078738,  0.78462229,  0.7884572 ,
        0.79229212,  0.79612703,  0.79996194,  0.80379685,  0.80763176,
        0.81146667,  0.81530159,  0.8191365 ,  0.82297141,  0.82680632,
        0.83064123,  0.83447614,  0.83831106,  0.84214597,  0.84598088,
        0.84981579,  0.8536507 ,  0.85748561,  0.86132053,  0.86515544,
        0.86899035,  0.87282526,  0.87666017,  0.88049508,  0.88433   ,
        0.88816491,  0.89199982,  0.89583473,  0.89966964,  0.90350455,
        0.90733947,  0.91117438,  0.91500929,  0.9188442 ,  0.92267911,
        0.92651402,  0.93034894,  0.93418385,  0.93801876,  0.94185367,
        0.94568858,  0.94952349,  0.95335841,  0.95719332,  0.96102823,
        0.96486314,  0.96869805,  0.97253296,  0.97636788,  0.98020279,
        0.9840377 ,  0.98787261,  0.99170752,  0.99554243,  0.99937735,
        1.00321226,  1.00704717,  1.01088208,  1.01471699,  1.0185519 ,
        1.02238682,  1.02622173,  1.03005664,  1.03389155,  1.03772646,
        1.04156137,  1.04539629,  1.0492312 ,  1.05306611,  1.05690102,
        1.06073593,  1.06457084,  1.06840576,  1.07224067,  1.07607558,
        1.07991049,  1.0837454 ,  1.08758031,  1.09141523,  1.09525014,
        1.09908505,  1.10291996,  1.10675487,  1.11058978,  1.1144247 ,
        1.11825961,  1.12209452,  1.12592943,  1.12976434,  1.13359925,
        1.13743417,  1.14126908,  1.14510399,  1.1489389 ,  1.15277381,
        1.15660872,  1.16044364,  1.16427855,  1.16811346,  1.17194837,
        1.17578328,  1.17961819,  1.18345311,  1.18728802,  1.19112293,
        1.19495784,  1.19879275,  1.20262767,  1.20646258,  1.21029749,
        1.2141324 ,  1.21796731,  1.22180222,  1.22563714,  1.22947205,
        1.23330696,  1.23714187,  1.24097678,  1.24481169,  1.24864661,
        1.25248152,  1.25631643,  1.26015134,  1.26398625,  1.26782116,
        1.27165608,  1.27549099,  1.2793259 ,  1.28316081,  1.28699572,
        1.29083063,  1.29466555,  1.29850046,  1.30233537,  1.30617028,
        1.31000519,  1.3138401 ,  1.31767502,  1.32150993,  1.32534484,
        1.32917975,  1.33301466,  1.33684957,  1.34068449,  1.3445194 ,
        1.34835431,  1.35218922,  1.35602413,  1.35985904,  1.36369396,
        1.36752887,  1.37136378,  1.37519869,  1.3790336 ,  1.38286851,
        1.38670343,  1.39053834,  1.39437325,  1.39820816,  1.40204307,
        1.40587798,  1.4097129 ,  1.41354781,  1.41738272,  1.42121763,
        1.42505254,  1.42888745,  1.43272237,  1.43655728,  1.44039219,
        1.4442271 ,  1.44806201,  1.45189692,  1.45573184,  1.45956675,
        1.46340166,  1.46723657,  1.47107148,  1.47490639,  1.47874131,
        1.48257622,  1.48641113,  1.49024604,  1.49408095,  1.49791586,
        1.50175078,  1.50558569,  1.5094206 ,  1.51325551,  1.51709042,
        1.52092533,  1.52476025,  1.52859516,  1.53243007,  1.53626498,
        1.54009989,  1.5439348 ,  1.54776972,  1.55160463,  1.55543954,
        1.55927445,  1.56310936,  1.56694427,  1.57077919,  1.5746141 ,
        1.57844901,  1.58228392,  1.58611883,  1.58995374,  1.59378866,
        1.59762357,  1.60145848,  1.60529339,  1.6091283 ,  1.61296322,
        1.61679813,  1.62063304,  1.62446795,  1.62830286,  1.63213777,
        1.63597269,  1.6398076 ,  1.64364251,  1.64747742,  1.65131233,
        1.65514724,  1.65898216,  1.66281707,  1.66665198,  1.67048689,
        1.6743218 ,  1.67815671,  1.68199163,  1.68582654,  1.68966145,
        1.69349636,  1.69733127,  1.70116618,  1.7050011 ,  1.70883601,
        1.71267092,  1.71650583,  1.72034074,  1.72417565,  1.72801057,
        1.73184548,  1.73568039,  1.7395153 ,  1.74335021,  1.74718512,
        1.75102004,  1.75485495,  1.75868986,  1.76252477,  1.76635968,
        1.77019459,  1.77402951,  1.77786442,  1.78169933,  1.78553424,
        1.78936915,  1.79320406,  1.79703898,  1.80087389,  1.8047088 ,
        1.80854371,  1.81237862,  1.81621353,  1.82004845,  1.82388336,
        1.82771827,  1.83155318,  1.83538809,  1.839223  ,  1.84305792,
        1.84689283,  1.85072774,  1.85456265,  1.85839756,  1.86223247,
        1.86606739,  1.8699023 ,  1.87373721,  1.87757212,  1.88140703,
        1.88524194,  1.88907686,  1.89291177,  1.89674668,  1.90058159,
        1.9044165 ,  1.90825141,  1.91208633,  1.91592124,  1.91975615,
        1.92359106,  1.92742597,  1.93126088,  1.9350958 ,  1.93893071,
        1.94276562,  1.94660053,  1.95043544,  1.95427035,  1.95810527,
        1.96194018,  1.96577509,  1.96961   ,  1.97344491,  1.97727982,
        1.98111474,  1.98494965,  1.98878456,  1.99261947,  1.99645438,
        2.00028929,  2.00412421,  2.00795912,  2.01179403,  2.01562894,
        2.01946385,  2.02329877,  2.02713368,  2.03096859,  2.0348035 ,
        2.03863841,  2.04247332,  2.04630824,  2.05014315,  2.05397806,
        2.05781297,  2.06164788,  2.06548279,  2.06931771,  2.07315262,
        2.07698753,  2.08082244,  2.08465735,  2.08849226,  2.09232718,
        2.09616209,  2.099997  ,  2.10383191,  2.10766682,  2.11150173,
        2.11533665,  2.11917156,  2.12300647,  2.12684138,  2.13067629,
        2.1345112 ,  2.13834612,  2.14218103,  2.14601594,  2.14985085,
        2.15368576,  2.15752067,  2.16135559,  2.1651905 ,  2.16902541,
        2.17286032,  2.17669523,  2.18053014,  2.18436506,  2.18819997,
        2.19203488,  2.19586979,  2.1997047 ,  2.20353961,  2.20737453,
        2.21120944,  2.21504435,  2.21887926,  2.22271417,  2.22654908,
        2.230384  ,  2.23421891,  2.23805382,  2.24188873,  2.24572364,
        2.24955855,  2.25339347,  2.25722838,  2.26106329,  2.2648982 ,
        2.26873311,  2.27256802,  2.27640294,  2.28023785,  2.28407276,
        2.28790767,  2.29174258,  2.29557749,  2.29941241,  2.30324732,
        2.30708223,  2.31091714,  2.31475205,  2.31858696,  2.32242188,
        2.32625679,  2.3300917 ,  2.33392661,  2.33776152,  2.34159643,
        2.34543135,  2.34926626,  2.35310117,  2.35693608,  2.36077099,
        2.3646059 ,  2.36844082,  2.37227573,  2.37611064,  2.37994555,
        2.38378046,  2.38761537,  2.39145029,  2.3952852 ,  2.39912011,
        2.40295502,  2.40678993,  2.41062484,  2.41445976,  2.41829467,
        2.42212958,  2.42596449,  2.4297994 ,  2.43363432,  2.43746923,
        2.44130414,  2.44513905,  2.44897396,  2.45280887,  2.45664379])
# repulsive potential in hartree/bohr
Vrep = \
array([  4.30345586e+00,   4.13471041e+00,   4.01308892e+00,
         3.92923692e+00,   3.87526215e+00,   3.84452981e+00,
         3.83148513e+00,   3.83149970e+00,   3.84073836e+00,
         3.85604413e+00,   3.87483855e+00,   3.89503561e+00,
         3.91496743e+00,   3.93332011e+00,   3.94907840e+00,
         3.96147809e+00,   3.96996506e+00,   3.97416009e+00,
         3.97382870e+00,   3.96885533e+00,   3.95922126e+00,
         3.94498583e+00,   3.92627044e+00,   3.90324500e+00,
         3.87611647e+00,   3.84511921e+00,   3.81050694e+00,
         3.77254595e+00,   3.73150956e+00,   3.68767352e+00,
         3.64131222e+00,   3.59269575e+00,   3.54208742e+00,
         3.48974189e+00,   3.43590378e+00,   3.38080653e+00,
         3.32467171e+00,   3.26770851e+00,   3.21011344e+00,
         3.15207032e+00,   3.09375025e+00,   3.03531183e+00,
         2.97690146e+00,   2.91865365e+00,   2.86069143e+00,
         2.80312684e+00,   2.74606138e+00,   2.68958653e+00,
         2.63378427e+00,   2.57872759e+00,   2.52448103e+00,
         2.47110120e+00,   2.41863725e+00,   2.36713143e+00,
         2.31661951e+00,   2.26713127e+00,   2.21869097e+00,
         2.17131772e+00,   2.12502594e+00,   2.07982572e+00,
         2.03572320e+00,   1.99272092e+00,   1.95081811e+00,
         1.91001105e+00,   1.87029333e+00,   1.83165614e+00,
         1.79408849e+00,   1.75757748e+00,   1.72210850e+00,
         1.68766544e+00,   1.65423089e+00,   1.62178629e+00,
         1.59031213e+00,   1.55978806e+00,   1.53019306e+00,
         1.50150553e+00,   1.47370345e+00,   1.44676444e+00,
         1.42066592e+00,   1.39538512e+00,   1.37089920e+00,
         1.34718535e+00,   1.32422079e+00,   1.30198290e+00,
         1.28044920e+00,   1.25959745e+00,   1.23940569e+00,
         1.21985223e+00,   1.20091575e+00,   1.18257525e+00,
         1.16481016e+00,   1.14760028e+00,   1.13092586e+00,
         1.11476758e+00,   1.09910658e+00,   1.08392443e+00,
         1.06920321e+00,   1.05492545e+00,   1.04107416e+00,
         1.02763282e+00,   1.01458541e+00,   1.00191637e+00,
         9.89610615e-01,   9.77653539e-01,   9.66030998e-01,
         9.54729309e-01,   9.43735246e-01,   9.33036030e-01,
         9.22619323e-01,   9.12473220e-01,   9.02586241e-01,
         8.92947322e-01,   8.83545805e-01,   8.74371430e-01,
         8.65414326e-01,   8.56664998e-01,   8.48114324e-01,
         8.39753537e-01,   8.31574222e-01,   8.23568302e-01,
         8.15728029e-01,   8.08045977e-01,   8.00515028e-01,
         7.93128365e-01,   7.85879462e-01,   7.78762076e-01,
         7.71770234e-01,   7.64898228e-01,   7.58140603e-01,
         7.51492151e-01,   7.44947899e-01,   7.38503105e-01,
         7.32153245e-01,   7.25894008e-01,   7.19721288e-01,
         7.13631175e-01,   7.07619949e-01,   7.01684070e-01,
         6.95820176e-01,   6.90025070e-01,   6.84295719e-01,
         6.78629243e-01,   6.73022911e-01,   6.67474136e-01,
         6.61980466e-01,   6.56539580e-01,   6.51149283e-01,
         6.45807500e-01,   6.40512271e-01,   6.35261745e-01,
         6.30054177e-01,   6.24887922e-01,   6.19761431e-01,
         6.14673245e-01,   6.09621995e-01,   6.04606394e-01,
         5.99625235e-01,   5.94677385e-01,   5.89761785e-01,
         5.84877443e-01,   5.80023435e-01,   5.75198896e-01,
         5.70403022e-01,   5.65635064e-01,   5.60894326e-01,
         5.56180165e-01,   5.51491982e-01,   5.46829227e-01,
         5.42191390e-01,   5.37578004e-01,   5.32988639e-01,
         5.28422902e-01,   5.23880433e-01,   5.19360906e-01,
         5.14864026e-01,   5.10389524e-01,   5.05937160e-01,
         5.01506720e-01,   4.97098011e-01,   4.92710865e-01,
         4.88345135e-01,   4.84000691e-01,   4.79677425e-01,
         4.75375242e-01,   4.71094065e-01,   4.66833833e-01,
         4.62594497e-01,   4.58376021e-01,   4.54178381e-01,
         4.50001563e-01,   4.45845563e-01,   4.41710389e-01,
         4.37596054e-01,   4.33502579e-01,   4.29429993e-01,
         4.25378330e-01,   4.21347632e-01,   4.17337944e-01,
         4.13349314e-01,   4.09381798e-01,   4.05435452e-01,
         4.01510335e-01,   3.97606510e-01,   3.93724042e-01,
         3.89862996e-01,   3.86023440e-01,   3.82205442e-01,
         3.78409070e-01,   3.74634393e-01,   3.70881479e-01,
         3.67150399e-01,   3.63441218e-01,   3.59754005e-01,
         3.56088826e-01,   3.52445744e-01,   3.48824824e-01,
         3.45226127e-01,   3.41649713e-01,   3.38095640e-01,
         3.34563964e-01,   3.31054738e-01,   3.27568014e-01,
         3.24103842e-01,   3.20662267e-01,   3.17243333e-01,
         3.13847081e-01,   3.10473551e-01,   3.07122776e-01,
         3.03794791e-01,   3.00489625e-01,   2.97207305e-01,
         2.93947855e-01,   2.90711295e-01,   2.87497644e-01,
         2.84306917e-01,   2.81139124e-01,   2.77994276e-01,
         2.74872377e-01,   2.71773430e-01,   2.68697436e-01,
         2.65644389e-01,   2.62614284e-01,   2.59607112e-01,
         2.56622859e-01,   2.53661510e-01,   2.50723048e-01,
         2.47807450e-01,   2.44914693e-01,   2.42044748e-01,
         2.39197588e-01,   2.36373178e-01,   2.33571484e-01,
         2.30792468e-01,   2.28036088e-01,   2.25302303e-01,
         2.22591064e-01,   2.19902325e-01,   2.17236035e-01,
         2.14592139e-01,   2.11970583e-01,   2.09371309e-01,
         2.06794255e-01,   2.04239360e-01,   2.01706559e-01,
         1.99195784e-01,   1.96706967e-01,   1.94240037e-01,
         1.91794920e-01,   1.89371542e-01,   1.86969826e-01,
         1.84589692e-01,   1.82231061e-01,   1.79893850e-01,
         1.77577975e-01,   1.75283351e-01,   1.73009889e-01,
         1.70757502e-01,   1.68526099e-01,   1.66315587e-01,
         1.64125875e-01,   1.61956867e-01,   1.59808467e-01,
         1.57680578e-01,   1.55573102e-01,   1.53485938e-01,
         1.51418987e-01,   1.49372146e-01,   1.47345313e-01,
         1.45338383e-01,   1.43351251e-01,   1.41383812e-01,
         1.39435958e-01,   1.37507583e-01,   1.35598577e-01,
         1.33708832e-01,   1.31838237e-01,   1.29986682e-01,
         1.28154055e-01,   1.26340244e-01,   1.24545138e-01,
         1.22768622e-01,   1.21010583e-01,   1.19270907e-01,
         1.17549479e-01,   1.15846185e-01,   1.14160908e-01,
         1.12493533e-01,   1.10843944e-01,   1.09212024e-01,
         1.07597657e-01,   1.06000726e-01,   1.04421113e-01,
         1.02858701e-01,   1.01313373e-01,   9.97850104e-02,
         9.82734958e-02,   9.67787113e-02,   9.53005390e-02,
         9.38388607e-02,   9.23935585e-02,   9.09645143e-02,
         8.95516101e-02,   8.81547280e-02,   8.67737501e-02,
         8.54085585e-02,   8.40590355e-02,   8.27250636e-02,
         8.14065254e-02,   8.01033036e-02,   7.88152810e-02,
         7.75423409e-02,   7.62843665e-02,   7.50412414e-02,
         7.38128495e-02,   7.25990747e-02,   7.13998014e-02,
         7.02149144e-02,   6.90442985e-02,   6.78878390e-02,
         6.67454215e-02,   6.56169320e-02,   6.45022568e-02,
         6.34012826e-02,   6.23138964e-02,   6.12399857e-02,
         6.01794383e-02,   5.91321427e-02,   5.80979874e-02,
         5.70768615e-02,   5.60686548e-02,   5.50732572e-02,
         5.40905593e-02,   5.31204520e-02,   5.21628268e-02,
         5.12175756e-02,   5.02845908e-02,   4.93637655e-02,
         4.84549931e-02,   4.75581675e-02,   4.66731832e-02,
         4.57999353e-02,   4.49383192e-02,   4.40882312e-02,
         4.32495678e-02,   4.24222262e-02,   4.16061041e-02,
         4.08011000e-02,   4.00071125e-02,   3.92240412e-02,
         3.84517861e-02,   3.76902477e-02,   3.69393273e-02,
         3.61989264e-02,   3.54689476e-02,   3.47492936e-02,
         3.40398680e-02,   3.33405749e-02,   3.26513189e-02,
         3.19720054e-02,   3.13025402e-02,   3.06428298e-02,
         2.99927814e-02,   2.93523025e-02,   2.87213015e-02,
         2.80996874e-02,   2.74873695e-02,   2.68842580e-02,
         2.62902637e-02,   2.57052978e-02,   2.51292723e-02,
         2.45620998e-02,   2.40036934e-02,   2.34539668e-02,
         2.29128345e-02,   2.23802114e-02,   2.18560132e-02,
         2.13401559e-02,   2.08325565e-02,   2.03331323e-02,
         1.98418013e-02,   1.93584822e-02,   1.88830942e-02,
         1.84155571e-02,   1.79557914e-02,   1.75037180e-02,
         1.70592586e-02,   1.66223354e-02,   1.61928713e-02,
         1.57707896e-02,   1.53560144e-02,   1.49484703e-02,
         1.45480823e-02,   1.41547764e-02,   1.37684789e-02,
         1.33891166e-02,   1.30166172e-02,   1.26509087e-02,
         1.22919198e-02,   1.19395797e-02,   1.15938184e-02,
         1.12545660e-02,   1.09217538e-02,   1.05953130e-02,
         1.02751759e-02,   9.96127505e-03,   9.65354371e-03,
         9.35191560e-03,   9.05632506e-03,   8.76670693e-03,
         8.48299663e-03,   8.20513011e-03,   7.93304386e-03,
         7.66667492e-03,   7.40596085e-03,   7.15083976e-03,
         6.90125028e-03,   6.65713157e-03,   6.41842332e-03,
         6.18506572e-03,   5.95699950e-03,   5.73416590e-03,
         5.51650668e-03,   5.30396409e-03,   5.09648091e-03,
         4.89400041e-03,   4.69646635e-03,   4.50382301e-03,
         4.31601515e-03,   4.13298804e-03,   3.95468741e-03,
         3.78105949e-03,   3.61205099e-03,   3.44760911e-03,
         3.28768151e-03,   3.13221633e-03,   2.98116217e-03,
         2.83446812e-03,   2.69208371e-03,   2.55395894e-03,
         2.42004427e-03,   2.29029060e-03,   2.16464930e-03,
         2.04307217e-03,   1.92551147e-03,   1.81191990e-03,
         1.70225057e-03,   1.59645707e-03,   1.49449339e-03,
         1.39631396e-03,   1.30187364e-03,   1.21112770e-03,
         1.12403184e-03,   1.04054218e-03,   9.60615236e-04,
         8.84207952e-04,   8.11277672e-04,   7.41782145e-04,
         6.75679522e-04,   6.12928352e-04,   5.53487577e-04,
         4.97316533e-04,   4.44374947e-04,   3.94622928e-04,
         3.48020970e-04,   3.04529948e-04,   2.64111113e-04,
         2.26726090e-04,   1.92336876e-04,   1.60905835e-04,
         1.32395697e-04,   1.06769555e-04,   8.39908604e-05,
         6.40234221e-05,   4.68314023e-05,   3.23793138e-05,
         2.06320178e-05,   1.15547204e-05,   5.11297021e-06,
         1.27265515e-06,   0.00000000e+00])