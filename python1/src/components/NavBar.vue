<template>
  <div class="nav-bar">
    <div class="nav-bar__container">
      <div class="nav-bar__son nav-bar__left">
        <router-link class="nav-bar__item home-button-container" to="/">
          <img :src="require('@/assets/logo1.png')" alt="logo" class="logo">
          <span>Sports</span>
        </router-link>
      </div>
      <div class="nav-bar__son nav-bar__right">
        <router-link class="nav-bar__item intr-button-container right-item" to="/introduce">
          <span>Introduce</span>
        </router-link>
        <router-link class="nav-bar__item docu-button-container right-item" to="/about">
          <span>About</span>
        </router-link>
        <router-link class="nav-bar__item edit-button-container right-item" to="/using">
          <span>Using</span>
        </router-link>
        <div class="nav-bar__item github-button-container right-item">
          <a href="https://github.com/SakuraLong/sakuraRenderer" target="_blank">仓库</a>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {

}
</script>

<style>
.nav-bar {
  position: sticky;
  top: 0;
  height: 50px;
  border-bottom: 1px solid var(--sa-color-base-border);
  display: flex;
  justify-content: center;
  background-color: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(5px);
}
.nav-bar__container {
  width: 100%;
  position: relative;
  max-width: var(--container-max-width);
}
.nav-bar__son {
  position: absolute;
  display: flex;
  flex-direction: row;
  padding: 0px 20px 0px 20px;
}
.nav-bar__left {
  left: 0;
}
.nav-bar__right {
  right: 0;
}
.nav-bar__item {
  height: 50px;
  line-height: 50px;
  font-size: 16px;
}
.home-button-container {
  cursor: pointer;
  user-select: none;
  color: var(--sa-color-primary-base);
  font-size: 30px;
  font-weight: 700;
  display: flex;
  align-items: center;
}
.right-item {
  padding: 0px 15px 0px 15px;
  cursor: pointer;
  transition: all 0.1s linear;
}
.right-item:hover ,
.right-item a:hover {
  transition: all 0.1s linear;
  color: var(--sa-color-primary-base);
}
.right-item--active {
  border-bottom: 2px solid var(--sa-color-primary-base);
}
.right-item a {
  color: initial;
  text-decoration: none;
}
.logo {
  width: 50px; 
  height: auto; 
}
</style>
  