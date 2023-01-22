<script>
  import { isLogin } from "../../Store.js";
  import { fade } from "svelte/transition";

  export let isCreatemode;
</script>

<div class="loginbox" transition:fade>
  <div class="box">
    <div class="text-center pt-5 pb-5"><h1>L O G I N</h1></div>
    <div>
      <div class="form-floating mb-3">
        <input type="email" class="form-control" id="ID" placeholder="name@example.com" />
        <label for="floatingInput">ID</label>
      </div>
      <div class="form-floating mb-3">
        <input type="email" class="form-control" id="PASSWORD" placeholder="name@example.com" />
        <label for="floatingInput">PASSWORD</label>
      </div>
      <div class="container">
        <div class="row justify-content-md-center">
          <button class="btn btn-lg btn-outline-secondary" on:click={() => (($isLogin = !$isLogin), location.reload)}
            >Sign in</button
          >
          <button class="btn btn-lg btn-outline-secondary mt-2" on:click={() => (isCreatemode = !isCreatemode)}
            >Sign up</button
          >
        </div>
      </div>
      <div class="container pt-3">
        <div class="row">
          <div class="col text-start">
            <a class="logintext" href="#/searchid">아이디 찾기</a>
          </div>

          <div class="col text-end">
            <a class="logintext" href="#/searchpwd">비밀번호 찾기</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
  .loginbox {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 70vh;
  }
  .box {
    width: 500px;
  }
  .logintext {
    color: black;
    text-decoration: none;
  }
</style>
