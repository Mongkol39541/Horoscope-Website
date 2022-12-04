var chart_pos = am4core.create(
    "chartdiv_pos",
    am4plugins_forceDirected.ForceDirectedTree
);

// Create series
var series_pos = chart_pos.series.push(
    new am4plugins_forceDirected.ForceDirectedSeries()
);

// Set data
series_pos.data = [
    {
        name: "คู่เลขมงคล",
        children: [
            {
                name: "การเงิน",
                children: [
                    {
                        name: "15",
                        value: 687,
                    },
                    {
                        name: "51",
                        value: 148,
                    },
                    {
                        name: "14",
                        value: 687,
                    },
                    {
                        name: "41",
                        value: 148,
                    },
                    {
                        name: "26",
                        value: 687,
                    },
                    {
                        name: "62",
                        value: 148,
                    },
                    {
                        name: "28",
                        value: 687,
                    },
                    {
                        name: "82",
                        value: 148,
                    },
                    {
                        name: "36",
                        value: 687,
                    },
                    {
                        name: "63",
                        value: 148,
                    },
                    {
                        name: "45",
                        value: 687,
                    },
                    {
                        name: "54",
                        value: 148,
                    },
                    {
                        name: "56",
                        value: 687,
                    },
                    {
                        name: "65",
                        value: 148,
                    },
                    {
                        name: "95",
                        value: 687,
                    },
                    {
                        name: "59",
                        value: 148,
                    },
                    {
                        name: "69",
                        value: 687,
                    },
                    {
                        name: "96",
                        value: 148,
                    },
                    {
                        name: "79",
                        value: 687,
                    },
                    {
                        name: "97",
                        value: 148,
                    },
                ],
            },
            {
                name: "ความรัก",
                children: [
                    {
                        name: "15",
                        value: 148,
                    },
                    {
                        name: "51",
                        value: 687,
                    },
                    {
                        name: "22",
                        value: 148,
                    },
                    {
                        name: "23",
                        value: 687,
                    },
                    {
                        name: "32",
                        value: 148,
                    },
                    {
                        name: "24",
                        value: 687,
                    },
                    {
                        name: "42",
                        value: 148,
                    },
                    {
                        name: "26",
                        value: 687,
                    },
                    {
                        name: "62",
                        value: 148,
                    },
                    {
                        name: "46",
                        value: 687,
                    },
                    {
                        name: "64",
                        value: 148,
                    },
                ],
            },
            {
                name: "การงาน",
                children: [
                    {
                        name: "16",
                        value: 687,
                    },
                    {
                        name: "61",
                        value: 148,
                    },
                    {
                        name: "19",
                        value: 687,
                    },
                    {
                        name: "91",
                        value: 148,
                    },
                    {
                        name: "28",
                        value: 148,
                    },
                    {
                        name: "82",
                        value: 687,
                    },
                    {
                        name: "29",
                        value: 148,
                    },
                    {
                        name: "92",
                        value: 687,
                    },
                    {
                        name: "35",
                        value: 148,
                    },
                    {
                        name: "53",
                        value: 687,
                    },
                    {
                        name: "49",
                        value: 148,
                    },
                    {
                        name: "94",
                        value: 687,
                    },
                    {
                        name: "55",
                        value: 148,
                    },
                    {
                        name: "46",
                        value: 687,
                    },
                    {
                        name: "64",
                        value: 148,
                    },
                    {
                        name: "56",
                        value: 687,
                    },
                    {
                        name: "65",
                        value: 148,
                    },
                    {
                        name: "66",
                        value: 687,
                    },
                ],
            },
            {
                name: "ความมั่นคง",
                children: [
                    {
                        name: "99",
                        value: 148,
                    },
                    {
                        name: "98",
                        value: 687,
                    },
                ],
            },
            {
                name: "การเรียน",
                children: [
                    {
                        name: "14",
                        value: 687,
                    },
                    {
                        name: "41",
                        value: 148,
                    },
                    {
                        name: "15",
                        value: 687,
                    },
                    {
                        name: "51",
                        value: 148,
                    },
                    {
                        name: "16",
                        value: 687,
                    },
                    {
                        name: "61",
                        value: 148,
                    },
                    {
                        name: "45",
                        value: 687,
                    },
                    {
                        name: "54",
                        value: 148,
                    },
                    {
                        name: "93",
                        value: 687,
                    },
                    {
                        name: "39",
                        value: 148,
                    },
                ],
            },
        ],
    },
];

