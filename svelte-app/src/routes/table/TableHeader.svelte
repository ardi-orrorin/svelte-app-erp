<script>
  import { DateInput, localeFromDateFnsLocale } from "date-picker-svelte";
  import { ko } from "date-fns/locale";
  import { winPopup, storeParams } from "../../Store";
  import { afterUpdate, beforeUpdate, onMount, onDestroy } from "svelte";
  import moment from "moment/min/moment-with-locales";
  import { getDate } from "date-fns";
  moment.locale("ko");

  const maxPage = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000];
  $: locale = localeFromDateFnsLocale(ko);

  /* 년 바뀜 오류 수정중 시작 */
  /* const maxThreeMonth = () => {
    if (
      ($storeParams.enddate.getFullYear() - $storeParams.startdate.getFullYear()) * 11 +
        $storeParams.enddate.getMonth() -
        $storeParams.startdate.getMonth() <
      2
    ) {
      $storeParams.enddate.setMonth(
        $storeParams.startdate.getMonth() + $storeParams.enddate.getMonth() - $storeParams.startdate.getMonth()
      );
    } else {
      $storeParams.enddate.setMonth($storeParams.startdate.getMonth() + 2);
      $storeParams.enddate.setFullYear($storeParams.startdate.getFullYear());
    }
    $storeParams.enddate.setDate($storeParams.startdate.getDate());
    console.log($storeParams.enddate);
    document.getElementById("enddate").value = moment($storeParams.enddate).format("YYYY-MM-DD");
  };
 
  afterUpdate(() => {
    maxThreeMonth();
  }); */

  /* 년 바뀜 오류 수정중 끝 */

  onDestroy(() => {
    $storeParams.enddate = new Date();
    $storeParams.startdate = new Date();
    $storeParams.keyword = "";
  });
</script>

<div>
  <div class="row st">
    <div class="cal me-3">
      <DateInput id="startdate" bind:value={$storeParams.startdate} {locale} format="yyyy-MM-dd" />
    </div>
    <div class="cal">
      <DateInput id="enddate" bind:value={$storeParams.enddate} {locale} format="yyyy-MM-dd" />
    </div>
    <div class="col d-flex justify-content-center">
      <div class="col-10">
        <input
          type="text"
          id="search"
          class="search"
          bind:value={$storeParams.keyword}
          placeholder="Search"
          on:dblclick={() => ($storeParams.keyword = "")}
        />
      </div>
    </div>
    <div class="sel me-3">
      <select class="form-select" aria-label="Default select example" bind:value={$storeParams.size}>
        {#each maxPage as page, i}
          <option id={"selectid" + i} value={page}>{page}</option>
        {/each}
      </select>
    </div>
    <div class="btn1 me-4">
      <input
        id="create"
        type="button"
        class="btn1 btn btn-outline-secondary"
        on:click={() => winPopup("#/db/create")}
        value="Create"
      />
    </div>
  </div>
</div>

<style>
  .cal {
    width: 120px;
  }
  .sel {
    width: 120px;
    padding-left: 11px;
    padding-right: 0px;
  }

  .st {
    position: sticky;
    top: 0;
  }
  .btn1 {
    width: 120px;
    border-radius: 0px;
  }
  .search {
    width: 100%;
    outline: none !important;
    border-color: rgba(98, 105, 113, 1);
    box-shadow: 0 0 10px rgba(98, 105, 113, 0.6);
    text-align: center;
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
