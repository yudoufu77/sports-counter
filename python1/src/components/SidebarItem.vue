<template>
  <div>
    <div class="sidebar-item" @click="toggle">
      <img v-if="icon" :src="icon" class="icon"/>
      <span class="title">{{ title }}</span>
      <span v-if="hasChildren" class="arrow" :class="{ 'expanded': isExpanded }"></span>
    </div>
    <div v-if="hasChildren && isExpanded && isSidebarCollapsed" class="submenu">
      <SidebarItem
        v-for="child in children"
        :key="child.title"
        :title="child.title"
        :icon="child.icon"
        :to="child.to"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'SidebarItem',
  props: {
    title: String,
    icon: String,
    to: String,
    children: Array,
    isSidebarCollapsed: { 
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      isExpanded: false
    }
  },
  computed: {
    hasChildren() {
      return this.children && this.children.length > 0
    }
  },
  methods: {
    handleClick() {
      if (this.to) {
        if (this.to.startsWith('#')) { // 检查 to 属性是否是锚点
          const section = document.querySelector(this.to)
          if (section) {
            section.scrollIntoView({ behavior: 'smooth' })
          }
        } else {
          this.$router.push(this.to) // 对于非锚点路由，使用正常的路由跳转
        }
      }
    },
    toggle() {
      if (this.hasChildren) {
        this.isExpanded = !this.isExpanded // 切换展开/折叠状态
        if (this.isSidebarCollapsed) {
          // 当侧边栏未折叠时
        }
        if (this.to) {
          this.handleClick() // 执行跳转逻辑
        }
      } else {
        this.handleClick() // 如果没有子菜单，直接执行跳转
      }
    },
  }
}
</script>

  
  <style scoped>
  .sidebar-item {
    display: flex;
    align-items: center;
    padding: 10px;
    cursor: pointer;
  }
  
  .icon {
    width: 48px;
    height: 48px;
    margin-right: 10px;
  }
  
  .title {
    font-size: 18px;
  }

  .submenu {
    margin-left: 54px; /* 调整子菜单的左边距 */
  }

  /* 如果需要，可以针对子菜单项进一步细化样式 */
  .submenu >>> .sidebar-item  {
    padding: 5px 10px; /* 调整子菜单项的内填充 */
    font-size: 0px; /* 也许让子菜单项的字体稍小 */
  }

  .arrow {
    display: inline-block;
    margin-left: auto; /* 将箭头推到右边 */
    width: 10px;
    height: 10px;
    border-right: 2px solid black; /* 箭头的一部分 */
    border-bottom: 2px solid black; /* 箭头的另一部分 */
    transform: rotate(45deg); /* 创建向下的箭头形状 */
    transition: transform 0.3s ease; /* 平滑过渡效果 */
  }

  .arrow.expanded {
    transform: rotate(-135deg); /* 当展开时，箭头向上 */
  }
  </style>
  