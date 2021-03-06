var vis = new pv.Panel()
    .width(200)
    .height(2200)
    .left(40)
    .right(160)
    .top(10)
    .bottom(10);

var layout = vis.add(pv.Layout.Cluster)
    .nodes(pv.dom(flare)
        .root("flare")
        .sort(function(a, b) pv.naturalOrder(a.nodeName, b.nodeName))
        .nodes())
    .group(true)
    .orient("left");

layout.link.add(pv.Line)
    .strokeStyle("#ccc")
    .lineWidth(1)
    .antialias(false);

layout.node.add(pv.Dot)
    .fillStyle(function(n) n.firstChild ? "#aec7e8" : "#ff7f0e");

layout.label.add(pv.Label);

vis.render();











