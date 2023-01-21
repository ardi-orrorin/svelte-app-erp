<script>
  import { isLogin, Account, pathName } from "../Store";
</script>

<div>
  <div class="row p-1">
    <div class="col">
      {$pathName}
    </div>
    <div class="col">&nbsp;</div>
    <div class="col text-end pe-2">{$isLogin ? "로그인 계정 :  " + $Account : ""}</div>
  </div>
</div>

<style>
</style>
