<script>
  import { onMount } from "svelte";
  import { popUp } from "../../Store";

  onMount(() => ($popUp = !$popUp));
</script>

컴포넌트 새창 열기

<style></style>
