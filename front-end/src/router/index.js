import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../components/HomePage.vue')
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../components/AboutPage.vue')
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../components/Profile.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../components/RegisterPage.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../components/LoginPage.vue')      
    },
    {
      path: '/profiles',
      name: 'profiles',
      component: () => import('../components/ProfilesPage.vue')      
    },
    {
      path: '/search',
      name: 'search',
      component: () => import('../components/SearchPage.vue')
    }/*,
    {
      path:'profile/:id',
      name: 'profile',
      component: () => import('../components/ProfileId.vue')
    },
    {
      path:'profile/:id/edit',
      name: 'profileEdit',
      component: () => import('../components/ProfileEdit.vue')
    },
    {
      path: '/showUsers',
      name: 'showUsers',
      component: () => import('../components/ShowUsers.vue')
    },
    {
      path: '/search',
      name: 'search',
      component: () => import('../components/Search.vue')
    }
*/
  ]
})

export default router
