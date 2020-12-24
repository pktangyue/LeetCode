import unittest


class TestSolution(unittest.TestCase):

    def test_removeStones(self):
        Solution = __import__('947_MostStonesRemovedWithSameRowOrColumn').Solution
        self.assertEqual(
            291,
            Solution().removeStones(
                [[1300, 492], [308, 246], [2399, 979], [424, 1003], [1382, 352], [2686, 2001], [1784, 950],
                 [2106, 2548], [889, 2706], [1144, 452], [1019, 1796], [1511, 810], [823, 1380], [255, 2918],
                 [2286, 2404], [677, 2119], [2520, 307], [1748, 2238], [1860, 2325], [916, 553], [2615, 231],
                 [284, 211], [1641, 2115], [576, 1357], [123, 746], [1019, 2059], [1507, 1894], [1364, 2277],
                 [1634, 531], [2062, 2899], [2936, 1638], [921, 524], [1093, 686], [284, 1364], [670, 2649],
                 [2417, 379], [1858, 218], [333, 1665], [177, 2473], [839, 1403], [1045, 1340], [1924, 465],
                 [1255, 287], [29, 1337], [1511, 1629], [659, 1118], [2747, 1355], [2038, 66], [1105, 1190],
                 [2495, 1682], [1727, 1730], [1588, 1668], [2498, 977], [108, 2446], [1188, 10], [490, 1637],
                 [2427, 2241], [391, 2304], [2709, 629], [1506, 1385], [865, 1623], [2241, 2349], [168, 533],
                 [1687, 2773], [2306, 1905], [1649, 2423], [2262, 346], [2675, 1181], [2223, 2249], [1431, 1160],
                 [989, 523], [2133, 1609], [546, 2436], [2730, 1812], [329, 1344], [2393, 1317], [2996, 404],
                 [1348, 1809], [829, 2796], [1490, 2790], [2275, 765], [2113, 1738], [1646, 399], [818, 1195],
                 [748, 680], [185, 498], [988, 2871], [406, 492], [2436, 2318], [1992, 191], [2533, 1294], [2269, 1964],
                 [1160, 1553], [1269, 775], [829, 666], [536, 2527], [1003, 1849], [2407, 2490], [988, 1289],
                 [1075, 2363], [1401, 780], [761, 685], [701, 759], [2816, 554], [1134, 132], [2509, 2237], [878, 1035],
                 [406, 663], [2401, 1275], [45, 1113], [2638, 792], [1787, 2285], [261, 571], [856, 1889], [28, 268],
                 [1282, 1745], [2960, 2124], [1561, 1738], [374, 293], [15, 943], [2231, 1748], [2870, 2418],
                 [2786, 889], [899, 16], [2405, 1729], [2653, 1339], [233, 1908], [2664, 2060], [1566, 1859],
                 [478, 2914], [2675, 2700], [430, 213], [1984, 328], [2692, 2259], [1447, 147], [90, 1309], [147, 1870],
                 [237, 1222], [1433, 2738], [2680, 2317], [1862, 504], [1743, 2163], [2819, 1924], [2661, 2283],
                 [2498, 821], [2868, 2955], [1991, 2521], [881, 243], [1505, 2442], [985, 778], [271, 663], [2143, 82],
                 [2579, 1550], [2706, 16], [1004, 2033], [798, 2480], [511, 1155], [2839, 1528], [1625, 1975],
                 [1216, 2273], [65, 661], [2318, 1489], [1449, 1353], [1646, 1998], [2136, 2838], [2387, 2399],
                 [2255, 2583], [2359, 1949], [2916, 1082], [2373, 552], [1997, 86], [1418, 2113], [2663, 940],
                 [358, 2965], [2133, 1042], [1696, 1282], [2698, 1489], [275, 1287], [2678, 1754], [694, 1993],
                 [2214, 2709], [2465, 1985], [61, 1014], [866, 1632], [2653, 1740], [452, 2809], [745, 1393],
                 [930, 773], [1778, 1884], [1536, 1569], [1308, 466], [1471, 1958], [238, 2858], [2371, 931],
                 [88, 2535], [2968, 143], [1656, 740], [31, 2228], [103, 1726], [2826, 2779], [2718, 2373], [102, 153],
                 [1946, 208], [1453, 2132], [97, 511], [2237, 2726], [1245, 2258], [219, 780], [2751, 2957],
                 [2067, 2592], [1406, 479], [287, 1456], [2807, 2331], [1812, 2906], [2947, 866], [174, 2442],
                 [938, 487], [2716, 2377], [1410, 1869], [260, 1694], [1607, 771], [1090, 2376], [196, 1922],
                 [2787, 2434], [1498, 1111], [689, 1994], [973, 2442], [1888, 824], [2121, 1884], [2812, 2594],
                 [1249, 2502], [2055, 2001], [2702, 564], [2029, 2773], [348, 1284], [38, 72], [1552, 1694],
                 [2390, 1999], [2979, 126], [2564, 2960], [759, 677], [2099, 558], [2640, 2705], [2102, 98],
                 [1120, 879], [1091, 1982], [2925, 1500], [1422, 58], [2479, 2883], [913, 26], [1419, 2604],
                 [2621, 2523], [1110, 249], [601, 1547], [979, 1725], [1112, 973], [1983, 1377], [1599, 700],
                 [936, 227], [379, 915], [1024, 2630], [1963, 2389], [1077, 1127], [1557, 1325], [1427, 1096],
                 [1563, 116], [2763, 1567], [1068, 460], [646, 1442], [2891, 2331], [87, 2234], [2555, 997],
                 [482, 2693], [883, 95], [2513, 1449], [2482, 2532], [1902, 2918], [2053, 719], [2962, 625],
                 [720, 2740], [2463, 672], [176, 353], [2481, 2724], [376, 2910], [1760, 2309], [901, 2267],
                 [2840, 2784], [1748, 2862], [2293, 1848], [134, 494], [1146, 2679], [2311, 2150], [1564, 1084],
                 [2567, 1272], [1155, 1853], [862, 2023], [1250, 1073], [1230, 2123], [1256, 46], [1861, 1023],
                 [1615, 512], [2936, 494], [1474, 108], [1613, 1779], [907, 2637], [2420, 2586], [2214, 1001],
                 [632, 998], [2262, 529], [853, 450], [1137, 1091], [1107, 803], [244, 591], [1184, 40], [1572, 939],
                 [169, 2003], [124, 1777], [663, 2538], [290, 1119], [2293, 834], [2520, 718], [491, 175], [1912, 2256],
                 [2674, 802], [2593, 2276], [1056, 2668], [2427, 2530], [2988, 1667], [199, 1428], [348, 114],
                 [1862, 2281], [1650, 2343], [2338, 2634], [2726, 846], [799, 2438], [2696, 2657], [1683, 1458],
                 [2392, 452], [1311, 2555], [2984, 1687], [2076, 2569], [2590, 1611], [2522, 2821], [969, 444],
                 [2482, 2440], [1153, 1771], [1774, 912], [2658, 2408], [1635, 1098], [1034, 2041], [1396, 2054],
                 [2385, 1132], [427, 207], [963, 913], [1482, 899], [952, 478], [1346, 1778], [1932, 1613],
                 [1128, 1483], [1888, 881], [1648, 2550], [1671, 1884], [185, 2102], [2530, 1479], [785, 1747],
                 [726, 2519], [2489, 1816], [61, 864], [1688, 439], [1412, 799], [2956, 1635], [813, 790], [2710, 1622],
                 [2509, 923], [1257, 1245], [2719, 56], [2670, 1710], [2371, 2810], [716, 1192], [1702, 2378],
                 [1603, 2187], [1128, 2869], [2702, 2765], [1558, 1198], [2040, 1283], [1468, 1908], [1178, 2062],
                 [497, 1965], [353, 2991], [341, 1556], [2955, 380], [1842, 1476], [196, 2096], [1628, 1493],
                 [1580, 1060], [431, 1543], [739, 1550], [1314, 1328], [2524, 2756], [2742, 823], [979, 2387],
                 [2314, 1906], [757, 446], [1230, 2762], [1907, 2508], [964, 1556], [420, 2470], [1243, 760],
                 [1574, 668], [1193, 1987], [2483, 1710], [2017, 769], [2976, 1861], [943, 1043], [2958, 105],
                 [416, 2376], [634, 2393], [1579, 1351], [1252, 713], [2226, 795], [217, 544], [2545, 2491], [176, 267],
                 [358, 615], [106, 1732], [1249, 410], [1474, 2389], [275, 433], [2772, 353], [2196, 2505], [934, 907],
                 [947, 1207], [232, 1773], [265, 84], [1901, 1027], [1447, 1747], [2679, 2959], [1479, 2282],
                 [2478, 206], [389, 2455], [696, 1023], [748, 1480], [338, 888], [1796, 2383], [1024, 2321],
                 [671, 2454], [147, 822], [1553, 1882], [2119, 846], [434, 310], [909, 1922], [1818, 794], [552, 1409],
                 [1275, 807], [1712, 440], [387, 5], [1718, 610], [2785, 1708], [1485, 1733], [278, 233], [2880, 2928],
                 [586, 2234], [889, 1570], [2502, 1167], [809, 141], [695, 1466], [101, 875], [1421, 430], [2409, 1813],
                 [2467, 2945], [1833, 950], [2485, 404], [2284, 1107], [1451, 1079], [990, 351], [441, 1922],
                 [863, 2179], [293, 2876], [2912, 1399], [453, 2027], [2773, 534], [1857, 2285], [676, 2925],
                 [2894, 974], [1268, 2735], [269, 2411], [1540, 2621], [1335, 2131], [1364, 20], [1834, 586],
                 [2278, 2634], [1551, 1375], [1220, 685], [343, 2202], [2878, 2305], [2443, 1032], [2624, 52],
                 [109, 1169], [1337, 1641], [1264, 1415], [641, 162], [1410, 7], [1230, 2480], [2365, 554],
                 [1210, 2428], [1666, 2528], [2296, 2274], [1588, 869], [2189, 107], [2874, 1493], [496, 1687],
                 [2176, 2961], [1597, 814], [73, 1171], [2194, 2829], [2835, 113], [172, 2829], [1989, 1977],
                 [2333, 1255], [2746, 2193], [2118, 332], [1697, 2466], [7, 2970], [94, 2645], [2595, 351], [732, 1443],
                 [2926, 1478], [2631, 1687], [877, 2333], [2058, 205], [2778, 1384], [1653, 1823], [2107, 2502],
                 [2327, 903], [960, 582], [2391, 2332], [2216, 768], [1475, 2772], [1455, 1994], [2822, 2494],
                 [888, 686], [684, 1055], [448, 2083], [278, 2691], [192, 2104], [2180, 1565], [1714, 2106],
                 [2750, 331], [1504, 1739], [2733, 519], [652, 2250], [983, 519], [2088, 708], [2840, 2233],
                 [1011, 2098], [2994, 664], [1979, 2067], [430, 1004], [415, 1779], [154, 1010], [2729, 2106],
                 [851, 1970], [1116, 2972], [1104, 926], [2308, 239], [513, 689], [565, 2985], [450, 460], [2116, 2680],
                 [2991, 2895], [2724, 1574], [1847, 202], [1136, 670], [1577, 2198], [480, 1616], [952, 340],
                 [183, 2020], [475, 833], [1277, 20], [343, 1762], [2474, 1051], [2080, 578], [597, 1907], [1465, 11],
                 [2614, 2903], [143, 1891], [2904, 1563], [1081, 475], [2838, 102], [792, 458], [2336, 1206],
                 [2141, 2621], [1378, 542], [2902, 2608], [1767, 0], [2983, 637], [1802, 383], [1125, 2160],
                 [491, 1716], [1935, 2426], [781, 2614], [2456, 2224], [305, 853], [1926, 758], [2132, 970],
                 [473, 2883], [2333, 91], [2083, 1336], [1083, 1787], [2210, 2514], [1986, 1512], [1803, 1250],
                 [1844, 266], [1760, 709], [2981, 672], [1070, 2434], [847, 91], [799, 1960], [2484, 1626],
                 [2032, 2205], [844, 1523], [474, 2727], [2125, 2087], [235, 1836], [2692, 331], [141, 619],
                 [1854, 705], [845, 919], [43, 421], [69, 1753], [1207, 1077], [221, 1378], [2110, 371], [80, 1710],
                 [187, 1922], [2384, 2189], [2501, 1514], [1445, 901], [1274, 681], [584, 2697], [1761, 2501],
                 [1773, 2653], [631, 1467], [1855, 739], [2003, 852], [1529, 1161], [1272, 2206], [1954, 1532],
                 [508, 1744], [2819, 503], [1428, 191], [2772, 2273], [2075, 2675], [2144, 1287], [2221, 465],
                 [1748, 2268], [1972, 1224], [2806, 2488], [2026, 881], [1186, 104], [2702, 2001], [2834, 2535],
                 [243, 2947], [1697, 860], [1808, 2830], [2021, 2838], [603, 2605], [344, 318], [1868, 1679],
                 [2288, 592], [734, 527], [2041, 1521], [625, 1735], [1384, 64], [264, 223], [1775, 124], [1109, 2614],
                 [1080, 280], [413, 1570], [403, 2848], [1584, 2221], [2201, 2876], [865, 155], [178, 780],
                 [2995, 2470], [891, 2293], [2873, 1266], [1932, 2682], [492, 1964], [499, 1016], [2353, 374],
                 [2945, 106], [228, 2338], [683, 618], [2689, 1881], [2635, 1157], [872, 2881], [1107, 943],
                 [2752, 651], [203, 2549], [1636, 1598], [2342, 420], [505, 276], [2266, 1002], [821, 1278], [609, 156],
                 [732, 2098], [1318, 1289], [2873, 75], [1627, 263], [983, 2275], [2800, 512], [748, 1744],
                 [2075, 2146], [1717, 2898], [1966, 424], [308, 2861], [1894, 958], [502, 1318], [2602, 2816],
                 [2496, 399], [928, 696], [2392, 2404], [1155, 735], [2052, 172], [1754, 2795], [1272, 119], [189, 665],
                 [2404, 671], [2213, 2691], [1695, 2354], [2897, 1290], [1748, 2177], [1586, 2148], [712, 317],
                 [2300, 2587], [1546, 410], [290, 655], [330, 1440], [1646, 1787], [2969, 942], [1100, 2191],
                 [2467, 2201], [2413, 1101], [1558, 301], [2028, 2592], [96, 1870], [1020, 2574], [2283, 149],
                 [1097, 2323], [35, 1802], [2605, 1760], [1486, 747], [1753, 1424], [2674, 2585], [2603, 2591],
                 [1352, 715], [265, 2281], [266, 2354], [2097, 90], [2560, 926], [2755, 2297], [2340, 1953],
                 [185, 2355], [2050, 1495], [770, 556], [937, 37], [1522, 2133], [754, 2219], [1427, 2674], [598, 2072],
                 [636, 2251], [2717, 490], [2461, 172], [1646, 2261], [2596, 2197], [547, 2023], [2139, 1730],
                 [18, 2967], [464, 1304], [1312, 2009], [635, 2546], [2914, 1795], [1755, 2396], [2913, 1057],
                 [2414, 470], [236, 706], [1627, 1070], [2392, 1776], [750, 2567], [746, 2607], [2763, 1303],
                 [2786, 1260], [2894, 2275], [292, 2111], [944, 274], [345, 2583], [999, 500], [1407, 459],
                 [2641, 2240], [1699, 715], [2698, 2073], [1773, 582], [2857, 708], [551, 700], [2792, 2683],
                 [443, 439], [941, 2296], [1300, 1781], [2640, 355], [2132, 2155], [608, 2833], [607, 2637],
                 [1224, 1927], [1153, 413], [778, 2415], [2793, 992], [662, 2221], [1458, 1496], [1636, 2799],
                 [2632, 2634], [2468, 208], [168, 924], [1810, 1172], [2940, 2456], [1189, 1321], [1782, 760],
                 [1240, 2663], [2163, 1501], [2042, 1373], [2089, 2131], [2440, 1455], [2770, 1228], [2174, 154],
                 [1605, 2960], [2601, 1812], [2600, 1889], [1799, 198], [2725, 1423], [651, 2936], [749, 105],
                 [2093, 2389], [647, 992], [1649, 1692], [988, 864], [105, 0], [209, 781], [1517, 1013], [1047, 1889],
                 [626, 2325], [2224, 173], [1226, 2108], [2951, 1537], [311, 2562], [671, 381], [83, 2787],
                 [2308, 1684], [1257, 1863], [2319, 52], [2409, 2229], [2623, 218], [1926, 2256], [1245, 2179],
                 [2906, 2406], [893, 1488], [661, 1806], [1604, 778], [2200, 723], [1013, 1487], [2991, 1751],
                 [1466, 2115], [2249, 2931], [1730, 1023], [2114, 779], [1935, 1372], [1404, 1186], [2673, 56],
                 [1355, 878], [2398, 83], [1346, 1371], [2738, 1911], [1758, 2260], [1086, 1289], [2992, 1099],
                 [2494, 977], [1547, 694], [1885, 291], [692, 1796], [791, 2584], [2224, 592], [2056, 2082],
                 [2103, 2108], [1118, 1341], [165, 1593], [1286, 89], [1018, 1613], [1687, 947], [1986, 444],
                 [137, 169], [2983, 2610], [1769, 2651], [608, 1668], [1913, 2633], [2268, 2354], [2060, 1999],
                 [287, 1800], [1285, 2541], [960, 748], [2218, 2959], [1331, 911], [2190, 1153], [1064, 1062],
                 [1926, 826], [1006, 439], [645, 2015], [2210, 434], [1947, 1163], [2267, 143], [1766, 660],
                 [517, 2014], [1839, 333], [333, 1325], [708, 2014], [2359, 2866], [224, 2959], [753, 551], [383, 356],
                 [1051, 2333], [2722, 797], [743, 85], [390, 2973], [1428, 661], [1340, 146], [2277, 2658], [328, 2516],
                 [1926, 2772], [184, 2904], [709, 2306], [1453, 2347], [2707, 2405], [1110, 1245], [204, 1885],
                 [2332, 218], [394, 2557], [1152, 1021], [2321, 79], [1174, 1942], [2731, 2216], [2629, 1713],
                 [837, 2872], [391, 644], [1301, 1897], [2962, 2044], [2645, 2795], [2681, 674], [163, 2897],
                 [157, 1851], [2306, 1849], [1768, 1579], [1032, 1109], [2513, 1205], [180, 1952], [1657, 2205],
                 [882, 2317], [1456, 784], [2140, 343], [2094, 2732], [132, 185], [2537, 1829], [2003, 1215],
                 [2242, 2630], [646, 454], [645, 1809], [2287, 262], [1900, 606], [628, 1158], [2202, 240], [812, 1085],
                 [192, 866], [1420, 1128], [2722, 1895], [184, 1192], [958, 1684], [2301, 392], [2728, 1558],
                 [2018, 341], [1292, 2552], [702, 1430], [480, 1803], [1496, 2955], [1549, 244], [2087, 226],
                 [2114, 2160], [1127, 1632], [2367, 114], [1554, 34], [2318, 402], [2900, 2602], [934, 2892],
                 [1687, 2471]])
        )
        self.assertEqual(
            713,
            Solution().removeStones(
                [[142, 714], [72, 205], [239, 692], [738, 542], [467, 57], [396, 528], [570, 455], [888, 349],
                 [682, 419], [153, 317], [544, 667], [589, 815], [970, 819], [774, 212], [905, 932], [992, 182],
                 [21, 794], [225, 780], [501, 406], [983, 55], [93, 151], [443, 383], [212, 334], [626, 163],
                 [166, 732], [741, 876], [415, 863], [357, 46], [803, 348], [824, 130], [589, 371], [405, 493],
                 [704, 695], [264, 494], [802, 595], [420, 580], [404, 352], [728, 2], [908, 331], [570, 880],
                 [469, 556], [606, 39], [358, 861], [688, 703], [195, 330], [241, 184], [596, 104], [373, 966],
                 [565, 594], [472, 884], [198, 243], [291, 559], [130, 371], [597, 412], [10, 454], [265, 489],
                 [180, 359], [364, 849], [754, 201], [846, 355], [354, 219], [47, 753], [853, 302], [339, 479],
                 [254, 643], [297, 508], [152, 804], [834, 791], [838, 823], [33, 60], [713, 383], [591, 378],
                 [904, 547], [836, 99], [693, 406], [400, 189], [23, 928], [597, 421], [195, 593], [386, 915],
                 [593, 777], [797, 421], [1, 584], [55, 480], [979, 820], [430, 203], [415, 582], [401, 425], [607, 50],
                 [920, 134], [578, 212], [674, 397], [759, 914], [210, 524], [302, 522], [175, 183], [984, 583],
                 [536, 641], [365, 741], [702, 470], [188, 34], [448, 223], [727, 97], [766, 4], [915, 286], [150, 407],
                 [384, 486], [505, 764], [503, 921], [438, 663], [774, 614], [778, 755], [559, 799], [676, 316],
                 [37, 758], [483, 261], [343, 927], [0, 718], [89, 911], [557, 934], [445, 961], [101, 148], [395, 846],
                 [488, 316], [627, 299], [740, 74], [152, 755], [961, 214], [838, 592], [992, 294], [178, 107],
                 [770, 871], [24, 893], [617, 232], [526, 344], [359, 57], [932, 364], [222, 446], [689, 974],
                 [694, 162], [833, 846], [236, 223], [707, 766], [427, 320], [323, 745], [821, 144], [275, 906],
                 [167, 258], [636, 571], [125, 660], [733, 618], [41, 343], [244, 412], [858, 627], [69, 641],
                 [821, 455], [589, 917], [13, 593], [55, 452], [371, 19], [801, 123], [910, 248], [987, 742],
                 [878, 123], [377, 630], [675, 974], [730, 559], [643, 665], [851, 635], [559, 810], [603, 551],
                 [397, 306], [309, 688], [970, 730], [771, 48], [857, 469], [672, 832], [36, 147], [440, 560],
                 [186, 585], [461, 539], [109, 447], [969, 17], [828, 562], [173, 930], [561, 201], [890, 1],
                 [105, 213], [911, 437], [604, 169], [36, 827], [382, 118], [863, 940], [955, 577], [851, 512],
                 [349, 850], [964, 289], [161, 180], [414, 774], [320, 851], [322, 791], [508, 303], [169, 37],
                 [100, 62], [88, 456], [107, 420], [623, 194], [809, 514], [275, 154], [768, 484], [799, 269],
                 [267, 452], [986, 930], [868, 893], [941, 759], [725, 164], [747, 986], [115, 207], [365, 487],
                 [263, 540], [819, 298], [825, 458], [384, 150], [313, 670], [797, 542], [680, 35], [398, 993],
                 [759, 283], [714, 837], [474, 404], [257, 524], [955, 463], [810, 781], [604, 667], [558, 377],
                 [513, 784], [283, 820], [676, 360], [948, 725], [757, 520], [22, 110], [927, 313], [750, 98],
                 [222, 44], [134, 413], [730, 392], [38, 564], [936, 787], [230, 849], [107, 109], [736, 160],
                 [521, 788], [242, 34], [214, 531], [158, 380], [914, 540], [682, 439], [594, 520], [101, 744],
                 [193, 130], [874, 296], [285, 316], [141, 287], [861, 627], [471, 939], [688, 438], [281, 636],
                 [554, 796], [665, 311], [813, 460], [337, 998], [618, 369], [998, 806], [984, 465], [585, 53],
                 [274, 410], [347, 752], [946, 863], [873, 664], [495, 686], [899, 802], [261, 976], [912, 124],
                 [126, 188], [401, 355], [408, 299], [120, 426], [525, 448], [105, 186], [783, 22], [386, 584],
                 [6, 278], [761, 646], [81, 65], [202, 445], [296, 357], [35, 277], [337, 872], [121, 203], [88, 533],
                 [589, 58], [754, 388], [537, 44], [97, 50], [544, 645], [500, 742], [54, 245], [348, 101], [60, 703],
                 [29, 777], [999, 390], [286, 866], [340, 513], [380, 995], [733, 118], [630, 584], [155, 991],
                 [778, 701], [952, 136], [273, 262], [537, 388], [665, 690], [525, 458], [575, 302], [9, 841], [90, 43],
                 [272, 186], [127, 994], [788, 168], [93, 14], [558, 168], [575, 842], [584, 653], [229, 122],
                 [982, 93], [896, 542], [721, 978], [3, 943], [695, 173], [392, 418], [448, 697], [151, 506],
                 [651, 181], [318, 435], [642, 848], [458, 574], [793, 881], [278, 438], [176, 861], [728, 858],
                 [13, 187], [144, 507], [65, 340], [216, 830], [472, 896], [234, 459], [880, 516], [992, 537],
                 [314, 637], [938, 6], [903, 743], [301, 679], [970, 439], [825, 981], [249, 503], [810, 220],
                 [499, 885], [636, 401], [201, 707], [642, 660], [440, 36], [311, 379], [51, 983], [949, 640],
                 [744, 929], [617, 437], [74, 53], [368, 405], [42, 218], [996, 194], [210, 693], [691, 788],
                 [310, 276], [153, 760], [393, 74], [590, 458], [420, 661], [700, 39], [352, 616], [371, 533],
                 [485, 106], [851, 48], [318, 817], [262, 994], [653, 296], [717, 971], [793, 554], [462, 112],
                 [192, 175], [541, 892], [769, 132], [454, 862], [591, 520], [885, 69], [557, 947], [734, 289],
                 [176, 482], [331, 382], [81, 320], [730, 738], [965, 409], [53, 298], [223, 547], [331, 786],
                 [80, 376], [492, 775], [997, 8], [680, 438], [748, 20], [622, 415], [70, 40], [749, 824], [684, 377],
                 [406, 185], [632, 367], [890, 887], [539, 413], [852, 121], [412, 176], [820, 821], [654, 996],
                 [14, 179], [788, 993], [646, 852], [46, 419], [930, 849], [571, 669], [251, 800], [25, 563], [39, 320],
                 [868, 851], [942, 883], [484, 657], [641, 229], [230, 737], [744, 397], [226, 357], [391, 921],
                 [923, 764], [32, 97], [72, 579], [34, 774], [74, 811], [666, 946], [666, 992], [205, 292], [432, 379],
                 [359, 678], [612, 740], [433, 103], [346, 253], [720, 450], [481, 517], [287, 544], [231, 829],
                 [724, 483], [907, 200], [91, 789], [646, 695], [120, 267], [766, 824], [882, 76], [907, 71], [23, 854],
                 [15, 669], [435, 758], [442, 166], [297, 294], [706, 666], [994, 811], [477, 480], [765, 549],
                 [341, 944], [18, 501], [262, 167], [982, 187], [985, 709], [748, 295], [898, 439], [493, 625],
                 [976, 955], [429, 905], [469, 77], [792, 839], [613, 139], [173, 825], [356, 782], [530, 689],
                 [711, 313], [34, 928], [718, 751], [191, 513], [933, 208], [307, 63], [574, 649], [204, 908],
                 [904, 639], [597, 163], [108, 619], [90, 490], [626, 232], [610, 741], [224, 823], [798, 190],
                 [797, 231], [729, 690], [689, 217], [287, 373], [911, 912], [287, 543], [737, 770], [258, 912],
                 [871, 717], [857, 38], [838, 0], [622, 301], [336, 820], [775, 60], [388, 322], [215, 147], [976, 937],
                 [569, 214], [44, 839], [155, 691], [562, 209], [322, 128], [269, 391], [493, 937], [994, 59],
                 [207, 719], [778, 671], [982, 407], [750, 546], [702, 936], [848, 855], [39, 825], [838, 123],
                 [70, 716], [608, 552], [326, 752], [793, 253], [260, 892], [188, 753], [463, 919], [802, 712],
                 [51, 17], [713, 841], [795, 158], [673, 459], [251, 764], [89, 188], [931, 187], [298, 144],
                 [924, 252], [85, 637], [728, 655], [24, 929], [633, 278], [618, 671], [728, 574], [437, 289],
                 [300, 901], [395, 155], [683, 500], [246, 183], [196, 904], [88, 17], [986, 320], [87, 989],
                 [769, 287], [458, 325], [247, 278], [283, 780], [459, 499], [694, 851], [308, 711], [148, 134],
                 [61, 457], [498, 776], [631, 550], [924, 409], [840, 964], [692, 730], [731, 474], [880, 453],
                 [625, 713], [337, 84], [609, 529], [473, 546], [543, 232], [829, 133], [868, 160], [890, 815],
                 [120, 792], [835, 582], [415, 437], [680, 517], [128, 194], [393, 958], [754, 855], [154, 538],
                 [321, 845], [948, 286], [933, 429], [988, 885], [226, 645], [527, 67], [447, 730], [858, 264],
                 [435, 483], [864, 100], [297, 857], [542, 941], [599, 708], [837, 938], [622, 208], [626, 376],
                 [994, 587], [428, 721], [451, 915], [103, 977], [20, 529], [242, 311], [177, 74], [303, 835],
                 [788, 75], [513, 608], [204, 255], [690, 264], [912, 333], [877, 725], [290, 154], [642, 167],
                 [649, 276], [179, 553], [736, 843], [473, 795], [699, 171], [702, 275], [335, 240], [411, 226],
                 [521, 163], [33, 225], [874, 149], [819, 556], [307, 269], [143, 947], [185, 584], [115, 724],
                 [260, 637], [355, 98], [66, 926], [485, 336], [841, 354], [537, 601], [922, 552], [460, 479],
                 [466, 818], [935, 3], [541, 830], [17, 756], [0, 966], [366, 218], [683, 526], [227, 199], [464, 755],
                 [818, 811], [365, 957], [534, 24], [724, 449], [420, 110], [819, 930], [306, 563], [588, 528],
                 [718, 991], [829, 932], [837, 659], [928, 790], [81, 885], [516, 452], [460, 549], [815, 157],
                 [874, 699], [33, 828], [656, 857], [568, 635], [6, 521], [977, 915], [638, 777], [969, 342],
                 [271, 257], [597, 838], [764, 300], [621, 117], [866, 380], [252, 623], [199, 357], [53, 984],
                 [559, 367], [48, 460], [363, 612], [561, 725], [305, 185], [696, 535], [966, 694], [803, 784],
                 [972, 764], [920, 532], [697, 292], [883, 663], [548, 210], [930, 629], [901, 345], [958, 753],
                 [833, 563], [280, 429], [923, 670], [416, 866], [844, 149], [510, 428], [353, 972], [133, 459],
                 [433, 417], [938, 698], [61, 185], [779, 313], [235, 433], [845, 67], [313, 517], [906, 652],
                 [288, 197], [52, 870], [978, 852], [651, 208], [728, 339], [655, 887], [565, 416], [716, 954],
                 [24, 527], [649, 394], [61, 65], [671, 162], [267, 405], [717, 288], [335, 279], [700, 495],
                 [615, 764], [653, 596], [286, 728], [783, 241], [625, 424], [488, 660], [363, 698], [787, 867],
                 [754, 252], [280, 640], [632, 597], [191, 647], [854, 547], [820, 631], [140, 411], [290, 607],
                 [354, 266], [869, 884], [37, 162], [402, 823], [373, 250], [566, 762], [614, 120], [999, 235],
                 [602, 262], [298, 42], [617, 949], [567, 681], [719, 73], [477, 334], [99, 474], [107, 138], [78, 402],
                 [3, 554], [794, 291], [465, 980], [999, 147], [269, 776], [113, 816], [477, 762], [499, 661],
                 [961, 632], [284, 996], [746, 75], [436, 735], [347, 934], [385, 722], [689, 643], [500, 550],
                 [780, 107], [67, 413], [567, 678], [766, 969], [184, 212], [115, 850], [299, 840], [913, 980],
                 [839, 665], [400, 758], [130, 470], [730, 793], [397, 385], [937, 705], [791, 156], [621, 838],
                 [527, 646], [260, 798], [134, 430], [983, 144], [306, 76], [89, 356], [352, 754], [815, 61],
                 [957, 112], [856, 2], [295, 896], [658, 725], [460, 399], [317, 957], [853, 160], [850, 928],
                 [108, 409], [955, 234], [650, 225], [851, 864], [504, 11], [228, 79], [292, 295], [582, 525],
                 [403, 902], [354, 882], [63, 846], [503, 521], [749, 230], [574, 915], [248, 789], [778, 668],
                 [212, 688], [472, 616], [514, 467], [53, 384], [238, 900], [222, 265], [539, 12], [848, 402],
                 [744, 195], [104, 162], [984, 167], [268, 672], [340, 821], [446, 72], [95, 876], [25, 795],
                 [322, 581], [306, 126], [680, 847], [931, 497], [259, 76], [170, 529], [47, 894], [49, 107], [34, 257],
                 [135, 602], [471, 355], [163, 562], [847, 338], [173, 383], [780, 297], [321, 564], [606, 410],
                 [186, 608], [795, 300], [509, 181], [946, 327], [988, 315], [833, 801], [9, 122], [726, 642],
                 [966, 157], [218, 288], [230, 664], [510, 710], [919, 435], [97, 376], [445, 925], [194, 722],
                 [257, 488], [812, 158], [65, 874], [524, 362], [197, 3], [923, 784], [608, 219], [338, 965],
                 [851, 433], [876, 479], [485, 143], [888, 501], [781, 907], [784, 779], [754, 312], [545, 192],
                 [61, 363], [49, 920], [546, 134], [231, 63], [492, 970], [401, 464], [99, 888], [299, 305], [724, 569],
                 [873, 385], [30, 884], [183, 41], [718, 27], [797, 195], [322, 229], [749, 864], [21, 789], [845, 229],
                 [157, 575], [601, 294], [527, 970], [525, 875], [290, 700], [846, 36], [777, 329], [263, 196],
                 [636, 930], [784, 603], [786, 393], [524, 930], [987, 600], [736, 659], [313, 44], [46, 782],
                 [351, 475], [808, 570], [883, 725], [479, 701], [44, 577], [817, 992], [802, 830], [285, 522],
                 [793, 161], [416, 1], [696, 382], [53, 212], [790, 13], [296, 705], [623, 32], [286, 875], [692, 18],
                 [275, 384], [848, 334], [664, 996], [613, 669], [357, 260], [989, 276], [666, 380], [614, 981],
                 [894, 138], [752, 334], [532, 207], [275, 94], [649, 800], [409, 126], [778, 900], [584, 694],
                 [797, 824], [174, 884], [84, 687], [305, 763], [568, 319], [494, 997], [939, 357], [978, 111],
                 [828, 953], [47, 351], [638, 221], [468, 256], [253, 161], [460, 471], [150, 970]])
        )
        self.assertEqual(
            5,
            Solution().removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]])
        )
        self.assertEqual(
            3,
            Solution().removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]])
        )
        self.assertEqual(
            0,
            Solution().removeStones([[0, 0]])
        )