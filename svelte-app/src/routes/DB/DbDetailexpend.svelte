<script>
  const itemList = [
    ["1", "name", "010-1111-2222", "dsfssdfsfsdfsldfisdloifjlsdifsdfksdjflsdifjsldifjlisdjflsdijflijjlsdis"],
    ["2", "name1", "010-1111-2222", "dfd23423f"],
    ["3", "name2", "010-1111-2222", "dfddfsd2342f"],
    ["4", "name3", "010-1111-2222", "dfd4f"],
    ["5", "name4", "010-1111-2222", "df3ddfdf1f"],
    ["6", "name5", "010-1111-2222", "d3dfssdfsfdsffdf"],
    ["7", "name5", "010-1111-2222", "d3fddff"],
    ["8", "name5", "010-1111-2222", "d3ffsddf"],
    ["9", "name5", "010-1111-2222", "d3fdf"],
    ["10", "name5", "010-1111-2222", "dfsddffsd3fdf"],
    ["11", "name5", "010-1111-2222", "d3fdf"],
    ["12", "name5", "010-1111-2222", "d3sdfsdfsfsdfsdfsdfsdf"],
    ["13", "name5", "010-1111-2222", "dsdf3fdf"],
    ["14", "name5", "010-1111-2222", "dsf3fdf"],
    ["15", "name5", "010-1111-2222", "d3fdf"],
    ["16", "name5", "010-1111-2222", "dsdf3dfdsffsdfdf"],
    ["17", "name5", "010-1111-2222", "d3fdf"],
    ["18", "name5", "010-1111-2222", "d3ffsddf"],
    ["19", "name5", "010-1111-2222", "d3dfsdffsfdf"],
    ["20", "name5", "010-1111-2222", "d3sdfsdffdf"],
    ["21", "name5", "010-1111-2222", "d3fdf"],
  ];
</script>

<div class="window">
  <table class="table talbe-sm">
    <thead>
      <tr>
        <th scope="col" class="col-1">No</th>
        <th scope="col" class="col-2">Name</th>
        <th scope="col" class="col-4">contact</th>
        <th scope="col">contact</th>
      </tr>
    </thead>
    <tbody>
      {#each itemList as item}
        <tr>
          <td>{item[0]}</td>
          <td>{item[1]}</td>
          <td>{item[2]}</td>
          <td><p class="contacts">{item[3]}</p></td>
        </tr>
      {/each}
    </tbody>
  </table>
</div>

<style>
  td {
    font-size: 12px;
  }
  .contacts {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    word-break: break-all;
    width: 150px;
    margin: 0;
    padding: 0;
  }
  tr:hover {
    background-color: rgba(98, 105, 113, 0.3);
    color: white;
  }
  .window {
    height: 485px;
    overflow-x: auto;
  }
</style>
