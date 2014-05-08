var storyData = [];

function ajaxStoryData(){
  $.ajax({
      type: "GET",
      url: "https://dl.dropboxusercontent.com/u/23549740/storyData.json",
      dataType: "json",
      async: false,
      success: function(data) { processStoryData(data);}
   });
}

function processStoryData(data) {
  for (var i in data) {
    storyData[i] = data[i];
  }
}

function chart(csvpath, runningpath, color) {
  var colorrange = [];

  if (color == "blue") {
    colorrange = ["#00A4E1", "#A300D5", "#6CCA00", "#C23300", "#6500D9", "#5f6772"];
  }
  else if (color == "pink") {
    colorrange = ["#980043", "#DD1C77", "#DF65B0", "#C994C7", "#D4B9DA", "#F1EEF6"];
  }
  else if (color == "orange") {
    colorrange = ["#41046F", "#052D6E", "#FF5F00", "#FFAD00", "#A67000", "#910033"];
  } 
  strokecolor = colorrange[0];

  var margin = {top: 20, right: 0, bottom: 30, left: 0},
      width = document.body.clientWidth - margin.left - margin.right + 2550;
      height = 500 - margin.top - margin.bottom;

  var numDays = 708/width;

  var parseDate = d3.time.format("%Y%m%d").parse;

  var currentDate, location, storyBlurb, storyPopup;

  var storyTooltipWidth = 100;
  
  var storyTooltipHeight = 20;

  var x = d3.time.scale()
      .range([0, width]);

  var y = d3.scale.linear()
      .range([height+100, 0]);

  var z = d3.scale.ordinal()
      .range(colorrange);

  var color = d3.scale.category10();

  var xAxis = d3.svg.axis()
      .scale(x)
      .ticks(d3.time.months)
      .tickSize(-height)
      .tickSubdivide(true);

  var xAxisYear = d3.svg.axis()
      .scale(x)
      .tickSize(-height)
      .ticks(d3.time.years);

  var yAxis = d3.svg.axis()
      .scale(y)
      .orient("left");

  var nest = d3.nest()
      .key(function(d) { return d.key; });

  var stack = d3.layout.stack()
      .values(function(d) { return d.values; })
      .x(function(d) { return d.date; })
      .y(function(d) { return d.value; });

  var area = d3.svg.area()
      .x(function(d) { return x(d.date); })
      .y0(height)
      .y1(function(d) { return y(d.value); });

  var line = d3.svg.line()
      .interpolate("basis")
      .x(function(d) { return x(d.date); })
      .y(function(d) { return y(d.value); });

  var svg = d3.select("#container").append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  function getMonthAndYear(x) {
    var numDaysToAdd = numDays * x;
    var newDate = new Date(2012, 5, 1);
    newDate.setDate(numDaysToAdd);
    return newDate;
  }

  function getStoryData(date){
    fullDate = formatDate(date);
    return storyData[fullDate];
  }

  function formatDate(date){
    var month = date.getMonth();
    month++;
    month = month.toString();
    if (month.length == 1) {
      month = "0" + month;
    }
    var day = date.getDate().toString();
    if (day.length == 1) {
      day = "0" + day;
    }
    var year = date.getFullYear();
    var fullDate = month.toString() + "/" + day.toString() + "/" + year.toString();
    return fullDate;
  }

  function createToolTip(x, y, selected, story, currentDate) {
    //console.log(selected);
    var firstDate = new Date(2012, 5, 1);
    var diff = currentDate.getTime() - firstDate.getTime();
    var index = Math.round(diff / (1000*60*60*24));
    //console.log(index);
    var weather = selected[index].value;
    var type = selected[index].key;
    var location = story["Location"];
    var story = story['Story'];
    storyPopup = d3.select("#storyTooltip")
      .html(location + "</br>" + type + ": " +  weather + "</br><div id='story'>" + story + "</div>")
      .style("min-height", storyTooltipHeight + "px")
      .style("width", storyTooltipWidth + "px");

    var h = $("#storyTooltip").outerHeight();
    var w = $("#storyTooltip").outerWidth();
    var yOffset = storyTooltipHeight;
    var textAlign = "right";
    if(x < w) {
      w = 0;
      textAlign = "left";
    }

    storyPopup
      .style("margin-left", (x - w - 6)+"px") 
      .style("margin-top", (y - 10)+"px")
      .style("display", "block")
      .style("text-align", textAlign);
  }

  //CREATE WEATHER MAPS
  d3.csv(csvpath, function(error, data) {
    data.forEach(function(d) {
      d.date = parseDate(d.date);
      d.value = +d.value;
    });

    var layers = stack(nest.entries(data));

    x.domain(d3.extent(data, function(d) { return d.date; }));
    y.domain([0, d3.max(data, function(d) { return d.value; })]);


    svg.selectAll(".layer")
      .data(layers)
    .enter().append("path")
      .attr("class", "layer")
      .attr("d", function(d) { return area(d.values); })
      .style("fill", function(d, i) { return z(i); });

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + (height + 5) + ")")
        .call(xAxis);

    svg.selectAll("text")
        .attr("transform", "translate(75,0)")
        .style("color", "grey")
        .style("font-style", "italic");


    svg.selectAll(".layer")
      .attr("opacity", 0.2)
      .on("mouseover", function(d, i) {
        svg.selectAll(".layer").transition()
        .duration(250)
        .attr("opacity", function(d, j) {
          return j != i ? 0.2 : 0.8;
      })})
      .on("mousemove", function(d, i) {
        mousex = d3.mouse(this);
        mousey = mousex[1];
        mousex = mousex[0];
        currentDate = getMonthAndYear(mousex);
        var story = getStoryData(currentDate);
        var selected = (d.values);
        createToolTip(mousex, mousey, selected, story, currentDate);
      })
    
      .on("mouseout", function(d,i){
        svg.selectAll(".layer").attr("opacity", 0.2);
        var p = d3.selectAll(".popup");
        p.style("display", "none");
      })
   }); 

  //CREATE RUNNING MAP
  d3.csv(runningpath, function(error, data) {
    var allBubbles = new dimple.chart(svg, data);
    allBubbles.setBounds(120, 0, 3720, 450);
    var rX = allBubbles.addTimeAxis("x", "Date", "%Y-%m-%d", "%m/%d/%Y");
    var rY = allBubbles.addMeasureAxis("y", "Distance");
    allBubbles.addColorAxis("Pace", ["#00A67C", "#BF9130", "#910033"]);
    rX.hidden = true;
    rY.hidden = true;
    var lines = allBubbles.addSeries(null, dimple.plot.line);
    lines.lineWeight = 2;
    lines.lineMarkers = true;
    allBubbles.draw();
  });

}

$(document).ready(function() {
  ajaxStoryData();
  chart("https://dl.dropboxusercontent.com/u/23549740/weatherDataFinal5.csv", 'https://dl.dropboxusercontent.com/u/23549740/runningData2.csv',  "orange");
  var allText = $(".container):text");
  allText.attr("x, 75px");
 });


