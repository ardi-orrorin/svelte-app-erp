<script>
  import { winPopup900, serverhost, ascRegExp, storeParams } from "../../Store";
  import axios from "axios";
  import moment from "moment/min/moment-with-locales";
  import { DateInput, localeFromDateFnsLocale } from "date-picker-svelte";
  import { ko } from "date-fns/locale";
  import { onDestroy } from "svelte";

  let data = [];

  moment.locale("ko");
  const maxPage = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000];
  const locale = localeFromDateFnsLocale(ko);

  $: selecttable = "";
  $: startdate = new Date();
  $: enddate = new Date();

  $: params = {
    page: 0,
    size: $storeParams.size,
    order: "create_date-desc",
    startdate: new Date(startdate.setHours(0, 0, 0, 0) + 32400000),
    enddate: new Date(enddate.setHours(23, 59, 59, 99) + 32400000),
    keyword: $storeParams.keyword,
    userid: $storeParams?.userid ? $storeParams.userid : 15,
    authority: $storeParams?.authority ? $storeParams.authority : 0,
  };

  const url = $serverhost + `/api/payment/list?`;

  $: data = axios({ method: "get", url: url, params: params }).then((res) => res.data);

  const seltable = (e) => {
    selecttable = e;
  };

  const prepage = () => {
    params.page > 0 ? (params.page = params.page - 1) : params.page;
  };
  const nextpage = (total) => {
    let totalPage = Math.ceil(total / params.size);
    if (params.page < totalPage - 1) params.page = params.page + 1;
    return params.page;
  };
  onDestroy(() => {
    $storeParams.size = 20;
    $storeParams.keyword = "";
  });
</script>

