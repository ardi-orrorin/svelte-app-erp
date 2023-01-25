<script>
  import { dbdetailExpendParams } from "../../Store";
  import axios from "axios";
  import moment from "moment/min/moment-with-locales";

  export let customer_id;
  export let id;
  export let num;
  export let writeMode;
  const headers = { accept: "application/json" };

  $: url = "http://localhost:8000/api/customerdetail/customer/customerdetail/" + customer_id;
  $: data = axios({ method: "get", url: url, params: $dbdetailExpendParams, headers: headers }).then((res) => res.data);
</script>

{#await data}
  <div class="window" />
{:then data}
  <div class="window">
    <table class="table talbe-sm align-middle text-center">
      <thead class="tablesticky">
        <tr>
          <!-- <th
            scope="col"
            class="col-1"
            on:click={() => (params.order === "id-asc" ? (params.order = "id-desc") : (params.order = "id-asc"))}>No</th
          > -->
          <th class="name align-middle">Name</th>
          <th class="phonenumber align-middle">Phone</th>
          <th class="contacts align-middle">contact</th>
          <th
            class="col-3 align-middle"
            on:click|preventDefault={() =>
              $dbdetailExpendParams.order === "create_date-asc"
                ? ($dbdetailExpendParams.order = "create_date-desc")
                : ($dbdetailExpendParams.order = "create_date-asc")}
            >생성일자{$dbdetailExpendParams.order === "create_date-desc" ? "▼" : "▲"}</th
          >
        </tr>
      </thead>
      <tbody>
        {#each data.customer_list as item}
          <tr
            on:click|preventDefault={() => {
              id = item.id;
              writeMode = false;
            }}
            class={item.id === Number(num) ? "bg-secondary text-white tabletr" : "tabletr"}
          >
            <!-- <td>{item.id}</td> -->
            <td>{item.name}</td>
            <td>{item.phonenumber}</td>
            <td><p class="contacts">{item.body}</p></td>
            <td class="text-center">{moment(item.create_date).format("YYYY-MM-DD HH:mm:ss")}</td></tr
          >
        {/each}
      </tbody>
    </table>
  </div>
{/await}
<div class="m-3 d-flex justify-content-center">
  <input class="form-control form-control-sm search" bind:value={$dbdetailExpendParams.keyword} placeholder="Search" />
</div>

<style>
  td {
    font-size: 10.5px;
  }
  th {
    font-size: 12px;
    text-align: center;
  }
  .contacts {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    word-break: break-all;
    width: 130px;
    margin: 0;
    padding: 0;
  }
  .tabletr:hover {
    background-color: rgba(98, 105, 113, 0.3);
    color: white;
  }
  .window {
    height: 485px;
    overflow-x: auto;
  }

  .tablesticky {
    position: sticky;
    top: 0;
    background-color: white;
    height: 50px;
  }
  .name {
    width: 10px;
    max-width: 10px;
    min-width: 10px;
    padding: 0;
    margin: 0;
  }
  .phonenumber {
    width: 100px;
    padding: 0;
    margin: 0;
  }
  .search {
    width: 300px;
  }
</style>
