<script>
  import { winPopup } from "../../Store";
  import axios from "axios";
  import { serverhost } from "../../Store";
  import moment from "moment/min/moment-with-locales";

  const url = $serverhost + "/api/notice/list?";
  const params = { size: 10, page: 0 };
  $: data = axios({ method: "get", url: url, params: params }).then((res) => res.data);
  export let noticeToggle;
</script>

<div class="m-2">
  {#await data}
    <div class="spiner">
      <div class="spinner-border text-secondary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  {:then data}
    <h1 class="text-center mt-4 mb-3" on:click={() => (noticeToggle = false)}>Notice</h1>
    <table class="table table-sm">
      <thead>
        <tr class="title ">
          <th scope="col" class="text-center">title</th>
          <th scope="col" class="text-center">작성자</th>
          <th scope="col" class="text-center">작성일자</th>
        </tr>
      </thead>
      <tbody>
        {#each data.notice_list as notice_list, index}
          <tr
            class={notice_list.important ? "bg-danger text-white" : ""}
            on:click={() => winPopup("#/notice/id/" + notice_list.id)}
          >
            <td class="text-center"><p class="titleimportant text-center">{notice_list.title}</p></td>

            <td class="text-center">{notice_list.user.name}</td>
            <td class="text-center">{moment(notice_list.create_date).format("YYYY-MM-DD")}</td>
          </tr>{/each}
      </tbody>
    </table>
  {/await}
</div>

<style>
  .spiner {
    display: grid;
    place-items: center;
    min-height: 300px;
  }
  .table {
    font-size: 10px;
  }
  .titleimportant {
    text-align: left;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    word-break: break-all;
    width: 250px;
    padding: 0;
    margin: 2px;
  }
  .title {
    font-size: 14px;
  }
</style>
