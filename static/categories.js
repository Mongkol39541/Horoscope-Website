am4core.ready(function () {
    am4core.useTheme(am4themes_animated);
    var chart = am4core.create("chartdivcategories", am4charts.PieChart);
    chart.hiddenState.properties.opacity = 0;
    let category = document.getElementById("category").value;
    let counts = document.getElementById("counts_category").value;
    let newcategory = category.slice(0, category.length - 1).split(",");
    let newcounts = counts.slice(1, counts.length - 1).split(", ");
    chart.data = [];
    for (let i = 0; i < newcategory.length; i++) {
        chart.data.push({
            category: newcategory[i],
            num: newcounts[i]
        });
    }

    var series = chart.series.push(new am4charts.PieSeries());
    series.dataFields.value = "num";
    series.dataFields.radiusValue = "num";
    series.dataFields.category = "category";
    series.slices.template.cornerRadius = 6;
    series.colors.step = 3;

    series.hiddenState.properties.endAngle = -90;

    chart.legend = new am4charts.Legend();
});

am4core.ready(function () {
    am4core.useTheme(am4themes_animated);
    var chart = am4core.create("pricecategories", am4charts.XYChart);
    chart.hiddenState.properties.opacity = 0;
    let category = document.getElementById("category").value;
    let counts = document.getElementById("price_category").value;
    let newcategory = category.slice(0, category.length - 1).split(",");
    let newcounts = counts.slice(1, counts.length - 1).split(", ");
    chart.data = [];
    for (let i = 0; i < newcategory.length; i++) {
        chart.data.push({
            category: newcategory[i],
            num: newcounts[i]
        });
    }

    let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
    categoryAxis.dataFields.category = "category";
    categoryAxis.renderer.labels.template.rotation = 270;
    categoryAxis.renderer.labels.template.hideOversized = false;
    categoryAxis.renderer.minGridDistance = 20;
    categoryAxis.renderer.labels.template.horizontalCenter = "right";
    categoryAxis.renderer.labels.template.verticalCenter = "middle";
    categoryAxis.tooltip.label.rotation = 270;
    categoryAxis.tooltip.label.horizontalCenter = "right";
    categoryAxis.tooltip.label.verticalCenter = "middle";

    let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
    valueAxis.title.text = "Price (Baht)";

    // Create series
    var series = chart.series.push(new am4charts.ColumnSeries3D());
    series.dataFields.valueY = "num";
    series.dataFields.categoryX = "category";
    series.tooltipText = "{categoryX}: {valueY}[/] บาท";
    series.columns.template.fillOpacity = .8;

    var columnTemplate = series.columns.template;
    columnTemplate.strokeWidth = 2;
    columnTemplate.strokeOpacity = 1;
    columnTemplate.stroke = am4core.color("#FFFFFF");

    columnTemplate.adapter.add("fill", function (fill, target) {
        return chart.colors.getIndex(target.dataItem.index);
    })

    columnTemplate.adapter.add("stroke", function (stroke, target) {
        return chart.colors.getIndex(target.dataItem.index);
    })

    chart.cursor = new am4charts.XYCursor();
    chart.cursor.lineX.strokeOpacity = 0;
    chart.cursor.lineY.strokeOpacity = 0;
});