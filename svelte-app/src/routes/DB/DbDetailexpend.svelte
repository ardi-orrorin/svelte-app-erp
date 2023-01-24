<script>
  import axios from "axios";

  export let customer_id;
  export let id;
  export let num;
  export let writeMode;
  const headers = { accept: "application/json" };
  $: url = "http://localhost:8000/api/customerdetail/customer/customerdetail/" + customer_id;
  $: data = axios({ method: "get", url: url, headers: headers }).then((res) => res.data);
</script>

{#await data then data}
  <div class="window">
    <table class="table talbe-sm">
      <thead class="tablesticky">
        <tr>
          <th scope="col" class="col-1">No</th>
          <th scope="col" class="col-2">Name</th>
          <th scope="col" class="col-4">Phone</th>
          <th scope="col">contact</th>
        </tr>
      </thead>
      <tbody>
        {#each data.customer_list as item}
          <tr
            on:click={() => {
              id = item.id;
              writeMode = false;
            }}
            class={item.id === Number(num) ? "bg-secondary text-white" : ""}
          >
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.phonenumber}</td>
            <td><p class="contacts">{item.body}</p></td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>
{/await}

<style>
  td {
    font-size: 12px;
  }
  .contacts {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    word-break: break-all;
    width: 150px;
    margin: 0;
    padding: 0;
  }
  tr:hover {
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
</style>
