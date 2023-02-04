<script>
  import axios from "axios";
  import Loading from "../Loading.svelte"; /* 포스팅과 상관없는 컴포넌트 */
  import { serverhost } from "../../Store"; /* restapi 서버 호스트 주소 강의내용과 관련없음 */
  import { onMount } from "svelte";

  let url;
  let params;
  let data = []; /* 설제 데이터 저장 변수 */
  let skip = 0;
  let page = 20;
  let result; /* api 호출 값 임시 저장변수 */

  const GetData = async (skip, page) => {
    url = serverhost + "/api/sqlcache/cache_customerdetail";
    params = { skip: skip, page: page };
    result = await axios({ method: "get", url: url, params: params }).then((res) => res.data);
    data ? (data = data.concat(result.result)) : (data = result.result);
  };

  onMount(() => {
    GetData(skip, page);
  });

  /* window.addEventListener("scroll", () => {
    const SCROLLED_HEIGHT = window.scrollY; 
    const WINDOW_HEIGHT = document.body.offsetHeight; 
    const DOC_TOTAL_HEIGHT = document.body.scrollHeight;

    if (SCROLLED_HEIGHT + WINDOW_HEIGHT === DOC_TOTAL_HEIGHT) {
      skip += page;
      GetData(skip, page);
    }
  }); */

  const MoreData = () => {
    skip += page;
    GetData(skip, page);
  };
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
      {#each data as customer_list, i}
        <tr>
          <th class="text-center" scope="row"><input type="checkbox" class="chk" /></th>
          <td class="text-center ">{i + 1}</td>
          <td><p class="contacts">{customer_list.body}</p></td>
          <td>{customer_list.phonenumber}</td>
          <td class="text-center">{customer_list.name}</td>
          <td class="text-center">{customer_list.create_date}</td>
        </tr>
      {/each}
    </tbody>
  </table>

  <!-- pagination start -->
  <!-- <div>
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
  </div> -->

  <!-- pagination end -->
  <div class="text-center p-5">
    <button on:click={() => MoreData()}>더보기</button>
  </div>
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
