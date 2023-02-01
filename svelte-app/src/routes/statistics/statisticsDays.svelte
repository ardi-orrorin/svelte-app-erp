<script>
  import Chart from "svelte-frappe-charts";
  import moment from "moment/min/moment-with-locales";
  import { serverhost } from "../../Store";
  import axios from "axios";
  import Loading from "../Loading.svelte";
  moment.locale("ko");
  let url;
  let params;
  let inputdata;

  $: url = serverhost + "/api/statistics/barone";
  $: params = { day: new Date() };
  $: inputdata = axios({ method: "get", url: url, params: params }).then((res) => res.data);

  let data = {
    labels: [],
    datasets: [{ values: [] }],
    yMarkers: [{ label: "Average", value: 0 }],
  };

  const onDataSelect = (event) => {
    console.log("Data select event fired!", event);
    selected = event;
  };
  let selected;
  const datainput = (i) => {
    data.labels = [...data.labels, i.user_id];

    data.datasets[0].values = [...data.datasets[0].values, i.usercount];
  };

  const dateSetting = (e) => {
    if (e === "prev") {
      params.day = new Date(params.day.setDate(params.day.getDate() - 1));
    }
    if (e === "next") {
      params.day = new Date(params.day.setDate(params.day.getDate() + 1));
    }
    data.labels = [];
    data.datasets[0].values = [];
    total = 0;
  };
  $: total = 0;
  const totalcount = (i) => {
    total += i.usercount;
  };

  const totalaverage = (i) => {
    data.yMarkers[0].value = total / i.length;
  };
</script>

{#await inputdata}
  <Loading />
{:then inputdata}
  <span t={totalaverage(inputdata.stat)} />
  {#each inputdata.stat as items}
    <span data={datainput(items)} total={totalcount(items)} />
  {/each}
  <div class="m-3">
    <h5 class="text-center ">
      Daily Write DB Amount Statistics {moment(new Date(params.day)).format("YYYY-MM-DD ")}({total})
    </h5>

    <div class="">
      <Chart {data} on:data-select={onDataSelect} isNavigable={true} barOptions={{ spaceRatio: 0.3 }} type="bar" />
    </div>
    <div class="text-center">
      <button
        on:click={() => {
          dateSetting("prev");
        }}>Prev</button
      >
      {#if new Date() - params.day > 24 * 60 * 59 * 1000}
        <button
          on:click={() => {
            dateSetting("next");
          }}>Next</button
        >
      {/if}
    </div>
  </div>
{/await}

<style>
  button {
    background-color: white;
    border: 1px solid rgba(98, 105, 113, 1);
    font-size: 15px;
    border-radius: 4px;
    width: 50px;
  }
</style>
