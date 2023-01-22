<script>
  import { DateInput, localeFromDateFnsLocale } from "date-picker-svelte";
  import { ko } from "date-fns/locale";
  const maxPage = [10, 20, 50, 100, 200];
  let startDate = new Date();
  let endDate = new Date();
  $: locale = localeFromDateFnsLocale(ko);
</script>

<div class="row pb-3">
  <div class="sel">
    <select class="form-select" aria-label="Default select example">
      {#each maxPage as page}
        <option value={page}>{page}</option>
      {/each}
    </select>
  </div>
  <div class="cal">
    <DateInput bind:value={startDate} {locale} format="yyyy-MM-dd" />
  </div>
  <div class="cal">
    <DateInput bind:value={endDate} {locale} format="yyyy-MM-dd" />
  </div>
  <div class="col">
    <button class="btn btn-outline-secondary" type="button">Search</button>
  </div>
  <div class="col-5">
    <div class="input-group">
      <div class="col-3 pe-2">
        <select class="form-select" id="inputGroupSelect01">
          <option selected>선택</option>
          <option value="1">One</option>
          <option value="2">Two</option>
          <option value="3">Three</option>
        </select>
      </div>
      <div class="col pe-2">
        <input type="text" class="form-control" />
      </div>
      <div><button class="btn btn-outline-secondary" type="button">Search</button></div>
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
</style>
