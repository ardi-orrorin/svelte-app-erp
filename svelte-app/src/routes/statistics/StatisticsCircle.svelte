<script>
  import Chart from "svelte-frappe-charts";

  let data = {
    labels: ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"],
    datasets: [
      {
        values: [10, 12, 3, 9, 8, 15, 9],
      },
    ],
  };

  let chartRef;
  let maxSlices = 7;
</script>

<div class="m-3">
  <h4 class="text-center">Svelte Frappe charts navigation demo</h4>
  <div class="">
    <Chart {data} type="pie" bind:this={chartRef} {maxSlices} />
  </div>
</div>
