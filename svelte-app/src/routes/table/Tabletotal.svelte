<script>
  import { winPopup, params, selecttable } from "../../Store";
  import axios from "axios";
  import moment from "moment/min/moment-with-locales";

  moment.locale("ko");

  const headers = { accept: "application/json" };
  const url = `http://localhost:8000/api/customer/list?`;

  $: param = {
    page: $params.page,
    size: $params.size,
    order: $params.order,
    startdate: new Date($params.startdate.setHours(0, 0, 0, 0)),
    enddate: new Date($params.enddate.setHours(23, 59, 59, 99)),
    keyword: $params.keyword,
    select_keyword: $params.select_keyworld,
  };

  $: data = axios({ method: "get", url: url, headers: headers, params: param }).then((res) => res.data);
  let checkList = [];

  const filterList = (e, index) => {
    e.target.checked
      ? (checkList = [...checkList, index])
      : (checkList = checkList.filter((element) => element !== index));
  };

  let checkIndex = false;

  const seltable = (e) => {
    $selecttable = e;
  };
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
  const prepage = () => {
    param.page > 0 ? (param.page = param.page - 1) : param.page;
  };
  const nextpage = (total) => {
    let totalPage = Math.ceil(total / param.size);
    if (param.page < totalPage) return (param.page = totalPage - 1);
    return param.page + 1;
  };
</script>

{#await data then data}
  <table class="table text-center align-middle">
    <thead>
      <tr class="bg-secondary text-white text-center">
        <th
          scope="col"
          class="chktable"
          on:click={() => (!checkList.length ? allCheck(data?.customer_list) : allNoneCheck())}
          >CHK({checkList.length})</th
        >
        <th
          scope="col"
          class="col-1"
          on:click={() => (param.order === "id-asc" ? (param.order = "id-desc") : (param.order = "id-asc"))}
          >INDEX {param.order === "id-desc" ? "▼" : "▲"}</th
        >
        <th scope="col" class="col-5">Contacts</th>
        <th scope="col" class="phonenumber">PhoneNumber</th>
        <th scope="col" class="col-1">Wirter</th>
        <th
          scope="col"
          class="col-2"
          on:click={() =>
            param.order === "create_date-asc" ? (param.order = "create_date-desc") : (param.order = "create_date-asc")}
          >Date {param.order === "create_date-desc" ? "▼" : "▲"}</th
        >
        <th scope="col" class="date">Modify</th>
      </tr>
    </thead>
    <tbody class="table-group-divider">
      {#each data.customer_list as customer_list, i}
        <tr
          class="{checkList.includes(customer_list.id) ? 'bg-danger text-white' : ''}{$selecttable === customer_list.id
            ? 'bg-secondary text-white'
            : ''}"
        >
          <th class="text-center" scope="row"
            ><input
              type="checkbox"
              class="chk"
              checked={checkList.includes(customer_list.id) ? true : false}
              on:change={(e) => filterList(e, customer_list.id)}
            /></th
          >
          <!-- {data.total - param.page * param.size - i} -->
          <td class="text-center "
            >{param.order === "id-desc" || param.order === "create_date-desc"
              ? data.total - param.page * param.size - i
              : param.page * param.size + i + 1}</td
          >
          <td
            on:click={() => {
              winPopup("#/db/id/" + customer_list.customerid);
              seltable(customer_list.id);
            }}><p class="contacts">{customer_list.body}</p></td
          >
          <td
            on:click={() => {
              winPopup("#/db/id/" + customer_list.customerid);
              seltable(customer_list.id);
            }}>{customer_list.phonenumber}</td
          >
          <td class="text-center">{customer_list.name}</td>
          <td class="text-center">{moment(customer_list.create_date).format("YYYY-MM-DD HH:mm:ss")}</td>
          <td class="text-center"><button>button</button></td>
        </tr>
      {/each}
    </tbody>
  </table>
  <!-- pagination start -->
  <div>
    <nav class="d-flex justify-content-center" aria-label="Page navigation ">
      <ul class="pagination">
        <li class="page-item">
          <a
            class="page-link text-black text-decoration-none"
            on:click|preventDefault={() => {
              prepage();
              scrollTo(0, 0);
            }}>Prev</a
          >
        </li>
        {#each Array(Math.ceil(data.total / param.size)) as _, number}
          <li class="page-item">
            <a
              class="page-link text-black text-decoration-none {param.page === number ? 'text-white bg-secondary' : ''}"
              href={"#/table/total/" + number}
              on:click|preventDefault={() => {
                param.page = number;
                scrollTo(0, 0);
              }}>{number + 1}</a
            >
          </li>
        {/each}
        <li class="page-item">
          <a
            class="page-link text-black text-decoration-none"
            on:click={() => {
              nextpage(data.total);
              scrollTo(0, 0);
            }}>Next</a
          >
        </li>
      </ul>
    </nav>
  </div>
  <!-- pagination end -->
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
  .contacts {
    text-align: left;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    word-break: break-all;
    width: 350px;
    margin: 0;
    padding: 0;
  }
  .seltr {
    background-color: rgba(98, 105, 113, 0.5);
    color: brown !important;
  }
  .phonenumber {
    width: 200px;
    min-width: 200px;
  }
  .date {
    min-width: 100px !important;
    max-width: 100px !important;
    width: 100px !important;
  }
</style>
