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
</script>

<h3 class="text-center m-5">Svelte Frappe charts navigation demo</h3>
<div class="mt-5">
  <Chart {data} type="pie" bind:this={chartRef} />
</div>
