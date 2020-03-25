# This file has been generated automatically by generate_gamma_integrals.py.
from numpy import array

# atoms for which gamma-integrals are available
atom_names = ['h', 'c', 'n', 'o']
# distances in bohr for which gamma-integrals are tabulated
r = array([  1.00000000e-03,   1.02677966e-01,   2.04355932e-01,
         3.06033898e-01,   4.07711864e-01,   5.09389831e-01,
         6.11067797e-01,   7.12745763e-01,   8.14423729e-01,
         9.16101695e-01,   1.01777966e+00,   1.11945763e+00,
         1.22113559e+00,   1.32281356e+00,   1.42449153e+00,
         1.52616949e+00,   1.62784746e+00,   1.72952542e+00,
         1.83120339e+00,   1.93288136e+00,   2.03455932e+00,
         2.13623729e+00,   2.23791525e+00,   2.33959322e+00,
         2.44127119e+00,   2.54294915e+00,   2.64462712e+00,
         2.74630508e+00,   2.84798305e+00,   2.94966102e+00,
         3.05133898e+00,   3.15301695e+00,   3.25469492e+00,
         3.35637288e+00,   3.45805085e+00,   3.55972881e+00,
         3.66140678e+00,   3.76308475e+00,   3.86476271e+00,
         3.96644068e+00,   4.06811864e+00,   4.16979661e+00,
         4.27147458e+00,   4.37315254e+00,   4.47483051e+00,
         4.57650847e+00,   4.67818644e+00,   4.77986441e+00,
         4.88154237e+00,   4.98322034e+00,   5.08489831e+00,
         5.18657627e+00,   5.28825424e+00,   5.38993220e+00,
         5.49161017e+00,   5.59328814e+00,   5.69496610e+00,
         5.79664407e+00,   5.89832203e+00,   6.00000000e+00])
