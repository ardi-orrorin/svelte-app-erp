<script>
  import { isLogin, Account, pathName } from "../Store";
</script>

<div>
  <div class="row p-1">
    <div class="col">
      {$pathName}
    </div>
    <div class="col">&nbsp;</div>
    <div class="col text-end pe-2">
      <!-- <p on:click={() => popup()}>{$isLogin ? "로그인 계정 :  " + $Account : ""} 새창으로 열기</p> -->
    </div>
  </div>
</div>

<style>
</style>
