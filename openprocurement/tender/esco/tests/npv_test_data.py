from datetime import date


NPV_PERIODS = 21
NBU_DISCOUNT_RATE = 0.125
ANNUAL_COSTS_REDUCTION = [
    92.47, 250, 250, 250, 250, 250, 250, 250,
    250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250
]

CONTRACT_DURATION_CHANGING = {
    'yearlyPaymentsPercentage': 0.70,
    'annualCostsReduction': ANNUAL_COSTS_REDUCTION,
    'announcementDate': date(2017, 8, 18),
    'contractDuration': [
        {'years': 15, 'days': 0},
        {'years': 0, 'days': 1},
        {'years': 3, 'days': 11},
        {'years': 3, 'days': 12},
        {'years': 3, 'days': 13},
        {'years': 3, 'days': 14},
        {'years': 3, 'days': 15},
        {'years': 4, 'days': 15},
        {'years': 5, 'days': 15},
        {'years': 6, 'days': 15},
        {'years': 7, 'days': 15},
    ],
    'NBUdiscountRate': NBU_DISCOUNT_RATE,
    'calculated': [
        {
            'amountContract': 2625,
            'amountPerformance': 650.193823614962
        },
        {
            'amountContract': 0.479452054794521,
            'amountPerformance': 1810.49202999925
        },
        {
            'amountContract': 530.27397260274,
            'amountPerformance': 1390.67464457115
        },
        {
            'amountContract': 530.753424657534,
            'amountPerformance': 1390.35279031706
        },
        {
            'amountContract': 531.232876712329,
            'amountPerformance': 1390.03093606298
        },
        {
            'amountContract': 531.712328767123,
            'amountPerformance': 1389.70908180889
        },
        {
            'amountContract': 532.191780821918,
            'amountPerformance': 1389.38722755481
        },
        {
            'amountContract': 707.191780821918,
            'amountPerformance': 1280.67201284187
        },
        {
            'amountContract': 882.191780821918,
            'amountPerformance': 1184.03626643037
        },
        {
            'amountContract': 1057.191780821920,
            'amountPerformance': 1098.13782517570
        },
        {
            'amountContract': 1232.191780821920,
            'amountPerformance': 1021.78365517155
        },
    ]
}

ANNOUNCEMENT_DATE_CHANGING = {
    'yearlyPaymentsPercentage': 0.70,
    'annualCostsReduction': ANNUAL_COSTS_REDUCTION,
    'contractDuration': {
        'years': 2,
        'days': 10,
    },
    'announcementDate': [
        date(2017, 5, 2),
        date(2017, 5, 3),
        date(2017, 5, 4),
        date(2017, 5, 5),
        date(2017, 5, 6),
        date(2017, 5, 7),
        date(2017, 5, 8),
        date(2017, 5, 9),
        date(2017, 5, 10),
        date(2017, 5, 11),
    ],
    'NBUdiscountRate': NBU_DISCOUNT_RATE,
    'calculated': [
        {
            'amountContract': 303.016671232877,
            'amountPerformance': 1493.11261864549
        },
        {
            'amountContract': 303.496123287671,
            'amountPerformance': 1493.29714530232
        },
        {
            'amountContract': 303.975575342466,
            'amountPerformance': 1493.48174786072
        },
        {
            'amountContract': 304.455027397260,
            'amountPerformance': 1493.66642643300
        },
        {
            'amountContract': 304.934479452055,
            'amountPerformance': 1493.85118113158
        },
        {
            'amountContract': 305.413931506849,
            'amountPerformance': 1494.03601206895
        },
        {
            'amountContract': 305.893383561644,
            'amountPerformance': 1494.22091935769
        },
        {
            'amountContract': 306.372835616438,
            'amountPerformance': 1494.40590311049
        },
        {
            'amountContract': 306.852287671233,
            'amountPerformance': 1494.59096344011
        },
        {
            'amountContract': 307.331739726027,
            'amountPerformance': 1494.77610045941
        },
    ]
}

PAYMENTS_PERCENTAGE_CHANGING = {
    'yearlyPaymentsPercentage': [
        0.7100,
        0.7200,
        0.7300,
        0.7400,
        0.7500,
        0.7600,
        0.7700,
        0.7800,
        0.7900,
        0.8000,
    ],
    'annualCostsReduction': ANNUAL_COSTS_REDUCTION,
    'contractDuration': {
        'years': 2,
        'days': 10,
    },
    'announcementDate': date(2017, 8, 18),
    'NBUdiscountRate': NBU_DISCOUNT_RATE,
    'calculated': [
        {
            'amountContract': 359.866028767123,
            'amountPerformance': 1509.25419393209
        },
        {
            'amountContract': 364.934564383562,
            'amountPerformance': 1505.00489590214
        },
        {
            'amountContract': 370.003100000000,
            'amountPerformance': 1500.75559787220
        },
        {
            'amountContract': 375.071635616438,
            'amountPerformance': 1496.50629984225
        },
        {
            'amountContract': 380.140171232877,
            'amountPerformance': 1492.25700181231
        },
        {
            'amountContract': 385.208706849315,
            'amountPerformance': 1488.00770378236
        },
        {
            'amountContract': 390.277242465753,
            'amountPerformance': 1483.75840575242
        },
        {
            'amountContract': 395.345778082192,
            'amountPerformance': 1479.50910772247
        },
        {
            'amountContract': 400.414313698630,
            'amountPerformance': 1475.25980969253
        },
        {
            'amountContract': 405.482849315069,
            'amountPerformance': 1471.01051166258
        },
    ]
}
