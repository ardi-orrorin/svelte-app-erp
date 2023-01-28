<script>
  import { onMount, onDestroy } from "svelte";
  import { popUp } from "../../Store";

  onMount(() => ($popUp = !$popUp));

  const onClose = () => {
    window.close();
  };
</script>

<div class="m-2">
  <h1 class="text-center mb-5">Create Notice</h1>
  <form>
    <div class="mb-3">
      <input class="w-100" placeholder="title" />
    </div>
    <div class="mt-3 mb-3">
      <input type="checkbox" id="important" />
      <label for="important"> important</label>
      <input type="checkbox" id="pin" />
      <label for="pin"> pin</label>
    </div>

    <div class="mt-3 mb-3">
      <textarea class="w-100" rows="10" placeholder="body" />
    </div>
    <div class="text-center">
      <button>Summit</button>
    </div>
  </form>
</div>

<style>
  input[type="checkbox"] {
    display: none;
  }
  input[type="checkbox"] + label {
    display: inline;
    border: 1px solid rgba(98, 105, 113, 1);
    background-color: white;
    border-radius: 5px;
    font-size: 15px;
    padding-top: 1%;
    padding-bottom: 1%;
    padding-left: 5%;
    padding-right: 5%;
    margin-right: 10px;
    margin-left: 0px;
  }
  input[type="checkbox"]:checked + label {
    background-color: rgba(98, 105, 113, 1);
    color: white;
  }
  button {
    width: 200px;
    border: 1px solid rgba(98, 105, 113, 1);
    background-color: white;
    color: rgba(98, 105, 113, 1);
    border-radius: 5px;
  }
  button:hover {
    background-color: rgba(98, 105, 113, 1);
    color: white;
  }
  input:focus {
    outline: 1px solid rgba(98, 105, 113, 0.5);
  }
  textarea:focus {
    outline: 1px solid rgba(98, 105, 113, 0.5);
  }
</style>