# gamma-integrals gamma_{A,lA,B,lB} = (F_{A,lA}|1/r12 + f_xc[rho0A+rho0B]|F_{B,lB}) for each
# atom combination A-B. The integrals are stored in a nested dictionary, the keys
# on the first level are the atomic numbers (Za,Zb) with Za <= Zb, the keys on the
# second level are the angular momenta of the valence shell on atom A and B, i.e. (la,lb)
# For example the integral between the s-shell on carbon and the p-shell on nitrogen
# would be stored in gamma_integrals[(6,7)][(0,1)]
#                                      |      |
#                                   (Za,Zb) (lA,lB)
gamma_integrals = \
{(1, 1): {(0, 0): array([ 0.90662492,  0.90463768,  0.8987513 ,  0.88903831,  0.87565264,
        0.8588518 ,  0.83899009,  0.81649823,  0.79185757,  0.76557213,
        0.73814259,  0.71004501,  0.6817131 ,  0.65352726,  0.62580844,
        0.59881668,  0.57275304,  0.54776486,  0.52394845,  0.50136179,
        0.48002746,  0.45993967,  0.44107179,  0.42338148,  0.40681555,
        0.39131292,  0.37680853,  0.36323662,  0.35053184,  0.33862955,
        0.32746778,  0.31698933,  0.30714095,  0.29787294,  0.28913847,
        0.28089441,  0.27310235,  0.2657282 ,  0.25874092,  0.25211149,
        0.24581276,  0.23981989,  0.23411093,  0.22866667,  0.22347001,
        0.21850514,  0.21375701,  0.20921127,  0.20485458,  0.20067489,
        0.19666154,  0.19280508,  0.18909697,  0.18552922,  0.1820942 ,
        0.17878458,  0.17559337,  0.17251404,  0.16954058,  0.16666753])},
 (1, 6): {(0, 0): array([ 0.7519825 ,  0.75073844,  0.74677482,  0.74041519,  0.7321229 ,
        0.7223422 ,  0.71127868,  0.69884602,  0.68490001,  0.66944076,
        0.65263107,  0.63472665,  0.61601151,  0.59676143,  0.57722686,
        0.55762772,  0.5381527 ,  0.51896043,  0.50018126,  0.48192036,
        0.46425929,  0.44725655,  0.43095425,  0.41537479,  0.40053026,
        0.38641577,  0.37302367,  0.3603309 ,  0.34831855,  0.33695572,
        0.32620777,  0.31605166,  0.30644641,  0.29735601,  0.2887605 ,
        0.28062214,  0.2728999 ,  0.26557897,  0.25864148,  0.2520444 ,
        0.24575578,  0.23977294,  0.23408803,  0.22866503,  0.2234675 ,
        0.21848972,  0.21374238,  0.20921626,  0.20487634,  0.20069022,
        0.19665409,  0.19278481,  0.18908982,  0.18555078,  0.18213315,
        0.17881214,  0.17558892,  0.17248242,  0.1695081 ,  0.16666116]),
          (0, 1): array([ 0.77718021,  0.77607897,  0.7723539 ,  0.76617647,  0.7576267 ,
        0.74676611,  0.73371503,  0.71867848,  0.70192712,  0.68376576,
        0.66450596,  0.64444811,  0.62387097,  0.60302884,  0.58214762,
        0.56142282,  0.54101951,  0.52107384,  0.50169459,  0.48296462,
        0.46494454,  0.44767532,  0.43117912,  0.41546572,  0.40053047,
        0.38636192,  0.37293852,  0.36023284,  0.34821966,  0.33686057,
        0.32612439,  0.31597983,  0.30638383,  0.2973066 ,  0.28872232,
        0.28058892,  0.27287349,  0.26556112,  0.25862559,  0.25202729,
        0.24574243,  0.23976507,  0.23407988,  0.22865231,  0.22345509,
        0.2184833 ,  0.21373985,  0.20921083,  0.20486586,  0.20068046,
        0.19665142,  0.19278871,  0.18909372,  0.18554889,  0.18212705,
        0.17880908,  0.17559422,  0.17249528,  0.16952189,  0.16666922])},
 (1, 7): {(0, 0): array([ 0.82968435,  0.82795934,  0.8229269 ,  0.81476974,  0.80403194,
        0.79119694,  0.77634204,  0.75937605,  0.74038448,  0.71965962,
        0.69759028,  0.67457705,  0.65099358,  0.62717349,  0.6034076 ,
        0.57994371,  0.55698705,  0.53470143,  0.51321165,  0.49260683,
        0.47294406,  0.45425362,  0.43654357,  0.41980225,  0.4040098 ,
        0.38912998,  0.37512409,  0.36194799,  0.34955062,  0.33789137,
        0.32691448,  0.31657523,  0.30683877,  0.2976519 ,  0.28897199,
        0.28077609,  0.27302495,  0.2656715 ,  0.25869458,  0.2520826 ,
        0.24580105,  0.23980982,  0.23409376,  0.22865385,  0.22347405,
        0.21851938,  0.21376213,  0.20919923,  0.20483914,  0.20067489,
        0.1966793 ,  0.19282459,  0.18910027,  0.18551411,  0.18207554,
        0.17878095,  0.17561071,  0.17254083,  0.16955732,  0.16666094]),
          (0, 1): array([ 0.8514969 ,  0.84979549,  0.84468655,  0.83617763,  0.82443502,
        0.80968135,  0.79222556,  0.77246205,  0.75083053,  0.72777517,
        0.70371723,  0.67904571,  0.65410909,  0.62921187,  0.60461318,
        0.58052696,  0.55712399,  0.53453493,  0.51285338,  0.49214069,
        0.47243168,  0.45373692,  0.43605126,  0.41935153,  0.40360879,
        0.38878135,  0.37482881,  0.36170022,  0.34934814,  0.3377276 ,
        0.32678385,  0.3164742 ,  0.30675933,  0.29758867,  0.28892488,
        0.28074056,  0.27299495,  0.26564787,  0.25867908,  0.25207   ,
        0.24578774,  0.23979858,  0.23408801,  0.22865027,  0.22346778,
        0.21851074,  0.21375648,  0.20919955,  0.2048413 ,  0.20067353,
        0.19667444,  0.19282063,  0.18910199,  0.18552111,  0.18208326,
        0.17878408,  0.17560878,  0.17253798,  0.16955858,  0.16666853])},
 (1, 8): {(0, 0): array([ 0.90309403,  0.90081015,  0.89439529,  0.88402059,  0.87032695,
        0.85374076,  0.83431335,  0.81220877,  0.7878444 ,  0.76175711,
        0.73448936,  0.70654297,  0.67836415,  0.65033923,  0.62279347,
        0.59598964,  0.57013033,  0.54536073,  0.52177559,  0.49942675,
        0.47832874,  0.45847159,  0.43982224,  0.42233339,  0.40594839,
        0.39060635,  0.37623746,  0.3627836 ,  0.35017448,  0.33835038,
        0.32725684,  0.31682858,  0.30701863,  0.29778591,  0.28907509,
        0.2808436 ,  0.27306729,  0.26571052,  0.25872855,  0.25209538,
        0.24579933,  0.23981784,  0.2341148 ,  0.22866491,  0.22346188,
        0.2185011 ,  0.21376386,  0.20922265,  0.20485799,  0.20066577,
        0.19664884,  0.19280205,  0.1891083 ,  0.18554686,  0.18210467,
        0.17878029,  0.17557812,  0.1724995 ,  0.16953731,  0.16667779]),
          (0, 1): array([ 0.92113222,  0.91879117,  0.91207074,  0.90092517,  0.88564172,
        0.86665539,  0.844511  ,  0.81981665,  0.79318794,  0.76521103,
        0.73642375,  0.70730447,  0.67826551,  0.64965161,  0.62174041,
        0.59474601,  0.56882513,  0.54408319,  0.52058184,  0.49834834,
        0.4773801 ,  0.45765264,  0.43912781,  0.42175289,  0.40546995,
        0.39021575,  0.37592457,  0.36253412,  0.34997705,  0.33819686,
        0.32713662,  0.31673615,  0.30694932,  0.29773218,  0.28903364,
        0.28081423,  0.27304563,  0.26569191,  0.25871405,  0.25208648,
        0.24579294,  0.23980996,  0.23410722,  0.22866083,  0.22346098,
        0.21849962,  0.21375953,  0.2092178 ,  0.20485647,  0.20066852,
        0.1966521 ,  0.19280224,  0.18910533,  0.18554419,  0.18210566,
        0.17878517,  0.17558396,  0.17250254,  0.16953606,  0.16667384])},
 (6, 6): {(0, 0): array([ 0.63191128,  0.63099114,  0.62850433,  0.62486033,  0.62026062,
        0.61469379,  0.60807775,  0.60035846,  0.59154231,  0.58168983,
        0.57090006,  0.55929432,  0.54700623,  0.53417205,  0.5209232 ,
        0.50738221,  0.49366111,  0.47986112,  0.46607326,  0.45237879,
        0.43884952,  0.42554804,  0.41252758,  0.39983298,  0.38750087,
        0.3755588 ,  0.36402688,  0.35291939,  0.34224425,  0.33200346,
        0.32219441,  0.31281087,  0.30384343,  0.29528008,  0.28710702,
        0.27930921,  0.27187061,  0.26477459,  0.25800461,  0.25154385,
        0.24537612,  0.23948543,  0.23385652,  0.22847463,  0.22332584,
        0.21839684,  0.21367512,  0.20914886,  0.20480697,  0.20063904,
        0.19663532,  0.1927867 ,  0.18908463,  0.18552114,  0.18208878,
        0.17878059,  0.17559006,  0.17251111,  0.16953806,  0.16666558]),
          (0, 1): array([ 0.64304006,  0.64236912,  0.64036814,  0.63702494,  0.63233461,
        0.62631471,  0.6190098 ,  0.61048827,  0.60083746,  0.59016086,
        0.57857612,  0.56621221,  0.553204  ,  0.53968652,  0.52578982,
        0.51163637,  0.49733998,  0.48300519,  0.46872652,  0.45458817,
        0.44066364,  0.42701582,  0.41369679,  0.40074876,  0.38820487,
        0.37608897,  0.36441662,  0.35319743,  0.34243494,  0.33212726,
        0.32226807,  0.31284782,  0.30385432,  0.29527321,  0.28708869,
        0.27928408,  0.27184206,  0.26474509,  0.25797573,  0.25151668,
        0.24535126,  0.23946317,  0.23383694,  0.22845767,  0.22331132,
        0.21838457,  0.21366482,  0.20914031,  0.20479992,  0.20063325,
        0.19663059,  0.19278285,  0.1890815 ,  0.1855186 ,  0.18208672,
        0.17877891,  0.17558869,  0.17250998,  0.16953712,  0.16666479]),
          (1, 0): array([ 0.64304009,  0.64236915,  0.64036816,  0.63702495,  0.63233463,
        0.62631471,  0.61900976,  0.61048817,  0.60083727,  0.59016058,
        0.57857575,  0.56621175,  0.55320348,  0.53968596,  0.52578924,
        0.51163581,  0.49733945,  0.48300471,  0.4687261 ,  0.45458781,
        0.44066334,  0.42701558,  0.4136966 ,  0.40074862,  0.38820477,
        0.37608889,  0.36441657,  0.3531974 ,  0.34243492,  0.33212725,
        0.32226806,  0.31284782,  0.30385432,  0.29527321,  0.2870887 ,
        0.27928409,  0.27184206,  0.2647451 ,  0.25797573,  0.25151669,
        0.24535126,  0.23946317,  0.23383695,  0.22845768,  0.22331133,
        0.21838457,  0.21366483,  0.20914031,  0.20479992,  0.20063325,
        0.1966306 ,  0.19278286,  0.18908151,  0.18551861,  0.18208673,
        0.17877892,  0.17558869,  0.17250998,  0.16953712,  0.16666479]),
          (1, 1): array([ 0.65776   ,  0.65701092,  0.65476892,  0.65101901,  0.64576923,
        0.63906031,  0.6309616 ,  0.62156736,  0.61099219,  0.59936828,
        0.58683981,  0.57355846,  0.55967452,  0.54533281,  0.53066966,
        0.51581178,  0.50087578,  0.48596769,  0.4711818 ,  0.45660048,
        0.44229402,  0.42832104,  0.41472861,  0.40155336,  0.38882277,
        0.37655563,  0.36476224,  0.35344722,  0.34260984,  0.33224459,
        0.32234189,  0.31288934,  0.30387242,  0.29527484,  0.2870792 ,
        0.27926745,  0.27182126,  0.26472239,  0.2579526 ,  0.25149422,
        0.24533014,  0.23944379,  0.23381952,  0.22844225,  0.22329786,
        0.21837296,  0.2136549 ,  0.20913191,  0.20479287,  0.20062737,
        0.19662571,  0.19277882,  0.18907819,  0.18551588,  0.18208449,
        0.17877708,  0.17558717,  0.17250873,  0.16953607,  0.16666391])},
 (6, 7): {(0, 0): array([ 0.67347447,  0.6723503 ,  0.66935004,  0.66498083,  0.65943689,
        0.65266933,  0.64458941,  0.63517258,  0.62447401,  0.61260686,
        0.59971935,  0.58597625,  0.57154666,  0.55659463,  0.54127389,
        0.52572608,  0.51008043,  0.49445363,  0.47895   ,  0.46366094,
        0.44866534,  0.43402976,  0.41980733,  0.40604016,  0.39275989,
        0.37998726,  0.36773407,  0.35600512,  0.34479852,  0.33410654,
        0.32391716,  0.31421515,  0.30498266,  0.29620007,  0.28784671,
        0.27990134,  0.27234263,  0.26514934,  0.25830091,  0.2517772 ,
        0.24555915,  0.23962842,  0.23396777,  0.22856083,  0.22339234,
        0.21844791,  0.21371416,  0.20917856,  0.20482944,  0.20065594,
        0.19664795,  0.19279606,  0.18909151,  0.18552614,  0.18209237,
        0.17878311,  0.17559179,  0.17251225,  0.16953877,  0.16666597]),
          (0, 1): array([ 0.67961467,  0.67880299,  0.67638973,  0.67236679,  0.66674472,
        0.65956775,  0.6509127 ,  0.64087983,  0.6295869 ,  0.61716706,
        0.6037671 ,  0.5895444 ,  0.57466038,  0.55927483,  0.54354152,
        0.52760544,  0.51160086,  0.49564945,  0.47985903,  0.46432306,
        0.4491201 ,  0.43431467,  0.41995767,  0.40608699,  0.3927298 ,
        0.37990279,  0.36761378,  0.35586362,  0.34464712,  0.33395369,
        0.32376887,  0.31407546,  0.30485412,  0.296084  ,  0.28774353,
        0.27981093,  0.27226435,  0.26508231,  0.25824409,  0.25172949,
        0.24551944,  0.23959566,  0.23394097,  0.22853908,  0.22337484,
        0.21843395,  0.21370312,  0.20916991,  0.20482273,  0.20065079,
        0.19664406,  0.19279316,  0.18908939,  0.18552463,  0.18209133,
        0.17878245,  0.1755914 ,  0.17251208,  0.16953876,  0.16666608]),
          (1, 0): array([ 0.68857196,  0.68771889,  0.68518069,  0.68095203,  0.67504278,
        0.66749723,  0.65839599,  0.64784953,  0.63599269,  0.62298048,
        0.60898254,  0.59417579,  0.57873518,  0.56282886,  0.54661539,
        0.53024217,  0.51384421,  0.49754295,  0.48144512,  0.46564187,
        0.45020933,  0.43520924,  0.42068832,  0.40668112,  0.3932114 ,
        0.38029259,  0.36792901,  0.35611852,  0.34485328,  0.33412069,
        0.32390446,  0.31418578,  0.30494404,  0.29615748,  0.28780371,
        0.27986015,  0.27230458,  0.26511521,  0.25827088,  0.25175128,
        0.24553709,  0.23960987,  0.23395235,  0.22854815,  0.22338199,
        0.21843956,  0.21370746,  0.20917322,  0.20482522,  0.20065262,
        0.19664535,  0.19279404,  0.18908994,  0.18552492,  0.18209142,
        0.17878238,  0.17559122,  0.17251181,  0.16953842,  0.1666657 ]),
          (1, 1): array([ 0.69825197,  0.69732487,  0.69456406,  0.6899673 ,  0.68356627,
        0.67543308,  0.66567446,  0.65442654,  0.64184944,  0.62812186,
        0.61343163,  0.59796897,  0.58191753,  0.56545199,  0.54873576,
        0.53191919,  0.51513798,  0.49851212,  0.48214471,  0.46612235,
        0.45051524,  0.43537885,  0.42075478,  0.40667156,  0.39314766,
        0.3801923 ,  0.36780609,  0.35598352,  0.34471415,  0.33398321,
        0.32377267,  0.3140623 ,  0.30483052,  0.2960547 ,  0.28771186,
        0.27977907,  0.27223374,  0.26505391,  0.25821832,  0.2517066 ,
        0.24549941,  0.23957836,  0.2339262 ,  0.22852662,  0.22336442,
        0.21842532,  0.21369602,  0.20916411,  0.20481804,  0.20064701,
        0.19664103,  0.19279075,  0.18908748,  0.18552312,  0.18209014,
        0.17878151,  0.17559067,  0.1725115 ,  0.1695383 ,  0.16666572])},
 (6, 8): {(0, 0): array([ 0.70850527,  0.70717193,  0.70367788,  0.69861902,  0.69216006,
        0.6842207 ,  0.67472851,  0.6637091 ,  0.65127431,  0.6375877 ,
        0.62283735,  0.60721857,  0.59092386,  0.57413714,  0.5570312 ,
        0.53976657,  0.52249045,  0.50533489,  0.48841644,  0.47183444,
        0.45567098,  0.43999225,  0.42484823,  0.41027483,  0.39629542,
        0.38292162,  0.37015573,  0.35799284,  0.34642159,  0.33542528,
        0.32498346,  0.31507332,  0.30567025,  0.29674858,  0.28828239,
        0.280246  ,  0.27261419,  0.26536248,  0.25846755,  0.25190701,
        0.24565989,  0.23970631,  0.23402779,  0.2286069 ,  0.22342758,
        0.21847478,  0.21373457,  0.20919402,  0.2048411 ,  0.2006647 ,
        0.19665453,  0.19280101,  0.18909522,  0.18552892,  0.18209446,
        0.17878469,  0.17559299,  0.1725132 ,  0.16953953,  0.16666659]),
          (0, 1): array([ 0.71085172,  0.70989983,  0.70707855,  0.70238567,  0.69585674,
        0.68757577,  0.67765991,  0.66624264,  0.65346782,  0.63949073,
        0.62447964,  0.60861264,  0.5920731 ,  0.57504402,  0.55770299,
        0.54021786,  0.52274284,  0.50541543,  0.48835452,  0.47166038,
        0.45541379,  0.43967767,  0.42449885,  0.4099095 ,  0.39592906,
        0.38256571,  0.3698185 ,  0.35767981,  0.34613603,  0.33516867,
        0.32475592,  0.31487393,  0.30549737,  0.29660017,  0.28815612,
        0.28013947,  0.27252502,  0.2652884 ,  0.25840644,  0.25185693,
        0.24561912,  0.23967333,  0.23400125,  0.22858567,  0.22341068,
        0.21846138,  0.213724  ,  0.2091857 ,  0.20483457,  0.20065959,
        0.19665052,  0.19279786,  0.18909274,  0.18552695,  0.18209288,
        0.17878341,  0.17559194,  0.17251232,  0.16953878,  0.16666593]),
          (1, 0): array([ 0.72807517,  0.72702384,  0.72391367,  0.7187527 ,  0.71158129,
        0.702487  ,  0.69159855,  0.67907759,  0.66511103,  0.64990508,
        0.63367453,  0.61663481,  0.5989946 ,  0.58095314,  0.56269739,
        0.5443989 ,  0.52621139,  0.50826851,  0.49068347,  0.47354827,
        0.45693482,  0.4408975 ,  0.42547379,  0.41068691,  0.39654843,
        0.38305972,  0.3702135 ,  0.3579966 ,  0.34639098,  0.33537479,
        0.32492338,  0.31501052,  0.3056092 ,  0.29669204,  0.28823179,
        0.28020179,  0.27257631,  0.26533063,  0.2584411 ,  0.25188536,
        0.24564238,  0.2396923 ,  0.23401671,  0.22859824,  0.22342089,
        0.21846969,  0.21373074,  0.20919118,  0.20483906,  0.20066327,
        0.19665356,  0.19280038,  0.18909485,  0.18552875,  0.18209443,
        0.17878478,  0.17559316,  0.17251342,  0.16953978,  0.16666687]),
          (1, 1): array([ 0.73364769,  0.73253765,  0.72925176,  0.72380774,  0.71626891,
        0.7067458 ,  0.69538727,  0.68237419,  0.66791199,  0.65222208,
        0.63553122,  0.61806448,  0.6000387 ,  0.58165937,  0.56311688,
        0.54458321,  0.5262096 ,  0.50812547,  0.49043785,  0.47323308,
        0.45657709,  0.44051815,  0.42508914,  0.4103092 ,  0.39618633,
        0.38271919,  0.36989826,  0.35770864,  0.34613097,  0.33514246,
        0.32471776,  0.3148301 ,  0.30545218,  0.29655642,  0.28811551,
        0.2801028 ,  0.27249259,  0.2652603 ,  0.25838239,  0.25183666,
        0.24560222,  0.23965938,  0.23398987,  0.22857648,  0.22340333,
        0.21845559,  0.21371947,  0.2091822 ,  0.20483193,  0.20065762,
        0.19664908,  0.19279684,  0.18909204,  0.18552651,  0.18209264,
        0.17878333,  0.17559197,  0.17251243,  0.16953894,  0.16666615])},
 (7, 7): {(0, 0): array([ 0.72358453,  0.72220844,  0.71855905,  0.71325602,  0.70647604,
        0.69812204,  0.68810242,  0.67643581,  0.66324401,  0.6487134 ,
        0.63306314,  0.61652103,  0.59930805,  0.5816298 ,  0.56367412,
        0.54561102,  0.52759292,  0.50975472,  0.49221392,  0.47506937,
        0.45840276,  0.44227912,  0.42674505,  0.41183334,  0.39756427,
        0.38394562,  0.37097516,  0.35864303,  0.34693306,  0.33582419,
        0.3252921 ,  0.31531026,  0.30585068,  0.29688499,  0.28838487,
        0.28032236,  0.27267069,  0.26540397,  0.25849773,  0.25192878,
        0.24567542,  0.23971726,  0.23403537,  0.22861209,  0.22343102,
        0.21847699,  0.21373592,  0.20919476,  0.20484145,  0.2006648 ,
        0.19665444,  0.19280078,  0.18909491,  0.18552857,  0.18209408,
        0.1787843 ,  0.17559258,  0.17251276,  0.16953905,  0.1666661 ]),
          (0, 1): array([ 0.73278695,  0.73175915,  0.72869775,  0.723595  ,  0.7164708 ,
        0.70739501,  0.69648533,  0.68389563,  0.66980933,  0.65443376,
        0.63799076,  0.62070608,  0.60279897,  0.58447726,  0.56593425,
        0.54734633,  0.528871  ,  0.51064555,  0.49278632,  0.47538855,
        0.4585275 ,  0.44226037,  0.42662649,  0.41165008,  0.39734357,
        0.38370831,  0.37073653,  0.35841346,  0.34671926,  0.33563001,
        0.32511925,  0.31515887,  0.30571998,  0.2967735 ,  0.28829073,
        0.28024369,  0.27260548,  0.26535036,  0.25845399,  0.25189336,
        0.24564692,  0.2396945 ,  0.2340173 ,  0.22859784,  0.22341987,
        0.21846832,  0.21372923,  0.20918965,  0.20483756,  0.20066188,
        0.19665227,  0.19279918,  0.18909375,  0.18552775,  0.18209352,
        0.17878393,  0.17559236,  0.17251265,  0.16953902,  0.16666613]),
          (1, 0): array([ 0.73278699,  0.73175919,  0.72869778,  0.72359503,  0.71647081,
        0.70739498,  0.69648523,  0.68389543,  0.66980901,  0.65443333,
        0.63799024,  0.6207055 ,  0.60279837,  0.58447666,  0.5659337 ,
        0.54734583,  0.52887057,  0.5106452 ,  0.49278604,  0.47538834,
        0.45852734,  0.44226026,  0.42662642,  0.41165003,  0.39734354,
        0.3837083 ,  0.37073653,  0.35841346,  0.34671927,  0.33563002,
        0.32511925,  0.31515888,  0.30571999,  0.29677351,  0.28829074,
        0.2802437 ,  0.27260549,  0.26535037,  0.258454  ,  0.25189336,
        0.24564692,  0.2396945 ,  0.2340173 ,  0.22859785,  0.22341988,
        0.21846833,  0.21372924,  0.20918965,  0.20483757,  0.20066188,
        0.19665228,  0.19279919,  0.18909376,  0.18552776,  0.18209352,
        0.17878394,  0.17559237,  0.17251265,  0.16953903,  0.16666613]),
          (1, 1): array([ 0.74584558,  0.74469936,  0.74128503,  0.73560717,  0.72772184,
        0.71774054,  0.70582217,  0.69216503,  0.67699788,  0.66056872,
        0.64312869,  0.62492337,  0.60618427,  0.58712689,  0.56794804,
        0.54882325,  0.52990557,  0.5113248 ,  0.49318759,  0.47557892,
        0.45856306,  0.44218664,  0.42648053,  0.4114602 ,  0.39713079,
        0.38348812,  0.37051994,  0.35820765,  0.3465287 ,  0.33545711,
        0.32496489,  0.31502287,  0.30560154,  0.29667138,  0.28820338,
        0.28016964,  0.27254314,  0.26529824,  0.2584107 ,  0.25185763,
        0.24561761,  0.23967062,  0.23399795,  0.22858227,  0.22340743,
        0.21845843,  0.21372143,  0.20918353,  0.20483281,  0.20065821,
        0.19664947,  0.19279707,  0.18909218,  0.18552659,  0.18209269,
        0.17878335,  0.17559198,  0.17251241,  0.16953889,  0.16666608])},
 (7, 8): {(0, 0): array([ 0.76708407,  0.76543443,  0.76111727,  0.75486327,  0.74681178,
        0.73683021,  0.7248543 ,  0.7109714 ,  0.69538145,  0.67834447,
        0.66014157,  0.64105032,  0.62133192,  0.60122659,  0.58095299,
        0.56070764,  0.54066431,  0.52097275,  0.50175911,  0.48312437,
        0.46514625,  0.44788179,  0.43136663,  0.41561981,  0.40064648,
        0.38643917,  0.37298085,  0.36024754,  0.34821006,  0.33683562,
        0.32608949,  0.31593617,  0.30633999,  0.297266  ,  0.28868042,
        0.28055082,  0.27284666,  0.26553906,  0.25860111,  0.25200764,
        0.24573539,  0.23976273,  0.23406974,  0.22863801,  0.22345052,
        0.21849163,  0.2137469 ,  0.20920298,  0.20484761,  0.20066942,
        0.19665792,  0.19280341,  0.18909691,  0.18553012,  0.18209529,
        0.17878526,  0.17559337,  0.17251341,  0.16953961,  0.16666659]),
          (0, 1): array([ 0.77159516,  0.77038254,  0.76677536,  0.76077108,  0.7524148 ,
        0.74181912,  0.72914913,  0.71460541,  0.69841763,  0.68083934,
        0.66213768,  0.64258111,  0.62243032,  0.60193165,  0.5813121 ,
        0.56077524,  0.54049825,  0.52063052,  0.50129362,  0.48258262,
        0.46456756,  0.44729664,  0.43079812,  0.4150842 ,  0.40015396,
        0.38599532,  0.37258757,  0.35990406,  0.34791381,  0.33658293,
        0.32587611,  0.31575759,  0.30619171,  0.29714381,  0.28858042,
        0.28046952,  0.27278095,  0.26548628,  0.25855894,  0.25197414,
        0.24570891,  0.23974191,  0.23405345,  0.22862533,  0.22344069,
        0.21848404,  0.21374106,  0.20919851,  0.20484419,  0.20066681,
        0.19665592,  0.19280188,  0.18909574,  0.18552921,  0.18209459,
        0.17878471,  0.17559292,  0.17251304,  0.16953931,  0.16666633]),
          (1, 0): array([ 0.78003118,  0.77875716,  0.77497337,  0.76868183,  0.75993178,
        0.74884237,  0.73559312,  0.72041043,  0.70355626,  0.68531641,
        0.66598189,  0.64583744,  0.62515283,  0.60417903,  0.58314451,
        0.56225156,  0.54167444,  0.52155795,  0.5020186 ,  0.4831453 ,
        0.46500168,  0.44763051,  0.43105533,  0.41528292,  0.40030817,
        0.38611585,  0.37268286,  0.35998022,  0.34797538,  0.3366333 ,
        0.32591767,  0.31579204,  0.30622045,  0.29716781,  0.2886004 ,
        0.28048618,  0.27279479,  0.26549772,  0.25856835,  0.25198185,
        0.24571518,  0.239747  ,  0.23405754,  0.22862859,  0.2234433 ,
        0.2184861 ,  0.21374268,  0.20919978,  0.20484518,  0.20066757,
        0.19665652,  0.19280235,  0.1890961 ,  0.18552949,  0.1820948 ,
        0.17878488,  0.17559307,  0.17251317,  0.16953941,  0.16666642]),
          (1, 1): array([ 0.78846552,  0.78708059,  0.78296836,  0.77615476,  0.76673471,
        0.75487261,  0.74079059,  0.72475732,  0.7070733 ,  0.6880532 ,
        0.66800767,  0.64723472,  0.6260126 ,  0.60459567,  0.58321045,
        0.56205275,  0.54128699,  0.52104658,  0.50143542,  0.48253149,
        0.46438812,  0.44703857,  0.4304995 ,  0.41477205,  0.39984652,
        0.38570459,  0.37232086,  0.35966482,  0.34770304,  0.3364    ,
        0.32571929,  0.31562446,  0.30607973,  0.29705035,  0.28850287,
        0.28040565,  0.27272863,  0.26544364,  0.25852437,  0.25194625,
        0.24568652,  0.23972403,  0.23403923,  0.22861406,  0.22343182,
        0.21847707,  0.21373561,  0.20919427,  0.20484089,  0.20066425,
        0.19665395,  0.19280036,  0.18909456,  0.18552829,  0.18209387,
        0.17878415,  0.17559249,  0.1725127 ,  0.16953903,  0.16666611])},
 (8, 8): {(0, 0): array([ 0.81909736,  0.81710209,  0.81191993,  0.80441525,  0.79467832,
        0.78254035,  0.76798306,  0.7511896 ,  0.73246781,  0.71218052,
        0.6906957 ,  0.66836161,  0.64549744,  0.62239177,  0.59930295,
        0.57645776,  0.55405056,  0.53224147,  0.51115824,  0.49089523,
        0.47151661,  0.45306215,  0.43554784,  0.41897084,  0.40331417,
        0.38854936,  0.37464017,  0.36154511,  0.34921945,  0.33761705,
        0.32669169,  0.31639821,  0.30669306,  0.29753472,  0.28888416,
        0.28070474,  0.27296252,  0.26562596,  0.25866603,  0.25205599,
        0.24577124,  0.23978922,  0.23408923,  0.22865227,  0.22346092,
        0.21849918,  0.21375233,  0.20920687,  0.20485037,  0.20067136,
        0.19665926,  0.19280433,  0.18909752,  0.18553048,  0.18209549,
        0.17878535,  0.17559338,  0.17251338,  0.16953954,  0.16666648]),
          (0, 1): array([ 0.82654437,  0.82503345,  0.82053735,  0.81306115,  0.80267981,
        0.78956282,  0.77395394,  0.75615211,  0.73649689,  0.71535103,
        0.69307803,  0.67002819,  0.64652969,  0.62288216,  0.59935151,
        0.57616591,  0.55351451,  0.53154719,  0.5103775 ,  0.49008563,
        0.47072132,  0.45231047,  0.43485852,  0.41835403,  0.4027731 ,
        0.38808276,  0.37424358,  0.36121219,  0.34894299,  0.3373897 ,
        0.32650637,  0.31624832,  0.30657266,  0.29743866,  0.28880795,
        0.28064465,  0.27291538,  0.26558919,  0.25863749,  0.25203395,
        0.2457543 ,  0.23977628,  0.23407939,  0.22864483,  0.22345532,
        0.21849499,  0.21374921,  0.20920457,  0.20484867,  0.20067012,
        0.19665837,  0.19280368,  0.18909706,  0.18553017,  0.18209527,
        0.1787852 ,  0.17559329,  0.17251332,  0.16953951,  0.16666647]),
          (1, 0): array([ 0.82654441,  0.8250335 ,  0.82053739,  0.81306118,  0.8026798 ,
        0.78956274,  0.77395375,  0.75615178,  0.73649641,  0.71535045,
        0.6930774 ,  0.67002754,  0.64652907,  0.62288161,  0.59935104,
        0.57616552,  0.55351421,  0.53154698,  0.51037736,  0.49008554,
        0.47072127,  0.45231044,  0.43485852,  0.41835403,  0.40277311,
        0.38808278,  0.3742436 ,  0.3612122 ,  0.348943  ,  0.33738971,
        0.32650638,  0.31624833,  0.30657267,  0.29743867,  0.28880796,
        0.28064466,  0.27291538,  0.26558919,  0.25863749,  0.25203395,
        0.24575431,  0.23977628,  0.23407939,  0.22864483,  0.22345533,
        0.21849499,  0.21374922,  0.20920457,  0.20484868,  0.20067012,
        0.19665837,  0.19280369,  0.18909707,  0.18553017,  0.18209528,
        0.17878521,  0.1755933 ,  0.17251333,  0.16953952,  0.16666648]),
          (1, 1): array([ 0.83834101,  0.83665558,  0.83164921,  0.82337173,  0.81196731,
        0.79767338,  0.78080368,  0.76172984,  0.74085556,  0.7185893 ,
        0.69532405,  0.67142758,  0.64723517,  0.62304382,  0.59910846,
        0.57564064,  0.5528097 ,  0.53074524,  0.50954078,  0.48925989,
        0.46993783,  0.45158799,  0.4342073 ,  0.41777783,  0.40227085,
        0.38765054,  0.37387562,  0.36090175,  0.34868316,  0.33717376,
        0.32632806,  0.31610192,  0.30645304,  0.29734143,  0.28872926,
        0.28058126,  0.27286453,  0.26554859,  0.25860521,  0.2520084 ,
        0.24573418,  0.2397605 ,  0.23406708,  0.22863527,  0.22344794,
        0.21848932,  0.21374489,  0.20920128,  0.20484619,  0.20066826,
        0.19665698,  0.19280266,  0.18909632,  0.18552963,  0.18209489,
        0.17878493,  0.17559311,  0.1725132 ,  0.16953944,  0.16666644])}}
