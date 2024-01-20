import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/components/HomePage'
import IntroducePage from '@/components/IntroducePage'
import AboutPage from '@/components/AboutPage'
import UsingPage from '@/components/UsingPage'


const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
  },
  {
    path: '/introduce',
    name: 'IntroducePage',
    component: IntroducePage,
  },
  {
    path: '/about',
    name: 'AboutPage',
    component: AboutPage,
    beforeEnter: (to, from, next) => {
      console.log('Navigating to AboutPage')
      next()
    },
    props: { msg: 'About' } 
  },
  {
    path: '/using',
    name: 'UsingPage',
    component: UsingPage,
    props: { msg: 'Using' }
  },
  {
    path: '/:pathMatch(.*)',
    redirect: '/'
  }
]

const router = createRouter({
  mode:'history',
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
