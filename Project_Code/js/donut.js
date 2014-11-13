function drawDonut(csv_file) {
    var width = 960 / 2,
        height = 500 / 2,
        radius = Math.min(width, height) / 2;

    var color = d3.scale.ordinal()
        .range(["red", "green", "blue"]);

    var arc = d3.svg.arc()
        .outerRadius(radius - 10)
        .innerRadius(radius - 80);

    var pie = d3.layout.pie()
        .sort(null)
        .value(function (d) {
            return d.finalcolor;
        });

    var svg = d3.select("body").append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

    d3.csv(csv_file, function (error, data) {

        data.forEach(function (d) {
            d.finalcolor = +d.finalcolor;
        });

        var g = svg.selectAll(".arc")
            .data(pie(data))
            .enter().append("g")
            .attr("class", "arc");

        g.append("path")
            .attr("d", arc)
            .style("fill", function (d) {
                return color(d.data.colors);
            });

        g.append("text")
            .attr("transform", function (d) {
                return "translate(" + arc.centroid(d) + ")";
            })
            .attr("dy", ".35em")
            .style("text-anchor", "middle")
            .text(function (d) {
                return d.data.colors;
            });

    });
}