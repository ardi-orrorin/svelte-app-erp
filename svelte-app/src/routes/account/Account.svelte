<script>
  import Loginpage from "./Loginpage.svelte";
  import Createuser from "./Createuser.svelte";
  let isCreatemode = false;
</script>

{#if !isCreatemode}
  <Loginpage bind:isCreatemode />
{:else}
  <Createuser bind:isCreatemode />
{/if}

<style></style>
