<script>
  import { serverhost, userID, storeParams } from "../../Store";
  import axios from "axios";
  import moment from "moment/min/moment-with-locales";
  import Loading from "../Loading.svelte";
  import { onMount } from "svelte";
  moment.locale("ko");

  let data;
  let result;
  let total;
  let params = [];
  let paramsPage = 0;
  let paramsSize = 40;
  let paramsOrder = "create_date-desc";
  let startDate = new Date();
  let endDate = new Date();
  let paramsStartdate = new Date(startDate.setHours(0, 0, 0, 0) + 32400000);
  let paramsEnddate = new Date(endDate.setHours(23, 59, 59, 99) + 32400000);
  let paramsKeyword = storeParams.keyword;
  let paramsUserid = /* $userID ??  */ 0;
  let headers;
  let url;

  onMount(async () => {
    await getData();
  });

  const getData = async () => {
    headers = { accept: "application/json" };
    url = serverhost + `/api/customer/list?`;
    params = {
      page: paramsPage,
      size: paramsSize,
      order: paramsOrder,
      startdate: paramsStartdate,
      enddate: paramsEnddate,
      keyword: paramsKeyword,
      userid: paramsUserid,
    };

    data = await axios({ method: "get", url: url, headers: headers, params: params }).then((res) => res.data);
    result ? await (result = result.concat(data.customer_list)) : (result = data.customer_list);
    total ? await (total = total += data.total) : (total = data.total);
  };

  window.addEventListener("scroll", async () => {
    const SCROLLED_HEIGHT = await window.scrollY;
    const WINDOW_HEIGHT = await document.body.offsetHeight;
    const DOC_TOTAL_HEIGHT = await document.body.scrollHeight;

    if (SCROLLED_HEIGHT + WINDOW_HEIGHT === DOC_TOTAL_HEIGHT) {
      paramsPage += 1;
      getData();
    }
  });
</script>

{#await result}
  <Loading />
{:then result}
  {console.log(result)}

  <table class="table table-striped">
    <thead>
      <tr>
        <th>CHK</th>
        <th scope="col">No</th>
        <th scope="col" class="contacts">Body</th>
        <th scope="col">Phone</th>
        <th scope="col">Name</th>
        <th scope="col" class="date">Date</th>
      </tr>
    </thead>
    <tbody>
      {#if result}
        {#each result as item, i}
          <tr>
            <td class="chk"><input type="checkbox" /></td>
            <th scope="row" class="indexnumber">{i + 1}</th>
            <td class="contacts">{item.body}</td>
            <td class="phonenumber">{item.phonenumber}</td>
            <td class="phonenumber">{item.name}</td>

            <td class="date">{moment(item.create_date).format("YYYY-MM-DD HH:mm:ss")}</td>
          </tr>
        {/each}
      {/if}
    </tbody>
  </table>
{/await}

<style>
  tr {
    height: 3em;
    vertical-align: middle;
    font-size: 13px;
  }
  tr:hover {
    background-color: rgba(98, 105, 113, 0.2);
    color: white;
  }
  .indexnumber {
    width: 70px;
    max-width: 70px;
  }
  .chk {
    width: 18px;
    height: 18px;
  }
  .contacts {
    text-align: left;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    word-break: break-all;
    width: 350px;
    max-width: 500px;
    margin: 0;
    padding: 0;
  }
  .date {
    min-width: 100px !important;
    max-width: 100px !important;
    width: 100px !important;
  }
  .phonenumber {
    width: 200px;
    max-width: 200px;
  }
</style>
