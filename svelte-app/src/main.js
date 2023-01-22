import App from "./App.svelte";

const app = new App({
  target: document.body,
  props: {
    name: "world",
  },
  stuff: {
    title: "erp",
  },
});

export default app;
