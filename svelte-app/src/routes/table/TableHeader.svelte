<script>
  import { DateInput, localeFromDateFnsLocale } from "date-picker-svelte";
  import { ko } from "date-fns/locale";
  import { winPopup, storeParams } from "../../Store";
  import { afterUpdate, beforeUpdate } from "svelte";

  const maxPage = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000];
  $: locale = localeFromDateFnsLocale(ko);

  /* 3개월 차이 업데이트 한 틱 지연됨 시작 */
  const threemonth = () => {
    if (
      ($storeParams.enddate.getFullYear() - $storeParams.startdate.getFullYear()) * 12 +
        $storeParams.enddate.getMonth() -
        $storeParams.startdate.getMonth() >
      2
    )
      $storeParams.enddate = new Date($storeParams.enddate.setMonth($storeParams.enddate.getMonth() - 1));
  };
  beforeUpdate(() => {
    threemonth();
  });
  afterUpdate(() => {
    threemonth();
  });
  /* 3개월 차이 업데이트 한 틱 지연됨 끝 */
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
