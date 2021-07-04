import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import DocumentPreview  from '../views/DocumentPreview.vue'
import DocumentSelection from '../views/DocumentsSelection.vue'
import Login from '../views/Login.vue'
import SignUp from '../views/SignUp.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
 
  {
    path: '/doc',
    name: 'DocumentPreview',
    component: DocumentPreview
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'Sign Up',
    component: SignUp
  },
  {
    path: '/selection',
    name: 'DocumentSelection',
    component: DocumentSelection
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
