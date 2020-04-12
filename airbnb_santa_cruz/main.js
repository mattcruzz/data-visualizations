// Variables
const width = 750;
const height = 750;
const entire_place = "Entire home/apt";
const private_room = "Private room";
const map_fill_color = "#8fc8c4";
const entire_place_color = "#fdf2c5";
const private_place_color = "#a0795f";
const unclassified_color = "#623d45";

// SVG Canvas
const canvas = d3
  .select("body")
  .append("svg")
  .attr("width", width)
  .attr("height", height);

// Define the div for the tooltip
const div = d3
  .select("body")
  .append("div")
  .attr("class", "tooltip")
  .style("opacity", 0);

// Fetch the Santa Cruz county
d3.json("./geojson/neighbourhoods.geojson").then((data) => {
  // Add all the SC Counties to the canvas
  const group = canvas.selectAll("g").data(data.features).enter().append("g");

  // Scale the projection to fit SC County
  const projection = d3.geoMercator().fitSize([width, height], data);

  // Create a path based on the scaled projection
  const path = d3.geoPath().projection(projection);

  // Add a group for each city
  const areas = group
    .append("path")
    .attr("d", path)
    .attr("class", "area")
    .attr("fill", map_fill_color);

  // Load and display the Airbnb listings
  d3.csv("./csv/listings.csv").then((data) => {
    // Parse the data and add circles to svg
    const point = canvas
      .selectAll("circle")
      .data(data)
      .enter()
      .append("circle")
      .attr("cx", (d) => {
        return projection([d.longitude, d.latitude])[0];
      })
      .attr("cy", (d) => {
        return projection([d.longitude, d.latitude])[1];
      })
      .attr("r", "2px")
      // Different color circles for different room types
      .attr("fill", (d) => {
        switch (d.room_type) {
          case entire_place:
            return entire_place_color;
          case private_room:
            return private_place_color;
          default:
            return unclassified_color;
        }
      })
      .on("mouseover", function (d) {
        console.log(d);
        div.transition().duration(200).style("opacity", 0.9);
        div
          .html(
            `<p>
                  id: ${d.id}
                  name: ${d.name}
                  host_id: ${d.host_id}
                  host_name: ${d.host_name}
                  neighbourhood_group: ${d.neighbourhood_group}
                  neighbourhood: ${d.neighbourhood}
                  price: ${d.price}
                  minimum_nights: ${d.minimum_nights}
                  number_of_reviews: ${d.number_of_reviews}
                  last_review: ${d.last_review}
                  reviews_per_month: ${d.reviews_per_month}
                  calculated_host_listings_count: ${d.calculated_host_listings_count}
                  namavailability_365e: ${d.availability_365}
              </p>`
          )
          .style("left", `${d3.event.pageX}px`)
          .style("top", `${d3.event.pageY}px`);
      })
      .on("mouseout", function (d) {
        div.transition().duration(500).style("opacity", 0);
      });
  });

  // zoom and pan
  const zoom = d3.zoom().on("zoom", () => {
    canvas.attr("transform", d3.event.transform);
    canvas.selectAll("circle").attr("d", path.projection(projection));
    canvas.selectAll("path").attr("d", path.projection(projection));
  });

  canvas.call(zoom);
});
