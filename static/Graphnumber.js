var chart = am4core.create("grapdiv", am4charts.PieChart3D);
let positive =
    document.getElementById("positive_result").value;
let negative =
    document.getElementById("negative_result").value;

// Let's cut a hole in our Pie chart the size of 40% the radius
chart.innerRadius = am4core.percent(40);

// Add data
chart.data = [{
    "result": "positive",
    "percentage": positive,
    "color": am4core.color("#b3990b")
  }, {
    "result": "negative",
    "percentage": negative,
    "color": am4core.color("#363322")
  }];

// Add and configure Series
var pieSeries = chart.series.push(new am4charts.PieSeries3D());
pieSeries.dataFields.value = "percentage";
pieSeries.dataFields.category = "result";
pieSeries.slices.template.stroke = am4core.color("#fff");
pieSeries.slices.template.strokeWidth = 2;
pieSeries.slices.template.strokeOpacity = 1;
pieSeries.slices.template.propertyFields.fill = "color";

// Disabling labels and ticks on inner circle
pieSeries.labels.template.disabled = true;
pieSeries.ticks.template.disabled = true;

// Disable sliding out of slices
pieSeries.slices.template.states.getKey("hover").properties.shiftRadius = 0;
pieSeries.slices.template.states.getKey("hover").properties.scale = 1.1;