<template>
    <div class="navbar">
      <hamburger class="hamburger-container" @toggleClick="toggleSideBar"/>
    </div>
  </template>
   
<script type="text/ecmascript-6">
import Hamburger from '@/components/Hamburger'


export default {
  data() {
    return {}
  },
  components: {
    Hamburger
  },
  methods: {
    toggleSideBar() {
      this.$store.dispatch('intrSide/toggleSideBar')
    }
  }
}

</script>
   
  <style lang="scss" scoped>
  .navbar {
    height: 50px;
    overflow: hidden;
    position: relative;
    background: #fff;
    box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08);
   
    .hamburger-container {
      line-height: 46px;
      height: 100%;
      float: left;
      cursor: pointer;
      transition: background 0.3s;
      -webkit-tap-highlight-color: transparent;
   
      &:hover {
        background: rgba(0, 0, 0, 0.025);
      }
    }
   
  }
  </style>
  