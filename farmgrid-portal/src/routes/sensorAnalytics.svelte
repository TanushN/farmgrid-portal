<script>
  import { Grid, Row, Column } from "carbon-components-svelte";
  import "@carbon/charts/styles.css";
  import { GaugeChart } from "@carbon/charts-svelte";
  import SensorDataHistory from '../components/sensorDataHistory.svelte'
  import {onMount, onDestroy} from 'svelte';

  import Api from "../util/api";

  const POLLING_RATE = 60  * 1000;

  let intervalId;
  let data = []
  let sensor_id = "0"

  let latest;

  const get_data = async() => {
    console.log("called poll")
    data = await Api.get(`/sensor_events/${sensor_id}`);
    latest = data[0]
  };

  onMount(async() => {
    await get_data();
    intervalId = setInterval(async () => {
      await get_data()
    }, POLLING_RATE)
  })

  onDestroy(() => clearInterval(intervalId));

</script>

<main>
  {#if data.length > 0}

  <Grid>
    <Row>
      <Column>
        <h1>Sensor 1</h1>
      </Column>
    </Row>
    <Row>
      <Column>
        <div class="padding">
          <GaugeChart
          data={[
            {
              group: "value",
              value: (latest.battery / 3.3) * 100,
            },
          ]}
          options={{
            title: "Battery",
            resizable: false,
            height: "250px",
          }}
        />
        </div>
      </Column>
    </Row>
    <Row>
      <Column>
        <h4>Moisture (%)</h4>
      </Column>
      <Column>
        <h4>Light (L)</h4>
      </Column>
      <Column>
        <h4>Temperature (*C)</h4>
      </Column>
    </Row>
    <Row>
      <Column>
        {latest.soil}
      </Column>
      <Column>
        {latest.light}
      </Column>
      <Column>
        {latest.temp}
      </Column>
    </Row>
    <Row>
      <Column>
        <SensorDataHistory data={data}/>
      </Column>
    </Row>
  </Grid>

  {:else}
    <h1>Loading...</h1>
  {/if}

</main>

<style>
  .padding {
    margin: auto;
    width: 30%;
    padding: 60px 0px;
  }
</style>
