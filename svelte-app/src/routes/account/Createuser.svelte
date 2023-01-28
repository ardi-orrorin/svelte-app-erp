<script>
  export let isCreatemode;
</script>

<div class="loginbox">
  <div class="box">
    <div class="text-center pt-5 pb-5"><h1>Create User</h1></div>
    <div>
      <div class="form-floating mb-3">
        <input type="" class="form-control" id="id" placeholder="name@example.com" />
        <label for="floatingInput">ID</label>
      </div>
      <div class="form-floating mb-3">
        <input type="password" class="form-control" id="password" placeholder="name@example.com" />
        <label for="floatingInput">PASSWORD</label>
      </div>
      <div class="form-floating mb-3">
        <input type="password" class="form-control" id="password-confirm" placeholder="name@example.com" />
        <label for="floatingInput">PASSWORD CONFIRM</label>
      </div>
      <div class="form-floating mb-3">
        <input type="email" class="form-control" id="email" placeholder="name@example.com" />
        <label for="floatingInput">EMAIL</label>
      </div>
      <div class="form-floating mb-3">
        <input type="string" class="form-control" id="name" placeholder="name@example.com" />
        <label for="floatingInput">NAME</label>
      </div>
      <div class="form-floating mb-3">
        <input type="string" class="form-control" id="phonenumber" placeholder="name@example.com" />
        <label for="floatingInput">PHONE-NUMBER</label>
      </div>
      <div class="container">
        <div class="row justify-content-md-center">
          <button class="btn btn-lg btn-outline-secondary" on:click={() => (isCreatemode = !isCreatemode)}
            >Sign Up</button
          >
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
</style>
