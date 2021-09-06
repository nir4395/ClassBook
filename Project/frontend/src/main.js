import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import '../src/styles/app.css'
import 'bootstrap'
import 'jquery/src/jquery.js'
import 'bootstrap/dist/css/bootstrap.min.css'

//  import '@fortawesome/fontawesome-free/css/all.css'
//  import '@fortawesome/fontawesome-free/js/all.js'
import vuetify from './plugins/vuetify'
// import Axios from 'axios'
//axios.create()
Vue.prototype.$http = axios.create();
// import 'material-design-icons-iconfont/dist/material-design-icons.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import axios from 'axios'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')