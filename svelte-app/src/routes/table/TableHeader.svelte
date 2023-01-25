<script>
  import { DateInput, localeFromDateFnsLocale } from "date-picker-svelte";
  import { ko } from "date-fns/locale";
  import { winPopup, params } from "../../Store";
  const maxPage = [10, 20, 50, 100, 200];

  $: locale = localeFromDateFnsLocale(ko);
</script>

<div>
  <div class="row st">
    <div class="btn1">
      <button class="btn btn-outline-secondary" type="button" on:click={() => winPopup("#/db/create")}>Create</button>
    </div>
    <div class="sel">
      <select class="form-select" aria-label="Default select example" bind:value={$params.size}>
        {#each maxPage as page}
          <option value={page}>{page}</option>
        {/each}
      </select>
    </div>
    <div class="cal">
      <DateInput bind:value={$params.startdate} {locale} format="yyyy-MM-dd" />
    </div>
    <div class="cal">
      <DateInput bind:value={$params.enddate} {locale} format="yyyy-MM-dd" />
    </div>
    <div class="col">
      <!-- <button class="btn btn-outline-secondary" type="button">Search</button> -->
    </div>
    <div class="col-5">
      <div class="input-group">
        <div class="col-3 pe-2">
          <select class="form-select" bind:value={$params.select_keyworld}>
            <option value="body">내용</option>
            <option value="phonenumber">연락처</option>
            <option value="name">이름</option>
          </select>
        </div>
        <div class="col pe-2">
          <input type="text" class="form-control" bind:value={$params.keyword} />
        </div>
        <!-- <div><button class="btn btn-outline-secondary" type="button">Search</button></div> -->
      </div>
    </div>
  </div>
</div>

<style>
  .cal {
    width: 120px;
  }
  .sel {
    width: 90px;
    padding-left: 11px;
    padding-right: 0px;
  }

  .st {
    position: sticky;
    top: 0;
  }
  .btn1 {
    width: 90px;
  }
</style>
