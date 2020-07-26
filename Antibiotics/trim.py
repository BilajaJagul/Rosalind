#! /usr/bin/python

import os, sys

with open(sys.argv[1],'r') as lh:
    amino_acid_weights = {}
    for line in lh:
        data = line[:-1].split(" ")
        amino_acid_weights[data[0]] = data[1]
amino_acids = list(amino_acid_weights.keys())

def linear_spectrum(peptide):
    peptide = peptide.strip("0")
    l_peptide = len(peptide)
    prefix_mass = [0]
    for j in range(l_peptide):
        prefix_mass += [prefix_mass[-1] + int(amino_acid_weights[peptide[j]])]

    full_mass = prefix_mass[l_peptide]

    peptide_counts = {str(0):1}

    for j in range(0, l_peptide):
        for i in range(j+1, l_peptide + 1):
            linear_peptide = prefix_mass[i] - prefix_mass[j]
            if peptide_counts.get(str(linear_peptide)):
                peptide_counts[str(linear_peptide)] += 1
            else:
                peptide_counts[str(linear_peptide)] = 1
    return peptide_counts

def scoring(peptide, compare_spectrum):
    peptide_counts = linear_spectrum(peptide)
    #print(peptide_counts)
    #print(compare_spectrum)
    score = 0
    for j in range(len(compare_spectrum)):
        if peptide_counts.get(compare_spectrum[j]):
            peptide_counts[compare_spectrum[j]] -= 1
            if peptide_counts[compare_spectrum[j]] >= 0:
                score += 1
    return score

def trim(peptides, spectrum, N):
    #print(peptides)
    if not peptides:
        return []
    scored_peptides = []
    for peptide in peptides:
        scored_peptides.append((peptide, scoring(peptide, spectrum)))
    scored_peptides = sorted(scored_peptides,reverse = True, key = lambda x:x[1])
    if len(scored_peptides) < N:
        leaderboard_new = scored_peptides
    else:
        nth_score = scored_peptides[N-1][1]
        leaderboard_new = scored_peptides[:N]
        for position in range(N, len(scored_peptides)):
            if scored_peptides[position][1] == nth_score:
                leaderboard_new.append(scored_peptides[position])
    leaderboard_n = [j[0] for j in leaderboard_new]
    return leaderboard_n


