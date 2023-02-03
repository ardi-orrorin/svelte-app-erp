<script>
  import axios from "axios";
  import moment from "moment/min/moment-with-locales";
  import Loading from "../Loading.svelte";
  moment.locale("ko");

  const url = serverhost + "/api/sqlcache/cache_customerdetail";

  $: data = axios({ method: "get", url: url }).then((res) => res.data);
</script>

{#await data}
  <Loading />
{:then data}
  <table class="table text-center align-middle">
    <thead>
      <tr class="bg-secondary text-white text-center">
        <th scope="col" class="chktable">CHK</th>
        <th scope="col" class="col-1">INDEX</th>
        <th scope="col" class="col-5">Contacts</th>
        <th scope="col" class="phonenumber">PhoneNumber</th>
        <th scope="col" class="col-1">Wirter</th>
        <th scope="col" class="col-2">Date</th>
      </tr>
    </thead>
    <tbody class="table-group-divider">
      <!-- {#each data as customer_list}
        <tr>
          <th class="text-center" scope="row"><input type="checkbox" class="chk" /></th>
          <td class="text-center " />
          <td><p class="contacts">{customer_list.body}</p></td>
          <td>{customer_list.phonenumber}</td>
          <td class="text-center">{customer_list.name}</td>
          <td class="text-center">{moment(customer_list.create_date).format("YYYY-MM-DD HH:mm:ss")}</td>
        </tr>
      {/each} -->
    </tbody>
  </table>
  <!-- pagination start -->
  <div>
    <nav class="d-flex justify-content-center" aria-label="Page navigation ">
      <ul class="pagination">
        <li class="page-item">
          <a id="prev" class="page-link text-black text-decoration-none">Prev</a>
        </li>
        <li class="page-item">
          <a id="next" class="page-link text-black text-decoration-none">Next</a>
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
    font-size: 13px;
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

  .phonenumber {
    width: 200px;
    min-width: 200px;
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
</style>
