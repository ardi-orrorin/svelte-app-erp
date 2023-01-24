<script>
  import { winPopup, params } from "../../Store";
  import axios from "axios";
  import moment from "moment/min/moment-with-locales";

  moment.locale("ko");

  const headers = { accept: "application/json" };
  $: url = `http://localhost:8000/api/customer/list?page=${$params.page}&size=${$params.size}`;
  $: data = axios({ method: "get", url: url, headers: headers }).then((res) => res.data);

  const pageination = Array.from({ length: 9 }, (v, k) => k + 1);

  let checkList = [];

  const filterList = (e, index) => {
    e.target.checked
      ? (checkList = [...checkList, index])
      : (checkList = checkList.filter((element) => element !== index));
  };

  let checkIndex = false;
  const allCheck = (e) => {
    for (let arr = 0; arr < e.length; arr++) {
      checkList = [...checkList, e[arr].id];
    }
    checkIndex = !checkIndex;
  };

  const allNoneCheck = () => {
    checkList = [];
    checkIndex = !checkIndex;
  };
</script>

{#await data}
  <p>loding...</p>
{:then data}
  <table class="table">
    <thead>
      <tr class="bg-secondary text-white text-center">
        <th
          scope="col"
          class="chktable"
          on:click={() => (!checkList.length ? allCheck(data.customer_list) : allNoneCheck())}
          >CHK({checkList.length})</th
        >
        <th scope="col" class="col-1">INDEX</th>
        <th scope="col" class="col-5">Contacts</th>
        <th scope="col" class="col-1">PhoneNumber</th>
        <th scope="col" class="col-1">Wirter</th>
        <th scope="col" class="col-2">Date</th>
        <th scope="col" class="col">Modify</th>
      </tr>
    </thead>
    <tbody class="table-group-divider">
      {#each data.customer_list as customer_list}
        <tr class={checkList.includes(customer_list.id) ? "bg-secondary text-white" : ""}>
          <th class="text-center" scope="row"
            ><input
              type="checkbox"
              class="chk"
              checked={checkList.includes(customer_list.id) ? true : false}
              on:change={(e) => filterList(e, customer_list.id)}
            /></th
          >
          <td class="text-center">{customer_list.id}</td>
          <td on:click={() => winPopup("#/db/id/" + customer_list.id)}>{customer_list.body}</td>
          <td on:click={() => winPopup("#/db/id/" + customer_list.id)}>{customer_list.phonenumber}</td>
          <td class="text-center">{customer_list.name}</td>
          <td class="text-center">{moment(customer_list.create_date).format("YYYY-MM-DD")}</td>
          <td class="text-center"><button>button</button></td>
        </tr>
      {/each}
    </tbody>
  </table>
  <div class="">
    <nav class="d-flex justify-content-center" aria-label="Page navigation ">
      <ul class="pagination">
        <li class="page-item">
          <a class="page-link text-black text-decoration-none" href="#/table/total/pre" on:click={() => scrollTo(0, 0)}
            >Previous</a
          >
        </li>
        {#each pageination as number}
          <li class="page-item">
            <a
              class="page-link text-black text-decoration-none"
              href={"#/table/total/" + number}
              on:click={() => scrollTo(0, 0)}>{number}</a
            >
          </li>
        {/each}
        <li class="page-item">
          <a class="page-link text-black text-decoration-none" href="#/table/total/next" on:click={() => scrollTo(0, 0)}
            >Next</a
          >
        </li>
      </ul>
    </nav>
  </div>
{/await}

<style>
  tr {
    height: 3em;
    vertical-align: middle;
  }
  tr:hover {
    background-color: rgba(98, 105, 113, 0.2);
    color: white;
  }
  .chk {
    width: 18px;
    height: 18px;
  }
  .chktable {
    width: 25px;
  }
</style>