peptides = "SSQYVWQMQMLHVNPYWMSTCFTTVHCGPNKAYCFAACPFGVHNDRFRYA YMKCRRMVGKCHQSAVNLLHVGIHLIETGANVTFGVAWNPPWTHGLVYNA DWCVMKMQQWKDGDGYKSSTVVGIGRGTFHGRRSIRHTRIDKDTICNPHH HNCIYNHASEFIRLCPHFLWEEGGHMGIANLMPDWLIMTYKCTMPFNDKM AKYVAPCHCTEWFKVFDFMCGQNEGGAESSAPKVKLKDYHWHCYSVLKEV VYDTQPSWCHSHPRFIPDQPETKAFCLANSIEEAPGYIWKVSQMTMGFVR CMAYWILYQKNMVNWGGSYNQWGHCFNTHKKFWYLAYRSPDMWQLALTLC DGRANFNGCGIEQIERWEIRWPLIRNFWCCCKPTHQTQNSSFWTDTWRLI NLTYWMNSHCPMFTESVVQVSCGNSLEIYGLGCWDCHRPGCSKFKETRGC DDPFQLNKHAYYCNRYLAGEDFMHGEEAERGPEGGCEHWECIEWVSKTGH FMHAAPHWSTWRIIPDQPIRYGSTCTNHPHATQDVLEMYPVGRTTKYNSK EHEQDWVEPEWYIAVPHPMCHKQIMGHHVWMYCNAYTKIGGPRWWPDASP RQWMLWFHPDMSTYRTLECYKTEDKRQYFWFPLKSRTSAVCYMDMGFTLT KNRYFVRTDMVWHQRYTKSGKSTDRNVMEKHLYWVSQVEPGKCWCLDKMN AGWWLEQQSERMHRQIWITKSMPKMKGEGKIHQIWQHYTFKFHFHIITWQ ESLISSEGAAQFSFRNKNKSLWGPPRGIMCSDCVDDHDCQQMGCHHQCLK AVTCTPNYLKEAACTNCARMHAAVQVMLCGWFCELCVICGSEWAHRESSK FPPPVIEWYSECLNVDSQEFYSAAGFCFRCSYDIHVLACKKSHRIHREDG"
spectrum = "0 57 57 71 71 71 87 87 87 97 99 99 99 101 101 103 113 113 113 113 113 114 114 114 115 115 115 115 128 128 128 128 128 128 129 129 129 131 131 131 131 137 144 156 156 156 158 160 160 163 170 171 172 184 185 186 186 186 186 186 186 186 199 212 214 214 214 215 217 226 228 229 230 241 241 241 242 243 247 250 251 255 257 257 257 259 259 259 260 262 269 273 273 274 283 284 284 285 287 287 292 294 299 300 300 301 301 304 314 314 314 315 329 329 330 330 331 340 341 343 345 354 356 363 364 370 371 371 372 372 372 380 387 387 388 388 390 397 397 397 400 400 401 402 411 413 414 415 415 415 416 418 423 425 427 427 430 433 442 444 444 445 454 459 469 477 478 484 484 486 486 486 487 488 489 490 491 493 500 500 501 508 510 515 516 519 519 525 528 528 528 529 529 529 540 542 543 544 544 553 554 557 557 557 558 573 582 583 583 587 587 588 593 599 601 601 604 605 606 609 613 614 614 619 621 621 628 630 631 641 643 644 644 644 647 650 654 654 656 657 657 657 670 672 675 675 676 682 682 685 686 686 692 700 700 701 702 711 714 714 720 724 727 729 734 734 734 740 742 743 743 743 747 756 757 758 759 761 768 769 769 773 774 778 783 785 787 788 790 791 800 801 804 806 807 811 813 814 817 823 825 828 829 829 833 840 842 843 847 855 856 857 858 860 861 862 868 871 871 872 887 890 892 898 900 901 904 905 906 913 915 916 916 917 918 919 922 928 928 929 929 931 938 941 942 946 954 955 958 960 962 969 971 972 973 975 977 983 985 987 989 997 1013 1015 1015 1016 1017 1018 1018 1020 1021 1028 1029 1031 1032 1035 1043 1044 1047 1053 1054 1057 1057 1058 1065 1069 1072 1073 1073 1074 1075 1082 1082 1087 1088 1091 1092 1098 1101 1102 1102 1112 1112 1116 1122 1128 1130 1131 1131 1141 1144 1145 1147 1149 1149 1157 1158 1166 1173 1178 1184 1186 1187 1188 1188 1188 1191 1197 1201 1201 1201 1204 1206 1209 1210 1211 1211 1214 1215 1220 1221 1227 1229 1230 1233 1235 1243 1244 1258 1258 1259 1262 1276 1277 1278 1284 1287 1288 1291 1297 1301 1301 1305 1312 1314 1316 1316 1316 1318 1322 1326 1327 1328 1329 1330 1333 1335 1339 1342 1344 1348 1348 1349 1352 1357 1358 1361 1375 1389 1390 1392 1395 1396 1397 1399 1404 1413 1415 1419 1419 1425 1429 1432 1432 1434 1435 1441 1441 1442 1444 1445 1447 1450 1457 1458 1461 1461 1463 1464 1470 1472 1472 1476 1480 1483 1488 1489 1498 1506 1508 1512 1518 1521 1521 1525 1525 1535 1542 1542 1546 1554 1560 1560 1562 1563 1563 1571 1572 1572 1575 1575 1576 1578 1578 1581 1581 1582 1585 1592 1598 1601 1603 1608 1611 1611 1611 1613 1617 1621 1631 1632 1640 1646 1649 1652 1666 1669 1674 1675 1675 1679 1685 1685 1692 1694 1698 1705 1706 1706 1707 1709 1711 1711 1712 1719 1723 1726 1726 1727 1728 1729 1730 1731 1739 1739 1739 1740 1745 1745 1746 1749 1762 1763 1774 1777 1783 1793 1798 1802 1807 1821 1822 1822 1826 1829 1834 1835 1835 1836 1837 1840 1841 1841 1841 1845 1850 1854 1855 1858 1858 1858 1860 1861 1868 1870 1871 1876 1886 1891 1897 1905 1905 1908 1911 1917 1922 1925 1932 1935 1935 1935 1948 1949 1949 1954 1958 1959 1962 1967 1969 1969 1972 1978 1978 1984 1986 1987 1989 1998 1999 2000 2007 2012 2015 2016 2020 2027 2036 2040 2040 2041 2046 2047 2048 2049 2050 2062 2063 2071 2077 2078 2082 2091 2091 2095 2099 2100 2101 2103 2109 2111 2115 2117 2118 2119 2120 2127 2129 2140 2144 2155 2155 2156 2161 2163 2164 2164 2170 2171 2176 2176 2198 2200 2201 2204 2206 2206 2219 2222 2222 2224 2226 2229 2232 2232 2235 2238 2246 2248 2255 2256 2258 2259 2262 2263 2263 2268 2268 2268 2283 2289 2299 2313 2315 2316 2319 2327 2332 2332 2333 2335 2341 2346 2350 2350 2350 2350 2351 2355 2358 2360 2366 2369 2370 2377 2386 2392 2396 2403 2411 2412 2414 2415 2418 2421 2428 2430 2440 2447 2449 2449 2454 2454 2463 2463 2464 2473 2478 2479 2485 2485 2488 2489 2491 2497 2497 2501 2504 2506 2511 2527 2529 2530 2536 2536 2536 2540 2540 2541 2549 2563 2568 2582 2588 2591 2592 2592 2598 2598 2600 2600 2603 2607 2610 2619 2619 2624 2628 2635 2640 2644 2645 2650 2654 2655 2660 2662 2664 2664 2669 2683 2699 2701 2713 2715 2720 2722 2722 2723 2726 2727 2741 2747 2748 2750 2751 2752 2754 2758 2759 2763 2763 2768 2777 2783 2784 2791 2812 2814 2818 2820 2830 2836 2841 2841 2850 2851 2854 2855 2855 2869 2872 2876 2876 2878 2879 2887 2904 2907 2908 2912 2920 2927 2929 2933 2937 2938 2940 2940 2943 2944 2949 2956 2963 2969 2970 2982 3007 3007 3007 3013 3015 3017 3022 3027 3027 3032 3033 3036 3042 3042 3055 3058 3064 3069 3072 3078 3084 3084 3093 3106 3114 3116 3119 3123 3124 3129 3135 3138 3138 3145 3146 3149 3150 3155 3163 3170 3171 3173 3183 3184 3186 3187 3193 3206 3211 3219 3221 3228 3244 3250 3251 3257 3263 3266 3268 3269 3274 3274 3279 3283 3287 3292 3298 3299 3301 3305 3320 3321 3331 3332 3334 3337 3341 3356 3358 3358 3364 3371 3379 3397 3407 3412 3413 3419 3420 3428 3429 3430 3432 3433 3435 3436 3445 3447 3452 3457 3460 3468 3469 3469 3507 3516 3520 3520 3526 3528 3542 3546 3548 3550 3550 3551 3560 3561 3565 3570 3575 3583 3597 3598 3613 3615 3616 3631 3638 3641 3651 3661 3663 3663 3674 3676 3679 3682 3689 3693 3698 3712 3712 3726 3728 3731 3746 3747 3760 3769 3769 3776 3776 3780 3789 3807 3807 3824 3825 3827 3830 3840 3845 3849 3856 3862 3875 3875 3889 3898 3904 3908 3932 3936 3938 3941 3945 3946 3953 3955 3961 3962 3974 3977 3985 3990 4012 4017 4039 4060 4061 4061 4061 4064 4069 4075 4076 4078 4082 4089 4090 4099 4118 4149 4160 4160 4170 4173 4176 4191 4191 4195 4196 4203 4203 4204 4232 4236 4247 4247 4262 4275 4275 4275 4304 4304 4319 4326 4331 4333 4333 4349 4359 4361 4362 4374 4375 4390 4390 4432 4432 4433 4446 4461 4462 4462 4487 4489 4489 4490 4503 4503 4505 4547 4548 4559 4576 4588 4590 4604 4618 4618 4618 4618 4647 4648 4659 4662 4687 4689 4691 4717 4719 4746 4746 4761 4762 4763 4790 4804 4804 4804 4817 4843 4847 4862 4876 4877 4877 4903 4918 4918 4919 4932 4974 4977 4989 4990 4990 4991 5005 5018 5031 5033 5076 5092 5102 5104 5104 5118 5132 5133 5173 5176 5191 5203 5205 5219 5248 5288 5290 5290 5290 5304 5361 5377 5387 5391 5405 5418 5474 5476 5519 5519 5547 5563 5590 5620 5660 5675 5677 5691 5774 5776 5778 5847 5875 5934 6031"
N = 6

peptides = peptides.split(" ")
spectrum = spectrum.split(" ")

print(trim(peptides, spectrum, N))