// Set up data fields
series_pos.dataFields.value = "value";
series_pos.dataFields.name = "name";
series_pos.dataFields.children = "children";

// Add labels
series_pos.nodes.template.label.text = "{name}";
series_pos.fontSize = 14;
series_pos.minRadius = 30;
series_pos.maxRadius = 100;

series_pos.centerStrength = 0.5;
series_pos.links.template.distance = 1.5;

var chart_neg = am4core.create(
    "chartdiv_neg",
    am4plugins_forceDirected.ForceDirectedTree
);

// Create series
var series_neg = chart_neg.series.push(
    new am4plugins_forceDirected.ForceDirectedSeries()
);

// Set data
series_neg.data = [
    {
        name: "คู่เลขไม่มงคล",
        children: [
            {
                name: "มีปัญหาด้าน\nการเงิน",
                children: [
                    {
                        name: "88",
                        value: 687,
                    },
                    {
                        name: "68",
                        value: 148,
                    },
                    {
                        name: "86",
                        value: 687,
                    },
                    {
                        name: "75",
                        value: 148,
                    },
                    {
                        name: "57",
                        value: 687,
                    },
                    {
                        name: "38",
                        value: 148,
                    },
                    {
                        name: "83",
                        value: 687,
                    },
                    {
                        name: "37",
                        value: 148,
                    },
                    {
                        name: "73",
                        value: 687,
                    },
                    {
                        name: "34",
                        value: 148,
                    },
                    {
                        name: "43",
                        value: 687,
                    },
                    {
                        name: "27",
                        value: 148,
                    },
                    {
                        name: "72",
                        value: 687,
                    },
                    {
                        name: "18",
                        value: 148,
                    },
                    {
                        name: "81",
                        value: 687,
                    },
                    {
                        name: "60",
                        value: 148,
                    },
                    {
                        name: "06",
                        value: 687,
                    },
                    {
                        name: "20",
                        value: 148,
                    },
                    {
                        name: "02",
                        value: 687,
                    },
                    {
                        name: "00",
                        value: 148,
                    },
                ],
            },
            {
                name: "ประมาท",
                children: [
                    {
                        name: "88",
                        value: 148,
                    },
                    {
                        name: "13",
                        value: 687,
                    },
                    {
                        name: "31",
                        value: 148,
                    },
                    {
                        name: "12",
                        value: 687,
                    },
                    {
                        name: "21",
                        value: 148,
                    },
                    {
                        name: "11",
                        value: 687,
                    },
                    {
                        name: "03",
                        value: 148,
                    },
                    {
                        name: "30",
                        value: 687,
                    },
                    {
                        name: "10",
                        value: 148,
                    },
                    {
                        name: "01",
                        value: 687,
                    },
                ],
            },
            {
                name: "ชีวิตอุปสรรค",
                children: [
                    {
                        name: "77",
                        value: 148,
                    },
                    {
                        name: "67",
                        value: 687,
                    },
                    {
                        name: "76",
                        value: 148,
                    },
                    {
                        name: "48",
                        value: 687,
                    },
                    {
                        name: "84",
                        value: 148,
                    },
                    {
                        name: "73",
                        value: 687,
                    },
                    {
                        name: "37",
                        value: 148,
                    },
                    {
                        name: "34",
                        value: 687,
                    },
                    {
                        name: "43",
                        value: 148,
                    },
                    {
                        name: "72",
                        value: 687,
                    },
                    {
                        name: "27",
                        value: 148,
                    },
                    {
                        name: "18",
                        value: 687,
                    },
                    {
                        name: "81",
                        value: 148,
                    },
                    {
                        name: "17",
                        value: 687,
                    },
                    {
                        name: "71",
                        value: 148,
                    },
                    {
                        name: "11",
                        value: 687,
                    },
                    {
                        name: "09",
                        value: 148,
                    },
                    {
                        name: "90",
                        value: 687,
                    },
                    {
                        name: "70",
                        value: 148,
                    },
                    {
                        name: "07",
                        value: 687,
                    },
                    {
                        name: "40",
                        value: 148,
                    },
                    {
                        name: "04",
                        value: 687,
                    },
                    {
                        name: "10",
                        value: 148,
                    },
                    {
                        name: "01",
                        value: 687,
                    },
                ],
            },
            {
                name: "ความเครียด",
                children: [
                    {
                        name: "75",
                        value: 148,
                    },
                    {
                        name: "57",
                        value: 687,
                    },
                    {
                        name: "77",
                        value: 148,
                    },
                    {
                        name: "34",
                        value: 687,
                    },
                    {
                        name: "43",
                        value: 148,
                    },
                    {
                        name: "17",
                        value: 687,
                    },
                    {
                        name: "71",
                        value: 148,
                    },
                    {
                        name: "12",
                        value: 687,
                    },
                    {
                        name: "21",
                        value: 148,
                    },
                    {
                        name: "09",
                        value: 687,
                    },
                    {
                        name: "90",
                        value: 148,
                    },
                    {
                        name: "08",
                        value: 687,
                    },
                    {
                        name: "80",
                        value: 148,
                    },
                    {
                        name: "00",
                        value: 687,
                    },
                ],
            },
            {
                name: "ปัญหาด้าน\nความรัก",
                children: [
                    {
                        name: "38",
                        value: 148,
                    },
                    {
                        name: "83",
                        value: 687,
                    },
                    {
                        name: "48",
                        value: 148,
                    },
                    {
                        name: "84",
                        value: 687,
                    },
                    {
                        name: "34",
                        value: 148,
                    },
                    {
                        name: "43",
                        value: 687,
                    },
                    {
                        name: "27",
                        value: 148,
                    },
                    {
                        name: "72",
                        value: 687,
                    },
                    {
                        name: "06",
                        value: 148,
                    },
                    {
                        name: "60",
                        value: 687,
                    },
                    {
                        name: "20",
                        value: 148,
                    },
                    {
                        name: "02",
                        value: 687,
                    },
                ],
            },
            {
                name: "ปัญหาด้าน\nสุขภาพ",
                children: [
                    {
                        name: "08",
                        value: 148,
                    },
                    {
                        name: "80",
                        value: 687,
                    },
                    {
                        name: "09",
                        value: 148,
                    },
                    {
                        name: "90",
                        value: 687,
                    },
                    {
                        name: "70",
                        value: 148,
                    },
                    {
                        name: "07",
                        value: 687,
                    },
                    {
                        name: "50",
                        value: 148,
                    },
                    {
                        name: "05",
                        value: 687,
                    },
                    {
                        name: "03",
                        value: 148,
                    },
                    {
                        name: "30",
                        value: 687,
                    },
                ],
            },
        ],
    },
];

// Set up data fields
series_neg.dataFields.value = "value";
series_neg.dataFields.name = "name";
series_neg.dataFields.children = "children";

// Add labels
series_neg.nodes.template.label.text = "{name}";
series_neg.fontSize = 14;
series_neg.minRadius = 30;
series_neg.maxRadius = 100;

series_neg.centerStrength = 0.5;
series_neg.links.template.distance = 1.5;