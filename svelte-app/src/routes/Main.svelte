<script>
  import Noticemini from "./notice/Noticemini.svelte";
  import StatisticsDays from "./statistics/StatisticsDays.svelte";
  import StatisticsCircle from "./statistics/StatisticsCircle.svelte";

  $: noticeToggle = true;
</script>

<div class="row m-3 d-flex justify-content-center">
  {#if noticeToggle}
    <div class="col shadow m-2 component"><Noticemini bind:noticeToggle /></div>
  {/if}
  {#if noticeToggle}
    <div class="col shadow m-2 component"><StatisticsDays /></div>
  {/if}
  {#if noticeToggle}
    <div class="col shadow m-2 component"><StatisticsCircle /></div>
  {/if}
</div>

<style>
  .row {
    height: 30em;
  }

  .component {
    border: 2px rgba(0, 0, 0, 1);
    width: 600px;
    min-width: 600px;
    max-width: 600px;
  }
</style>
