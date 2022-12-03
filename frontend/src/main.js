import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import qs from "qs";
import "vis/dist/vis.css";

Vue.config.productionTip = false;
Vue.use(ElementUI, { size: "small" });

axios.defaults.baseURL = "http://43.138.47.53:5000";
//axios.defaults.baseURL="/api";
Vue.prototype.$axios = axios;

Vue.prototype.$qs = qs;

new Vue({
  el: "#app",
  router,
  store,
  render: (h) => h(App),
});
