<template>
  <!-- FeatureButtons 组件 -->
  <div class="feature-buttons">
    <h1>选择功能</h1>
    <div class="button-container">
      <button class="feature-button">
        <span>跳  绳</span>
      </button>
      <button class="feature-button">
        <span>俯 卧 撑</span>
      </button>
      <button class="feature-button">
        <span>引体向上</span>
      </button>
    </div>
  </div>

  <div class="using-page">
    <!-- 新增元素和效果 -->

    <div class="additional-content">
      <h3>精彩时刻集锦</h3>
      <p>查看其他用户在运动计数器上记录的精彩时刻：</p>
      <div class="moment-gallery">
        <!-- 以循环方式添加一些展示精彩时刻的卡片 -->
        <div v-for="moment in moments" :key="moment.id" class="moment-card">
          <img :src="moment.image" alt="Moment Image">
          <p>{{ moment.description }}</p>
        </div>
      </div>
    </div>

    <div class="user-reviews">
      <h3>用户评价</h3>
      <p>听听其他用户对运动计数器的评价：</p>
      <div class="review-list">
        <!-- 以循环方式添加一些用户评价的卡片 -->
        <div v-for="review in reviews" :key="review.id" class="review-card">
          <p><strong>{{ review.username }}</strong></p>
          <p>{{ review.comment }}</p>
        </div>
      </div>
    </div>

    <!-- 添加动画效果 -->

    <!-- <transition name="fade">
      <img v-if="showLogo" alt="运动计数器应用标志" src="@/assets/bgmain.png" @click="toggleLogo">
    </transition> -->

    <h2>如何使用运动计数器</h2>
    <p>运动计数器的使用非常简单，让我们一起来了解如何充分利用这个强大的工具：</p>

    <ol>
      <li><strong>打开应用：</strong> 启动运动计数器并授予摄像头权限。</li>
      <li><strong>站在摄像头前：</strong> 让摄像头捕捉您的身体动作，运动计数器将立即开始追踪。</li>
      <li><strong>查看统计信息：</strong> 在直观的仪表板上查看实时的运动统计和分析。</li>
    </ol>

    <h3>探索更多功能</h3>
    <p>运动计数器的开发有待探索，更多新功能敬请期待：</p>

    <ul>
      <li><strong>个性化设置：</strong> 调整应用以适应您的偏好和需求。</li>
      <li><strong>健康建议：</strong> 根据您的运动数据提供定制的健康建议。</li>
      <li><strong>社区互动：</strong> 加入我们的社区，与其他用户分享经验和成就。</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'UsingPage',
  props: {
    msg: String,
  },
  data() {
    return {
      moments: [
        { id: 1, image: require('@/assets/ts.gif'), description: '跳绳锻炼，感觉身体更灵活了！' },
        { id: 2, image: require('@/assets/fwc.gif'), description: '完成今日俯卧撑目标，锻炼胸肌和手臂！' },
        { id: 3, image: require('@/assets/ytxs.gif'), description: '成功完成引体向上，提升背部和手臂力量！' },
        // ... 其他时刻卡片的数据
      ],
      reviews: [
        { id: 1, username: 'ActiveLifestyle', comment: '这个应用改变了我的生活方式，让锻炼变得有趣而容易！' },
        { id: 2, username: 'FitJourney', comment: '运动计数器让我更有动力，成为我的健身旅程不可或缺的一部分！' },
        // ... 其他用户评价卡片的数据
      ],
      showLogo: true,
    }
  },
  methods: {
    toggleLogo() {
      this.showLogo = !this.showLogo
    },
  },
}
</script>

<style scoped>
.using-page {
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
}

h2 {
  margin: 40px 0 20px;
}

p {
  margin-bottom: 20px;
}

ol, ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
}

strong {
  font-weight: bold;
}

a {
  color: #42b983;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

/* 新增样式 */

.additional-content {
  margin-top: 60px;
}

.moment-gallery {
  display: flex;
  justify-content: space-around;
  margin-top: 20px;
}

.moment-card {
  width: 200px;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 10px;
  margin-bottom: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.moment-card img {
  width: 100%;
  border-radius: 4px;
  margin-bottom: 10px;
}

.user-reviews {
  margin-top: 60px;
}

.review-list {
  display: flex;
  justify-content: space-around;
  margin-top: 20px;
}

.review-card {
  width: 200px;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 10px;
  margin-bottom: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* 添加动画效果样式 */

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

h3 {
  margin-top: 40px;
}

.feature-buttons {
  display: flex;
  justify-content: space-around;
  margin-top: 20px;
}

.feature-buttons button {
  background-color: #42b983;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  position: relative;
  transition: background-color 0.3s ease;
}

.feature-buttons button:hover {
  background-color: #368b74;
}

.feature-buttons button.active {
  background-color: #2d7a62;
}

.feature-buttons button i {
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  color: #fff;
}

/* 新增样式 */

.feature-buttons {
  margin-top: 40px;
  text-align: center;
}

.button-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.feature-button {
  background-color: #42b983;
  color: #fff;
  border: none;
  padding: 15px 30px;
  border-radius: 8px;
  cursor: pointer;
  position: relative;
  transition: background-color 0.3s ease;
  margin: 0 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.feature-button span {
  margin-top: 10px;
}

.feature-button:hover {
  background-color: #368b74;
}


</style>
