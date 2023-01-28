<script>
  import { winPopup, serverhost, ascRegExp } from "../../Store";
  import axios from "axios";
  import moment from "moment/min/moment-with-locales";
  import { DateInput, localeFromDateFnsLocale } from "date-picker-svelte";
  import { ko } from "date-fns/locale";

  moment.locale("ko");
  const maxPage = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000];
  const locale = localeFromDateFnsLocale(ko);

  $: selecttable = "";
  $: startdate = new Date();
  $: enddate = new Date();
  $: size = 20;
  $: keyword = "";
  $: params = {
    page: 0,
    size: size,
    order: "create_date-desc",
    startdate: new Date(startdate.setHours(0, 0, 0, 0) + 32400000),
    enddate: new Date(enddate.setHours(23, 59, 59, 99) + 32400000),
    keyword: keyword,
  };

  const url = serverhost + `/api/payment/list?`;

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
</script>

<div class="tablesticky">
  <div class="row mb-3">
    <div class="cal me-3">
      <DateInput bind:value={startdate} {locale} format="yyyy-MM-dd" />
    </div>
    <div class="cal">
      <DateInput bind:value={enddate} {locale} format="yyyy-MM-dd" />
    </div>
    <div class="col d-flex justify-content-center">
      <div class="col-10">
        <input
          type="text"
          id="tablesearch"
          class="form-control text-center"
          bind:value={keyword}
          placeholder="Search"
        />
      </div>
    </div>
    <div class="sel me-3">
      <select class="form-select" aria-label="Default select example" bind:value={size}>
        {#each maxPage as page}
          <option value={page}>{page}</option>
        {/each}
      </select>
    </div>
    <div class="btn1 me-4">
      <button class="btn1 btn btn-outline-secondary" type="button" on:click={() => winPopup("#/Notice/create")}
        >Create</button
      >
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
        <th scope="col" class="wirter">Company</th>
        <th scope="col" class="writer">Bank_name</th>
        <th scope="col" class="writer">Bank_account</th>
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
        <th scope="col" class="col">Modify</th>
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
              winPopup("#/payment/id/" + payment_list.id);
              seltable(payment_list.id);
            }}>{payment_list.corp_name}</td
          >
          <td on:dblclick={() => (keyword = payment_list.bank_name)}>{payment_list.bank_name}</td>
          <td>{payment_list.bank_account}</td>
          <td on:dblclick={() => (keyword = payment_list.bank_number)}>{payment_list.bank_number}</td>
          <td>{payment_list.money.toLocaleString("ko-kr")}</td>
          <td
            on:dblclick={() => {
              keyword = payment_list.name;
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
            class="page-link text-black text-decoration-none"
            on:click|preventDefault={() => {
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
    width: 200px;
    min-width: 200px;
  }
  .money {
    width: 100px;
    min-width: 100px;
  }
  .date {
    min-width: 150px !important;
    max-width: 150px !important;
    width: 150px !important;
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
  }
</style>
