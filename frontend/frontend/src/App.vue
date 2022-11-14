<template>
  <div>
    <el-header>
      <el-menu
        class="el-menu-demo"
        mode="horizontal"
        background-color="#FFF"
        style="padding-left: 0%; padding-right: 10%">
        <el-menu-item><svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" data-v-78e17ca8="">
          <path fill="currentColor" d="M224 480h640a32 32 0 1 1 0 64H224a32 32 0 0 1 0-64z">
          </path>
          <path fill="currentColor" d="m237.248 512 265.408 265.344a32 32 0 0 1-45.312 45.312l-288-288a32 32 0 0 1 0-45.312l288-288a32 32 0 1 1 45.312 45.312L237.248 512z">
          </path>
          </svg>
        </el-menu-item>
        <el-menu-item>风险分析</el-menu-item>
      </el-menu>
    </el-header>
    <main>
      <div class="container">
        <el-card class="card">
          <el-col :span="15">
            <MyCharts :options="options" :width="width"></MyCharts>
            <el-button type="primary" @click="changeWidth">changeWidth</el-button>
            <el-button type="primary" @click="changeOpt">changeOpt</el-button>
          </el-col>
          <el-col :span="9">
            <MyCharts :options="reflect_options"></MyCharts>
          </el-col>
        </el-card>
      </div>
    </main>
  </div>
</template>

<script>
import MyCharts from './components/MyCharts.vue'
import { options1, options2, options3, options4 } from './options'

export default {
  name: 'App',
  components: {
    MyCharts
  },
  data() {
    return {
      options: options1,
      reflect_options: options3,
      width: '500px'
    }
  },
  methods: {
    changeWidth() {
      if(this.width == '500px') {
        //console.log(1)
        this.width = '700px'
      } 
      else {
        //console.log(2)
        this.width = '500px'
      }
    },
    changeOpt() {
      if (this.options == options1) {
        this.options = options2
        this.reflect_options = options4
      } 
      else {
        this.options = options1
        this.reflect_options = options3
      }
    }
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: Helvetica, "PingFang SC", "Microsoft Yahei", sans-serif;
}

/* 整个页面 */
main {
  width: 100vw;
  min-height: 100vh;
  padding: 10px 10px;
  display: grid;
  align-items: start;
  justify-items: left;
  background: #d8dfff;
}

/* 容器 */
.container {
  width: 100%;
  height: 100%;

  box-shadow: 0px 0px 24px rgba(0, 0, 0, 0.15);
  padding: 20px 25px;
  background-color: rgb(245, 246, 252);
}

.card {
  padding: 0 0 10px 0;
}
</style>