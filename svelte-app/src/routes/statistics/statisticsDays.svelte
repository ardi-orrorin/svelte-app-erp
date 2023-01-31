<script>
  import Chart from "svelte-frappe-charts";

  let data = {
    labels: [
      "Sun",
      "Mon",
      "Tue",
      "Wed",
      "Thu",
      "Fri",
      "Sat",
      "Sun",
      "Mon",
      "Tue",
      "Wed",
      "Thu",
      "Fri",
      "Sat",
      "Sun",
      "Mon",
    ],
    datasets: [{ values: [300, 250, 720, 560, 370, 610, 690, 410, 370, 480, 620, 260, 170, 510, 630, 710] }],
  };

  const onDataSelect = (event) => {
    console.log("Data select event fired!", event);
    selected = event;
  };
  let selected;
</script>

<h3 class="text-center m-5">Svelte Frappe charts navigation demo</h3>
<div class="mt-5">
  <Chart {data} on:data-select={onDataSelect} isNavigable type="bar" />
</div>
