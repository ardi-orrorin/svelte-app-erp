<script>
  import { winPopup, serverhost, ascRegExp, storeParams } from "../../Store";
  import axios from "axios";
  import moment from "moment/min/moment-with-locales";
  import { DateInput, localeFromDateFnsLocale } from "date-picker-svelte";
  import { ko } from "date-fns/locale";
  import { onDestroy } from "svelte";

  moment.locale("ko");
  const maxPage = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000];
  const locale = localeFromDateFnsLocale(ko);
  const options = [
    { label: "important", option: 1 },
    { label: "", option: 2 },
    { label: "important", option: 1 },
  ];
  $: selecttable = "";
  $: startdate = new Date(new Date().setMonth(new Date().getMonth() - 1));
  $: enddate = new Date();

  $: params = {
    page: 0,
    size: $storeParams.size,

    order: "desc" /* 이전값 create_date-desc fastapi 호출값 다름 */,
    startdate: new Date(startdate.setHours(0, 0, 0, 0)),
    enddate: new Date(enddate.setHours(23, 59, 59, 99)),
    keyword: $storeParams.keyword,
  };

  const url = serverhost + `/api/notice/list?`;

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
        <input type="text" id="search" class="search" bind:value={$storeParams.keyword} placeholder="Search" />
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
        on:click={() => winPopup("#/notice/create")}
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
  <table class="table text-center align-middle mt-3">
    <thead>
      <tr class="bg-secondary text-white text-center">
        <th
          scope="col"
          class="col-1"
          on:click={() => (ascRegExp.test(params.order) ? (params.order = "id-desc") : (params.order = "id-asc"))}
          >INDEX {params.order === "id-desc" ? "▼" : "▲"}</th
        >
        <th scope="col" class="col">TITLE</th>
        <th scope="col" class="writer">Writer</th>
        <th
          scope="col"
          class="date"
          on:click={() =>
            ascRegExp.test(params.order) ? (params.order = "create_date-desc") : (params.order = "create_date-asc")}
          >Date {params.order === "create_date-desc" ? "▼" : "▲"}</th
        >
        <th scope="col" class="date">Modify</th>
      </tr>
    </thead>

    <tbody class="table-group-divider">
      {#each data.list as notice_list, i}
        <tr
          class={selecttable === notice_list.id || notice_list.title === $storeParams.keyword
            ? "bg-secondary text-white "
            : ""}
        >
          <td class="text-center "
            >{params.order === "id-desc" || params.order === "create_date-desc"
              ? data.total - params.page * params.size - i
              : params.page * params.size + i + 1}</td
          >
          <td
            on:click={() => {
              winPopup("#/notice/id/" + notice_list.id);
              seltable(notice_list.id);
            }}
            ><p class="contacts">
              {notice_list.title} &nbsp;&nbsp;&nbsp;{#if notice_list.important}<span class="options">important</span
                >{/if}
              {#if notice_list.pin}<span class="options">pin</span>{/if}
            </p></td
          >
          <td
            on:click={() => {
              $storeParams.keyword = $storeParams.keyword + notice_list.user_name;
            }}>{notice_list.user_name}</td
          >
          <td
            class="text-center "
            on:click|preventDefault={() => {
              startdate = new Date(notice_list.create_date);
              enddate = new Date(notice_list.create_date);
            }}>{moment(notice_list.create_date).format("YYYY-MM-DD HH:mm:ss")}</td
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
    font-size: 13px;
  }
  tr:hover {
    background-color: rgba(98, 105, 113, 0.2);
    color: white;
    border-color: white;
  }

  .contacts {
    text-align: left;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    word-break: break-all;
    width: 700px;
    margin: 0;
    padding: 0;
  }

  .writer {
    width: 200px;
    min-width: 200px;
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
    border-radius: 0px;
  }
  .options {
    border: 1px solid rgba(98, 105, 113, 1);
    border-radius: 5px;
    font-size: 10px;
    padding-top: 0.2%;
    padding-bottom: 0.2%;
    padding-left: 3%;
    padding-right: 3%;
    margin-right: 10px;
    margin-left: 0px;
  }
  .search {
    text-align: center;
    width: 100%;
    outline: none !important;
    border-color: rgba(98, 105, 113, 1);
    box-shadow: 0 0 10px rgba(98, 105, 113, 0.6);
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
</style>
