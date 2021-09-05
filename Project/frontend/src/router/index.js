import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import DocumentPreview  from '../views/DocumentPreview.vue'
import DocumentSelection from '../views/DocumentsSelection.vue'
import Catergories from '../views/Catergories.vue'
import Login from '../views/Login.vue'
import PageNotFound from '../views/PageNotFound.vue'
import SignUp from '../views/SignUp.vue'
import CoursesSelection from '../views/CoursesSelection.vue'
import Profile from '../views/Profile.vue'
import CourseCategorySelection from '../views/CourseCategorySelection.vue'
// import MyCourses from '../views/MyCourses.vue'
import SearchResults from '../views/SearchResults.vue'
// import SchoolSelection from '../views/SchoolSelection.vue'
import Error404 from '../views/Error404.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/search/:query',
    name: 'SearchResults',
    component: SearchResults
  },
  

 
  {
    path: '/doc',
    name: 'DocumentPreview',
    component: DocumentPreview
  },

  {
    path: '/profile',
    name: 'Profile',
    component: Profile
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
    path: '/notfound',
    name: 'NotFound',
    component: PageNotFound
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
    path: '/courses/:catName/:ins/:yearCode',
    name: 'CoursesSelection',
    component: CoursesSelection
  },
  {
    path: '/selection',
    name: 'DocumentSelection',
    component: DocumentSelection
  },
  // {

  //   path: '/mycourses',
  //   name: 'MyCourses',
  //   component: MyCourses
  // },
  {
    path: '/schools',
    name: 'SchoolSelection',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/SchoolSelection.vue')
  },
  {
    path: '/404',
    name: '404',
    component: Error404
  },
  { 
    path: '/:catchAll(.*)', 
    redirect: '/404',
    name: 'NotFound'
  }
]

const router = new VueRouter({
  mode: 'history',
  // base: process.env.BASE_URL,
  routes
})

export default router
