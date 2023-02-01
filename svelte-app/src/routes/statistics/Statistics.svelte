<script>
  let email = "";
  let password = "";
</script>

<div class="login-container">
  <form on:submit|preventDefault={() => console.log("Log In")}>
    <div class="form-control">
      <div class="mdc-text-field mdc-text-field--outlined">
        <input type="email" id="email-field" class="mdc-text-field__input" bind:value={email} />
        <div class="mdc-notched-outline">
          <div class="mdc-notched-outline__leading" />
          <div class="mdc-notched-outline__notch">
            <label for="email-field" class="mdc-floating-label"> Email </label>
          </div>
          <div class="mdc-notched-outline__trailing" />
        </div>
      </div>
    </div>
    <div class="form-control">
      <div class="mdc-text-field mdc-text-field--outlined">
        <input type="password" id="password-field" class="mdc-text-field__input" bind:value={password} />
        <div class="mdc-notched-outline">
          <div class="mdc-notched-outline__leading" />
          <div class="mdc-notched-outline__notch">
            <label for="password-field" class="mdc-floating-label"> Password </label>
          </div>
          <div class="mdc-notched-outline__trailing" />
        </div>
      </div>
    </div>
    <button class="mdc-button mdc-button--raised" type="submit"> Log In </button>
  </form>
</div>

<style>
  .login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
  }

  .form-control {
    margin-bottom: 1rem;
    width: 25rem;
  }

  .mdc-text-field--outlined .mdc-notched-outline {
    border-width: 1px;
    border-color: rgba(0, 0, 0, 0.38);
  }

  .mdc-floating-label {
    left: 1rem;
  }

  .mdc-button {
    width: 10rem;
    margin-top: 1rem;
  }
</style>
