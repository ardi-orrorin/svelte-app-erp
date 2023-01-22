<script>
  import { fade } from "svelte/transition";
  import { winPopup } from "../../Store";

  const pageination = Array.from({ length: 9 }, (v, k) => k + 1);
  let tableDB = [
    [1, "A", "B", "C", "D1", "E"],
    [2, "1", "1", "C", "D2", "E"],
    [3, "2", "2", "C", "D3", "E"],
    [4, "3", "3", "C", "D4", "E"],
    [5, "4", "4", "C", "D5", "E"],
    [6, "A", "5", "C", "D6", "E"],
    [7, "A", "B", "C", "D7", "E"],
    [8, "A", "B", "C", "D8", "E"],
    [9, "A", "B", "C", "D9", "E"],
    [10, "A", "B", "C", "D0", "E"],
    [11, "A", "B", "C", "D1", "E"],
    [12, "A", "B", "C", "D2", "E"],
    [13, "A", "c", "C", "D3", "E"],
    [14, "A", "d", "C", "D4", "E"],
    [15, "A", "b", "C", "D5", "E"],
    [16, "A", "a", "C", "D6", "E"],
    [17, "A", "B", "C", "D7", "E"],
  ];
  let checkList = [];

  const filterList = (e, index) => {
    e.target.checked
      ? (checkList = [...checkList, index])
      : (checkList = checkList.filter((element) => element !== index));
  };

  const allCheck = () => {
    for (let arr = 0; arr < tableDB.length; arr++) {
      checkList = [...checkList, tableDB[arr][0]];
    }
    checkIndex = !checkIndex;
  };

  const allNoneCheck = () => {
    checkList = [];
    checkIndex = !checkIndex;
  };
</script>

<table class="table" transition:fade>
  <thead>
    <tr class="bg-secondary text-white">
      <th scope="col" class="col" on:click={() => (!checkList.length ? allCheck() : allNoneCheck())}
        >CHK({checkList.length})</th
      >
      <th scope="col" class="col-1" on:click={() => (tableDB = tableDB.reverse())}>INDEX</th>
      <th scope="col" class="col-6">Contacts</th>
      <th scope="col" class="col-1">Wirter</th>
      <th scope="col" class="col-2">Date</th>
      <th scope="col" class="col">Modify</th>
      <th scope="col" class="col">Button</th>
    </tr>
  </thead>
  <tbody class="table-group-divider">
    {#each tableDB as DB}
      <tr class={checkList.includes(DB[0]) ? "bg-secondary text-white" : ""}>
        <th class="text-center" scope="row"
          ><input
            type="checkbox"
            class="chk"
            checked={checkList.includes(DB[0]) ? true : false}
            on:change={(e) => filterList(e, DB[0])}
          /></th
        >
        <td class="text-center">{DB[0]}</td>
        <td on:click={() => winPopup("#/db/id/" + DB[0])}>{DB[2]}</td>
        <td>{DB[3]}</td>
        <td>{DB[4]}</td>
        <td>{DB[5]}</td>
        <td>{DB[6]}</td>
      </tr>
    {/each}
  </tbody>
</table>
<div class="">
  <nav class="d-flex justify-content-center" aria-label="Page navigation ">
    <ul class="pagination">
      <li class="page-item">
        <a class="page-link text-black text-decoration-none" href="#/table/total/pre" on:click={() => scrollTo(0, 0)}
          >Previous</a
        >
      </li>
      {#each pageination as number}
        <li class="page-item">
          <a
            class="page-link text-black text-decoration-none"
            href={"#/table/total/" + number}
            on:click={() => scrollTo(0, 0)}>{number}</a
          >
        </li>
      {/each}
      <li class="page-item">
        <a class="page-link text-black text-decoration-none" href="#/table/total/next" on:click={() => scrollTo(0, 0)}
          >Next</a
        >
      </li>
    </ul>
  </nav>
</div>

<style>
  tr {
    height: 3em;
    vertical-align: middle;
  }
  tr:hover {
    background-color: rgba(98, 105, 113, 0.2);
    color: white;
  }
  .chk {
    width: 18px;
    height: 18px;
  }
</style>
