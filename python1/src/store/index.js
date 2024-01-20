import { createStore } from 'vuex'
import intrSide from './intrSide'

const store = createStore({
  state: {
    'githubToken': '',
    permission_routes: []
  },
  getters: {
    permission_routes: state => state.permission_routes,
    sidebar: state => state.yourSidebarState
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    intrSide 
  }
})

export default store