<div class="tablesticky">
  <div class="row mb-3">
    <div class="cal me-3">
      <DateInput id="startdate" bind:value={startdate} {locale} format="yyyy-MM-dd" />
    </div>
    <div class="cal">
      <DateInput id="enddate" bind:value={enddate} {locale} format="yyyy-MM-dd" />
    </div>
    <div class="col d-flex justify-content-center">
      <div class="col-10">
        <input
          type="text"
          id="search"
          class="search"
          bind:value={$storeParams.keyword}
          placeholder="Search"
          on:dblclick={() => {
            $storeParams.keyword = "";
          }}
        />
      </div>
    </div>
    <div class="sel me-3">
      <select class="form-select" aria-label="Default select example" bind:value={$storeParams.size}>
        {#each maxPage as page}
          <option value={page}>{page}</option>
        {/each}
      </select>
    </div>
    <div class="btn1 me-4">
      <input
        id="create"
        class="btn1 btn btn-outline-secondary"
        type="button"
        value="Create"
        on:click={() => winPopup("#/Notice/create")}
      />
    </div>
  </div>
</div>
{#await data}
  <div class="spiner">
    <div class="spinner-border text-secondary" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
  </div>
{:then data}
  <table class="table align-middle mt-3">
    <thead>
      <tr class="bg-secondary text-white">
        <th
          scope="col"
          class="index"
          on:click={() => (ascRegExp.test(params.order) ? (params.order = "id-desc") : (params.order = "id-asc"))}
          >No. {params.order === "id-desc" ? "▼" : "▲"}</th
        >
        <th scope="col" class="company">Company</th>
        <th scope="col" class="writer">Bank_name</th>
        <th scope="col" class="bankaccount">Bank_account</th>
        <th scope="col" class="writer">Bank_number</th>
        <th scope="col" class="money">Money</th>
        <th scope="col" class="writer">Writer</th>
        <th
          scope="col"
          class="date"
          on:click={() =>
            ascRegExp.test(params.order) ? (params.order = "create_date-desc") : (params.order = "create_date-asc")}
          >Date {params.order === "create_date-desc" ? "▼" : "▲"}</th
        >
        <th scope="col" class="writer">Modify</th>
      </tr>
    </thead>
    <tbody class="table-group-divider">
      {#each data.payment_list as payment_list, i}
        <tr class={selecttable === payment_list.id ? "bg-secondary text-white " : ""}>
          <td class=""
            >{params.order === "id-desc" || params.order === "create_date-desc"
              ? data.total - params.page * params.size - i
              : params.page * params.size + i + 1}</td
          >
          <td
            on:click={() => {
              winPopup900("#/payment/id/" + payment_list.id);
              seltable(payment_list.id);
            }}>{payment_list.corp_name}</td
          >
          <td
            on:dblclick={() => {
              $storeParams.keyword = payment_list.bank_name;
              document.getElementById("paymentsearch").focus();
            }}>{payment_list.bank_name}</td
          >
          <td
            on:dblclick={() => {
              $storeParams.keyword = payment_list.bank_account;
              document.getElementById("paymentsearch").focus();
            }}>{payment_list.bank_account}</td
          >
          <td
            on:dblclick={() => {
              $storeParams.keyword = payment_list.bank_number;
              document.getElementById("paymentsearch").focus();
            }}>{payment_list.bank_number}</td
          >
          <td>{payment_list.money.toLocaleString("ko-kr")}</td>
          <td
            on:dblclick={() => {
              $storeParams.keyword = payment_list.name;
              document.getElementById("paymentsearch").focus();
            }}>{payment_list.name}</td
          >
          <td
            class="text-center "
            on:dblclick|preventDefault={() => {
              startdate = new Date(payment_list.create_date);
              enddate = new Date(payment_list.create_date);
            }}>{moment(payment_list.create_date).format("YYYY-MM-DD HH:mm:ss")}</td
          >
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
            id="prev"
            class="page-link text-black text-decoration-none"
            on:click={() => {
              prepage();
              scrollTo(0, 0);
            }}>Prev</a
          >
        </li>
        {#each Array(Math.ceil(data.total / params.size)) as _, number}
          {#if number >= params.page - 2 && number <= params.page + 2}
            <li class="page-item">
              <a
                class="page-link text-black text-decoration-none {params.page === number
                  ? 'text-white bg-secondary'
                  : ''}"
                on:click={() => {
                  params.page = number;
                  scrollTo(0, 0);
                }}>{number + 1}</a
              >
            </li>
          {/if}
        {/each}
        <li class="page-item">
          <a
            id="next"
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
  .tablesticky {
    position: sticky;
    top: 0px;
    background-color: rgba(255, 255, 255, 1);
    height: 50px;
    padding-top: 5px;
  }
  tr {
    height: 3em;
    vertical-align: middle;
    padding: 0;
    font-size: 14px;
  }
  tr:hover {
    background-color: rgba(98, 105, 113, 0.2);
    color: white;
    border-color: white;
  }
  .index {
    width: 70px;
    min-width: 70px;
  }
  .writer {
    width: 150px;
    min-width: 150px;
    max-width: 150px;
  }
  .company {
    min-width: 260px;
    width: 260px;
    max-width: 260px;
  }
  .money {
    width: 100px;
    min-width: 100px;
  }
  .bankaccount {
    min-width: 260px;
    width: 260px;
    max-width: 260px;
  }
  .date {
    min-width: 100px !important;
    max-width: 100px !important;
    width: 100px !important;
  }
  .spiner {
    display: grid;
    place-items: center;
    min-height: 300px;
  }
  .cal {
    width: 120px;
  }
  .sel {
    width: 120px;
    padding-left: 11px;
    padding-right: 0px;
  }

  .btn1 {
    width: 120px;
    border-radius: 0px;
  }
  .search {
    width: 100%;
    text-align: center;
    transition: 0.2s;
  }
  .search:focus {
    outline: none !important;
    border-color: rgba(98, 105, 113, 1);
    box-shadow: 0 0 10px rgba(98, 105, 113, 0.6);

    list-style: none;
    color: white;
    background-color: rgba(98, 105, 113, 0.5);
  }
  .search:focus::placeholder {
    color: white;
  }
  .search {
    outline: none !important;
    border-color: rgba(98, 105, 113, 1);
    box-shadow: 0 0 10px rgba(98, 105, 113, 0.6);
  }
</style>
