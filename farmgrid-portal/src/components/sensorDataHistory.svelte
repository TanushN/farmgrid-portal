<script>
  import { BarChartStacked } from "@carbon/charts-svelte";

  export let data;

  let items = [];

  for(let item of data){
    for(let group of ["battery", "light", "soil", "temp"]){
      items.push({
        group: group,
        date: item.timestamp,
        value: item[group]
      })
    }
  }

  console.log(items)


</script>

<main>
  <div>
    <BarChartStacked
      data={items}
      options={{
        title: "Sensor History",
        axes: {
          left: {
            mapsTo: "value",
            stacked: true,
          },
          bottom: {
            mapsTo: "date",
            scaleType: "time",
          },
        },
        height: "500px",
      }}
    />
  </div>
</main>

<style>
  div {
    padding-top: 7rem;
  }
</style>
