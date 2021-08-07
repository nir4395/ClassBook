import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import DocumentPreview  from '../views/DocumentPreview.vue'
import DocumentSelection from '../views/DocumentsSelection.vue'
import Catergories from '../views/Catergories.vue'
import Login from '../views/Login.vue'
import SignUp from '../views/SignUp.vue'
import CoursesSelection from '../views/CoursesSelection.vue'

import CourseCategorySelection from '../views/CourseCategorySelection.vue'
import MyCourses from '../views/MyCourses.vue'

// import SchoolSelection from '../views/SchoolSelection.vue'
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
    path: '/coursecat',
    name: 'CourseCategorySelection',
    component: CourseCategorySelection
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
    path: '/nav',
    name: 'Catergories',
    component: Catergories
  },
  {
    path: '/courses',
    name: 'CoursesSelection',
    component: CoursesSelection
  },
  {
    path: '/selection',
    name: 'DocumentSelection',
    component: DocumentSelection
  },
  {

    path: '/mycourses',
    name: 'MyCourses',
    component: MyCourses
  },
  {
    path: '/schools',
    name: 'SchoolSelection',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/SchoolSelection.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
